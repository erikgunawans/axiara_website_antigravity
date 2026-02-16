# 30-Day Sprint — Design Overrides

> Overrides `MASTER.md` for `src/pages/services/sprint.html` only.
> **Primary conversion page** — highest CTA density.
> Content source: Manual §3.1–§3.5

---

## Page Structure

```
┌─────────────────────────────────────────────────────┐
│  NAVBAR                                             │
├─────────────────────────────────────────────────────┤
│                                                     │
│  HERO — "30-Day Risk & Compliance Sprint"           │
│  Subtitle: "From Shadow AI to Glass Box"            │
│  Ghost CTA: "Book Your Sprint"                      │
│                                                     │
├─────────────────────────────────────────────────────┤
│  SPRINT OVERVIEW — What it is, why 30 days          │
│  Left editorial text + right stat cards             │
├─────────────────────────────────────────────────────┤
│  WEEK-BY-WEEK TIMELINE — 4 vertical phases          │
│  Alternating left/right layout (Asymmetric Weave)   │
├─────────────────────────────────────────────────────┤
│  FRAMEWORK ALIGNMENT — NIST / OWASP / ISO table     │
│  Summary table from §3.5                            │
├─────────────────────────────────────────────────────┤
│  DELIVERABLES — What the client receives            │
│  Icon grid of key outputs                           │
├─────────────────────────────────────────────────────┤
│  CONVERSION CTA — Book Your Sprint                  │
│  Full-width, crimson accent, contact form trigger    │
├─────────────────────────────────────────────────────┤
│  FOOTER                                             │
└─────────────────────────────────────────────────────┘
```

---

## Section 1: Hero

### Layout
- Full viewport, `min-height: 80vh`
- Background: obsidian-to-charcoal gradient
- Content left-aligned (60% width on desktop)

### Typography
- **Label:** `JetBrains Mono`, Crimson, uppercase, `letter-spacing: 3px`
  - `"SERVICE — 30 DAYS"`
- **H1:** Outfit 900, White, uppercase
  - `"30-DAY RISK & COMPLIANCE SPRINT"`
  - Size: `clamp(2rem, 5vw, 4rem)`
- **H2:** Playfair Display 400, italic, Silver
  - `"From Shadow AI to Glass Box in 30 days"`
- **Body:** Outfit 300, Silver
  - `"A low-friction, high-impact diagnostic designed to insulate client leadership from liability and provide a definitive technical roadmap."`

### CTAs (dual)
- Primary: `"BOOK YOUR SPRINT →"` (ghost button, white)
- Secondary: `"SEE THE PROCESS ↓"` (ghost link, silver, scrolls to timeline)

---

## Section 2: Sprint Overview

### Layout
- **2-column asymmetric** — 60% text / 40% stat cards
- Text left, stat cards right (stacked glass cards)

### Left Column (Editorial)
- **H2 (Playfair, italic, Silver):**
  - `"The on-ramp to governed excellence"`
- **Body paragraphs** from Manual §3 intro:
  - Sprint = E2E Phases 1–3 (Diagnose, Architect, Illuminate)
  - Produces blueprint for Phases 4–5 (Integrate, Sustain)
  - Not a standalone deliverable — engineers the full transformation on-ramp

### Right Column (Stat Cards)
3 stacked frosted glass cards:

| Stat | Label | Source |
|------|-------|--------|
| `30` | Days to Glass Box | Sprint duration |
| `4` | Framework Alignments | NIST + OWASP + ISO + UU PDP |
| `Level 4` | Maturity Exit Target | From Level 1–2 to Level 4 |

Card style:
```
┌──────────────────────┐
│ ▌  30                │  ← Outfit 900, White, 48px
│ ▌  DAYS TO GLASS BOX │  ← JetBrains Mono 300, Crimson, uppercase
└──────────────────────┘
```

---

## Section 3: Week-by-Week Timeline

> **This is the centerpiece of the page.** Most visual weight.

