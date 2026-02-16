# Directive: Generate & Manage the Design System

> SOP for running the ui-ux-pro-max design system generator.
> Tools: .agent/.shared/ui-ux-pro-max/scripts/search.py

## When to Run

- ALWAYS run --design-system before building the first page
- Run page-specific overrides (--page flag) for complex pages
- Run supplementary domain searches when you need deeper detail

## Master Design System Generation
```bash
python3 .agent/.shared/ui-ux-pro-max/scripts/search.py \
  "AI governance enterprise dark luxury editorial cinematic B2B" \
  --design-system --persist -p "Axiara"
```

Output: design-system/MASTER.md

## Page-Specific Overrides
```bash
python3 .agent/.shared/ui-ux-pro-max/scripts/search.py \
  "<page-specific-keywords>" \
  --design-system --persist -p "Axiara" --page "<page-name>"
```

Output: design-system/pages/{page-name}.md

## Hierarchical Retrieval Rule

When building a page:
1. Check design-system/pages/{page-name}.md FIRST
2. If it exists, its rules OVERRIDE the Master file
3. If it does not exist, use design-system/MASTER.md exclusively

## Conflict Resolution

If ui-ux-pro-max output conflicts with docs/agency_9_creative.md:
→ agency_9_creative.md ALWAYS WINS
→ The brand file is the supreme authority on visual decisions
→ ui-ux-pro-max provides supplementary intelligence (UX patterns, 
  landing structure, chart types) — not brand overrides

## Supplementary Searches

| Need | Command |
|------|---------|
| UX guidelines | --domain ux "animation accessibility" |
| Landing structure | --domain landing "hero social-proof CTA" |
| Typography detail | --domain typography "serif sans editorial" |
| Color detail | --domain color "dark obsidian crimson" |
| Chart types | --domain chart "real-time dashboard" |
| Stack guidelines | --stack html-tailwind "responsive glassmorphism" |

## Self-Annealing Notes
- [Placeholder]
