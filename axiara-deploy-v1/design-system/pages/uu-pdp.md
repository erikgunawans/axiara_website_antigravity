# Compliance: UU PDP (Law No. 27/2022) — Design Overrides

> Overrides `MASTER.md` for `src/pages/compliance/uu-pdp.html` only.
> **Privasi Adalah Hak (Privacy is a Right).**
> Content source: Manual §4.2

---

## Page Structure

```
┌─────────────────────────────────────────────────────┐
│  NAVBAR                                             │
├─────────────────────────────────────────────────────┤
│  HERO — "Kedaulatan Data Pribadi"                   │
│  Visual: Digital Shield / Padlock / Batik Network   │
├─────────────────────────────────────────────────────┤
│  THE LAW — 72-Hour Breach Notification              │
│  Editorial layout (Urgency & Accountability)        │
├─────────────────────────────────────────────────────┤
│  CONTROLLER OBLIGATIONS — Article 35 Grid           │
│  1. Legal Basis                                     │
│  2. Purpose Limitation                              │
│  3. Data Minimization                               │
│  4. Security Measures                               │
├─────────────────────────────────────────────────────┤
│  DATA SUBJECT RIGHTS — Interactive Accordion        │
│  Access, Correction, Erasure, Portability           │
├─────────────────────────────────────────────────────┤
│  COMPLIANCE CHECKLIST — Readiness Meter             │
│  Visual: DPO Appointed? DPIA Conducted?             │
├─────────────────────────────────────────────────────┤
│  CTA — "Appoint Your DPO"                           │
├─────────────────────────────────────────────────────┤
│  FOOTER                                             │
└─────────────────────────────────────────────────────┘
```

---

## Section 1: Hero

### Layout
- **Center-aligned** text (Protective).
- **Background**: "Digital Batik" pattern (Parang motif) interwoven with lock icons.

### Typography
- **Label:** `JetBrains Mono`, Garuda Gold, uppercase
  - `"COMPLIANCE — UNDANG-UNDANG NO. 27 TAHUN 2022"`
- **H1:** Outfit 900, White, uppercase
  - `"PRIVASI\nTERLINDUNGI."`
- **H2:** Playfair Display 400, italic, Silver
  - `"Protecting 270 million identities under one law."`

---

## Section 2: Controller Obligations (Article 35)

### Layout
- **Grid**: 4 Cards.
- **Style**: "Legal Codex" aesthetic. Minimalist, high contrast.

### 1. Lawful Basis
- **Text**: Ensure consent or legitimate interest for all processing.

### 2. Purpose Limitation
- **Text**: Process data *only* for specific, explicitly stated purposes.

### 3. Security Measures
- **Text**: Implement technical and organizational measures to prevent unauthorized access.

### 4. Breach Notification
- **Text**: Mandatory reporting within **3x24 hours** (72 hours) of a data breach.

---

## Section 3: Data Subject Rights

### Layout
- **Vertical Accordion**: Click to reveal details.
- **Visual**: Iconography for each right (Eye for Access, Trash for Erasure).

1. **Right to Access**: Request a copy of personal data.
2. **Right to Correction**: Rectify inaccurate data.
3. **Right to Erasure**: The "Right to be Forgotten".
4. **Right to Portability**: Move data between platforms.

---

## Section 4: Compliance Checklist

### Layout
- **Checklist Visual**:
- [ ] DPO Appointed (Data Protection Officer).
- [ ] DPIA (Impact Assessment) for high-risk processing.
- [ ] Cross-Border Transfer Assessment.
- [ ] Record of Processing Activities (ROPA).

---

## Compliance Specifics

| Property | Default | UU PDP Override |
|----------|---------|-----------------|
| Hero Visual | Abstract | Digital Batik / Shield |
| Icons | Generic | Padlock, Scales, Indonesia Map |
| Accent | Crimson | Crimson + "Privacy Green" (#0F9D58) |
