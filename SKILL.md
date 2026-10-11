---
name: local-exact-match-domain-research
description: Research, validate, score, and recommend exact-match domains (EMDs), partial-match domains (PMDs), and brandable domain alternatives for legitimate local-business SEO and lead generation. Use when the user wants EMD or PMD domain research, domain availability/history/trademark due diligence, local SERP or Google Business Profile (local-pack) competitive analysis, or an entity-first local SEO launch plan. Provides multi-agent research, market and domain scoring models, risk checks, and guardrails. Do not use to enable fake locations, doorway pages, fake reviews, or deceptive lead generation.
---

# Local Exact-Match Domain Research Skill

## Purpose

Use this skill to identify high-quality, defensible domain opportunities for a
real local business, a lead-generation asset, or a local SEO client.

The skill must not treat exact-match domains as an automatic ranking mechanism.
Google considers domain words as one of many relevance signals and operates an
exact-match-domain system to prevent excessive ranking credit simply because a
domain matches a search phrase.

The real objective is to find domain names that improve:

- Relevance and clarity for users
- Brand recall and direct traffic
- Organic click-through potential
- Local-service topical focus
- Anchor-text and citation naturalness
- Lead-generation conversion potential
- Long-term business usability

For Google local results, prioritize the actual local-ranking system:

- Relevance
- Distance
- Prominence

An EMD does not replace a legitimate business, proximity, complete Google
Business Profile, reviews, links, content quality, local trust signals, or
conversion quality.

---

# Operating Principles

## Principle 1: Entity first, domain second

Never begin by purchasing domains.

First verify:

1. A real business or legitimate lead-generation model exists.
2. The business can genuinely serve the target geography.
3. The service has meaningful commercial demand.
4. The market has an achievable organic opportunity.
5. The name is legal, non-deceptive, and usable as a real business asset.

## Principle 2: Do not promise rankings

Never state or imply:

- "This exact-match domain will rank automatically."
- "Authority does not matter if the domain matches the keyword."
- "A domain name can override local relevance, distance, or prominence."
- "Buy this EMD and you will rank in Google Maps."

Use cautious language:

- "Potential relevance and CTR advantage."
- "A useful supporting asset when combined with strong local SEO."
- "Worth testing where the SERP and business model support it."
- "A naming and conversion asset, not a substitute for quality."

## Principle 3: Never enable deceptive local SEO

Do not recommend:

- Fake business locations
- Virtual-office manipulation
- Fake or keyword-stuffed Google Business Profile names
- Misleading service-area claims
- Fake reviews
- Doorway pages made solely to rank for cities where the business has no
  genuine service capability
- Trademark-infringing domains
- Impersonation of a competitor, franchise, city authority, or government body
- Mass production of low-quality city/service websites

If the user proposes any of these methods, refuse that part and redirect toward
a compliant alternative: a legitimate service-area business, accurate
service-area pages, transparent lead-generation disclosures, or a scalable
brandable domain structure.

## Principle 4: Use an evidence hierarchy

Rank evidence in this order:

1. Official Google documentation and official registries
2. Live SERP observations and search-result data
3. Google Business Profile / Maps observations
4. Domain registrar and WHOIS/RDAP data
5. Internet Archive or domain-history sources
6. Link-index data and crawl data
7. Reputable industry datasets and case studies
8. Practitioner and UGC discussions
9. Assumptions or inferences, clearly labelled

Do not use UGC comments as proof that EMDs override ranking systems.
Use UGC only to generate hypotheses that must be tested against live SERPs.

---

# Required Agent Capabilities

The orchestrator should use available capabilities where possible:

- Web search
- Browser and search-result capture
- Google Maps / local-pack observation
- Keyword research data
- Domain availability lookup
- WHOIS or RDAP lookup
- Internet Archive / historical-page review
- Indexation checks
- Backlink and referring-domain checks
- Trademark database search
- Social-handle search
- Business registry search
- Spreadsheet/CSV creation
- Web crawling and structured-data validation
- Geographic rank tracking or grid-rank tools, if available

If a tool is unavailable, state the limitation, record the missing evidence, and
downgrade confidence rather than fabricating results.

---

# Multi-Agent Team Structure

The Orchestrator coordinates the process and resolves contradictions. Delegate
tasks in parallel when the environment supports sub-agents.

## Agent A: Intake and Commercial Model Analyst

Responsibilities:

- Clarify business model, service, geography, offer, and constraints.
- Identify whether the use case is a real operating business, client site,
  rank-and-rent asset, referral site, directory, or future resale asset.
- Flag compliance, franchise, licensing, and trademark concerns.
- Produce the project brief.

## Agent B: Keyword and Market Mapper

Responsibilities:

- Build service, subservice, emergency, transactional, and modifier keyword sets.
- Identify primary and secondary geographic units.
- Estimate search intent and economic value.
- Create the service-location candidate matrix.

