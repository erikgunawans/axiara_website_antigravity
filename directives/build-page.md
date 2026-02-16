# Directive: Build a Page

> SOP for constructing any HTML page in the Axiara.id project.
> Read directives/axiara-brand.md FIRST for all visual rules.

## Pre-Build Checklist

Before writing any code:
1. Read directives/axiara-brand.md (brand rules)
2. Read design-system/MASTER.md (design system)
3. Check design-system/pages/{page-name}.md for page-specific overrides
4. Check execution/ for existing scripts that can help
5. Identify the correct Manual section for content

## Standard Page Structure

Every page must include:
1. <!DOCTYPE html> with lang="en"
2. Google Fonts import (Outfit, Playfair Display, JetBrains Mono)
3. Tailwind CSS CDN
4. Link to src/css/axiara.css (the Darkroom kit)
5. Lucide Icons CDN
6. Navbar component (from src/components/navbar.html)
7. Main content sections
8. Footer component (from src/components/footer.html)
9. Scroll-triggered animation JavaScript (IntersectionObserver)
10. prefers-reduced-motion media query to disable animations

## Content Source

All page copy comes from:
docs/Axiara_Master_Architecture_Operations_Manual_v2_0.md

Reference specific sections as noted in the project plan.
Do NOT invent content. Every claim must trace to the manual.

## Output Location

- Working files: src/pages/{category}/{page}.html
- Intermediate/temp files: .tmp/
- Final deliverables: pushed to cloud or exported for BeTheme

## Post-Build Verification

After building any page, run:
1. execution/validate_html.py {page} — checks structure & brand compliance
2. Visual review at 375px, 768px, 1024px, 1440px
3. Verify all animations are fade-in-up only (no bounce/spin/zoom)
4. Verify all border-radius is 0px
5. Verify no emojis are used as icons

## Self-Annealing Notes
(Updated as issues are discovered)
- [Placeholder]
