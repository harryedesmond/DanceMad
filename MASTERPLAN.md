# DanceMad — MASTERPLAN

## What we're building

A salsa & Latin dance class directory — think Nomad List meets ClassPass but community-led, scrappy, and global. Users find classes in 10–20 cities worldwide, filtered by style/level/location. Revenue from Google Ads + optional Stripe charitable donations (not class bookings).

Vibe: Pieter Levels — fast, useful, SEO-first, personality over polish, ship daily.

## Who it's for

**Primary user:** Dancers (especially travellers/expats) looking for salsa/bachata/kizomba classes in a new city.

**Secondary:** Local dancers discovering new classes in their own city.

**Not building for (yet):** Instructors managing their own listings or booking flow.

## Success criteria (MVP is done when…)

- [ ] 10–12 cities have real, scraped class data (school name, style, schedule, location, price range, link)
- [ ] Users can search/filter by city, dance style, level, day of week
- [ ] Each city has an SEO-optimised landing page (e.g. `/salsa-classes-london`)
- [ ] Google Ads are live and rendering on listing/city pages
- [ ] Stripe donation flow works ("Buy us a coffee" / "Support DanceMad")
- [ ] Feedback/bug report button is live on every page (floating widget, bottom-right)
- [ ] Site is live on a custom domain, indexed by Google
- [ ] Loads fast, works on mobile, looks good enough to share

## Non-goals (v1)

- User accounts / login
- Instructor dashboards or self-service listings
- Class booking or payments to instructors
- Native mobile app
- Real-time availability / live schedules
- Reviews or ratings (yet)
- Map view (yet — nice to have for v2)

## Tech stack

| Layer | Choice | Why |
|-------|--------|-----|
| Framework | **Next.js 14 (App Router)** | SSR/SSG for SEO, React ecosystem, fast pages |
| Styling | **Tailwind CSS** | Rapid UI, Levels-style aesthetic |
| Database | **Supabase (Postgres)** | Free tier (500MB DB, 50K MAUs), real-time if needed later |
| Hosting | **Cloudflare Pages** | Free tier, unlimited bandwidth, commercial use allowed, global CDN |
| Payments | **Stripe Payment Links** | Donation/tip jar, no monthly fee, pay-per-transaction only (2.9% + 30p) |
| Ads | **Google AdSense** | Standard display ads — added later once content + traffic exist |
| Scraping | **Python (requests + BeautifulSoup / Playwright)** | Harry's strength, run as scheduled scripts |
| Data pipeline | **Python scripts → Supabase** | Scrape → clean → upsert to DB |
| DNS/Domain | **Cloudflare Registrar** | At-cost domain pricing, integrated with hosting |

## Data model (core)

```
cities
  id, name, slug, country, country_code, lat, lng, timezone, image_url

schools
  id, city_id, name, slug, address, lat, lng, website, phone, description, source_url

classes
  id, school_id, style (salsa/bachata/kizomba/etc), level (beginner/intermediate/advanced/open),
  day_of_week, start_time, end_time, price_info, notes, last_scraped_at

styles (enum/lookup)
  salsa, bachata, kizomba, zouk, semba, afro-latin, reggaeton, other
```

## Target cities (curated salsa hotspots — 25 cities)

### UK (7 cities)
| City | Why |
|------|-----|
| London | Biggest UK scene, multiple congresses, 50+ schools |
| Bristol | Strong scene, Bristol Salsa Congress, home turf |
| Southampton | Active scene, regular socials |
| Manchester | Large Latin community, multiple venues |
| Birmingham | Growing scene, central UK hub |
| Leeds | Established schools, regular weekenders |
| Edinburgh | Scotland's Latin dance capital |

### Americas (9 cities)
| City | Why |
|------|-----|
| New York | Birthplace of modern salsa, On2/mambo capital |
| Miami | Year-round scene, South Florida Latin culture |
| Los Angeles | On1 capital, huge Latin population |
| Cali, Colombia | Self-proclaimed "World Capital of Salsa", caleña style |
| Medellín, Colombia | Major nomad hub + strong dance scene |
| Mexico City | Massive scene, affordable, nomad-friendly |
| Havana, Cuba | Casino style, cultural origin point |
| Bogotá, Colombia | 30+ year salsa tradition |
| San Juan, Puerto Rico | Historic salsa roots, Nuyorican scene |

### Europe (9 cities)
| City | Why |
|------|-----|
| Barcelona | Spain's salsa capital, Antilla Salsa etc |
| Berlin | Huge international/expat scene |
| Paris | Major congress city, strong scene |
| Lisbon | Growing nomad hub, vibrant Latin nights |
| Rome | Surprisingly strong Italian scene |
| Amsterdam | Active scene, international crowd |
| Madrid | Strong Latin community |
| Warsaw | Fast-growing Eastern European scene |
| Prague | Bachata/salsa festival hub |