## Agent C: Organic SERP Analyst

Responsibilities:

- Review organic SERPs for high-priority keyword-location pairs.
- Identify organic competitors, directories, aggregators, weak pages, content
  gaps, link gaps, and local-intent signals.
- Evaluate whether the opportunity is realistically winnable.

## Agent D: Local-Pack and Entity Analyst

Responsibilities:

- Inspect Google Maps/local packs where available.
- Evaluate category fit, location patterns, reviews, prominence, local links,
  Google Business Profile completeness, and entity competitors.
- Distinguish organic opportunity from map-pack opportunity.

## Agent E: Domain Discovery Analyst

Responsibilities:

- Generate EMD, PMD, hybrid, metro, neighborhood, and brandable candidates.
- Check availability, price, extension quality, length, readability, and typo risk.
- Recommend the best domain architecture for the intended expansion model.

## Agent F: Domain Risk and History Analyst

Responsibilities:

- Inspect domain age/history, archived snapshots, indexation, spam risk,
  backlinks, anchor text, redirects, prior topics, malware/abuse indicators,
  trademark risk, and ownership ambiguity.
- Classify every candidate as clean, caution, or reject.

## Agent G: Local SEO Implementation Strategist

Responsibilities:

- Convert a chosen domain into an entity-first launch plan.
- Specify site architecture, local landing-page requirements, Business Profile
  alignment, review strategy, citations, schema, local links, conversion tracking,
  and measurement.
- Make recommendations only for real, eligible business operations.

## Agent H: Quality Assurance and Skeptical Reviewer

Responsibilities:

- Challenge unsupported assumptions.
- Verify citations, data consistency, scoring logic, and compliance.
- Identify risks and explain why a recommendation may fail.
- Reject domains whose advantages rely mainly on keyword stuffing or deceptive use.

---

# Mandatory Intake Gate

Before any research begins, ask the user the following primary questions.
Ask them in one structured message. Do not begin domain recommendations until
the user answers or explicitly authorizes reasonable assumptions.

## Primary Questions

1. What is the exact business model?
   - Existing local business
   - New local business
   - Service-area business
   - Lead-generation / rank-and-rent site
   - Referral or marketplace site
   - Agency client project
   - Brand acquisition / future resale

2. What is the primary service?
   Include the highest-value service, not only a broad category.
   Example: "water damage restoration" instead of "home services."

3. Which services are real, licensed, and operationally deliverable?
   List primary, secondary, emergency, and high-ticket subservices.

4. What target location is required?
   Provide:
   - Country
   - State/province/region
   - City
   - ZIP codes, neighborhoods, suburbs, or service radius
   - Whether the business has a real public address, service-area model, or both

5. Is this a single-city business or a multi-location expansion model?
   State the likely 12- to 36-month expansion area.

6. Who is the ideal customer?
   Describe buyer type, urgency, budget, common problem, and decision cycle.

7. What is the average job value, lifetime value, gross margin, or target
   cost per qualified lead?

8. Are there existing competitors, a current website, a Google Business Profile,
   existing domain(s), or Search Console/Analytics data?
   Provide URLs if available.

9. Is there a domain budget?
   Specify:
   - New-registration budget
   - Acquisition budget
   - Maximum annual renewal tolerance
   - Whether aftermarket domains are acceptable

10. What extensions are permitted?
    Example: `.com` only, country-code domains allowed, or brandable alternatives.

11. Are there words, competitors, brands, franchise names, or legal terms to avoid?

12. What is the success definition?
    Choose and rank:
    - Organic rankings
    - Local-pack visibility
    - Calls
    - Form leads
    - Lead resale
    - Brand launch
    - Future geographic expansion
    - Resale value

13. What research depth is desired?
    - Fast screen: 3 to 5 candidates
    - Standard: 10 to 20 candidates and market scoring
    - Deep research: full multi-agent analysis, competitor review, history checks,
      legal screening, and launch plan

14. What tools/data sources are accessible?
    Example: Ahrefs, Semrush, DataForSEO, Google Ads Keyword Planner, GSC,
    GBP access, registrar APIs, Wayback Machine, Majestic, Moz, or custom crawlers.

## Intake Completion Rule

Do not proceed until the following fields are known or explicitly marked
"assumed":

- Service
- Target geography
- Business model
- Expansion model
- Domain budget
- Legal/brand constraints
- Success metric

If assumptions are necessary, create an `Assumptions Register` and ask the user
to confirm it before making a purchase recommendation.

---

# Research Workflow

## Phase 0: Create the Project Brief

Create a concise project brief containing:

