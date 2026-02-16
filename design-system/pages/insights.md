# Insights Blog — Design Overrides

> Overrides `MASTER.md` for `src/pages/insights/index.html` only.
> **Thought Leadership & Regulatory Intelligence.**
> Content source: Manual §5.0

---

## Page Structure

```
┌─────────────────────────────────────────────────────┐
│  NAVBAR                                             │
├─────────────────────────────────────────────────────┤
│  HERO — "The Signal in the Noise"                   │
│  Visual: Abstract Data Wave / Signal Rendering      │
├─────────────────────────────────────────────────────┤
│  FEATURED ARTICLE — Large Hero Card                 │
│  Headline: "The End of Black Box AI"                │
│  Tag: "Deep Dive"                                   │
├─────────────────────────────────────────────────────┤
│  CATEGORIES — Filter Bar                            │
│  [All] [Regulatory] [Technical] [Strategic]         │
├─────────────────────────────────────────────────────┤
│  ARTICLE GRID — 3-Column Layout                     │
│  - Card 1: UU PDP Implementation Guide              │
│  - Card 2: ISO 42001 Checklist                      │
│  - Card 3: The Ethics of Generative AI              │
├─────────────────────────────────────────────────────┤
│  NEWSLETTER — "Intelligence, Weekly"                │
│  Input field + "Subscribe" button                   │
├─────────────────────────────────────────────────────┤
│  FOOTER                                             │
└─────────────────────────────────────────────────────┘
```

---

## Section 1: Hero

### Layout
- **Left-aligned** text (Editorial Style).
- **Background**: "Signal" visualization (Sine waves or frequency bars).

### Typography
- **Label:** `JetBrains Mono`, White, uppercase
  - `"AXIARA INTELLIGENCE"`
- **H1:** Playfair Display 700, White, Italic
  - `"The Signal in the Noise."`
- **Subtitle:** Outfit 300, Silver
  - `"Navigating the complexity of AI regulation with clarity and precision."`

---

## Section 2: Featured Article

### Layout
- **Full-width Card**: Image on left (or top on mobile), Text on right.
- **Visual**: High-contrast photography or abstract 3D render.

### Content
- **Headline**: "Creating the Gold Standard for AI Governance in Indonesia."
- **Excerpt**: "Why Circular No. 9 is just the beginning of a new regulatory era."
- **CTA**: "Read Analysis ->"

---

## Section 3: Article Grid

### Layout
- **Grid**: 3 Columns.
- **Card Style**: "Glass" background, thin border, hover glow.

### Sample Content
1.  **Regulatory**: "Understanding Article 35: Your Obligations Explained." (UU PDP)
2.  **Technical**: "De-biasing Algorithms: A Practical Guide." (AI Decree)
3.  **Strategic**: "ISO 42001: The competitive advantage of trust." (Standards)

---

## Section 4: Newsletter

### Layout
- **Minimalist Band**.
- **Copy**: "Join 5,000+ Risk Officers and CTOs."
- **Form**: Email input (Ghost style) + "Subscribe" button (Solid White).

---

## Compliance Specifics

| Property | Default | Insights Override |
|----------|---------|-------------------|
| Hero Visual | Abstract | Signal Waves |
| Icons | Generic | Book, Lightbulb, Signal |
| Accent | Crimson | Crimson + White |
