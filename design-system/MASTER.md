# Axiara Design System — MASTER

> **Global Source of Truth.** All pages inherit from this file unless overridden by a page-specific file in `design-system/pages/`.
>
> Sources: `docs/agency_9_creative.md` · `directives/axiara-brand.md`

---

## Visual Concept

**"The Darkroom"** — Editorial & Cinematic

The site feels like a high-end architectural portfolio crossed with a sovereign intelligence platform. Zaha Hadid Architects meets Palantir. Content does not "pop" (playful) — it **"unveils"** (premium).

---

## Color Palette

> [!CAUTION]
> **Non-negotiable.** No other colors permitted unless explicitly approved.

| Token | Hex | CSS Variable | Usage |
|-------|-----|-------------|-------|
| Obsidian | `#0D0D0D` | `--axiara-obsidian` | Primary background |
| Crimson | `#C41E3A` | `--axiara-crimson` | Accent lines, hover states, "Weave" motif |
| White | `#FFFFFF` | `--axiara-white` | H1 headlines, button borders |
| Silver | `#A8A8A8` | `--axiara-silver` | Body text, H2 subheads |
| Charcoal | `#1A1A2E` | `--axiara-charcoal` | Gradient endpoint |

### Extended Tokens (Derived)

| Token | Value | Usage |
|-------|-------|-------|
| Glass | `rgba(26,26,46,0.4)` | Frosted card backgrounds |
| Glass Hover | `rgba(26,26,46,0.8)` | Card hover state |
| Crimson Glow | `rgba(196,30,58,0.05)` | Button hover tint |
| Gradient | `linear-gradient(135deg, #0D0D0D 0%, #1A1A2E 100%)` | "Episteme" layer bg |

---

## Typography

### Font Stack

| Font | CSS Variable | Weight(s) | Role |
|------|-------------|-----------|------|
| **Outfit** | `--font-eng` | 300, 400, 700, 900 | Structure — headings (H1, H3), body, navigation |
| **Playfair Display** | `--font-phil` | 400, 600, 400i | Philosophy — H2 editorial headlines |
| **JetBrains Mono** | `--font-code` | 300, 400 | Technical truth — buttons, labels, code |

### Google Fonts Import

```
https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400&family=Outfit:wght@300;400;700;900&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap
```

### Heading Hierarchy

| Level | Font | Weight | Style | Color | Transform |
|-------|------|--------|-------|-------|-----------|
| H1 | Outfit | 900 | Normal | White | `uppercase`, `letter-spacing: 0.05em` |
| H2 | Playfair Display | 400 | *Italic* | Silver | None |
| H3 | Outfit | 700 | Normal | White | `uppercase` |
| H4–H6 | Outfit | 400 | Normal | Silver | None |

### Body Text

- Font: Outfit, weight 300
- Color: Silver (`#A8A8A8`)
- Size: `18px` (larger "book" size for readability)
- Line-height: `1.7`

---

## UI Components

### Ghost Buttons

```css
background: transparent;
border: 1px solid var(--axiara-white);
color: var(--axiara-white);
font-family: var(--font-code);    /* JetBrains Mono */
border-radius: 0px;               /* Knife-edge apex */
text-transform: uppercase;
letter-spacing: 2px;
transition: all 0.4s ease;
```

**Hover state:**
```css
border-color: var(--axiara-crimson);
color: var(--axiara-crimson);
background: rgba(196, 30, 58, 0.05);  /* Crimson glow */
```

### Frosted Glass Cards

```css
background: rgba(26, 26, 46, 0.4);
backdrop-filter: blur(12px);
-webkit-backdrop-filter: blur(12px);
border-left: 1px solid var(--axiara-crimson);  /* Asymmetric border — left only */
border-top: none;
border-right: none;
border-bottom: none;
padding: 40px;
```

**Hover state:**
```css
background: rgba(26, 26, 46, 0.8);
border-left-width: 4px;  /* Thicker crimson line */
```