```yaml
project:
  project_name:
  business_model:
  primary_service:
  secondary_services:
  country:
  state_or_region:
  primary_city:
  target_postcodes_or_neighborhoods:
  service_radius:
  real_business_address_status:
  target_customer:
  average_job_value:
  lead_value:
  domain_budget:
  preferred_extensions:
  prohibited_words_or_brands:
  current_domains:
  current_website:
  google_business_profile:
  expansion_horizon:
  primary_success_metric:
  research_depth:
  tools_available:
  assumptions:
  risks:
```

The Orchestrator must confirm that the brief is internally consistent.

Example contradiction to resolve:
A user wants `cityservice.com` but also plans to expand to 50 cities in two
years. Explain that a city EMD may constrain branding and recommend a
brandable root domain with city/service architecture, or a carefully separated
portfolio strategy.

---

## Phase 1: Determine the Domain Strategy Before Searching

Classify the project into one of these strategies.

### Strategy A: Single-city EMD

Use when:

- One city will remain the primary market.
- The core service is narrow and high-value.
- The phrase is natural, short, and memorable.
- There is no likely expansion beyond the city or close metro area.
- The business can honestly operate and build prominence there.

Examples:

- `mesaroofrepair.com`
- `friscoepoxyflooring.com`

### Strategy B: Metro or regional PMD

Use when:

- The business serves multiple adjacent cities.
- A city-only domain would be too restrictive.
- The metro has recognized identity and meaningful search demand.

Examples:

- `northdallasroofing.com`
- `tampabaywaterdamage.com`

### Strategy C: Brandable root domain plus local architecture

Use when:

- The business has multi-city or multi-state ambitions.
- The service mix may expand.
- A differentiated brand matters.
- Local pages can be built around genuine service availability.

Example:

```text
brandname.com/
brandname.com/roof-repair/frisco-tx/
brandname.com/roof-repair/plano-tx/
brandname.com/emergency-roof-repair/
```

### Strategy D: Hybrid brand + descriptive domain

Use when:

- The brand needs memorability but the category should remain obvious.
- The exact phrase is unavailable or carries trademark risk.

Examples:

- `SummitRoofCare.com`
- `BlueLineWaterRestore.com`
- `MesaHomeRepair.com`

### Strategy E: Lead-generation asset with transparent routing

Use only when:

- The site discloses its lead-generation/referral role as appropriate.
- Leads are delivered to legitimate providers.
- There is no fake Business Profile, fake address, or deceptive representation.
- The domain’s branding does not falsely imply it is a specific licensed
  contractor when it is not.

---

## Phase 2: Build the Keyword-Service-Location Matrix

Agent B must generate a matrix before any domain search.

### Service Layers

Create these layers:

1. Core category  
   Example: roofing

2. Primary commercial service  
   Example: roof repair

3. High-ticket service  
   Example: roof replacement

4. Emergency service  
   Example: emergency roof repair

5. Diagnostic/problem service  
   Example: roof leak repair

6. Material or specialty service  
   Example: metal roofing, flat roof repair

7. Buyer-modifier terms  
   Example: contractor, company, estimate, near me, cost, same day

8. Adjacent services  
   Example: gutters, storm damage, roof inspection

### Geographic Layers

Create these layers:

1. Core city
2. Major suburbs
3. High-income neighborhoods
4. ZIP codes only when naturally searched or operationally relevant
5. County
6. Metro
7. Regional terms
8. Directional modifiers, only if naturally recognized by residents

### Candidate Phrase Patterns

Generate and normalize:

```text
{service} {city}
{city} {service}
{service} in {city}
{city} {service} company
{city} {service} contractor
emergency {service} {city}
{high_ticket_service} {city}
{problem_solution} {city}
{metro} {service}
{service} {neighborhood}
```

Do not convert every phrase into a domain candidate.
The phrase must first pass commercial and SERP validation.

### Keyword Qualification Fields

For each phrase, capture:

| Field | Meaning |
|---|---|
| Search phrase | Exact query researched |
| Service layer | Core, emergency, high-ticket, etc. |
| Location layer | City, suburb, metro, neighborhood |
| Search intent | Transactional, commercial, informational, navigational |
| Estimated demand | Tool estimate or qualitative category |
| CPC / value proxy | If available |
| Lead value | Expected value of a qualified lead |
| SERP local intent | Local pack, ads, organic local results, directories |
| Seasonality | Stable, seasonal, emergency-driven |
| Business eligibility | Can the business genuinely deliver it? |
| Domain suitability | Natural phrasing, length, brand usability |

---

## Phase 3: Score Market Quality

Score each service-location phrase from 0 to 5 on each criterion.

```text
Market Opportunity Score =
Commercial Intent
+ Economic Value
+ Organic SERP Weakness
+ Local-Pack Opportunity
+ Content/Entity Gap
+ Operational Fit
```

Maximum score: 30.

### 1. Commercial Intent: 0-5

Score 5 if:

