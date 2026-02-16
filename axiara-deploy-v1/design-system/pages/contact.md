# Contact — Design Overrides

> Overrides `MASTER.md` for `src/pages/contact.html` only.
> **Enterprise contact form** — minimal, authoritative, no-nonsense.
> Content source: Standalone page (no Manual section)

---

## Page Structure

```
┌─────────────────────────────────────────────────────┐
│  NAVBAR                                             │
├─────────────────────────────────────────────────────┤
│                                                     │
│  HERO — "Begin the Conversation"                    │
│  No subtitle clutter — just the invitation          │
│                                                     │
├─────────────────────────────────────────────────────┤
│                                                     │
│  MAIN — 2-column: Form + Company Info               │
│  60% form / 40% info (asymmetric weave)             │
│                                                     │
├─────────────────────────────────────────────────────┤
│  FOOTER                                             │
└─────────────────────────────────────────────────────┘
```

---

## Section 1: Hero

### Layout
- `min-height: 40vh`, vertically centered (shorter hero — form is the focus)
- Background: obsidian-to-charcoal gradient
- Content centered

### Typography
- **Label:** `JetBrains Mono`, Crimson, uppercase, `letter-spacing: 3px`
  - `"CONTACT"`
- **H1:** Outfit 900, White, uppercase
  - `"BEGIN THE CONVERSATION"`
  - Size: `clamp(2rem, 5vw, 3.5rem)`
- **Body:** Outfit 300, Silver
  - `"Every engagement begins with understanding. No obligation. No pitch decks."`

---

## Section 2: Form + Company Info

### Layout
- **2-column asymmetric** on desktop: 60% form / 40% info
- Single column on mobile: form first, info below
- Gap: `60px`

---

### Left Column: Contact Form

#### Form Container
- Frosted glass card (MASTER spec)
- `padding: 48px`
- Crimson left border (1px)

#### Fields

| Field | Type | Label | Placeholder |
|-------|------|-------|-------------|
| Name | `text` | `FULL NAME` | `"Your name"` |
| Company | `text` | `COMPANY` | `"Organization name"` |
| Role | `select` | `YOUR ROLE` | Options below |
| Email | `email` | `EMAIL` | `"your@company.com"` |
| Phone | `tel` | `PHONE (OPTIONAL)` | `"+62"` |
| Message | `textarea` | `MESSAGE` | `"Describe your AI governance challenge"` |

#### Role Select Options
```
— Select your role —
Chief Executive Officer (CEO)
Chief Risk Officer (CRO)
Data Protection Officer (DPO)
Chief Technology Officer (CTO)
IT Lead / Head of Engineering
Board Member
Other
```

#### Field Styling
```css
/* Labels */
font-family: var(--font-code);      /* JetBrains Mono */
font-size: 11px;
letter-spacing: 2px;
text-transform: uppercase;
color: var(--axiara-silver);
margin-bottom: 8px;

/* Inputs */
background: transparent;
border: none;
border-bottom: 1px solid rgba(255,255,255,0.2);
color: var(--axiara-white);
font-family: var(--font-eng);       /* Outfit */
font-weight: 300;
font-size: 16px;
padding: 12px 0;
transition: border-color 0.3s ease;

/* Focus state */
border-bottom-color: var(--axiara-crimson);
outline: none;

/* Select dropdown */
background: var(--axiara-obsidian);
border: 1px solid rgba(255,255,255,0.2);
color: var(--axiara-white);
font-family: var(--font-eng);
appearance: none;                    /* Custom arrow */

/* Textarea */
min-height: 120px;
resize: vertical;
```

#### Submit Button
- Ghost button (MASTER spec), full-width
- Text: `"SEND MESSAGE →"`
- `font-family: var(--font-code)` (JetBrains Mono)
- Hover: crimson border + crimson text + crimson glow bg

#### Form States
```css
/* Validation error */
border-bottom-color: var(--axiara-crimson);
/* Error text below field */
font-family: var(--font-code);
font-size: 11px;
color: var(--axiara-crimson);

/* Success state (after submit) */
/* Replace form with confirmation message */
```

#### Success State
After submission, replace the form content with:
```
┌──────────────────────────────────────────┐
│ ▌                                       │
│ ▌  ✓ MESSAGE RECEIVED                  │  ← Outfit 700, White
│ ▌                                       │
│ ▌  We will respond within               │  ← Outfit 300, Silver
│ ▌  24 business hours.                   │
│ ▌                                       │
│ ▌  Your reference:                      │
│ ▌  AXR-2026-XXXX                        │  ← JetBrains Mono, Crimson
│ ▌                                       │
└──────────────────────────────────────────┘
```
- The `✓` is an SVG checkmark icon (Lucide `check`), not an emoji

---

### Right Column: Company Info

#### Layout
- Sticky on desktop (`position: sticky; top: 100px`)
- 3 stacked info blocks, no glass card — clean minimal

#### Info Blocks

**Block 1: Entity**
```
PT AKSARA INOVASI TERPADU          ← Outfit 700, White, uppercase
Operating as Axiara.ai             ← Outfit 300, Silver
Jakarta, Indonesia                 ← Outfit 300, Silver

**Block 1.5: Global Presence**
```
Singapore
80 Robinson Road                   ← Outfit 300, Silver

Zurich
Bahnhofstrasse 10                  ← Outfit 300, Silver
```
```

**Block 2: Direct Contact**
```
EMAIL                              ← JetBrains Mono, Crimson, uppercase label
hello@axiara.ai                    ← Outfit 300, White, hover: Crimson

LINKEDIN                           ← JetBrains Mono, Crimson, uppercase label
linkedin.com/company/axiara        ← Outfit 300, White, hover: Crimson
```

**Block 3: Engagement Note**
```
┌──────────────────────────────────┐
│ ▌  HOW WE ENGAGE                │  ← JetBrains Mono, Crimson
│ ▌                                │
│ ▌  Every partnership begins      │  ← Outfit 300, Silver
│ ▌  with a 30-Day Sprint.        │
│ ▌  No retainers without         │
│ ▌  diagnosis. No solutions      │
│ ▌  without architecture.        │
│ ▌                                │
│ ▌  LEARN ABOUT THE SPRINT →     │  ← Ghost link → sprint.html
└──────────────────────────────────┘
```
- This block uses a frosted glass card with crimson left border

---

## Accessibility Requirements

| Element | A11Y Rule |
|---------|-----------|
| All `<input>` | Must have `<label>` with `for` attribute |
| `<select>` | Must have `<label>` and `aria-label` |
| `<textarea>` | Must have `<label>` |
| Error messages | Use `aria-live="polite"` |
| Submit button | `type="submit"`, clear focus ring |
| Required fields | Use `required` attribute + `aria-required="true"` |
| Success state | Use `role="status"` and `aria-live="polite"` |

---

## Contact-Specific Overrides from MASTER

| Property | MASTER Default | Contact Override |
|----------|---------------|-----------------|
| Hero height | `100vh` | `40vh` (form is the focus, not the hero) |
| Form inputs | N/A | Underline-only style (no bordered boxes) |
| Labels | N/A | JetBrains Mono, 11px, uppercase, Silver |
| Right column | N/A | Sticky positioning on desktop |
| Page density | Sections + scroll | Compact — hero + form + footer only |
| CTA | Ghost button | Full-width submit as CTA |

---

*Override for: src/pages/contact.html*
*Inherits all unspecified rules from: design-system/MASTER.md*
