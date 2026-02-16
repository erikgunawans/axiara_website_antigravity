# Homepage — Design Overrides

> Overrides `MASTER.md` for `index.html` only.
> Content source: Manual §1.1, §1.2, §1.3, §1.4

---

## Page Structure

```
┌─────────────────────────────────────────────────────┐
│  NAVBAR (transparent → glass on scroll)             │
├─────────────────────────────────────────────────────┤
│                                                     │
│  HERO — Full viewport                               │
│  "Foundational Logic. Integrated Innovation."       │
│  Tagline + Ghost CTA "Begin Assessment"             │
│                                                     │
├─────────────────────────────────────────────────────┤
│  THE MANDATE — Mission statement (§1.1)             │
│  Left-aligned editorial, Playfair H2                │
├─────────────────────────────────────────────────────┤
│  THREE PILLARS — Axiom · Aksara · Terpadu (§1.3)   │
│  3 frosted glass cards, crimson left border          │
├─────────────────────────────────────────────────────┤
│  E2E MODEL — 5-phase timeline (§1.2)                │
│  Horizontal crimson-dot timeline                    │
├─────────────────────────────────────────────────────┤
│  INDUSTRIES — 4 sector cards (§1.4)                 │
│  Glass cards with B&W bg, hover reveal              │
├─────────────────────────────────────────────────────┤
│  30-DAY SPRINT CTA — Full-width crimson band        │
│  "From Shadow AI to Glass Box in 30 Days"           │
├─────────────────────────────────────────────────────┤
│  FOOTER                                             │
└─────────────────────────────────────────────────────┘
```

---

## Section 1: Hero

### Layout
- **Full viewport** (`min-height: 100vh`)
- Background: `--axiara-gradient` (obsidian → charcoal, 135deg)
- Optional: subtle animated hex grid or diagonal crimson "Weave" lines as bg watermark
- Content centered vertically, left-aligned on desktop (asymmetric)

### Typography
- **Pre-title:** `JetBrains Mono`, weight 300, Silver, uppercase, `letter-spacing: 3px`
  - Text: `"PT AKSARA INOVASI TERPADU"`
- **H1:** Outfit, weight 900, White, uppercase, `letter-spacing: 0.05em`
  - Line 1: `"FOUNDATIONAL LOGIC."`
  - Line 2: `"INTEGRATED INNOVATION."`
  - Size: `clamp(2.5rem, 6vw, 5rem)`
- **Subtitle:** Outfit, weight 300, Silver, 18px
  - Text: `"Your End-to-End AI Transformation Partner"`

### CTA
- Ghost button: `"BEGIN ASSESSMENT →"`
- Secondary ghost: `"EXPLORE THE ARCHITECTURE"`

### Animation
- H1: `fade-in-up`, 0.8s delay
- Subtitle: `fade-in-up`, 1.0s delay
- CTA: `fade-in-up`, 1.2s delay

---

## Section 2: The Mandate

### Layout
- Max-width container, **left-aligned** (not centered — editorial style)
- Large left padding, tight right margin (asymmetric weave)
- Crimson vertical accent line on the left edge

### Typography
- **H2 (Playfair Display, italic, Silver):**
  - `"The sovereign certainty your board demands"`
- **Body (Outfit 300, Silver, 18px):**
  - Mission statement from §1.1: *"AI adoption without governance is not innovation but institutional liability."*
  - 2–3 sentences max, direct quotes from Manual

### Animation
- `fade-in-up`, triggered on scroll

---

## Section 3: Three Pillars

### Layout
- **3 columns** on desktop, single stack on mobile
- Each column: frosted glass card (standard MASTER component)
- Equal height cards with `align-items: stretch`

### Cards

| Pillar | Icon (Lucide) | Title | Subtitle |
|--------|--------------|-------|----------|
| **The Axiom** | `eye` | TRUTH IN LOGIC | "If the Board cannot audit it in 30 seconds, it is not ready for production." |
| **The Aksara** | `database` | FOUNDATIONAL SCRIPT | "Without the Aksara, AI is guessing. With it, AI is grounded in verified institutional truth." |
| **The Terpadu** | `plug` | INTEGRATED INNOVATION | "Axiara rejects silos. AI becomes an operational organ, not an appendage." |

