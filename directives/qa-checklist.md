# QA Checklist for Axiara.ai

This document serves as the master checklist for Quality Assurance, specifically focusing on Accessibility (WCAG 2.1 AA) and Brand Compliance.

## 1. Accessibility (A11Y)

### Images & Media
- [ ] **Alt Text**: All `<img>` tags must have a descriptive `alt` attribute. Decorational images must have `alt=""`.
- [ ] **Icons**: `lucide` icons should be aria-hidden or have appropriate aria-labels if interactive.

### Forms
- [ ] **Labels**: All `<input>`, `<textarea>`, and `<select>` elements must have an associated `<label>` (via `for` attribute or nesting) or `aria-label`.
- [ ] **Focus States**: Interactive elements must have a visible focus state (Crimson outline).

### Content Structure
- [ ] **Language**: `<html>` tag must have `lang="en"`.
- [ ] **Headings**: H1-H6 hierarchy must be sequential without skipping levels (e.g. H2 -> H4 is forbidden).
- [ ] **Skip Link**: A "Skip to content" link must exist as the first focusable element.

### Navigation
- [ ] **Keyboard**: All interactive elements must be reachable via Tab key.
- [ ] **Focus Order**: Focus order must match visual order.

### Color & Contrast
- [ ] **Contrast**: Text must satisfy 4.5:1 contrast against background (AA).
    - *Warning*: Crimson text on Obsidian background is low contrast (~3.96:1). Use for large text only or non-text elements.

### Motion
- [ ] **Reduced Motion**: Respect `prefers-reduced-motion` media query (disable animations).

## 2. Responsive Design
- [ ] **Mobile**: Single column grids, legible text (16px+ for inputs), tap targets >= 48px.
- [ ] **No Overflow**: No horizontal browsing on any viewport.

## 3. Brand Compliance
- [ ] **Border Radius**: 0px everywhere.
- [ ] **Fonts**: Outfit / Playfair Display / JetBrains Mono only.
- [ ] **Icons**: Lucide only (No Emojis).