- The query shows paid ads, local pack, service providers, quote pages, calls,
  booking options, or strong purchase/urgent intent.

Score 0 if:

- The query is purely informational or unrelated to direct service purchase.

### 2. Economic Value: 0-5

Score 5 if:

- One conversion has high gross profit or repeat value.
- The business can afford ongoing local SEO and lead acquisition.
- The service has urgent or high-consideration demand.

### 3. Organic SERP Weakness: 0-5

Score 5 if multiple top organic results show:

- Thin or generic pages
- Poor content/service detail
- Outdated site quality
- Weak local relevance
- Low brand trust
- Limited local proof
- Weak backlink/entity profile
- Overreliance on directories or aggregators

Score 0 if page one is dominated by strong, relevant, well-established local
brands, national authorities, government resources, or highly trusted directories.

### 4. Local-Pack Opportunity: 0-5

Score 5 if:

- The local pack exists.
- Competitors have weak review volume/quality.
- Categories and services are poorly optimized.
- There is a clear quality/prominence gap.
- The business can establish legitimate geographic relevance.

Do not score highly solely because competitors are far away. Distance cannot be
manufactured and should not be manipulated.

### 5. Content and Entity Gap: 0-5

Score 5 if:

- Important service questions are unanswered.
- Competitors lack proof of work, FAQs, pricing context, local case studies,
  team credentials, or localized expertise.
- The entity ecosystem is weak: few trusted citations, local mentions, reviews,
  local links, or coherent brand signals.

### 6. Operational Fit: 0-5

Score 5 if:

- The business is licensed/eligible where required.
- The service can be delivered at acceptable margins.
- The service area is genuine.
- Sales, dispatch, and fulfillment capacity exist.
- The user can sustain content, reputation, and customer experience.

### Decision Thresholds

| Score | Decision |
|---:|---|
| 25-30 | Priority market. Proceed to domain and competitive due diligence. |
| 20-24 | Viable. Proceed if domain is clean and business fit is strong. |
| 15-19 | Conditional. Prefer a broader brandable strategy or test first. |
| 0-14 | Do not buy an EMD based on this phrase. |

---

## Phase 4: Analyze Organic SERPs

Agent C must analyze the top 10 to 20 organic results for each priority phrase.

### Capture for Each Result

- Rank
- Domain
- URL
- Page type
- Brand type: local business, national chain, directory, publisher, government,
  marketplace, aggregator
- Exact keyword usage in title and URL
- Content depth and helpfulness
- Local proof: address, projects, service areas, reviews, photos, case studies
- Unique value proposition
- Indexable/page-quality observations
- Approximate authority/link signals, if tools exist
- Content gaps
- Conversion quality
- Whether the result is an EMD, PMD, or brandable domain

### SERP Opportunity Signals

Positive signals:

- Multiple thin city pages
- Old websites with weak UX
- Search results with poor service differentiation
- Generic national content above weak local sites
- Missing high-value service pages
- Few local proof points
- Inconsistent or weak entities
- Low-quality directories ranking due to lack of better alternatives

Negative signals:

- Strong local brands with years of reviews and local coverage
- Dominant marketplaces/directories consuming most clicks
- Strong franchise or national entities with local branches
- Local intent but no feasible physical/service-area eligibility
- Extremely high ad density that reduces organic lead value
- Query interpreted differently than the intended service

### SERP Analysis Output

For every prioritized phrase, produce:

```yaml
serp_assessment:
  phrase:
  search_location:
  local_pack_present:
  ads_present:
  organic_opportunity: low|medium|high
  dominant_result_types:
  weakest_competitor_patterns:
  strongest_competitor_patterns:
  content_gaps:
  entity_gaps:
  emd_observation:
  recommendation:
  confidence:
```

Important:
Do not conclude that EMDs cause ranking merely because EMDs appear in results.
Check whether those domains also have better links, older brands, reviews, content,
location relevance, or strong conversion signals.

---

## Phase 5: Analyze Local Pack and Local Entity Competition

Agent D must separately analyze local visibility. Organic and Maps results are
not interchangeable.

### For Each Top Local Competitor, Capture

- Business name
- Primary category
- Secondary categories, if visible
- Address/service-area model
- Review count
- Average rating
- Review recency
- Owner responses
- Photos and media quality
- Website/domain
- Service list
- Appointment/call capability
- Local links and citations, if available
- Years in business / brand mentions
- Evidence of real operations
- Proximity pattern where legitimate and observable

### Local Entity Opportunity Score

```text
Local Entity Opportunity =
Category Fit
+ Review Gap
+ Profile Completeness Gap
+ Website Relevance Gap
+ Local Link / Mention Gap
+ Proof-of-Work Gap
```

Maximum score: 30.

Do not use or recommend false addresses, manipulated pin locations, or fake
profiles to exploit proximity.

