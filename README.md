# Local Exact-Match Domain Research Skill for Claude, Codex & OpenCode

**EMD / PMD research, validation, scoring and live availability checks** — a reusable
AI-agent skill for evaluating exact-match domains, partial-match domains and brandable
alternatives for **legitimate local-business SEO and lead generation**.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Format: Agent Skill](https://img.shields.io/badge/format-SKILL.md-blue.svg)
![Agents: Claude Code · Codex · OpenCode](https://img.shields.io/badge/agents-Claude%20Code%20%C2%B7%20Codex%20%C2%B7%20OpenCode-purple.svg)

> An exact-match domain is **not** an automatic ranking mechanism. This skill finds
> domains that actually improve relevance, brand recall, click-through, topical focus
> and conversion — and it refuses tactics that rely on deception.

## Table of contents

- [What is this?](#what-is-this)
- [Who it's for](#who-its-for)
- [Highlights](#highlights)
- [What "exact-match domain" means here](#what-exact-match-domain-means-here)
- [Compatibility](#compatibility)
- [Install](#install)
- [Quick start](#quick-start)
- [The verified execution playbook](#the-verified-execution-playbook)
- [Worked example](#worked-example)
- [What's inside](#whats-inside)
- [Guardrails — what this skill will NOT do](#guardrails--what-this-skill-will-not-do)
- [FAQ](#faq)
- [Keywords](#keywords)
- [Disclaimer](#disclaimer)
- [License](#license)

## What is this?

A portable **agent skill** (`SKILL.md` + assets) that runs a full EMD/PMD/brandable
domain research project: market mapping, organic SERP analysis, Google Business
Profile / local-pack analysis, candidate generation, live domain-availability checks
via public RDAP, historical / backlink / trademark due diligence, financial modelling,
and an entity-first local SEO launch plan.

It is intentionally built around the real local-ranking system — **relevance, distance,
prominence** — not around the myth that a keyword domain guarantees rankings.

## Who it's for

- Local SEO consultants and agencies evaluating a client domain.
- Founders and lead-gen operators assessing EMD/PMD opportunities.
- Service-area businesses choosing between a city EMD and a brandable root domain.
- Anyone who wants a **skeptical, evidence-ranked** domain recommendation instead of a
  "buy this and rank" pitch.

## Highlights

- **Mandatory intake gate** — a real project brief before any research or purchase.
- **Multi-agent structure** — intake, keyword mapping, SERP analysis, local-pack
  analysis, domain discovery, risk/history, implementation, and QA roles.
- **Scoring models** — Market Opportunity Score (0–30), Local Entity Opportunity
  Score (0–30), Domain Candidate Score (0–35), with explicit decision thresholds.
- **Live availability checks** — public RDAP endpoints (Nominet, Verisign, PIR), no API
  key, with a definitive/transient status model and an automatic retry pass.
- **Due diligence** — WHOIS/RDAP, archive history, indexation, backlink profile,
  trademark/naming safety, classified clean / caution / reject.
- **Financial model** — payback range and risk-adjusted expected value, not guarantees.
- **Guardrails** — refuses fake locations, doorway pages, fake reviews and deceptive
  lead generation.
- **Evidence log** — every claim gets a source, date and confidence label.

## What "exact-match domain" means here

An **EMD** is a domain whose words match a search phrase (e.g. `mesaroofrepair.com`).
A **PMD** partially matches (e.g. `northdallasroofing.com`). This skill treats both as
*naming and conversion assets* that support user clarity and click-through — never as a
substitute for business legitimacy, proximity, reviews, links or content quality.

## Compatibility

| Agent / harness | How to use |
|-----------------|------------|
| **Claude Code** | Place the folder in your skills directory (e.g. `~/.claude/skills/`) |
| **Codex CLI** | Place the folder in your skills directory |
| **OpenCode** | Place the folder in your skills directory |
| **Cursor / other agents** | Paste `SKILL.md` into context, or point the agent at the file |

> The folder name should match the `name` in the `SKILL.md` frontmatter:
> `local-exact-match-domain-research`. Check your harness docs for its exact skills path.

## Install

```bash
git clone https://github.com/IliasSami/local-exact-match-domain-research.git \
  ~/.claude/skills/local-exact-match-domain-research
```

Then ask your agent to use the **`local-exact-match-domain-research`** skill.

## Quick start

1. Runs the **mandatory intake questions** and records any assumptions.
2. Builds and confirms the project brief.
3. Maps the service and geo layers and scores market quality.
4. Analyses organic SERPs and the local pack separately.
5. Generates EMD / PMD / hybrid / brandable candidates in tiers.
6. Checks availability with the bundled RDAP script.
7. Scores and performs due diligence on the **available** shortlist only.
8. Returns a decision-ready report and a 90-day launch plan.

## The verified execution playbook

```bash
# one-off availability check
python3 assets/rdap_availability_check.py treeremovallondon.co.uk treesurgeon.co.uk

# generate a service x city x tld matrix and check it
python3 assets/rdap_availability_check.py \
  --service treeremoval treesurgeon treefelling \
  --city london manchester leeds birmingham \
  --tld co.uk \
  --out results.csv
```

Status model: `HTTP 200 = registered`, `HTTP 404 = available`, transient results
(`429/503/timeout`) are automatically retried. Availability is **not** quality — only
survivors go to scoring and due diligence.

## Worked example

A live run for **UK tree removal** (459 candidates, 6 workers, ~3 minutes):

| Metric | Result |
|---|---|
| Candidates checked | 459 |
| Available | **339** |
| Registered | 120 |
| Available `.co.uk` city EMDs | **334** |

Every generic head term was already registered except `treelopping.co.uk` and
`treefellings.co.uk`. The exploitable layer was **city + service** EMDs. Full data:
[`examples/uk-tree-removal-live-run.md`](examples/uk-tree-removal-live-run.md) and
[`examples/uk-treeremoval-availability.csv`](examples/uk-treeremoval-availability.csv).

## What's inside

```
local-exact-match-domain-research/
├── SKILL.md                                  # full skill (phases + verified playbook)
├── assets/
│   └── rdap_availability_check.py            # reusable RDAP availability checker
└── examples/
    ├── uk-tree-removal-live-run.md           # worked example write-up
    └── uk-treeremoval-availability.csv       # raw availability evidence
```

## Guardrails — what this skill will NOT do

- Recommend fake business locations or virtual-office manipulation.
- Use fake or keyword-stuffed Google Business Profile names.
- Build doorway pages for cities a business cannot genuinely serve.
- Post fake reviews or deceptive testimonials.
- Recommend trademark-infringing or competitor-impersonating domains.
- Bypass WHOIS privacy protections or obtain non-public registrant data.
- Promise or imply guaranteed rankings.

## FAQ

**Does an exact-match domain guarantee rankings?**
No. Google treats domain words as one of many relevance signals and operates an EMD
system to prevent excessive credit for a matching phrase. This skill returns a
*relevance and conversion asset*, not a ranking guarantee.

**Do I need paid SEO tools?**
No. The availability checks use free public RDAP. Paid tools (Ahrefs, Semrush,
DataForSEO) improve the SERP and backlink phases, but the skill states limitations and
downgrades confidence when a tool is missing rather than fabricating data.

**Which agents does it work with?**
Claude Code, Codex and OpenCode are the primary targets; any agent that can read a
`SKILL.md` can use it.

**Is it free?**
Yes — MIT-licensed. It targets free data sources and never recommends spending the
launch budget on a domain before funding real operations, content and reviews.

## Keywords

local SEO · exact match domain · EMD · PMD · partial match domain · domain research ·
domain availability · RDAP · WHOIS · SERP analysis · local pack · Google Business
Profile · local SEO skill · SEO skill for AI agents · Claude skill · Claude Code skills ·
agent skills · Codex skill · OpenCode skill · lead generation · service-area business ·
entity SEO

## Disclaimer

This skill provides research and decision support, **not legal advice**. Trademark and
regulatory questions must be escalated to qualified counsel. Availability data reflects
the moment of checking; domains can be registered by others at any time.

## License

MIT © 2026 Ilias Ahmed. See [LICENSE](LICENSE).
