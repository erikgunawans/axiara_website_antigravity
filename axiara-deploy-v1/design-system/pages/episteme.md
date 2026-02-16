# Episteme — Design Overrides

> Overrides `MASTER.md` for `src/pages/technology/episteme.html` only.
> **Technical product page** — explains the Glass Box engine.
> Content source: Manual §2.2–§2.2.3

---

## Page Structure

```
┌─────────────────────────────────────────────────────┐
│  NAVBAR                                             │
├─────────────────────────────────────────────────────┤
│                                                     │
│  HERO — "NTRJ Episteme" / "The Glass Box"           │
│  Tagline: "We do not ask you to trust AI."          │
│                                                     │
├─────────────────────────────────────────────────────┤
│  WHAT IT IS — Product definition paragraph          │
│  Left-aligned editorial, asymmetric                 │
├─────────────────────────────────────────────────────┤
│  CAPABILITIES — 6 feature cards (§2.2.1)            │
│  3×2 glass card grid                                │
├─────────────────────────────────────────────────────┤
│  DIFFERENTIATOR — Workflow vs Model table (§2.2.2)  │
│  Side-by-side comparison                            │
├─────────────────────────────────────────────────────┤
│  INTEGRATION — Zero-Disruption diagram (§2.2.3)    │
│  Architecture visual                                │
├─────────────────────────────────────────────────────┤
│  BOARDROOM TRANSLATION — Executive framing          │
│  Pull-quote highlight                               │
├─────────────────────────────────────────────────────┤
│  CTA — "See Your AI Clearly"                        │
├─────────────────────────────────────────────────────┤
│  FOOTER                                             │
└─────────────────────────────────────────────────────┘
```

---

## Section 1: Hero

### Layout
- `min-height: 70vh`, vertically centered
- Background: obsidian-to-charcoal gradient
- Subtle animated glow: faint crimson radial gradient pulsing behind the title (CSS only, opacity 0.03–0.06)

### Typography
- **Label:** `JetBrains Mono`, Crimson, uppercase, `letter-spacing: 3px`
  - `"TECHNOLOGY — AXIOM ENGINE"`
- **H1:** Outfit 900, White, uppercase
  - `"NTRJ EPISTEME"`
  - Size: `clamp(2.5rem, 6vw, 5rem)`
- **H2:** Playfair Display 400, italic, Silver
  - `"The Glass Box"`
- **Body:** Outfit 300, Silver
  - `"We do not ask organizations to trust AI. We enable them to inspect, review, and defend AI-assisted decisions."`
  - *(Direct quote from NATARAJA positioning, §2.2)*

### CTA
- Ghost button: `"EXPLORE CAPABILITIES ↓"`

---

## Section 2: What It Is

### Layout
- Max-width container, left-aligned editorial (asymmetric weave)
- Crimson vertical line on the left edge
- 60% width text block on desktop

### Content
- **H2 (Playfair, italic, Silver):**
  - `"Transparency at the workflow level"`
- **Body** (direct from §2.2):
  - "NTRJ Episteme is a transparency layer for AI workflows that enables teams to clearly see how inputs, context, and AI-based transformations combine to produce outputs."
  - "It does not replace models, does not modify model weights, and does not require retraining. It operates around existing AI tools."
- **Emphasis line (JetBrains Mono, Crimson):**
  - `"Developed by NATARAJA Pte. Ltd. (Singapore)"`

---

## Section 3: Key Capabilities

### Layout
- **3×2 grid** on desktop, 2-column on tablet, single on mobile
- Each: frosted glass card (MASTER spec)

### Cards (from §2.2.1)

| Icon (Lucide) | Capability | Glass Box Outcome |
|--------------|------------|-------------------|
| `file-input` | **Explicit Input Visibility** | Every decision traceable to a specific document in the Aksara Vector Core. No hallucinated sources. |
| `layers` | **Transparent Context Control** | CRO can verify no unauthorized data or bias-inducing prompts influenced a decision. |
| `git-branch` | **Structured Reasoning Steps** | Raw LLM reasoning translated into executive-readable Logic Maps (visual flowcharts, not code). |
| `replace` | **Add vs. Replace Tracking** | Full decision-state versioning. CRO sees how conclusions evolved and when prior reasoning was invalidated. |
| `history` | **Reviewable Decision Lineage** | Post-hoc reconstruction without reliance on screenshots, assumptions, or informal narratives. |
| `user-check` | **Human Oversight Support** | Axiara layers the Accountability Map: every automated step assigned a human Logic Owner. |

### Card Internal Structure
```
┌──────────────────────────────────────────┐
│ ▌  [Lucide icon — 32px, White]          │
│ ▌                                       │
│ ▌  EXPLICIT INPUT VISIBILITY            │  ← H3: Outfit 700, White, uppercase
│ ▌                                       │
│ ▌  Every decision traceable to a        │  ← Body: Outfit 300, Silver
│ ▌  specific document in the Aksara      │
│ ▌  Vector Core. No hallucinated         │
│ ▌  sources.                             │
└──────────────────────────────────────────┘
```

