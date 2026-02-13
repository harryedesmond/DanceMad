# DanceMad — TASKS

## How to use this file

- Work top to bottom, one task at a time
- Check off tasks as you complete them
- Each task has scope, acceptance criteria, and test steps
- Don't skip ahead or combine tasks unless they're trivial
- After each task: verify it works before moving on

---

## Phase 1 — Foundation

### Task 1.1: Project scaffolding

**Scope:** Create Next.js project with Tailwind, push to GitHub, deploy to Cloudflare Pages.

**Acceptance criteria:**
- [ ] Next.js 14 (App Router) project initialised
- [ ] Tailwind CSS configured and working
- [ ] GitHub repo created, code pushed
- [ ] Cloudflare Pages project connected to GitHub repo
- [ ] Auto-deploy triggers on push to `main`
- [ ] Live Cloudflare URL shows the default Next.js page

**Test steps:**
1. Run `npm run dev` locally — see default page
2. Push to `main` — Cloudflare build triggers
3. Visit Cloudflare Pages URL — see the same page live

---

### Task 1.2: Supabase setup + schema

**Scope:** Create Supabase project, define core tables, verify connection from Next.js.

**Acceptance criteria:**
- [ ] Supabase project created (free tier)
- [ ] Tables created: `cities`, `schools`, `classes`
- [ ] `styles` enum or lookup values defined (salsa, bachata, kizomba, zouk, semba, afro-latin, reggaeton, other)
- [ ] Supabase env vars added to Next.js (`.env.local` + Cloudflare Pages env settings)
- [ ] Can query Supabase from Next.js (e.g. fetch cities list on homepage)

**Schema:**
```sql
cities: id, name, slug, country, country_code, lat, lng, timezone, image_url, created_at

schools: id, city_id (FK), name, slug, address, lat, lng, website, phone, description, source_url, created_at, updated_at

classes: id, school_id (FK), style, level, day_of_week, start_time, end_time, price_info, notes, last_scraped_at, created_at, updated_at

-- style: enum (salsa, bachata, kizomba, zouk, semba, afro-latin, reggaeton, other)
-- level: enum (beginner, intermediate, advanced, open)
-- day_of_week: integer 0-6 (Monday=0)
```

**Test steps:**
1. Insert a test city row via Supabase dashboard
2. Fetch it from Next.js API route or server component
3. See the city name rendered on homepage
4. Delete test data

---

### Task 1.3: Seed cities table

**Scope:** Populate `cities` table with the initial launch cities.

**Acceptance criteria:**
- [ ] 12 cities seeded with name, slug, country, country_code, lat, lng, timezone
- [ ] Slugs are URL-friendly (e.g. `london`, `new-york`, `mexico-city`, `medellin`)

**Cities to seed:**
London, Bristol, Southampton, Manchester, New York, Miami, Los Angeles, Barcelona, Berlin, Medellín, Cali, Mexico City

**Test steps:**
1. Query `SELECT * FROM cities` in Supabase — 12 rows returned
2. Each row has all required fields populated
3. No duplicate slugs

---

### Task 1.4: Homepage — city list

**Scope:** Homepage displays all cities as clickable cards.

**Acceptance criteria:**
- [ ] Homepage fetches cities from Supabase
- [ ] Each city displayed as a card (name, country, country flag emoji)
- [ ] Cards link to `/[city-slug]`
- [ ] Mobile-first layout (single column on mobile, grid on desktop)
- [ ] Dark theme, basic Tailwind styling
- [ ] Sorted alphabetically or grouped by region

**Test steps:**
1. Visit homepage — see 12 city cards
2. Click a city — navigates to `/london` (or equivalent slug)
3. Resize to mobile width — cards stack vertically
4. Deploy to Cloudflare — works live

---

### Task 1.5: City page — basic layout

**Scope:** City detail page showing city name and placeholder for listings. No real class data yet.

**Acceptance criteria:**
- [ ] Dynamic route `/[city-slug]` created
- [ ] Page fetches city data from Supabase by slug
- [ ] Displays city name, country as page header
- [ ] Placeholder text: "Classes coming soon" (until scraped data exists)
- [ ] 404 for invalid slugs
- [ ] Page title set dynamically (`<title>Salsa Classes in London — DanceMad</title>`)

**Test steps:**
1. Visit `/london` — see "London, United Kingdom" header
2. Visit `/invalid-slug` — see 404
3. Check page `<title>` in browser tab — correct
4. Deploy — works on Cloudflare

---

### Task 1.6: Scraper — research sources

