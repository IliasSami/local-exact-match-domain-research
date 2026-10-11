#!/usr/bin/env python3
"""
build_emd_report.py — Stage B presentation for the
``local-exact-match-domain-research`` skill.

Turn the JSON produced by ``emd_matrix_run.py`` into a single, self-contained,
offline HTML dashboard (no CDN, no external fonts, no network):
stat cards, availability-by-service and availability-by-location-type bars, an
insight card, a highlighted tier list, and a searchable / filterable table.

Usage
-----
    python3 build_emd_report.py --input data.json --out report.html
    python3 build_emd_report.py --input data.json --out report.html \\
        --title "US dentist EMD research" --highlight-type city

Design goals: readable in any browser, no build step, no dependencies, safe to
email or open offline. Human-readable labels come from the input JSON
(``service_labels`` / per-record ``service_display`` and ``geo_display``) —
never show raw concatenated tokens in a client-facing report.
"""
from __future__ import annotations

import argparse
import json

TEMPLATE = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__SUBTITLE__">
<style>
  :root{
    --bg:#f6f7f9; --card:#fff; --line:#e9e9ee; --ink:#14141a; --muted:#71717a;
    --avail:#0f9d58; --availbg:#e8f6ef; --reg:#a1a1aa; --regbg:#f3f3f5;
    --accent:#4f46e5; --accent2:#0ea5e9;
    --radius:16px; --shadow:0 1px 2px rgba(15,15,20,.04),0 10px 30px rgba(15,15,20,.05);
  }
  *{box-sizing:border-box}
  html,body{margin:0}
  body{background:var(--bg);color:var(--ink);-webkit-font-smoothing:antialiased;
    font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
  .wrap{max-width:1140px;margin:0 auto;padding:0 22px}
  header{padding:58px 0 30px;
    background:radial-gradient(880px 320px at 12% -25%,#eef2ff 0,transparent 60%),
               radial-gradient(720px 300px at 96% -35%,#ecfeff 0,transparent 55%)}
  .eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:700;letter-spacing:.09em;
    text-transform:uppercase;color:var(--accent);background:#fff;border:1px solid var(--line);
    padding:6px 12px;border-radius:999px;box-shadow:var(--shadow)}
  .dot{width:7px;height:7px;border-radius:999px;background:var(--avail)}
  h1{font-size:clamp(27px,4.6vw,44px);line-height:1.06;letter-spacing:-.028em;margin:18px 0 12px;font-weight:760}
  .sub{color:var(--muted);max-width:790px;font-size:16px;margin:0}
  .sub b{color:var(--ink);font-weight:650}
  main{padding:6px 0 70px}
  .stats{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:8px 0 18px}
  .stat{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:16px 16px 14px;box-shadow:var(--shadow)}
  .stat .k{font-size:12.5px;color:var(--muted);font-weight:650}
  .stat .v{font-size:30px;font-weight:750;letter-spacing:-.02em;margin-top:6px}
  .stat .d{font-size:12.5px;color:var(--muted);margin-top:2px}
  .grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px}
  .card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:20px;box-shadow:var(--shadow)}
  .card h2{margin:0 0 4px;font-size:15px;font-weight:700;letter-spacing:-.01em}
  .cap{color:var(--muted);font-size:13px;margin:0 0 14px}
  .bars{display:flex;flex-direction:column;gap:12px}
  .bar{display:grid;grid-template-columns:150px 1fr 40px;align-items:center;gap:12px;font-size:13.5px}
  .bar .lbl{color:var(--ink);font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
  .track{background:#f1f1f4;border-radius:999px;height:9px}
  .fill{height:9px;border-radius:999px;background:linear-gradient(90deg,var(--accent),var(--accent2))}
  .bar .val{text-align:right;color:var(--muted);font-weight:700}
  .highlight{background:linear-gradient(180deg,#fff,#fbfbff)}
  .taglist{display:flex;flex-wrap:wrap;gap:8px}
  .tag{font-size:13px;font-weight:650;color:#3730a3;background:#eef2ff;border:1px solid #e0e7ff;
    padding:6px 11px;border-radius:999px}
  .toolbar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-bottom:14px}
  #q{flex:1 1 240px;min-width:200px;font:inherit;color:var(--ink);background:#fff;border:1px solid var(--line);
    border-radius:11px;padding:10px 13px;outline:none}
  #q:focus{border-color:#c7d2fe;box-shadow:0 0 0 3px rgba(79,70,229,.12)}
  select{font:inherit;color:var(--ink);background:#fff;border:1px solid var(--line);border-radius:11px;padding:10px 12px}
  .chips{display:flex;gap:6px;flex-wrap:wrap}
  .chip{border:1px solid var(--line);background:#fff;color:var(--muted);font-weight:650;font-size:13px;
    padding:8px 13px;border-radius:999px;cursor:pointer;transition:.15s}
  .chip:hover{border-color:#d4d4d8;color:var(--ink)}
  .chip.on{background:var(--ink);color:#fff;border-color:var(--ink)}
  .switch{display:inline-flex;align-items:center;gap:8px;color:var(--muted);font-size:13.5px;font-weight:650;
    background:#fff;border:1px solid var(--line);padding:8px 13px;border-radius:999px;cursor:pointer;user-select:none}
  .switch input{accent-color:var(--accent)}
  .count{margin-left:auto;color:var(--muted);font-size:13px;font-weight:650}
  .tablewrap{max-height:640px;overflow:auto;border:1px solid var(--line);border-radius:12px}
  table{width:100%;border-collapse:separate;border-spacing:0;font-size:14px}
  thead th{position:sticky;top:0;background:#fbfbfc;z-index:1;text-align:left;font-size:11.5px;letter-spacing:.05em;
    text-transform:uppercase;color:var(--muted);font-weight:750;padding:12px 15px;border-bottom:1px solid var(--line)}
  tbody td{padding:11px 15px;border-bottom:1px solid #f4f4f6;vertical-align:middle}
  tbody tr:hover{background:#fafafb}
  td.domain{font-weight:680;letter-spacing:-.01em}
  .badge{display:inline-block;font-size:12px;font-weight:750;padding:3px 10px;border-radius:999px}
  .badge.available{color:#0b6b3f;background:var(--availbg)}
  .badge.registered{color:#71717a;background:var(--regbg)}
  .type{color:var(--muted);font-size:12.5px}
  .empty{padding:44px;text-align:center;color:var(--muted)}
  footer{padding:26px 0 60px;color:var(--muted);font-size:13px;max-width:820px}
  @media (max-width:880px){.stats{grid-template-columns:repeat(2,1fr)}.grid2{grid-template-columns:1fr}}
</style>
</head>
<body>
<header>
  <div class="wrap">
    <span class="eyebrow"><span class="dot"></span> Exact-match domain research</span>
    <h1>__H1__</h1>
    <p class="sub">__SUBTITLE__ Checked live via RDAP · <span id="date"></span></p>
  </div>
</header>
<main class="wrap">
  <section class="stats" id="stats"></section>
  <section class="grid2">
    <div class="card"><h2>Availability by service</h2><p class="cap">How many exact-match domains are still free</p><div class="bars" id="chartService"></div></div>
    <div class="card"><h2>Availability by location type</h2><p class="cap">Where the open opportunities sit</p><div class="bars" id="chartGeo"></div></div>
  </section>
  <section class="card" style="margin-bottom:16px">
    <h2>Reading the results</h2>
    <p class="cap" id="insightText" style="margin-bottom:0"></p>
  </section>
  <section class="card highlight" style="margin-bottom:16px" id="hlCard" hidden>
    <h2 id="hlTitle">Featured available domains</h2>
    <p class="cap" id="hlCap"></p>
    <div class="taglist" id="hlTags"></div>
  </section>
  <section class="card">
    <h2 style="margin-bottom:14px">Full domain list</h2>
    <div class="toolbar">
      <input id="q" placeholder="Search domain, location or service…">
      <div class="chips" id="chips"></div>
      <select id="service"></select>
      <label class="switch"><input type="checkbox" id="availOnly" checked> Available only</label>
      <span class="count" id="count"></span>
    </div>
    <div class="tablewrap">
      <table>
        <thead><tr><th>Domain</th><th>Service</th><th>Location</th><th>Type</th><th>Status</th></tr></thead>
        <tbody id="rows"></tbody>
      </table>
    </div>
  </section>
  <footer>
    Generated <span id="date2"></span> · Availability checked against public RDAP and can change at any moment.
    Availability is not quality — run market, local-pack, history and trademark checks before buying.
  </footer>
</main>
<script>
const META = __META__;
const DATA = __DATA__;
const $ = s => document.querySelector(s);
const TYPE_LABEL = META.type_labels || {};
const TYPE_ORDER = META.type_order || [...new Set(DATA.map(r=>r.geotype))];
const SVC_ORDER = META.services || [...new Set(DATA.map(r=>r.service))];
const HL = META.highlight_type || "city";

function barChart(el, entries){
  const max = Math.max(1, ...entries.map(e=>e[1]));
  el.innerHTML = entries.map(([label,val])=>{
    const w = (val/max*100).toFixed(1);
    return `<div class="bar"><div class="lbl">${label}</div>
      <div class="track"><div class="fill" style="width:${w}%"></div></div>
      <div class="val">${val}</div></div>`;
  }).join("") || "<p class='cap'>No data.</p>";
}

function renderStats(){
  const total = DATA.length;
  const av = DATA.filter(r=>r.status==="available").length;
  const cards = [
    ["Domains checked", total.toLocaleString(), (META.tlds || ["exact-match"]).join(" · ")],
    ["Available", av.toLocaleString(), (DATA.length?Math.round(av/DATA.length*100):0)+"% still open"],
    ["Registered", (DATA.length-av).toLocaleString(), "already taken"],
    ["Coverage", TYPE_ORDER.length + " tiers", TYPE_ORDER.map(t=>TYPE_LABEL[t]||t).join(" · ")],
  ];
  $("#stats").innerHTML = cards.map(([k,v,d])=>
    `<div class="stat"><div class="k">${k}</div><div class="v">${v}</div><div class="d">${d}</div></div>`).join("");
}

function renderCharts(){
  const av = DATA.filter(r=>r.status==="available");
  const s = {}; av.forEach(r=>{ s[r.service]=(s[r.service]||0)+1; });
  barChart($("#chartService"), SVC_ORDER.map(k=>[(META.service_labels||{})[k]||k, s[k]||0]).sort((a,b)=>b[1]-a[1]));
  const t = {}; av.forEach(r=>{ t[r.geotype]=(t[r.geotype]||0)+1; });
  barChart($("#chartGeo"), TYPE_ORDER.map(k=>[TYPE_LABEL[k]||k, t[k]||0]).sort((a,b)=>b[1]-a[1]));
}

let activeType = "all";
function renderChips(){
  const entries = [["all","All"]].concat(TYPE_ORDER.map(k=>[k, TYPE_LABEL[k]||k]));
  $("#chips").innerHTML = entries.map(([v,l])=>`<button class="chip ${v===activeType?"on":""}" data-t="${v}">${l}</button>`).join("");
  $("#chips").querySelectorAll(".chip").forEach(b=>b.onclick=()=>{ activeType=b.dataset.t; renderChips(); renderTable(); });
}

function renderServiceSelect(){
  $("#service").innerHTML = '<option value="">All services</option>' +
    SVC_ORDER.map(s=>`<option value="${s}">${(META.service_labels||{})[s]||s}</option>`).join("");
}

function renderTable(){
  const q=$("#q").value.trim().toLowerCase();
  const svc=$("#service").value;
  const availOnly=$("#availOnly").checked;
  let rows = DATA.filter(r=>
    (activeType==="all"||r.geotype===activeType) &&
    (!svc||r.service===svc) &&
    (!availOnly||r.status==="available") &&
    (!q||r.domain.includes(q)||(r.geo_display||"").toLowerCase().includes(q)||r.service.includes(q))
  );
  rows.sort((a,b)=>(a.status===b.status?0:(a.status==="available"?-1:1)) || a.domain.localeCompare(b.domain));
  $("#count").textContent = rows.length.toLocaleString()+" shown";
  $("#rows").innerHTML = rows.map(r=>`<tr>
      <td class="domain">${r.domain}</td>
      <td>${r.service_display||r.service}</td>
      <td>${r.geo_display||"—"}</td>
      <td class="type">${TYPE_LABEL[r.geotype]||r.geotype}</td>
      <td><span class="badge ${r.status}">${r.status}</span></td></tr>`).join("")
    || `<tr><td colspan="5" class="empty">No domains match these filters.</td></tr>`;
}

function renderInsight(){
  const av = DATA.filter(r=>r.status==="available");
  const tot = t => DATA.filter(r=>r.geotype===t).length;
  const avt = t => av.filter(r=>r.geotype===t).length;
  const pct = (a,b) => b ? Math.round(a/b*100) : 0;
  const parts = TYPE_ORDER.filter(t=>tot(t)>0).map(t=>
    `<b>${avt(t)} of ${tot(t)}</b> ${(TYPE_LABEL[t]||t).toLowerCase()} matches (${pct(avt(t),tot(t))}%)`);
  $("#insightText").innerHTML =
    `Availability rises with specificity — the longer and more local the phrase, the more likely it is still free: `+
    parts.join(", ") + `. `+
    `Generic head terms are effectively gone, so the exploitable layer is the long tail `+
    `(neighbourhood/district + service and second-tier cities). Availability is <b>not</b> quality — `+
    `validate local demand, the local pack, domain history and trademarks before buying.`;
}

function renderHighlight(){
  const tags = DATA.filter(r=>r.status==="available" && r.geotype===HL).map(r=>r.domain);
  if(!tags.length){ $("#hlCard").hidden = true; return; }
  $("#hlCard").hidden = false;
  $("#hlTitle").textContent = "Featured available domains — " + (TYPE_LABEL[HL]||HL);
  $("#hlCap").textContent = "The strongest tier still open after head terms (switch the location filter below to see the full tier).";
  $("#hlTags").innerHTML = tags.sort().map(d=>`<span class="tag">${d}</span>`).join("");
}

function init(){
  const dt = META.generated || new Date().toISOString().slice(0,10);
  $("#date").textContent = dt; $("#date2").textContent = dt;
  renderStats(); renderCharts(); renderChips(); renderServiceSelect(); renderInsight(); renderHighlight(); renderTable();
  $("#q").oninput=renderTable; $("#service").onchange=renderTable; $("#availOnly").onchange=renderTable;
}
init();
</script>
</body>
</html>
"""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", required=True, help="JSON produced by emd_matrix_run.py")
    ap.add_argument("--out", default="emd-report.html")
    ap.add_argument("--title", help="override the page title")
    ap.add_argument("--subtitle", help="override the subtitle")
    ap.add_argument("--highlight-type", help="override the featured geotype")
    args = ap.parse_args()

    d = json.load(open(args.input))
    recs = d.get("records", [])
    if not recs:
        raise SystemExit("input JSON has no 'records'")

    title = args.title or d.get("title") or "Exact-match domain research"
    subtitle = args.subtitle or d.get("subtitle") or ""
    if args.highlight_type:
        d["highlight_type"] = args.highlight_type

    # Trim records to the fields the page needs (keeps the file small).
    slim = [
        {
            "domain": r["domain"], "service": r["service"],
            "service_display": r.get("service_display", r["service"]),
            "geo": r.get("geo", ""), "geo_display": r.get("geo_display", r.get("geo", "")),
            "geotype": r.get("geotype", "geo"), "status": r.get("status", ""),
        }
        for r in recs
    ]

    meta_js = json.dumps(d, separators=(",", ":"))
    data_js = json.dumps(slim, separators=(",", ":")).replace("</", "<\\/")

    out = (TEMPLATE
           .replace("__TITLE__", title)
           .replace("__SUBTITLE__", subtitle)
           .replace("__H1__", title)
           .replace("__META__", meta_js)
           .replace("__DATA__", data_js))

    with open(args.out, "w") as fh:
        fh.write(out)
    print(f"wrote {args.out} ({len(out):,} bytes, {len(slim):,} records)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