### Layout — "Asymmetric Weave" Timeline
- **Vertical crimson line** running down the center (desktop)
- Weeks alternate **left and right** of the center line
- Each week is a frosted glass card connected to the spine by a crimson dot
- Mobile: single column, cards stacked, crimson line on the left edge

### Desktop Layout
```
          Week 1                    
    ┌─────────────┐                 
    │  DIAGNOSE   │───● ───────────
    └─────────────┘    │           
                       │           
             ───────── ●───┌─────────────┐
                       │   │  ARCHITECT  │
                       │   └─────────────┘
                       │           
    ┌─────────────┐    │           
    │  ILLUMINATE │───● ───────────
    └─────────────┘    │           
                       │           
             ───────── ●───┌─────────────┐
                           │  BLUEPRINT  │
                           └─────────────┘
```

### Week Cards

#### Week 1: The Diagnostic (§3.1)
| Field | Content |
|-------|---------|
| Week Label | `WEEK 01` (JetBrains Mono, Crimson) |
| Pillar | `SHIELD` (Outfit 700, White, uppercase) |
| NIST Function | `MAP` |
| Title | `"Shadow AI Audit & Risk Mapping"` |
| Body | Deploy Shadow AI Audit Template across all departments. Identify unauthorized AI tools, data flows, PII exposure. |
| Deliverables | Shadow AI Landscape Report · Regulatory Exposure Assessment · Governance Maturity Score · Executive Briefing |
| Exit Level | `Level 1 → Level 2 (Confirmed)` |

#### Week 2: The Aksara Foundation (§3.2)
| Field | Content |
|-------|---------|
| Week Label | `WEEK 02` |
| Pillar | `AKSARA` |
| NIST Function | `GOVERN` |
| Title | `"Data Sovereignty & Vector Core"` |
| Body | Vector Readiness Audit. Legacy database mapping. RAG pipeline architecture. PII scrubbing activation. |
| Deliverables | Vector Core Migration Plan · Security & Sovereignty Audit · Draft Episteme Logic Map · Technical Milestone Report |
| Exit Level | `Level 2 → Level 2+ (Foundation Secured)` |

#### Week 3: The Axiom Transition (§3.3)
| Field | Content |
|-------|---------|
| Week Label | `WEEK 03` |
| Pillar | `AXIOM` |
| NIST Function | `MEASURE` |
| Title | `"Logic Mapping & Stress-Testing"` |
| Body | The Logic Mapping Workshop — the moment AI transforms from Black Box to Glass Box. DPO Red-Team Challenge. |
| Deliverables | Episteme Logic Maps · Prompt Integrity Report · Finalized Accountability Map · DPO Validation Sign-Off |
| Exit Level | `Level 2+ → Level 3+ (Transparent, Measured)` |

#### Week 4: The Blueprint (§3.4)
| Field | Content |
|-------|---------|
| Week Label | `WEEK 04` |
| Pillar | `TERPADU` |
| NIST Function | `MANAGE` |
| Title | `"Integration & Transformation Roadmap"` |
| Body | Final Executive Blueprint. 24-month Nexus Implementation Roadmap. Board authorization. |
| Deliverables | Executive Transformation Blueprint · Nexus 2026 Roadmap · Live Episteme Dashboard · ROI Projections · MSA |
| Exit Level | `Level 3+ → Level 4 (Managed)` |

### Card Internal Structure
```
┌──────────────────────────────────────────┐
│ ▌  WEEK 01              MAP             │  ← Label row: JetBrains Mono
│ ▌                                       │
│ ▌  SHIELD                               │  ← Pillar: Outfit 700, Crimson
│ ▌  Shadow AI Audit & Risk Mapping       │  ← H3: Outfit 700, White
│ ▌                                       │
│ ▌  Deploy Shadow AI Audit Template      │  ← Body: Outfit 300, Silver
│ ▌  across all departments...            │
│ ▌                                       │
│ ▌  ┌──────────────────────────────┐     │
│ ▌  │ ◆ Shadow AI Landscape Report │     │  ← Deliverable list
│ ▌  │ ◆ Regulatory Exposure        │     │     Outfit 300, Silver
│ ▌  │ ◆ Governance Maturity Score   │     │     Crimson diamond bullets
│ ▌  │ ◆ Executive Briefing         │     │
│ ▌  └──────────────────────────────┘     │
│ ▌                                       │
│ ▌  EXIT: Level 1 → Level 2             │  ← JetBrains Mono, Crimson
└──────────────────────────────────────────┘
```

