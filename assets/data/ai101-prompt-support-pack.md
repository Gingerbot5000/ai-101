# AI-101 Prompt Support Pack

Purpose: provide ready-to-use demo inputs for prompts that need extra context.

How to use:
1. Pick the prompt category.
2. Run 2-3 targeted searches (or skip and use mock data when offline).
3. Paste the facts or mock block into your AI chat before running the full prompt.

Important:
- All mock data below is synthetic and for demonstration only.
- Healthcare and legal sections are not professional advice.

## Hospitality

Targeted searches:
1. `site:weather.gov Petersburg IL forecast tomorrow`
2. `Petersburg IL events this weekend site:eventbrite.com OR site:visitspringfieldillinois.com`
3. `Springfield IL road closures today official`

Mock data:
```text
Hotel: Prairie Lantern Inn (32 rooms)
Date: Friday
Occupancy tonight: 84% (27/32)
Expected weather tomorrow: 58F high, 42F low, 60% rain chance
Guest mix: 6 business, 12 leisure couples, 9 family bookings
Known disruptions: Main lobby elevator maintenance 10:00-13:00
Front desk priorities: early check-in messaging, rainy-day local recommendations, parking overflow notice
```

## Real Estate

Targeted searches:
1. `site:fred.stlouisfed.org 30 year fixed mortgage average`
2. `Petersburg IL recently sold homes last 90 days`
3. `site:realtor.com Petersburg IL median days on market`

Mock data:
```text
Subject property: 3 bed, 2 bath, 1,860 sqft, built 1998, updated kitchen 2023
Lot: 0.28 acres, attached 2-car garage, school district PORTA
Seller timeline: list in 10 days, target close in 45 days
Comparable sales:
- 412 Meadow Ln: 1,790 sqft, sold $264,000, DOM 21
- 228 Oak Crest Dr: 1,920 sqft, sold $279,500, DOM 18
- 505 Lincoln Ave: 1,845 sqft, sold $271,000, DOM 26
```

## Trades

Targeted searches:
1. `12/2 NM-B wire 250 ft price Illinois`
2. `20 amp GFCI receptacle retail price`
3. `electrical permit fee Petersburg IL residential`

Mock data:
```text
Job type: residential kitchen and basement electrical refresh
Scope:
1) Replace 8 standard outlets with tamper-resistant outlets
2) Add 2 GFCI outlets near sink area
3) Install 4 recessed LED fixtures in basement
4) Troubleshoot one non-working switch loop
Crew: 1 licensed electrician + 1 helper
Labor assumption: 11-14 total crew hours
Material assumptions:
- 10 duplex outlets
- 2 GFCI outlets
- 4 LED recessed lights
- 150 ft 14/2 wire
- 50 ft 12/2 wire
```

## Libraries

Targeted searches:
1. `site:imls.gov grant opportunities public library`
2. `site:illinoishumanities.org grants`
3. `site:librarytechnology.org digital literacy program examples`

Mock data:
```text
Library profile: Riverbend Public Library
Service population: 5,200
Annual circulation: 41,000
Staffing: 6 FTE
Priority goals:
- Digital literacy for adults 45+
- Homework support for grades 6-10
- AI basics workshop pilot
Constraints:
- Max local match budget: $8,000
- Programming room capacity: 24
```

## Retail

Targeted searches:
1. `site:weather.gov Petersburg IL 7 day forecast`
2. `Springfield IL weekend events calendar`
3. `local boutique pricing Springfield IL [product type]`

Mock data:
```text
Store: Maple & Main Gifts
Week summary:
Foot traffic: 1,140
Conversion rate: 28%
Top SKUs:
- Candle-12oz-Lavender | On hand 24 | Last 7d sold 31 | Unit cost $7.20 | Price $18
- Mug-Handmade-Blue | On hand 18 | Last 7d sold 22 | Unit cost $9.10 | Price $24
- Notebook-Linen-A5 | On hand 42 | Last 7d sold 27 | Unit cost $4.40 | Price $14
Upcoming demand risk: weekend artisan market expected to increase traffic 20-30%
```

## Job Seekers

Targeted searches:
1. `[Company Name] latest press release investor relations`
2. `[Company Name] product launch 2025 2026`
3. `[Role Title] salary range [City, State]`

Mock data:
```text
Candidate snapshot:
Name: Alex Rivera
Target role: Operations Analyst
Experience highlights:
- Reduced weekly reporting time by 38% using automation
- Built KPI dashboard used by 4 department leads
- Managed vendor projects with $240k annual spend
Job posting summary:
- Requires SQL, stakeholder communication, and process mapping
- Prefers Tableau/Power BI
- Salary listed: $68,000-$82,000
```

## Education

Targeted searches:
1. `site:weather.gov [district city] school day forecast`
2. `[District Name] academic calendar 2026`
3. `[State] middle school science standards grade 7`

Mock data:
```text
Class profile:
Grade: 7
Subject: Life Science
Class size: 26
Learning objective: Explain ecosystem energy flow
Constraints:
- 45 minute period
- 4 English learners
- 3 students with reading accommodations
Available materials:
- Projector
- Whiteboard
- Printed worksheet (1 page)
```

## Healthcare

Targeted searches:
1. `site:cdc.gov respiratory virus data tracker`
2. `site:dph.illinois.gov influenza surveillance`
3. `site:weather.gov Petersburg IL 7 day forecast`

Mock data:
```text
De-identified outpatient visit note:
Visit date: 2026-03-10
Chief complaint: sore throat, fatigue, mild cough x3 days
Vitals: BP 126/82, HR 84, Temp 99.2F, SpO2 97%
History: no chest pain, no shortness of breath, no medication allergies listed
Assessment in raw note: likely viral upper respiratory illness
Missing fields to flag: pharmacy preference, work note request status, follow-up interval confirmation
Administrative ask: produce SOAP draft + patient-friendly summary
```

## Legal

Targeted searches:
1. `site:ilga.gov [topic] statute`
2. `[issue] case summary Illinois appellate court`
3. `site:law.justia.com [issue] contract clause examples`

Mock data:
```text
Contract excerpt (mock):
Term: 24 months with auto-renewal unless 60-day notice
Limitation of liability: capped at 3 months of fees
Indemnity: vendor seeks broad defense obligation for all third-party claims
Payment terms: net-15 with 2% monthly late fee
Termination: customer may terminate only for uncured material breach after 45 days
Confidentiality: unilateral (customer obligations only)
Task objective: identify risk areas and propose negotiation edits
```

## Local News

Targeted searches:
1. `Petersburg IL local news today`
2. `site:weather.gov Petersburg IL current conditions`
3. `SPY price QQQ price AAPL price marketwatch`

Mock data:
```text
Mock local newsroom feed:
Headline 1: City council approves downtown sidewalk repair budget
Headline 2: School board posts revised spring testing schedule
Headline 3: County announces temporary road work near Route 97
Headline 4: Chamber of commerce releases weekend event lineup
Headline 5: Public library launches free digital-skills classes
Weather snapshot: 61F, light winds, rain chance 30%
Market snapshot: SPY 562.10, QQQ 488.34, AAPL 212.47
```