### Card Structure
```
┌──────────────────────────┐
│ ▌ [Lucide icon]          │  ← crimson left border
│ ▌                        │
│ ▌ THE AXIOM              │  ← H3 (Outfit 700, White, uppercase)
│ ▌ Truth in Logic         │  ← Label (JetBrains Mono 300, Crimson)
│ ▌                        │
│ ▌ "If the Board cannot   │  ← Body (Outfit 300, Silver)
│ ▌  audit it in 30        │
│ ▌  seconds..."           │
│ ▌                        │
│ ▌ LEARN MORE →           │  ← Ghost link (JetBrains Mono, White)
└──────────────────────────┘
```

---

## Section 4: E2E Model

### Layout
- **Horizontal timeline** on desktop (5 nodes connected by crimson line)
- **Vertical timeline** on mobile
- Crimson dot markers at each phase node

### Timeline Nodes

| Phase | Label | Deliverable |
|-------|-------|-------------|
| Phase 1 | DIAGNOSE | Governance Maturity Score |
| Phase 2 | ARCHITECT | Aksara Vector Core |
| Phase 3 | ILLUMINATE | Episteme Glass Box |
| Phase 4 | INTEGRATE | Production API |
| Phase 5 | SUSTAIN | ISO 42001 Certification |

### Typography
- Phase number: `JetBrains Mono`, Crimson, uppercase
- Phase label: `Outfit 700`, White, uppercase
- Deliverable: `Outfit 300`, Silver

### Animation
- Nodes reveal left-to-right with staggered `fade-in-up` (0.2s increment)

---

## Section 5: Industries

### Layout
- **2×2 grid** on desktop, single column on mobile
- Each card: frosted glass with B&W background image (low opacity)

### Cards

| Sector | Image Theme | Pain Point (hover reveal) |
|--------|-------------|--------------------------|
| Telecommunications | Network tower silhouette | "AI-driven routing without auditable logic" |
| Energy & Utilities | Industrial refinery | "AI-cleared safety assessments carry life-safety consequences" |
| Banking & Insurance | Financial district | "Unaudited algorithmic lending creates systemic risk" |
| State-Owned (BUMN) | Indonesian cityscape | "Public accountability + Presidential AI Decree" |

### Card Behavior
- Default: B&W image bg + sector title (H3, White)
- Hover: glass overlay darkens, pain point text reveals with `fade-in-up`
- CTA: `"VIEW SECTOR →"` ghost link

---

## Section 6: Sprint CTA Band

### Layout
- Full-width band, `padding: 80px 0`
- Background: solid Obsidian with single diagonal crimson line SVG watermark
- Content centered

### Typography
- **H2 (Playfair Display, italic, Silver):**
  - `"From Shadow AI to Glass Box in 30 Days"`
- **Body:** 1 sentence, Outfit 300, Silver
  - `"The 30-Day Sprint insulates your leadership from liability and delivers a definitive technical roadmap."`
- **CTA:** Ghost button, `"BOOK YOUR SPRINT →"`

---

## Tailwind Utilities — Homepage Specific

```
/* No rounded-* classes — ever */
/* Use these instead: */

.hero-gradient   { @apply bg-gradient-to-br from-[#0D0D0D] to-[#1A1A2E]; }
.glass-card      { @apply bg-[rgba(26,26,46,0.4)] backdrop-blur-xl border-l border-l-[#C41E3A]; }
.ghost-btn       { @apply bg-transparent border border-white text-white uppercase tracking-[2px] font-mono; }
.ghost-btn:hover { @apply border-[#C41E3A] text-[#C41E3A] bg-[rgba(196,30,58,0.05)]; }
```

---

## Performance Notes

- Hero image (if used): WebP, max 200KB, lazy-load disabled (above fold)
- Industry images: WebP, `loading="lazy"`, responsive srcset
- Critical CSS: inline the hero gradient + font-face in `<head>`
- Lucide icons: load only needed icons, not full bundle

---

*Override for: index.html (Homepage)*
*Inherits all unspecified rules from: design-system/MASTER.md*
