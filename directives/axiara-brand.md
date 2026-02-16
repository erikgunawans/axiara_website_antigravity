# Directive: Axiara Brand Guidelines

> SOP for all UI/visual decisions on the Axiara.id website.
> Read this directive BEFORE building any page or component.
> Source of truth: docs/agency_9_creative.md

## Visual Concept: "The Darkroom"

The site feels like a high-end architectural portfolio crossed with 
a sovereign intelligence platform. Zaha Hadid Architects meets Palantir.
Content does not "pop" (playful) — it "unveils" (premium).

## Color Palette (Non-Negotiable)

| Token | Value | CSS Variable | Usage |
|-------|-------|-------------|-------|
| Obsidian | #0D0D0D | --axiara-obsidian | Primary background |
| Crimson | #C41E3A | --axiara-crimson | Accent lines, hover, "Weave" |
| White | #FFFFFF | --axiara-white | H1 headlines, button borders |
| Silver | #A8A8A8 | --axiara-silver | Body text, H2 subheads |
| Charcoal | #1A1A2E | --axiara-charcoal | Gradient endpoint |
| Glass | rgba(26,26,46,0.4) | — | Frosted card backgrounds |
| Glass Hover | rgba(26,26,46,0.8) | — | Card hover state |
| Crimson Glow | rgba(196,30,58,0.05) | — | Button hover tint |

No other colors are permitted unless explicitly approved.

## Typography (Non-Negotiable)

| Element | Font | Weight | Style | Notes |
|---------|------|--------|-------|-------|
| H1 | Outfit | 900 | Normal, UPPERCASE | letter-spacing: 0.05em |
| H2 | Playfair Display | 400 | ITALIC | color: Silver |
| H3 | Outfit | 700 | Normal | color: White |
| Body | Outfit | 300 | Normal | 18px, color: Silver |
| Code/Labels | JetBrains Mono | 300-400 | Normal | For data, badges, buttons |
| Buttons | JetBrains Mono | 400 | UPPERCASE | letter-spacing: 2px |

Google Fonts import:
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400&family=Outfit:wght@300;400;700;900&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap');

## UI Components

### Ghost Buttons (The ONLY button style)
- background: transparent
- border: 1px solid white
- border-radius: 0px (ALWAYS — "knife-edge apex")
- font: JetBrains Mono, uppercase, letter-spacing 2px
- hover: border-color crimson, text crimson, bg crimson-glow
- transition: all 0.4s ease
- padding: 14px 32px
- ALWAYS add cursor-pointer

### Frosted Glass Cards (The ONLY card style)
- background: rgba(26,26,46,0.4)
- backdrop-filter: blur(12px) + -webkit-backdrop-filter: blur(12px)
- border-LEFT only: 1px solid crimson (NO top, right, bottom borders)
- hover: bg opacity 0.8 + border-left thickens to 4px
- padding: 40px
- transition: all 0.4s ease
- Fallback for no backdrop-filter support: solid bg-charcoal

### Asymmetric Image Treatment
- transform: translate(20px, 20px) on desktop
- 1px wireframe border behind (rgba(255,255,255,0.1))
- Remove offset on mobile (transform: none below 768px)

## Motion Rules (STRICTLY ENFORCED)

ALLOWED:
- Fade In Up (translateY 20-30px → 0, opacity 0 → 1)
- Duration: 0.8–1.2s
- Easing: ease-out
- Staggered delays (0.1-0.2s between siblings)
- Slow parallax (0.3-0.5x scroll speed)
- Color/opacity/border transitions (0.3-0.4s)

FORBIDDEN (Never use, under any circumstances):
- Bounce, elastic, spring
- Zoom, scale transforms on hover that shift layout
- Spin, rotate entrance animations
- Any animation faster than 0.6s for entrance
- Any "playful" or "fun" motion

## Icons
- USE: Lucide Icons via CDN (lucide.dev)
- NEVER: Emoji icons (🎨 🚀 ⚙️ etc.)
- Style: 48-64px, white, stroke-width 1 (thin wireframe)

## Border Radius
- 0px on EVERYTHING. Buttons, cards, inputs, images, badges.
- No exceptions. This is the "knife-edge apex" brand rule.

## Photography
- Black & white only, with optional Crimson color overlay
- No full-color stock photography
- Editorial, documentary aesthetic

## Responsive Rules (Self-Annealing Notes)
> Added 2026-02-16 per User Request

### 1. Typhography Scaling
- **Hero H1**:
    - Mobile (<768px): 40px
    - Tablet (768px-1024px): 56px
    - Desktop (>1024px): 72px
- Use `.text-hero` utility class to enforce this.

### 2. Layout & Grids
- **Grids**: MUST collapse to single column (`grid-cols-1`) below 768px (`md:`).
- **Horizontal Timelines**: Convert to vertical stack on mobile.
- **Image Offsets**: `transform: translate(0,0)` on mobile. Only offset on desktop.
- **Navbar**: Hamburger menu visible below 1024px (`lg:`).

### 3. Touch Targets
- **Ghost Buttons**: Minimum 48px height/width on mobile.
- **Inputs**: Text size 16px min on mobile to prevent iOS zoom.

### 4. Scroll
- **Horizontal Scroll**: FORBIDDEN at any breakpoint. Use `overflow-x-hidden` on `body`.

## Edge Cases & Learnings
(This section gets updated by the agent via self-annealing)
- [Placeholder — agent adds learnings as it discovers them]