### Animation
- Cards: staggered `fade-in-up`, 0.3s delay between weeks
- Crimson spine line: draws downward as user scrolls (CSS or IntersectionObserver)

---

## Section 4: Framework Alignment Table

### Layout
- Full-width glass card containing the summary table from §3.5
- Horizontal scroll on mobile

### Table Design
- Header row: Obsidian bg, JetBrains Mono, Crimson text, uppercase
- Body rows: alternating `rgba(26,26,46,0.2)` and `transparent`
- No border-radius on cells

| Week | Pillar | NIST | AIMA Domains | AIMA Exit | Axiara Scale | E2E Phase |
|------|--------|------|-------------|-----------|-------------|-----------|
| 1 | Shield | MAP | Governance, Responsible AI | Level 1 | Level 2 | Diagnose |
| 2 | Aksara | GOVERN | Data Mgmt, Privacy | Level 1+ | Level 2+ | Architect |
| 3 | Axiom | MEASURE | Responsible AI, Verification | Level 2 | Level 3+ | Illuminate |
| 4 | Terpadu | MANAGE | Governance, Operations | Level 2+ | Level 4 | Blueprint |

---

## Section 5: Key Deliverables Grid

### Layout
- **3×2 grid** on desktop, 2-column on tablet, single on mobile
- Each: frosted glass card with Lucide icon

### Cards

| Icon (Lucide) | Deliverable | Description |
|--------------|-------------|-------------|
| `file-search` | Shadow AI Report | Complete landscape of unauthorized AI tools |
| `shield-check` | Governance Score | Level 1–5 maturity baseline established |
| `database` | Vector Core Plan | Aksara migration architecture ready |
| `eye` | Episteme Logic Maps | Visual audit trails for all workflows |
| `users` | Accountability Map | Named human Logic Owner per decision |
| `map` | Nexus Roadmap | 24-month implementation blueprint |

---

## Section 6: Conversion CTA

> **Primary conversion point.** This page is the #1 funnel for booking engagements.

### Layout
- Full-width band, `padding: 100px 0`
- Background: obsidian with double diagonal crimson SVG lines (The Weave)
- Content centered

### Typography
- **H2 (Playfair, italic, Silver):**
  - `"Every engagement begins with the Sprint"`
- **Body (Outfit 300, Silver):**
  - `"50% upon commencement. 50% upon delivery of the Final Executive Blueprint. No hidden fees. No scope creep."`
- **CTA:** Ghost button, larger (padding 20px 48px)
  - `"BOOK YOUR SPRINT →"`
- **Trust line (JetBrains Mono, Silver, small):**
  - `"NIST AI RMF · OWASP AIMA · ISO 42001 · UU PDP ALIGNED"`

### Animation
- CTA button: subtle crimson border pulse (CSS keyframe, 2s loop)
- Respects `prefers-reduced-motion`

---

## Sprint-Specific Overrides from MASTER

| Property | MASTER Default | Sprint Override |
|----------|---------------|-----------------|
| Timeline layout | N/A | Alternating left/right with crimson spine |
| Card bullets | None | Crimson diamond `◆` for deliverables |
| Stat cards | N/A | Oversized number + label format |
| CTA density | 1–2 per page | 3 CTAs (hero, mid-page, footer band) |
| Table styling | N/A | Glass card with JetBrains Mono headers |

---

*Override for: src/pages/services/sprint.html*
*Inherits all unspecified rules from: design-system/MASTER.md*
