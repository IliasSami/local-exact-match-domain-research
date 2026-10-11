#!/usr/bin/env python3
"""
rdap_availability_check.py

Reusable domain-availability checker for the
`local-exact-match-domain-research` skill.

Checks domains against public RDAP endpoints (no API key, no cost):

    .co.uk / .uk  -> https://rdap.nominet.uk/uk/domain/<domain>
    .com          -> https://rdap.verisign.com/com/v1/domain/<domain>
    .net          -> https://rdap.verisign.com/net/v1/domain/<domain>
    .org          -> https://rdap.publicinterestregistry.org/rdap/domain/<domain>

HTTP 200 = registered (delegated), 404 = available, 429/503/timeout = transient.

Only "available" and "registered" are treated as definitive. Transient results
are retried automatically, then left as "unresolved" for a manual/rerun pass.

Usage
-----
    # domains as arguments
    python3 rdap_availability_check.py treeremovallondon.co.uk treesurgeon.co.uk

    # domains from a file (one per line, '#' comments allowed)
    python3 rdap_availability_check.py --input candidates.txt --out results.csv

    # generate a service x city matrix on the fly
    python3 rdap_availability_check.py \
        --service treeremoval treesurgeon \
        --city london manchester leeds \
        --tld co.uk

Output
------
Prints a summary and writes a CSV with columns:
    domain,tld,status
"""
from __future__ import annotations

import argparse
import csv
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

UA = "Mozilla/5.0 (compatible; EMD-research/1.0; +https://github.com)"
DEFINITIVE = {"available", "registered"}


def rdap_url(domain: str) -> str | None:
    d = domain.lower().strip()
    if d.endswith(".co.uk") or d.endswith(".uk"):
        return f"https://rdap.nominet.uk/uk/domain/{d}"
    if d.endswith(".com"):
        return f"https://rdap.verisign.com/com/v1/domain/{d}"
    if d.endswith(".net"):
        return f"https://rdap.verisign.com/net/v1/domain/{d}"
    if d.endswith(".org"):
        return f"https://rdap.publicinterestregistry.org/rdap/domain/{d}"
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


def generate(services: list[str], cities: list[str], tlds: list[str]) -> list[str]:
    out: list[str] = []
    for tld in tlds:
        for s in services:
            out.append(f"{s}.{tld}")
            for c in cities:
                out.append(f"{s}{c}.{tld}")
                out.append(f"{c}{s}.{tld}")
    # de-duplicate, preserve order
    seen = set()
    uniq = [d for d in out if not (d in seen or seen.add(d))]
    return uniq


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("domains", nargs="*", help="domains to check")
    ap.add_argument("--input", help="file with one domain per line")
    ap.add_argument("--out", default="domain_availability.csv", help="output CSV path")
    ap.add_argument("--workers", type=int, default=6, help="parallel workers (default 6)")
    ap.add_argument("--service", nargs="*", default=[], help="service tokens for matrix mode")
    ap.add_argument("--city", nargs="*", default=[], help="city tokens for matrix mode")
    ap.add_argument("--tld", nargs="*", default=[], help="tlds for matrix mode, e.g. co.uk com")
    args = ap.parse_args()

    domains: list[str] = []
    if args.input:
        for line in open(args.input):
            line = line.strip().lower()
            if line and not line.startswith("#"):
                domains.append(line)
    domains += [d.lower().strip() for d in args.domains]
    if args.service and args.tld:
        domains += generate(args.service, args.city, args.tld)

    domains = list(dict.fromkeys(d for d in domains if d))
    if not domains:
        ap.error("no domains supplied (pass domains, --input, or --service/--tld)")

    print(f"Checking {len(domains)} domain(s) with {args.workers} workers...", file=sys.stderr)
    results: dict[str, str] = {}
    t0 = time.time()
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        futs = {ex.submit(check, d): d for d in domains}
        done = 0
        for f in as_completed(futs):
            results[futs[f]] = f.result()
            done += 1
            if done % 50 == 0:
                print(f"  {done}/{len(domains)}", file=sys.stderr)

    # retry pass over non-definitive results
    retry = [d for d, s in results.items() if s not in DEFINITIVE]
    if retry:
        print(f"Retrying {len(retry)} non-definitive result(s)...", file=sys.stderr)
        with ThreadPoolExecutor(max_workers=max(2, args.workers // 2)) as ex:
            futs = {ex.submit(check, d, 5): d for d in retry}
            for f in as_completed(futs):
                results[futs[f]] = f.result()

    rows = [{"domain": d, "tld": d.rsplit(".", 2)[-2] if d.endswith(".co.uk") else d.split(".")[-1], "status": results[d]} for d in domains]
    rows.sort(key=lambda r: (r["status"] != "available", r["domain"]))
    with open(args.out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["domain", "tld", "status"])
        w.writeheader()
        w.writerows(rows)

    avail = [r["domain"] for r in rows if r["status"] == "available"]
    unresolved = [r["domain"] for r in rows if r["status"] not in DEFINITIVE]
    print(f"\nDone in {time.time()-t0:.0f}s")
    print(f"available={len(avail)} registered={sum(1 for r in rows if r['status']=='registered')} unresolved={len(unresolved)}")
    print(f"CSV: {args.out}")
    print("\nAVAILABLE:")
    for d in avail:
        print("  " + d)
    if unresolved:
        print("\nUNRESOLVED (rerun manually):")
        for d in unresolved:
            print("  " + d)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
