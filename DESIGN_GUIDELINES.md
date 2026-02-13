# DESIGN_GUIDELINES.md
## Red + Glassmorphism Design System

---

## Core Brand Identity

**Primary Color:** Red (actionable, energetic, draws focus)
**Visual Treatment:** Glassmorphism (frosted glass effect with transparency, backdrop blur, subtle borders)
**Era:** Modern, premium, tech-forward
**Tone:** Bold primary actions with elegant, subtle secondary layers

---

## Color Palette

### Primary Colors
- **Red (Accent/CTA):** `#E63946` or `#DC2626` – Actions, highlights, interactive elements
- **Dark Red (Hover/Active):** `#A4161A` or `#991B1B` – Pressed states, deeper emphasis
- **Light Red (Subtle):** `#FCA5A5` or `#FECACA` – Light backgrounds, disabled states, supporting UI

### Neutrals
- **Near Black (Text/Shadows):** `#0F172A` or `#1E293B` – Primary text, dense information
- **Dark Gray (Secondary Text):** `#475569` or `#64748B` – Body copy, subtle labels
- **Light Gray (Backgrounds):** `#E2E8F0` or `#F1F5F9` – Default card backgrounds, dividers
- **Off-White (Canvas):** `#FAFAFA` or `#FFFFFF` – Page/screen background

### Glassmorphism-Specific Palette
- **Glass Base (Light Mode):** `rgba(255, 255, 255, 0.7)` – Frosted glass cards
- **Glass Base (Dark Mode, if needed):** `rgba(30, 41, 59, 0.5)` – Dark frosted glass
- **Glass Border:** `rgba(255, 255, 255, 0.2)` or `1px solid rgba(100, 100, 100, 0.1)` – Subtle edge definition
- **Backdrop Blur Intensity:** `12px` or `16px` – Readable yet premium effect

---

## Typography

### Scale (Tailwind-based)
- **Display/Hero:** 48px–64px, weight 700, line-height 1.1
- **Headline 1 (H1):** 36px–42px, weight 600, line-height 1.2
- **Headline 2 (H2):** 28px–32px, weight 600, line-height 1.3
- **Headline 3 (H3):** 22px–24px, weight 600, line-height 1.4
- **Body Large:** 18px, weight 400, line-height 1.6
- **Body Regular:** 16px, weight 400, line-height 1.6
- **Body Small:** 14px, weight 400, line-height 1.5
- **Caption:** 12px, weight 500, line-height 1.4
- **Overline:** 11px–12px, weight 700, letter-spacing 0.5px, text-transform uppercase

### Font Families
- **Headlines/Display:** `Inter`, `Poppins`, or `SF Pro Display` (modern, geometric)
- **Body Copy:** `Inter`, `Segoe UI`, or system stack (`-apple-system, BlinkMacSystemFont`)

### Text Color Rules
- **Heading on Red:** Always white or light gray (contrast ≥ WCAG AA)
- **Body on Glass (Light):** Dark gray (`#475569`), never pure black on frosted backgrounds
- **Body on Dark Backgrounds:** `#F1F5F9` or white

---

## Glassmorphism Implementation

### Glass Card Base (CSS/Tailwind)
```css
background: rgba(255, 255, 255, 0.7);
backdrop-filter: blur(12px);
border: 1px solid rgba(255, 255, 255, 0.2);
border-radius: 16px;
box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
```

### Depth Layering
1. **Solid Background:** Full opacity, no blur (page/screen canvas)
2. **Secondary Cards:** 70% opacity glass, 12px blur
3. **Interactive Floating:** 80% opacity glass, 16px blur (modals, popovers)
4. **Decorative Overlays:** 50% opacity glass, 8px blur (background patterns)

### Border Treatment
- **Subtle Edge:** `1px solid rgba(255, 255, 255, 0.2)` – Very light on light backgrounds
- **Dark Mode Edge:** `1px solid rgba(100, 100, 100, 0.1)` – Slightly darker on dark
- **Never fully opaque borders** on glass – defeats the purpose of transparency

### Shadows
- **Light Lift (Cards):** `0 4px 12px rgba(0, 0, 0, 0.08)` – Subtle layering
- **Medium Lift (Popovers):** `0 8px 32px rgba(0, 0, 0, 0.12)` – Clear elevation
- **Heavy Lift (Modals):** `0 16px 48px rgba(0, 0, 0, 0.15)` – Top-level emphasis