### Interpret Correctly

The local pack is primarily shaped by:

- Relevance: how well the business information matches the search
- Distance: how close the business is to the searcher or stated location
- Prominence: how known/trusted the business is, including reviews and web mentions

Therefore:

- An EMD may support website relevance and user clarity.
- An EMD does not solve distance.
- An EMD does not create prominence.
- A weak local entity with an EMD is still weak.

---

## Phase 6: Generate Domain Candidates

Agent E must generate candidates only from phrases that pass Phases 2 through 5.

### Candidate Types

Generate candidates in this priority order.

#### Tier 1: Clean exact-match `.com`

```text
{service}{city}.com
{city}{service}.com
```

Examples:

```text
roofrepairmesa.com
mesaroofrepair.com
```

#### Tier 2: Natural partial-match `.com`

```text
{city}{service}pros.com
{city}{service}experts.com
{metro}{service}.com
{service}{metro}.com
```

Use only when natural and not overly generic.

#### Tier 3: Hybrid descriptive brand `.com`

```text
{brand}{service}.com
{service}{brand}.com
{city}{brand}.com
```

Examples:

```text
summitroofcare.com
mesaroofco.com
```

#### Tier 4: Brandable root domain

Use where expansion, differentiation, or legal safety outweighs exact matching.

### Candidate Generation Constraints

Reject or heavily downgrade domains that are:

- Longer than approximately 18 to 22 characters excluding extension, unless
  exceptionally clear
- Hard to pronounce
- Easily misspelled
- Hyphenated
- Numeric
- Grammatically awkward
- Misleading about service scope
- Trademark-confusing
- Similar to existing competitor brands
- Dependent on a low-quality extension
- Too narrow for the stated expansion plan
- Clearly designed only to manipulate rankings

### Domain Naming Evaluation

Score 0 to 5 for each category:

| Criterion | Question |
|---|---|
| Query relevance | Does it clearly reflect a validated service-location theme? |
| Brand usability | Can it be spoken, remembered, and trusted? |
| Expansion fit | Does it fit the business’s 12-36 month plan? |
| Conversion clarity | Will a local prospect understand the offer immediately? |
| Legal safety | Is trademark/confusion risk low? |
| Technical cleanliness | Is history/index/backlink risk low? |
| Acquisition value | Is price justified by expected business value? |

```text
Domain Candidate Score =
Query Relevance
+ Brand Usability
+ Expansion Fit
+ Conversion Clarity
+ Legal Safety
+ Technical Cleanliness
+ Acquisition Value
```

Maximum score: 35.

### Domain Decision Thresholds

| Score | Recommendation |
|---:|---|
| 29-35 | Strong shortlist candidate |
| 24-28 | Viable with stated caveats |
| 18-23 | Backup only |
| 0-17 | Reject |

---

## Phase 7: Domain Availability, History, and Risk Due Diligence

Agent F must investigate every shortlisted candidate.

### A. Availability and Acquisition

Record:

- Available / registered / for sale
- Registrar or marketplace
- Asking price
- Renewal cost
- Transfer restrictions
- Premium status
- Estimated total acquisition cost
- Comparable alternatives

### B. Ownership and Registration

Use lawful public data sources only.

Check:

- WHOIS/RDAP availability
- Creation date
- Expiry date
- Recent ownership/registrar changes, if visible
- Privacy status
- Suspicious listing patterns

Do not attempt to bypass privacy protections or obtain non-public registrant data.

### C. Historical Use

Review archived snapshots and other legitimate history sources.

Flag:

- Adult content
- Gambling
- Pharmacy
- Crypto scams
- Malware
- Scraped content
- Auto-generated pages
- Doorway pages
- Foreign-language spam unrelated to future use
- Link selling/PBN indicators
- Sudden topic changes
- Large redirect chains
- Reputation-damaging usage

### D. Indexation and Search Footprint

Check:

```text
site:example.com
"example.com"
"brand name"
```

Record:

- Indexed pages
- Cached remnants or historical mentions
- Spam results
- Existing branded queries
- Past reputation complaints
- Manual-action indications if supplied by owner through Search Console

Do not claim a manual action exists unless documented.

### E. Backlink Profile

If tools are available, check:

- Referring domains
- Link relevance
- Anchor-text concentration
- Foreign-language or irrelevant links
- Sitewide links
- Spam indicators
- Sudden historical growth/decline
- Redirect history
- Link-network patterns

Classify:

```text
clean
low-risk
caution
high-risk
reject
```

### F. Trademark and Naming Safety

Search relevant official trademark registries where applicable and conduct broad
web searches.

Check for:

- Exact trademark conflicts
- Confusing similarity
- Local competitor similarity
- Franchise restrictions
- Regulated profession terms
- Government/municipality implied affiliation
- Geographic-indication restrictions where applicable

