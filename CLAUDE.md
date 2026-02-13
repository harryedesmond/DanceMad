# AGENT.md
## Rules for working on DanceMad

---

## Before doing anything

1. Read `MASTERPLAN.md` to understand what we're building and why
2. Read `TASKS.md` to find the next unchecked task
3. Read `DESIGN_GUIDELINES.md` before any UI/styling work
4. Do only the next unchecked task — nothing more

---

## Project context

- **DanceMad** is a salsa & Latin dance class directory for 10–20 cities worldwide
- Built with **Next.js 14 (App Router)** + **Tailwind CSS** + **Supabase** (Postgres)
- Hosted on **Cloudflare Pages**
- Revenue: Stripe donations + Google AdSense (added later)
- Scraping pipeline is **Python** (separate from Next.js app)
- Style: Pieter Levels / Nomad List vibe — ship fast, personality over polish
- Design: **Red + glassmorphism** — see `DESIGN_GUIDELINES.md`

---

## Workflow rules

1. **One task at a time.** Find the next unchecked task in `TASKS.md`, do it, verify it, then move on.
2. **After each task:** List what changed (files created/modified) and how to test it.
3. **Don't refactor unrelated code.** Only touch files relevant to the current task.
4. **Don't add features not in the plan.** If something seems missing, flag it — don't build it.
5. **Don't rename or restructure files** unless the current task specifically requires it.
6. **If uncertain:** Present 2 options with tradeoffs, recommend one, then proceed with the recommendation unless told otherwise.

---

## Code standards

### Next.js
- Use App Router (`/app` directory), not Pages Router
- Server components by default; client components only when interactivity is needed (`'use client'`)
- Use `@supabase/supabase-js` for database queries
- Environment variables: `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY`
- Static generation (SSG) for city pages where possible

### Tailwind CSS
- Follow `DESIGN_GUIDELINES.md` for colors, spacing, typography
- Red (`#E63946`) for CTAs and interactive elements only
- Glassmorphism: `backdrop-blur-lg bg-white/70 border border-white/20 rounded-2xl shadow-lg`
- Mobile-first: design for phone, then scale up
- No inline styles — Tailwind classes only

### TypeScript
- Use TypeScript throughout (`.ts` / `.tsx` files)
- Define types for database models (City, School, Class)
- No `any` types unless absolutely unavoidable

### File structure
```
/app                    # Next.js App Router pages
  /[city-slug]          # Dynamic city pages
  /about
  /contact
  /privacy
  layout.tsx            # Root layout
  page.tsx              # Homepage
/components             # Reusable UI components
/lib                    # Utilities, Supabase client, types
/scripts                # Python scraping scripts (separate from Next.js)
/public                 # Static assets, images
```

---

## Styling rules

- **Always check `DESIGN_GUIDELINES.md`** before building any component
- Red is for CTAs and interactive elements — never for backgrounds or body text
- Glass cards: `bg-white/70 backdrop-blur-lg border border-white/20 rounded-2xl shadow-lg`
- Dance style badges have specific colors (see Design Guidelines → Tags/Badges)
- Transitions: 200ms ease-out for hover states
- Minimum touch target: 44px × 44px on mobile

---

## Database rules

- Always use parameterised queries (Supabase client handles this)
- Include `last_scraped_at` when inserting/updating scraped data
- Use city `slug` for URL routing, not `id`
- Foreign keys: `schools.city_id → cities.id`, `classes.school_id → schools.id`

---

## Scraping rules (Python)

- Scripts live in `/scripts` directory
- Use `requirements.txt` for dependencies
- Respect rate limits: 1–2 second delay between requests
- Check `robots.txt` before scraping any source
- Always set `last_scraped_at` timestamp on upserted records
- Log errors but don't crash on individual record failures
- Output clean data — no HTML tags in text fields

---

## Debugging protocol

1. **Add visibility first** — console.log / print to understand the state
2. **Read the error message** — don't guess
3. **Check the simplest explanation** — typo? wrong env var? missing import?
4. **If stuck for > 10 minutes:** Step back, describe the problem clearly, try a different approach
5. **After fixing:** Add a note to `TASKS.md` if the issue reveals a gap in the plan

---

## What NOT to do

- Don't install unnecessary packages — keep dependencies lean
- Don't add user auth (not in scope for v1)
- Don't build a map view (v2)
- Don't build reviews/ratings (v2)
- Don't add booking/payments to instructors (v2)
- Don't optimise prematurely — ship working first, polish later
- Don't create README files unless asked