---

## Spacing System

**Base unit:** 4px

| Token | Value | Use |
|-------|-------|-----|
| xs | 4px | Tight gaps, icon padding |
| sm | 8px | Between related elements |
| md | 16px | Default padding, card content |
| lg | 24px | Section gaps, card margins |
| xl | 32px | Major section separation |
| 2xl | 48px | Page-level spacing |
| 3xl | 64px | Hero/banner padding |

---

## Component Patterns

### Buttons
- **Primary (Red CTA):** Solid red background, white text, rounded corners (12–16px)
  - Hover: Darker red, shadow lift
  - Active/Pressed: Darker red + inset shadow
  - Disabled: Light red (`#FECACA`), gray text, no shadow
- **Secondary (Glass):** Glass card treatment with red text, red border
  - Hover: Slight backdrop blur increase, red shadow
  - Active: Solid red background, white text (state toggle)
- **Tertiary (Text Link):** Red text, no background, underline on hover
- **Icon Button:** Glass circle, red on hover, smooth transitions

### Cards
- **Data/Content Cards:** Glass base (70% opacity), 12px blur, 16px border-radius
- **Interactive Cards:** Slightly higher opacity (80%), red accent on left border or top
- **Floating Cards:** 80% opacity, 16px blur, prominent shadow (modals, popovers)
- **Disabled/Inactive Cards:** Reduced opacity (50%), grayed-out text

### Input Fields
- **Text Input:** Glass background (50% opacity), red border on focus, red placeholder accent
- **Search Bar:** Wider glass treatment, magnifying glass icon in red
- **Dropdowns/Selects:** Glass background, red chevron icon, red highlight on selected option

### Tags/Badges (Dance Styles)
- **Salsa:** Red (`#E63946`) background, white text
- **Bachata:** Purple (`#7C3AED`) background, white text
- **Kizomba:** Amber (`#D97706`) background, white text
- **Zouk:** Teal (`#0D9488`) background, white text
- **Other styles:** Gray glass with dark text

---

## Motion & Transitions

### Timing
- **Micro-interactions:** 120ms (button press, toggle)
- **Standard transitions:** 200ms (hover states, fade-in)
- **Layout shifts:** 300ms (expand/collapse, drawer open)
- **Page transitions:** 400ms (route changes, modal open)

### Easing
- **Default:** `ease-out` (natural deceleration)
- **Enter:** `cubic-bezier(0.0, 0.0, 0.2, 1)` (fast start, smooth land)
- **Exit:** `cubic-bezier(0.4, 0.0, 1, 1)` (accelerate out)

### What to Animate
- Hover elevation on cards and buttons
- Focus ring appearance on inputs
- Filter panel expand/collapse
- Page/route fade transitions
- Backdrop blur on modal open

### What NOT to Animate
- Color changes on text (jarring)
- Layout reflows (causes jank)
- Multiple simultaneous transitions on the same element

---

## Do's and Don'ts

✓ Use red for primary CTAs and key interactive elements only
✓ Always maintain WCAG AA contrast ratios (4.5:1 for text)
✓ Apply glassmorphism to cards, modals, and navigation — not everything
✓ Use whitespace generously between glass layers
✓ Provide solid-color fallbacks for browsers without backdrop-filter support
✓ Test glassmorphism on mobile devices (GPU/memory constraints)

✗ Don't use red for backgrounds, body text, or large areas (overwhelming)
✗ Don't stack multiple glass layers on top of each other without purpose
✗ Don't use red with other bold colors in close proximity (visual clash)
✗ Don't blur video or high-motion content behind glassmorphic overlays
✗ Don't forget accessibility: always check color contrast, provide focus rings, test with screen readers
✗ Don't apply transparency without backdrop filter (looks like a mistake)

---

## Reference Sources

**Babbel Case Study (Learning App):**
- Clean, educational color hierarchy
- Generous whitespace for clarity
- Bold CTA treatment with rounded corners
- Multi-step progress indicators with color coding
- Light, accessible backgrounds

**Realify Case Study (Real Estate Directory App):**
- Premium card layouts with subtle shadows
- Light & dark theme support
- Icon-first navigation patterns
- Hierarchical content cards (hero → details)
- Large, scannable typography