### Animation
- Cards: staggered `fade-in-up`, 0.15s delay between cards

---

## Section 4: The Differentiator

> **Critical section.** This is what separates Episteme from every xAI vendor.

### Layout
- **Side-by-side comparison** in a frosted glass container
- Left column (gray/muted): Traditional xAI
- Right column (white/crimson accent): NTRJ Episteme
- Crimson vertical divider between columns

### Comparison Table (from §2.2.2)

| Dimension | Traditional xAI | NTRJ Episteme |
|-----------|----------------|---------------|
| **Focus** | Model internals, feature attribution | Workflow-level reasoning |
| **Output** | SHAP plots, statistical explanations | Episteme Logic Maps (visual flowcharts) |
| **Audience** | Data scientists | CRO, Board, DPO |
| **Answers** | "Which variable mattered most" | "Which document was used, which regulation applied, which human approved" |
| **Classification** | Research tool | Liability shield |

### Typography
- Column headers: JetBrains Mono, uppercase
- Left column label: `"TRADITIONAL xAI"` — Silver, muted
- Right column label: `"NTRJ EPISTEME"` — White, crimson underline
- Table cells: Outfit 300

### Boardroom Translation (pull-quote below table)
```
┌────────────────────────────────────────────────────────────┐
│  ▌  "A SHAP plot tells a data scientist which variable    │
│  ▌   mattered most. An Episteme Logic Map tells a CRO     │
│  ▌   which company document was used, which regulatory     │
│  ▌   constraint was applied, and which human approved      │
│  ▌   the output."                                          │
│  ▌                                                         │
│  ▌   — §2.2.2, Axiara Master Manual                       │
└────────────────────────────────────────────────────────────┘
```
- Quote: Playfair Display 400, italic, White, 22px
- Attribution: JetBrains Mono 300, Crimson

---

## Section 5: Integration Architecture

### Layout
- Full-width section with centered architecture diagram
- Diagram built as **layered HTML/CSS** (not an image)

### Architecture Visual
```
┌─────────────────────────────────────────────────┐
│              EXISTING AI MODELS                  │
│         (unchanged, no retraining)               │
├─────────────────────────────────────────────────┤
│                                                  │
│    ┌───────────────────────────────────────┐     │
│    │        NTRJ EPISTEME LAYER            │     │  ← Crimson border,
│    │     transparency · audit · lineage     │     │    glass bg
│    └───────────────────────────────────────┘     │
│                                                  │
├─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─┤
│    ┌──────────┐  ┌──────────┐  ┌──────────┐     │
│    │ Financial│  │ Health-  │  │  Energy  │     │
│    │ Services │  │   care   │  │  & Util  │     │
│    └──────────┘  └──────────┘  └──────────┘     │
│              REGULATED ENVIRONMENTS              │
└─────────────────────────────────────────────────┘
```

### Key Points (from §2.2.3)
- 3 frosted glass info cards below the diagram:

| Icon (Lucide) | Point |
|--------------|-------|
| `shield-off` | Does not replace models or modify weights |
| `zap` | Zero-disruption deployment over existing AI |
| `building-2` | Designed for financial, healthcare, energy, telecom |

---

## Section 6: Boardroom Translation

### Layout
- Full-width crimson accent band (subtle — `rgba(196,30,58,0.03)` bg)
- Centered content, max-width constrained

### Content
- **H2 (Playfair, italic, Silver):**
  - `"From research tool to liability shield"`
- **Body (Outfit 300, Silver):**
  - "The first is a research tool. The second is a liability shield." (§2.2.2)
  - Position Episteme as the component that makes ISO 42001 certification achievable

---

## Section 7: CTA

### Layout
- Full-width band, `padding: 80px 0`
- Background: obsidian with single diagonal crimson line

### Content
- **H2 (Playfair, italic, Silver):**
  - `"See your AI clearly"`
- **CTA:** Ghost button `"BOOK A DEMO →"`
- **Trust line (JetBrains Mono, Silver):**
  - `"POWERED BY NATARAJA PTE. LTD. (SINGAPORE)"`

---

## Episteme-Specific Overrides from MASTER

| Property | MASTER Default | Episteme Override |
|----------|---------------|-------------------|
| Card grid | 3-column | 3×2 for capabilities, side-by-side for comparison |
| Pull-quote style | N/A | Playfair italic, 22px, crimson left border, glass bg |
| Architecture diagrams | N/A | Layered HTML/CSS boxes with crimson borders |
| Comparison layout | N/A | 2-column with crimson vertical divider |
| Hero glow | None | Faint crimson radial gradient pulse (CSS) |

---

*Override for: src/pages/technology/episteme.html*
*Inherits all unspecified rules from: design-system/MASTER.md*