This is not legal advice. Escalate medium/high-risk names to qualified legal counsel.

### Domain Risk Decision Rules

Reject a domain if:

- It has unresolved trademark risk.
- It has strong evidence of historical spam or abuse.
- It is likely to confuse users with a competitor.
- It has a misleading service/geographic claim.
- Its price cannot be justified by lead economics.
- It conflicts with the user’s expansion or brand plan.

---

## Phase 8: Financial Decision Model

The Orchestrator must not recommend a premium domain without a basic business case.

### Inputs

```text
Domain acquisition cost
Annual renewal cost
Website build cost
Local SEO setup cost
Monthly operating cost
Expected monthly qualified leads
Lead-to-sale rate
Average gross profit per sale
Expected time to traction
Risk-adjusted confidence
```

### Core Calculations

```text
Monthly Gross Profit from SEO Leads =
Qualified Leads
x Lead-to-Sale Rate
x Average Gross Profit per Sale
```

```text
Estimated Payback Months =
Initial Investment
/
Monthly Gross Profit from SEO Leads
```

```text
Risk-Adjusted Expected Value =
Expected Value
x Confidence Multiplier
```

Use a conservative confidence multiplier such as:

```text
High confidence: 0.70 to 0.85
Medium confidence: 0.40 to 0.69
Low confidence: 0.10 to 0.39
```

Do not present speculative revenue as guaranteed.
Use ranges and identify assumptions.

### Domain Acquisition Rules

- Prefer a clean hand-registration or low-cost acquisition when possible.
- Pay a premium only where the name provides durable brand, conversion, or
  strategic value independent of rankings.
- Do not spend a large portion of the launch budget on a domain while leaving
  insufficient funds for real operations, content, reviews, website quality,
  tracking, and local promotion.
- Compare premium EMD cost against a brandable `.com` plus the investment needed
  for better local assets.

---

## Phase 9: Select the Domain Architecture

Choose one of the following and explain why.

### Option 1: One EMD for one true local business

Use when the business will remain focused on a single service and location.

### Option 2: One brandable root domain with service and city directories

Use when coverage will expand.

```text
example.com/
example.com/services/
example.com/services/roof-repair/
example.com/locations/
example.com/locations/mesa-az/
example.com/roof-repair/mesa-az/
```

Do not create pages for locations with no genuine service delivery, unique local
value, or business purpose.

### Option 3: Brand domain plus a defensive EMD redirect

Use only when:

- The EMD is clean and affordable.
- The brandable domain is the canonical public brand.
- The redirect is simple, permanent, and does not create duplicate sites.
- There is no attempt to build multiple thin sites for the same market.

### Option 4: Separate lead-generation asset

Use only with transparent representation and legitimate provider relationships.
The site must not masquerade as a local company that does not exist.

---

## Phase 10: Post-Acquisition Local SEO Execution

Agent G creates the launch plan after a domain is selected.

### A. Establish Brand and Trust

Create:

- Clear business name
- Consistent NAP where applicable
- About page with real operators/team
- Licensing and insurance evidence where relevant
- Contact page
- Service-area clarity
- Privacy policy and terms
- Lead-disclosure language where the site is a referral asset
- Real business photos, work examples, and customer proof

### B. Build High-Intent Pages

Create pages for:

1. Primary service
2. Highest-value subservice
3. Emergency service where genuinely offered
4. Service process
5. Pricing/estimate expectations where appropriate
6. Reviews and case studies
7. Location page only where it adds real local value
8. FAQ pages responding to real customer questions

Every page must have:

- A unique purpose
- Clear service relevance
- Original, helpful content
- Real local context
- Strong conversion action
- Internal links to related services/locations
- No duplicate or spun city content

### C. Google Business Profile Alignment

For eligible legitimate businesses:

- Use the real-world business name.
- Select accurate categories.
- Complete services, service area, hours, phone, website, appointment links,
  descriptions, and attributes.
- Add authentic photos and updates as appropriate.
- Request genuine reviews through compliant workflows.
- Respond to reviews professionally.
- Never add geographic keywords to the business name unless they are part of
  the true registered/real-world name.

### D. Local Authority and Prominence

Prioritize:

- Trusted local directories and industry citations
- Chamber, association, and supplier listings
- Local sponsorships and community partnerships
- Local press where genuinely newsworthy
- Project features
- Expert contributions
- Vendor/partner links
- Review acquisition from real customers
- Local social proof and branded mentions

### E. Structured Data

Implement valid structured data where applicable:

- `LocalBusiness` or the most specific relevant subtype
- Organization identity
- Contact information
- Address or service-area details only when accurate
- Opening hours
- SameAs profiles
- Service information where supported and truthful
- Review markup only when compliant and visible on the page

Validate through supported rich-result and URL-inspection tools where available.

