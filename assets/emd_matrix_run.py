#!/usr/bin/env python3
"""
emd_matrix_run.py — Stage A of the EMD research pipeline.

Build a `service x geo x order` candidate matrix, check every candidate against
public RDAP (no API key, no cost), and emit:

  * a canonical CSV  (the evidence log), and
  * a structured JSON (feeds ``build_emd_report.py``).

Geos are supplied as a CSV with columns ``geo,geotype[,display]``, e.g.::

    geo,geotype,display
    texas,state,Texas
    houston,city,Houston
    brooklyn,place,Brooklyn

Geotypes are free-form, but the bundled report builder recognises
``head``, ``state``, ``city`` and ``place`` out of the box.

Status model
------------
HTTP 200 = registered, HTTP 404 = available. Only these two are *definitive*.
429/503/timeouts are *transient*: they are retried with backoff, then left as
``unresolved`` for a rerun. Never decide on a non-definitive status.

Usage
-----
    python3 emd_matrix_run.py \\
        --service dentist dentists dental orthodontist \\
        --geo-file geo_us.csv \\
        --tld com \\
        --out-csv dentist-availability.csv \\
        --json-out dentist-data.json \\
        --title "US dentist EMD research"

    # resume a partially completed run: reuses definitive statuses already
    # present in --json-out and only checks new / unresolved candidates
    python3 emd_matrix_run.py ... --resume
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

UA = "Mozilla/5.0 (compatible; EMD-research/1.0; +https://github.com)"
DEFINITIVE = {"available", "registered"}

# Public RDAP endpoints. Longest suffix first so ".co.uk" wins over ".uk".
RDAP = [
    ("co.uk", "https://rdap.nominet.uk/uk/domain/{d}"),
    ("uk", "https://rdap.nominet.uk/uk/domain/{d}"),
    ("com", "https://rdap.verisign.com/com/v1/domain/{d}"),
    ("net", "https://rdap.verisign.com/net/v1/domain/{d}"),
    ("org", "https://rdap.publicinterestregistry.org/rdap/domain/{d}"),
]

DEFAULT_TYPE_LABELS = {
    "head": "Head term",
    "state": "State",
    "region": "Region",
    "metro": "Metro",
    "city": "City",
    "place": "Neighbourhood",
    "suburb": "Suburb",
    "geo": "Location",
}


def rdap_url(domain: str) -> str | None:
    d = domain.lower().strip()
    for suffix, tmpl in RDAP:
        if d.endswith("." + suffix):
            return tmpl.format(d=d)
    return None


def check(domain: str, retries: int = 4) -> str:
    url = rdap_url(domain)
    if not url:
        return "unsupported_tld"
    last = "unresolved"
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": UA, "Accept": "application/rdap+json"}
            )
            with urllib.request.urlopen(req, timeout=25) as r:
                return "registered" if r.status == 200 else f"http_{r.status}"
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return "available"
            last = f"http_{e.code}"
            time.sleep(1.5 * (attempt + 1))
        except Exception as e:  # noqa: BLE001
            last = f"unresolved:{type(e).__name__}"
            time.sleep(0.6 * (attempt + 1))
    return last


def load_geos(path: str) -> list[dict]:
    geos: list[dict] = []
    first = True
    with open(path, newline="") as fh:
        for row in csv.reader(fh):
            if not row or row[0].strip().startswith("#"):
                continue
            row = [c.strip() for c in row]
            if first:
                first = False
                if row[0].lower() in ("geo", "token", "name", "location"):
                    continue  # header row
            geo = row[0].lower().replace(" ", "").replace("-", "")
            geotype = row[1].lower() if len(row) > 1 and row[1] else "geo"
            display = row[2] if len(row) > 2 and row[2] else geo
            geos.append({"geo": geo, "geotype": geotype, "display": display})
    return geos


def load_labels(pairs: list[str]) -> dict:
    out = {}
    for p in pairs or []:
        if "=" in p:
            k, v = p.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def service_display(token: str, labels: dict) -> str:
    return labels.get(token) or (token[:1].upper() + token[1:])


def build(services, geos, tlds, order, service_labels, head=True) -> list[dict]:
    rows: list[dict] = []
    seen: set[str] = set()

    def add(domain, service, geo, geo_display, geotype, kind):
        if domain in seen:
            return
        seen.add(domain)
        rows.append({
            "domain": domain,
            "tld": domain.split(".", 1)[1],
            "service": service,
            "service_display": service_display(service, service_labels),
            "geo": geo,
            "geo_display": geo_display,
            "geotype": geotype,
            "order": kind,
            "status": "",
        })

    for tld in tlds:
        if head:
            for s in services:
                add(f"{s}.{tld}", s, "", "", "head", "head")
        for g in geos:
            for s in services:
                if order in ("both", "service_geo"):
                    add(f"{s}{g['geo']}.{tld}", s, g["geo"], g["display"], g["geotype"], "service+geo")
                if order in ("both", "geo_service"):
                    add(f"{g['geo']}{s}.{tld}", s, g["geo"], g["display"], g["geotype"], "geo+service")
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--service", nargs="+", required=True, help="service tokens")
    ap.add_argument("--geo-file", help="CSV of geo,geotype[,display]")
    ap.add_argument("--tld", nargs="+", default=["com"], help="TLDs (e.g. com co.uk)")
    ap.add_argument("--order", choices=["both", "service_geo", "geo_service"], default="both")
    ap.add_argument("--no-head", action="store_true", help="skip {service}.{tld} head terms")
    ap.add_argument("--service-label", action="append", default=[], help="token=Display")
    ap.add_argument("--highlight-type", default="city", help="geotype to feature in the report")
    ap.add_argument("--title", default="Exact-match domain research")
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--workers", type=int, default=5)
    ap.add_argument("--out-csv", default="availability.csv")
    ap.add_argument("--json-out", default="")
    ap.add_argument("--resume", action="store_true", help="reuse definitive statuses from --json-out")
    args = ap.parse_args()

    geos = load_geos(args.geo_file) if args.geo_file else []
    if not geos and args.no_head:
        raise SystemExit("no geos and --no-head: nothing to check")
    labels = load_labels(args.service_label)
    services = [s.lower().replace(" ", "") for s in args.service]
    rows = build(services, geos, [t.lower() for t in args.tld], args.order, labels, head=not args.no_head)

    for r in rows:
        r["status"] = ""

    if args.resume and args.json_out and os.path.exists(args.json_out):
        prev = json.load(open(args.json_out))
        done = {
            r["domain"]: r["status"]
            for r in prev.get("records", [])
            if r.get("status") in DEFINITIVE
        }
        reused = 0
        for r in rows:
            if r["domain"] in done:
                r["status"] = done[r["domain"]]
                reused += 1
        print(f"Resume: reused {reused} definitive result(s)", file=sys.stderr)

    todo = [r for r in rows if r["status"] not in DEFINITIVE]
    print(f"Checking {len(todo)} of {len(rows)} candidate(s) with {args.workers} workers...", file=sys.stderr)
    t0 = time.time()
    if todo:
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            futs = {ex.submit(check, r["domain"]): r for r in todo}
            done_n = 0
            for f in as_completed(futs):
                futs[f]["status"] = f.result()
                done_n += 1
                if done_n % 100 == 0:
                    print(f"  {done_n}/{len(todo)}  ({time.time()-t0:.0f}s)", file=sys.stderr)

    retry = [r for r in rows if r["status"] not in DEFINITIVE]
    if retry:
        print(f"Retry pass: {len(retry)} non-definitive", file=sys.stderr)
        with ThreadPoolExecutor(max_workers=max(2, args.workers - 1)) as ex:
            futs = {ex.submit(check, r["domain"], 5): r for r in retry}
            for f in as_completed(futs):
                futs[f]["status"] = f.result()

    rows.sort(key=lambda r: (r["status"] != "available", r["geotype"], r["service"], r["geo"], r["domain"]))

    with open(args.out_csv, "w", newline="") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=["domain", "tld", "service", "service_display", "geo", "geo_display", "geotype", "order", "status"],
        )
        w.writeheader()
        w.writerows(rows)

    genered_types = list(dict.fromkeys(r["geotype"] for r in rows))
    meta_types = [t for t in ["head", "state", "region", "metro", "city", "place", "suburb"] if t in genered_types]
    meta_types += [t for t in genered_types if t not in meta_types]

    summary = {
        "generated": time.strftime("%Y-%m-%d"),
        "title": args.title,
        "subtitle": args.subtitle,
        "services": services,
        "service_labels": {s: service_display(s, labels) for s in services},
        "type_labels": {t: DEFAULT_TYPE_LABELS.get(t, t.title()) for t in meta_types},
        "type_order": meta_types,
        "highlight_type": args.highlight_type,
        "total": len(rows),
        "available": sum(1 for r in rows if r["status"] == "available"),
        "registered": sum(1 for r in rows if r["status"] == "registered"),
        "unresolved": sum(1 for r in rows if r["status"] not in DEFINITIVE),
        "records": rows,
    }

    json_out = args.json_out or (os.path.splitext(args.out_csv)[0] + ".json")
    with open(json_out, "w") as fh:
        json.dump(summary, fh)

    print(f"\nDone in {time.time()-t0:.0f}s", file=sys.stderr)
    print(
        f"available={summary['available']} registered={summary['registered']} "
        f"unresolved={summary['unresolved']}",
        file=sys.stderr,
    )
    print(f"CSV:  {args.out_csv}\nJSON: {json_out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