### Wireframe Image Containers

```css
transform: translate(20px, 20px);
border: 1px solid rgba(255, 255, 255, 0.1);
z-index: 1;
```

---

## Layout

- **Full Width** (100%) — no boxed layout
- **Asymmetric Weave** — offset images and text to break the grid
- **Background texture** — obsidian-to-charcoal gradient with optional hex grid pattern, `background-attachment: fixed`

### Responsive Breakpoints

| Breakpoint | Width | Target |
|------------|-------|--------|
| Mobile | `375px` | Phones |
| Tablet | `768px` | iPad / tablets |
| Desktop | `1440px` | Standard desktop |

---

## Motion & Animation

> [!IMPORTANT]
> **Only `fade-in-up` is permitted.** No bounce, spin, zoom, elastic, or scale.

| Property | Value |
|----------|-------|
| Animation | `fade-in-up` only |
| Duration | `0.8s–1.2s` |
| Easing | `ease-out` |
| Trigger | `IntersectionObserver` (scroll-triggered) |
| Parallax | Slow, heavy parallax scrolling allowed |

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Icons

- **Library:** Lucide (SVG icons via CDN)
- **CDN:** `https://unpkg.com/lucide@latest`
- **Style:** Stroke-only, 24×24, `stroke-width: 1.5`
- **Color:** Default White, Crimson on hover/active

> [!WARNING]
> No emojis anywhere in visible UI text. Ever.

---

## Photography

- **Style:** Black & white only
- **Optional overlay:** Crimson (`#C41E3A`) duotone at 25% opacity
- **Format:** WebP, responsive srcset (375w, 768w, 1440w)
- **Aesthetic:** Editorial, documentary — no stock photography poses
- **Processing:** `python3 execution/optimize_images.py`

---

## Border Radius

> [!CAUTION]
> **`border-radius: 0px` everywhere.** No exceptions. No Tailwind `rounded-*` classes.
> This is the "knife-edge apex" — the brand's architectural identity.

---

## Anti-Patterns (NEVER Do)

| ❌ Don't | ✅ Do Instead |
|----------|--------------|
| Use emojis as icons | Use Lucide SVG icons |
| Use `rounded-*` Tailwind classes | Use `rounded-none` or no radius |
| Use bounce/spin/zoom animations | Use `fade-in-up` only |
| Use full-color stock photos | Use B&W with optional crimson overlay |
| Use playful/bright colors | Stick to the 5-color palette |
| Use exclamation marks in copy | Engineering tone, period. |
| Use "help you leverage synergies" | Use "We build" / "We deploy" / "We transform" |
| Use `border-radius > 0` anywhere | Everything is `0px` sharp |
| Use solid opaque cards | Use frosted glass with `backdrop-filter: blur` |
| Use solid-fill buttons | Use ghost buttons (transparent bg, white border) |

---

## CSS Kit

Generated by `python3 execution/generate_css.py` → `src/css/axiara.css`

**7 Blocks:**
1. **A — Fonts** (Google Fonts import)
2. **B — Variables** (Darkroom palette + font stack)
3. **C — Typography** (Mixed serif/sans editorial look)
4. **D — UI Elements** (Ghost buttons + frosted glass cards)
5. **E — Layout** (Asymmetric weave + background texture)
6. **F — Motion** (Fade-in-up + reduced motion)
7. **G — Utilities** (Helper classes)

---

## Conflict Resolution

When `agency_9_creative.md` output conflicts with `directives/axiara-brand.md`:

1. **`axiara-brand.md` wins** — it is the non-negotiable constraint layer
2. **`agency_9_creative.md` informs** — it provides the aesthetic direction
3. **This MASTER file is the synthesis** — the resolved, final answer

---

*Generated: 2026-02-16 from agency_9_creative.md + axiara-brand.md*
*Retrieval: page files in `design-system/pages/` override this MASTER*
