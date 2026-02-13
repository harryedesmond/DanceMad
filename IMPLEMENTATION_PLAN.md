# DanceMad — IMPLEMENTATION PLAN

## Guiding principle

Build the site first. Monetise once there's something worth paying for. Ship something ugly that works before something pretty that doesn't.

---

## Phase 1 — Foundation (data + DB + basic site)

**Goal:** Scraped data for 3 cities, visible on a working site deployed to Cloudflare Pages.

### 1.1 Project setup
- [ ] Init Next.js 14 (App Router) + Tailwind CSS
- [ ] GitHub repo, Cloudflare Pages connected (auto-deploy on push)
- [ ] Supabase project created, connection working from Next.js
- [ ] Basic project structure: `/app`, `/lib`, `/scripts`

### 1.2 Database schema
- [ ] Create tables in Supabase: `cities`, `schools`, `classes`, `styles` (enum/lookup)
- [ ] Seed `cities` table with initial 3 cities (London, Bristol, NYC)
- [ ] Seed `styles` lookup (salsa, bachata, kizomba, zouk, semba, afro-latin, reggaeton, other)

### 1.3 Scraping pipeline (Python)
- [ ] Research scrapable sources for London, Bristol, NYC (Google Maps, school websites, Facebook events, existing directories)
- [ ] Build scraper for first source → outputs clean JSON
- [ ] Build upsert script: JSON → Supabase `schools` + `classes` tables
- [ ] Add `last_scraped_at` timestamp on every record
- [ ] Test: 3 cities each have 10+ schools with class data

### 1.4 Basic city pages
- [ ] Homepage: list of cities (cards with name + country + class count)
- [ ] City page (`/[city-slug]`): list of schools + classes, grouped by school
- [ ] Basic Tailwind styling — dark theme, card-based, mobile-first
- [ ] Deploy to Cloudflare Pages, verify it works

**Done when:** You can visit the live Cloudflare URL, click a city, and see real scraped class listings.

---

## Phase 2 — Search, filter & usability

**Goal:** Users can actually find what they want. Site feels usable, not just a data dump.

### 2.1 Filtering
- [ ] Filter by dance style (multi-select)
- [ ] Filter by level (beginner/intermediate/advanced/open)
- [ ] Filter by day of week
- [ ] Filters work via URL params (shareable, SEO-friendly)

### 2.2 City scene guides (content)
- [ ] Write 200–400 word intro per city ("London's salsa scene is one of Europe's biggest...")
- [ ] Add to city page as hero section above listings
- [ ] This is critical for SEO + future AdSense approval

### 2.3 Feedback widget
- [ ] Floating button (bottom-right), opens simple form
- [ ] Fields: message (required), email (optional), page URL (auto-captured)
- [ ] Submissions go to Supabase `feedback` table
- [ ] No login required

### 2.4 Static pages
- [ ] About page (what is DanceMad, who built it)
- [ ] Contact page
- [ ] Privacy Policy (template, GDPR-aware)

### 2.5 Expand to 10–12 cities
- [ ] Run scrapers for remaining launch cities (Miami, Barcelona, Berlin, Medellín, Cali, Mexico City, Lisbon, Southampton, Manchester)
- [ ] Write scene guides for each
- [ ] Verify data quality per city (minimum 10 schools each)

**Done when:** All filters work, 10+ cities have data + scene guides, feedback button works, static pages exist.

---

## Phase 3 — SEO & polish

**Goal:** Site is ready to be shared publicly and found via Google.

### 3.1 SEO
- [ ] Dynamic `<title>` and `<meta description>` per city page (e.g. "Salsa Classes in London — DanceMad")
- [ ] OpenGraph + Twitter card meta tags
- [ ] Sitemap generation (`/sitemap.xml`)
- [ ] Structured data (JSON-LD) for local business listings where possible
- [ ] `robots.txt`

### 3.2 Performance
- [ ] Static generation (SSG) for city pages where possible
- [ ] Image optimisation (city hero images)
- [ ] Lighthouse audit: target 90+ on mobile
- [ ] Data freshness indicator on listings ("Last updated 3 days ago")

### 3.3 Design polish
- [ ] Consistent typography, spacing, colour
- [ ] Empty states (city with no classes yet)
- [ ] Error states (scraper failed, no data)
- [ ] Loading states
- [ ] Responsive: test on phone, tablet, desktop

**Done when:** Lighthouse 90+ mobile, all city pages have proper meta tags, sitemap exists, site looks good enough to tweet about.

---

## Phase 4 — Go live (domain + donations)

**Goal:** Real URL, real donations, real users.

### 4.1 Domain
- [ ] Buy domain via Cloudflare Registrar
- [ ] Configure DNS (point to Cloudflare Pages)
- [ ] Verify HTTPS working

### 4.2 Stripe donations
- [ ] Create Stripe account
- [ ] Create Payment Link ("Support DanceMad — pay what you want")
- [ ] Embed as button in footer/sidebar of every page
- [ ] Test: complete a real donation end-to-end

### 4.3 Google Search Console
- [ ] Verify domain ownership
- [ ] Submit sitemap
- [ ] Monitor indexing

### 4.4 Launch
- [ ] Share in dance communities (Reddit r/salsa, Facebook salsa groups, dance forums)
- [ ] Post on social media
- [ ] Monitor feedback submissions

**Done when:** Site is live on custom domain, Stripe donations work, submitted to Google for indexing, shared with real people.

---

## Phase 5 — Monetise (ads)

**Goal:** AdSense approved, ads rendering, earning revenue.

### 5.1 AdSense
- [ ] Ensure all city pages have original scene guide content (not just scraped data)
- [ ] Cookie consent banner implemented
- [ ] Apply for Google AdSense
- [ ] If rejected: review feedback, improve content, reapply
- [ ] Once approved: add ad placements (sidebar, between listings)
- [ ] Keep ads non-intrusive — don't sacrifice UX for ad revenue

**Done when:** AdSense approved and ads rendering on city pages alongside donations.

---

## Risks & mitigations

| Risk | Mitigation |
|------|------------|
| Scraping breaks / data goes stale | `last_scraped_at` field, freshness indicator shown to users, manual override |
| Thin content per city (< 10 schools) | Start only with cities that have 15+ scrapable schools; supplement with curated guides |
| Cloudflare Pages SSR limitations | Use SSG (static generation) for city pages; only use SSR if absolutely needed |
| AdSense rejection | Write genuine scene guides, ensure enough original content, don't apply too early |
| Low traffic at launch | SEO-first architecture, share in dance communities, local Facebook groups |
| Scope creep | Stick to TASKS.md, one task at a time, no features not in the plan |

---

## What's deliberately NOT in this plan (v2+)

- User accounts / login
- Instructor dashboards
- Map view
- Reviews / ratings
- Real-time class availability
- Native mobile app
- Booking / payments to instructors
- Email newsletter