**Scope:** Research and document scrapable data sources for first 3 cities (London, Bristol, NYC). No code yet — just a list of sources.

**Acceptance criteria:**
- [ ] For each city: list of 3–5 scrapable sources (school websites, directories, Google Maps, Facebook pages)
- [ ] Note per source: what data is available (school name, address, class schedule, style, level, price)
- [ ] Note per source: scraping difficulty (simple HTML, JS-rendered, API available, needs Playwright)
- [ ] Document in a `SCRAPING_SOURCES.md` file

**Test steps:**
1. Review the document — each city has viable sources
2. At least one source per city is simple HTML (no JS rendering needed)
3. Estimated total: 10+ schools per city achievable

---

### Task 1.7: Scraper — build first pipeline

**Scope:** Python script that scrapes one source for one city and upserts to Supabase.

**Acceptance criteria:**
- [ ] Python script in `/scripts` directory
- [ ] Scrapes one source for London (pick the easiest from Task 1.6)
- [ ] Extracts: school name, address, website, classes (style, level, day, time)
- [ ] Upserts to Supabase `schools` and `classes` tables
- [ ] Sets `last_scraped_at` on each record
- [ ] Handles errors gracefully (logs failures, doesn't crash on one bad record)
- [ ] Respects rate limits (1-2 second delay between requests)

**Test steps:**
1. Run script locally — see console output of scraped schools
2. Check Supabase — schools and classes rows created
3. Run again — upserts (no duplicates), `last_scraped_at` updated
4. Break one source URL — script logs error, continues with others

---

### Task 1.8: Scraper — expand to 3 cities

**Scope:** Extend scraping to cover London, Bristol, NYC with 10+ schools each.

**Acceptance criteria:**
- [ ] Scrapers work for all 3 cities
- [ ] Each city has 10+ schools in Supabase
- [ ] Each school has at least 1 class record
- [ ] Data is reasonable (no garbage, no test data left over)
- [ ] Can re-run scrapers without creating duplicates

**Test steps:**
1. Run all scrapers
2. Query: `SELECT cities.name, COUNT(schools.id) FROM cities JOIN schools ON cities.id = schools.city_id GROUP BY cities.name` — each city has 10+
3. Spot-check 3 random schools — data matches source website

---

### Task 1.9: City page — real listings

**Scope:** City page displays real scraped data grouped by school.

**Acceptance criteria:**
- [ ] City page fetches schools + classes for that city from Supabase
- [ ] Schools displayed as cards with: name, address, website link
- [ ] Under each school: list of classes (style, level, day, time, price if available)
- [ ] Style shown as coloured tag/badge (salsa = red, bachata = purple, etc.)
- [ ] "Last updated X days ago" freshness indicator per school
- [ ] If no data: show "No classes found yet" message

**Test steps:**
1. Visit `/london` — see real schools with real class data
2. Each school card has name, address, at least 1 class
3. Style badges are coloured and readable
4. Visit a city with no data — see empty state message
5. Deploy — works on Cloudflare

---

### Task 1.10: Phase 1 review

**Scope:** Verify everything works end-to-end on Cloudflare Pages.

**Acceptance criteria:**
- [ ] Homepage shows 12 cities
- [ ] 3 cities (London, Bristol, NYC) have real scraped data
- [ ] City pages display schools + classes correctly
- [ ] Remaining 9 cities show "coming soon" placeholder
- [ ] Site works on mobile
- [ ] No console errors
- [ ] Deploy is green on Cloudflare

**Test steps:**
1. Full walkthrough on desktop and mobile
2. Check Cloudflare deploy logs — no build errors
3. Share URL with one person — they can browse without confusion

---

## Phase 2 — Search, filter & usability

### Task 2.1: Filter by dance style

**Scope:** Add style filter to city page.

**Acceptance criteria:**
- [ ] Multi-select filter for dance styles on city page
- [ ] Filters applied via URL query params (`/london?style=salsa,bachata`)
- [ ] Listings update to show only matching classes
- [ ] If school has no matching classes, hide the school
- [ ] "Clear filters" option
- [ ] Filters work without page reload (client-side)

**Test steps:**
1. Select "salsa" — only salsa classes shown
2. Select "salsa" + "bachata" — both shown
3. Copy URL with params, paste in new tab — same filter state
4. Clear filters — all classes return

---

### Task 2.2: Filter by level

**Scope:** Add level filter to city page.

**Acceptance criteria:**
- [ ] Multi-select filter for levels (beginner, intermediate, advanced, open)
- [ ] Combines with style filter via URL params
- [ ] Same UX pattern as style filter

**Test steps:**
1. Select "beginner" — only beginner classes shown
2. Combine "salsa" + "beginner" — only beginner salsa classes shown
3. URL params reflect both filters

---

### Task 2.3: Filter by day of week

**Scope:** Add day filter to city page.

**Acceptance criteria:**
- [ ] Single or multi-select for days (Mon–Sun)
- [ ] Combines with existing filters
- [ ] URL param: `day=1,3` (Monday, Wednesday)

**Test steps:**
1. Select "Monday" — only Monday classes shown
2. Combine all three filter types — correct intersection shown
3. URL is shareable with all filters

---

### Task 2.4: Feedback widget

**Scope:** Floating feedback button on all pages, stores submissions in Supabase.

**Acceptance criteria:**
- [ ] Floating button bottom-right corner on every page
- [ ] Click opens a small modal/drawer with: message (required), email (optional)
- [ ] Page URL auto-captured
- [ ] Submission creates row in Supabase `feedback` table
- [ ] Success confirmation shown to user
- [ ] No login required
- [ ] `feedback` table: id, message, email, page_url, created_at

**Test steps:**
1. Click feedback button on any page — form appears
2. Submit with message only — success shown, row in Supabase
3. Submit with message + email — both stored
4. Check `page_url` is correct in Supabase

---

### Task 2.5: City scene guides

**Scope:** Write and add original content intros for each city page.

**Acceptance criteria:**
- [ ] 200–400 word scene guide per city with data
- [ ] Stored in Supabase `cities` table (new `scene_guide` text column) or as MDX
- [ ] Displayed as hero section above listings on city page
- [ ] Covers: scene size, popular styles, notable venues, best nights, vibe
- [ ] Written in DanceMad voice (friendly, opinionated, helpful — not corporate)

**Test steps:**
1. Visit city page — scene guide visible above listings
2. Content is original, not scraped
3. Read through — informative and engaging

---

### Task 2.6: Static pages

**Scope:** About, Contact, Privacy Policy pages.

**Acceptance criteria:**
- [ ] `/about` — what DanceMad is, who built it, why
- [ ] `/contact` — how to reach us (email or feedback form link)
- [ ] `/privacy` — GDPR-aware privacy policy (template is fine)
- [ ] All linked from footer on every page
- [ ] Basic styling consistent with rest of site

**Test steps:**
1. Click each link in footer — correct page loads
2. Privacy policy mentions data handling, cookies, no personal data stored
3. Deploy — all pages work on Cloudflare

---

### Task 2.7: Expand scraping to 10+ cities

**Scope:** Run scrapers for remaining launch cities, seed data.

**Acceptance criteria:**
- [ ] Scrapers built/adapted for: Miami, Barcelona, Berlin, Medellín, Cali, Mexico City, Lisbon, Southampton, Manchester
- [ ] Each city has 10+ schools with class data
- [ ] Scene guides written for each new city
- [ ] All visible on live site

**Test steps:**
1. Visit each city page — real data displayed
2. Filters work correctly with new data
3. No cities stuck on "coming soon"

---

### Task 2.8: Phase 2 review

**Scope:** Full usability check.

**Acceptance criteria:**
- [ ] All filters work individually and combined
- [ ] 10+ cities with real data + scene guides
- [ ] Feedback widget works
- [ ] Static pages exist and are linked
- [ ] Site is usable enough to share with friends for testing

**Test steps:**
1. Full walkthrough: pick a city, filter by style + level + day, read scene guide, submit feedback
2. Test on mobile — everything works
3. Share with 2–3 people — collect feedback

---

## Phase 3 — SEO & polish

_Tasks to be broken out when Phase 2 is complete._

Key work:
- Dynamic meta tags + OpenGraph per page
- Sitemap generation
- Structured data (JSON-LD)
- robots.txt
- Lighthouse 90+ mobile
- Image optimisation
- Empty/error/loading states
- Design consistency pass

---

## Phase 4 — Go live

_Tasks to be broken out when Phase 3 is complete._

Key work:
- Buy domain (Cloudflare Registrar)
- DNS configuration
- Stripe account + Payment Link
- Donate button in footer/sidebar
- Google Search Console setup + sitemap submission
- Launch: share in dance communities

---

## Phase 5 — Monetise

_Tasks to be broken out when Phase 4 is complete._

Key work:
- Cookie consent banner
- AdSense application
- Ad placement implementation
- Revenue monitoring