### F. Measurement

Track:

- Organic impressions and clicks
- Indexed URLs
- Keyword movement by location
- Local-pack/grid movement
- Calls
- Forms
- Bookings
- Qualified leads
- Lead-to-sale rate
- Cost per qualified lead
- Review velocity and rating
- Referring domains/local mentions
- Branded search growth
- Revenue attributable to organic/local visibility

---

# Execution Playbook (verified, agentic)

This is the concrete, repeatable pipeline validated by a live run. Follow it in
order. It is optimized for parallel agents, low cost, and exact reproduction.

## Step 1 — Normalize the service and geo terms

- Build the service lexicon from local search language, not generic/US terms.
  UK example: `tree removal`, `tree surgeon`, `tree surgery`, `tree felling`,
  `tree lopping`, `stump grinding`, `arborist`, `tree care`.
- Normalize every term to a domain token: lowercase, no spaces, no hyphens.
  Hyphens must be rejected per the Candidate Generation Constraints.
- List the geo layers: country/ccTLD, region/metro, city, suburb.
- Choose the ccTLD strategy before searching:
  - `.co.uk` is the primary UK EMD asset.
  - `.uk` is a second-level registration; registrants must hold the matching
    `.co.uk` (Nominet rules). Check it, but treat it as a companion, not a
    standalone buy.
  - `.com` for global/brand head terms.

## Step 2 — Build the candidate matrix in tiers, then de-duplicate

- Tier 1 head terms: `{service}.{tld}`
- Tier 2 city EMDs: `{service}{city}.{tld}` and `{city}{service}.{tld}`
- Tier 3 partial/hybrid: `{city}{service}pros.{tld}`, `{metro}{service}.{tld}`
- De-duplicate on the exact domain string before any availability check.

## Step 3 — Check availability with public RDAP (no key, no cost)

| Extension(s) | RDAP endpoint | 200 | 404 |
|---|---|---|---|
| `.co.uk`, `.uk` | `https://rdap.nominet.uk/uk/domain/<domain>` | registered | available |
| `.com` | `https://rdap.verisign.com/com/v1/domain/<domain>` | registered | available |

- Treat `200` = registered and `404` = available as **definitive**.
- Treat `429`, `503`, timeouts, and network errors as **non-definitive**.
- Never decide on a non-definitive status. Collect statuses, then run a retry
  pass over non-definitive rows only, with exponential backoff.
- Concurrency: 4–6 workers. Higher rates trigger transient errors with little
  time saved.
- Fallback where RDAP is unavailable: `whois <domain>` and parse the response,
  or a registrar availability API.
- Cache every result to CSV. Reruns must only check new candidates.
- A reusable implementation is provided at `assets/rdap_availability_check.py`.

## Step 3.5 — Separate "available" from "good"

Availability is not quality. Do not stop at the availability list. Only
available candidates proceed to scoring and due diligence.

## Step 4 — Score the survivors only

Apply Phase 3 (market), Phase 5 (local pack), Phase 6 (naming), and Phase 8
(economics) to the available shortlist. Reject candidates that are:

- low commercial intent (informational-only tokens),
- geo/service mismatches the business cannot genuinely serve,
- trademark-confusing or competitor-similar (Phase 7F).

## Step 5 — Due diligence the shortlist (Phase 7)

Run history, indexation, backlink, and trademark checks. Classify each as
clean / caution / reject before any purchase recommendation.

## Step 6 — Report

Produce the Required Deliverables below, plus the raw availability CSV as the
evidence log.

## Efficiency rules

- De-duplicate before checking; never re-check a cached domain.
- Retry only non-definitive statuses, never definitive ones.
- Two-phase cost model: bulk availability is cheap and parallel; scoring and
  due diligence are expensive and run only on survivors.
- Keep one canonical CSV as the evidence log; derive all tables from it.

## Field notes from a live run (UK tree removal, 2026)

- 459 candidates checked via RDAP in about 3 minutes at 6 workers.
- 339 available, 120 registered.
- Every generic head term was registered except `treelopping` and
  `treefellings` — so head-term EMDs were effectively unavailable.
- The real opportunity was city EMDs: 334 available `.co.uk` city matches.
- Token quality varied: `{city}treefelling`, `{city}treelopping`, and
  `{city}treeremoval` are the strongest commercial EMDs; `arborist` availability
  was high but commercial intent in the UK is lower.
- Transient `URLError`/`429` occurred at concurrency 6. A retry pass over
  non-definitive statuses resolved all of them — always include the retry pass.

---

# Output Requirements

The final report must be practical and decision-ready.

## Required Deliverables

### 1. Executive Decision

Include:

- Recommended strategy: EMD, PMD, brandable, hybrid, or no purchase
- Best domain candidate
- Backup candidates
- Clear recommendation: buy / negotiate / monitor / reject
- Confidence level
- Top reasons
- Key risks