**Launch strategy:** Start with 10–12 cities where scraping is easiest (London, Bristol, NYC, Miami, Barcelona, Berlin, Medellín, Cali, Mexico City, Lisbon). Expand to full 25 based on data quality.

## Monetisation

1. **Stripe donations** — "Support DanceMad" button using Stripe Payment Links (pay-what-you-want). No code needed, embed as a button. Live from day 1.
2. **Google AdSense** — display ads on city pages and listing pages. Applied for AFTER launch once there are 10+ content-rich city pages and some organic traffic. Keep ads non-intrusive (sidebar + between listings).
3. **Future:** Featured listings (schools pay to be highlighted), affiliate links to dance gear/shoes.

## Constraints

- Must be mobile-first (most dancers search on phone)
- Page load < 2s (static generation where possible)
- SEO is critical — each city/style combo should be indexable
- Scraping must be respectful (rate limits, robots.txt, caching)
- GDPR-aware (no personal data stored for users in v1, cookie consent for ads later)
- Budget: £0/mo running costs until domain purchase; free tiers everywhere
- Cloudflare Pages: 500 builds/month on free tier (plenty), 1 concurrent build

## Key risks

| Risk | Mitigation |
|------|------------|
| Scraping breaks / data goes stale | Store `last_scraped_at`, show freshness indicator, manual override capability |
| Thin content per city | Start with cities that have 15+ schools, supplement with curated "scene guides" |
| Low traffic initially | SEO-first architecture, share in dance communities, Reddit, Facebook groups |
| Google Ads rejection | Ensure enough original content per page, avoid thin affiliate vibes |
| Stripe compliance for donations | Keep it simple — one-time donations, clear "donation" language |

## Design direction

- Dark or vibrant theme (salsa energy, not corporate)
- Big city hero images, card-based listings
- Minimal chrome — content-dense like Nomad List
- Personality in copy (not "enterprise SaaS" voice)
- Fast, no-nonsense filters (no modals, inline everything)
- **Feedback/bug button:** Floating widget (bottom-right corner), opens a simple form — message + optional screenshot + page URL auto-captured. Store submissions in Supabase `feedback` table. No login required.

---

## Accounts & costs

### To start building (3 accounts)

| Account | What for | Cost |
|---------|----------|------|
| **GitHub** | Code repo | £0 |
| **Cloudflare** | Hosting (Pages) + DNS | £0 |
| **Supabase** | Database (Postgres) | £0 |

### Added when ready to go live

| Account | What for | Cost | When |
|---------|----------|------|------|
| **Stripe** | Donation payments (Payment Links) | £0 base, 2.9% + 30p per txn | When site is shareable |
| **Cloudflare Registrar** | Domain (dancemad.com or similar) | ~£8/yr | When ready to share publicly |
| **Google Search Console** | SEO indexing & monitoring | £0 | At domain setup |
| **Google AdSense** | Display ad revenue | £0 | After 10+ city pages + traffic |

**Total to launch: ~£8** (just the domain). Everything else is free tier.

### When costs increase

| Trigger | What | Cost |
|---------|------|------|
| DB exceeds 500MB or need daily backups | Supabase Pro | $25/mo |
| Need Cloudflare Workers (SSR, API routes) beyond free tier | Cloudflare Workers Paid | $5/mo |
| Want privacy-friendly analytics | Plausible / Fathom | ~$9/mo |

### AdSense approval notes

Google AdSense requires original content before approval:
- Write 200–400 word "scene guide" intros per city (doubles as SEO content)
- Need: About page, Privacy Policy, Contact page, Cookie consent banner
- No hard minimum traffic, but some organic visitors helps
- Apply after 10+ content-rich city pages are live and indexed

---

## Build order

Build the product first. Monetise once there's something worth paying for.

| Phase | What | Accounts needed |
|-------|------|----------------|
| **1. Build** | Site + scraping pipeline + city pages + filters | GitHub, Cloudflare, Supabase |
| **2. Donate** | Add Stripe Payment Link button | + Stripe |
| **3. Launch** | Buy domain, DNS, Google Search Console, share publicly | + Domain |
| **4. Monetise** | Apply for AdSense once content + traffic exist | + AdSense |

## References

- [Nomad List](https://nomadlist.com) — city-based directory, community vibe, SEO play
- [levels.io projects](https://levels.io) — solo-dev shipping style
- [ClassPass](https://classpass.com) — class discovery UX (but we're much simpler)
- [Bachata Ambassador](https://www.bachata-ambassador.com/) — dance-specific directory for reference
