# Page-Specific Design Overrides

Place page-specific `.md` files here to override the `MASTER.md` rules.

## Retrieval Rules

1. When building **page X**, check `design-system/pages/X.md` first
2. If the page file exists, its rules **override** `MASTER.md`
3. If no page file exists, `MASTER.md` applies exclusively
4. Page files only need to define **deviations** — anything not specified inherits from MASTER

## Naming Convention

```
design-system/pages/
├── homepage.md
├── about.md
├── sprint.md
├── e2e.md
├── aksara.md
├── episteme.md
├── terpadu.md
├── telco.md
├── energy.md
├── banking.md
├── bumn.md
├── iso-42001.md
├── uu-pdp.md
├── ai-decree.md
├── insights.md
└── contact.md
```

## Example Override

```markdown
# Sprint Page — Design Overrides

> Overrides MASTER.md for sprint.html only

## Layout
- Use **4-column timeline** layout for Weeks 1–4 (horizontal on desktop, vertical on mobile)
- Each week card gets a **numbered crimson accent** instead of default glass card

## Typography
- Week labels: JetBrains Mono, weight 400, uppercase, crimson
```