### 2. Intake Summary

Include confirmed facts and explicit assumptions.

### 3. Market Opportunity Table

| Service + location | Intent | Market score | Organic opportunity | Local opportunity | Decision |
|---|---:|---:|---|---|---|

### 4. SERP Findings

For top opportunities, summarize:

- Who ranks
- Why they likely rank
- Weaknesses
- Unmet user needs
- Whether EMDs appear and why that observation is not proof of causation

### 5. Domain Shortlist Table

| Domain | Type | Availability/cost | Brand score | Risk status | Total score | Recommendation |
|---|---|---:|---:|---|---:|---|

### 6. Domain Risk Register

| Risk | Severity | Evidence | Mitigation | Decision impact |
|---|---|---|---|---|

### 7. Business Case

Include conservative assumptions, estimated payback range, and reasons the
model could underperform.

### 8. 90-Day Execution Plan

Use three phases:

- Days 1-30: domain, brand/entity foundation, technical site launch, core pages,
  tracking, Business Profile setup if eligible.
- Days 31-60: proof assets, reviews, citations, outreach, additional service
  content, conversion iteration.
- Days 61-90: local authority, case studies, expansion pages only where valid,
  technical audit, reporting, and prioritization.

### 9. Evidence Log

For every important claim, record:

```yaml
evidence:
  claim:
  source_type:
  source_url_or_tool:
  date_checked:
  confidence:
  notes:
```

---

# Quality-Control Checklist

Before presenting recommendations, Agent H must verify:

- [ ] The user answered the mandatory intake questions or approved assumptions.
- [ ] The service and geography are operationally legitimate.
- [ ] The analysis distinguishes organic ranking from local-pack ranking.
- [ ] The analysis does not claim EMDs override quality, authority, or local signals.
- [ ] Primary keywords have commercial intent.
- [ ] Search results were evaluated, not guessed.
- [ ] Domain names fit the expansion model.
- [ ] Trademark and competitor-confusion risks were checked.
- [ ] Domain history and backlink risks were checked or limitations disclosed.
- [ ] The financial recommendation is conservative.
- [ ] The plan does not use fake locations, fake profiles, deceptive reviews, or doorway pages.
- [ ] All data points have sources, dates, or confidence labels.
- [ ] The recommendation identifies a no-buy option when evidence is weak.

---

# Stop Conditions

Stop and request clarification if:

- The user will not disclose the business model or target geography.
- The service may be regulated and licensing status is unclear.
- The strategy requires false locations or misleading identities.
- The domain presents unresolved trademark risk.
- The user expects guaranteed rankings.
- Search demand or economics do not support the domain cost.
- The domain’s historical spam risk cannot be assessed sufficiently.
- The domain architecture conflicts materially with future expansion plans.

---

# Final Recommendation Language Templates

## Strong Buy

> Recommend acquiring `{domain}` if the verified acquisition cost remains at or
> below `{budget}`. It is a clean, readable service-location asset that matches
> the business’s single-market strategy. Its value is primarily branding,
> relevance clarity, memorability, and conversion support; it is not a
> guarantee of organic or Maps rankings.

## Conditional Buy

> `{domain}` is viable, but only if history and trademark checks remain clean and
> the acquisition cost stays within the calculated payback threshold. A
> brandable alternative should be retained as the fallback because the business
> has expansion plans beyond the domain’s geographic scope.

## Reject

> Do not acquire `{domain}`. The candidate has insufficient market opportunity,
> poor expansion fit, unresolved legal/history risk, or an acquisition cost that
> cannot be justified by conservative lead economics. Invest instead in a
> clean brandable domain and the local-entity assets that influence actual
> visibility and conversion.

---

# First User Message Template

Use this exact workflow opening when the skill is invoked:

> To identify the right EMD, PMD, or brandable alternative responsibly, first
> provide:
>
> 1. Business model: real local business, service-area business, lead-gen asset,
>    agency client, or other?
> 2. Primary service and highest-value subservices.
> 3. Target country, city, suburbs/neighborhoods, and true operating/service area.
> 4. Whether there is a verified physical location or service-area model.
> 5. Single-city versus multi-city expansion plans over the next 12-36 months.
> 6. Ideal customer and approximate job value or value per closed lead.
> 7. Existing website, Google Business Profile, competitors, and domains.
> 8. Domain purchase budget and acceptable extensions.
> 9. Brand/trademark words or competitors to avoid.
> 10. Main success metric: calls, forms, local-pack visibility, organic rankings,
>     lead resale, or brand launch.
>
> Once these details are available, the research team will validate demand,
> analyze organic and local competitors, generate domain candidates, check
> availability/history/legal risk, score the business case, and return a
> prioritized domain recommendation with a practical local SEO launch plan.

