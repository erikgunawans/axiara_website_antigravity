# Industry: Telecommunications — Design Overrides

> Overrides `MASTER.md` for `src/pages/industries/telco.html` only.
> **Intelligence at the Edge.**
> Content source: Manual §3.1

---

## Page Structure

```
┌─────────────────────────────────────────────────────┐
│  NAVBAR                                             │
├─────────────────────────────────────────────────────┤
│  HERO — "Intelligence at the Edge"                  │
│  Visual: 5G Network Topology / Signal Waves         │
├─────────────────────────────────────────────────────┤
│  THE CHALLENGE — Scale & Governance                 │
│  Editorial layout                                   │
├─────────────────────────────────────────────────────┤
│  USE CASES — 3 Deep Dives                           │
│  1. 5G Slice Optimization                           │
│  2. Churn Prediction (Retention)                    │
│  3. Infrastructure Predictive Maintenance           │
├─────────────────────────────────────────────────────┤
│  REGULATORY MATRIX — Compliance Grid                │
│  FCC CPNI, GDPR, local provisions                   │
├─────────────────────────────────────────────────────┤
│  CASE STUDY — Tier-1 Carrier Success                │
│  Metric-focused results                             │
├─────────────────────────────────────────────────────┤
│  CTA — "Secure Your Network"                        │
├─────────────────────────────────────────────────────┤
│  FOOTER                                             │
└─────────────────────────────────────────────────────┘
```

---

## Section 1: Hero

### Layout
- **Left-aligned** text.
- **Background**: Abstract 5G signal waves (CSS/SVG), pulsing crimson/silver.

### Typography
- **Label:** `JetBrains Mono`, Crimson, uppercase
  - `"INDUSTRY — TELECOMMUNICATIONS"`
- **H1:** Outfit 900, White, uppercase
  - `"INTELLIGENCE\nAT THE EDGE."`
- **H2:** Playfair Display 400, italic, Silver
  - `"Governing the neural network of the modern world."`

---

## Section 2: Use Cases (The Triad)

### Layout
- **Vertical Stack**: 3 distinct sections, alternating layout (Left/Right).
- **Style**: High-tech, data-dense.

### 1. 5G Network Optimization
- **Goal**: Dynamic slicing based on real-time traffic.
- **Axiara Role**: Audit the reinforcement learning models managing bandwidth allocation. Ensure fair usage policy compliance.

### 2. Predictive Churn & Retention
- **Goal**: Identify at-risk subscribers.
- **Axiara Role**: Prevent algorithmic bias in retention offers (e.g., ensuring high-value offers aren't racially skewed).

### 3. Infrastructure Resilience
- **Goal**: Predict tower/node failure.
- **Axiara Role**: Verify the integrity of sensor data inputs and maintenance schedule outputs.

---

## Section 3: Regulatory Matrix

### Layout
- **Grid**: 2x2 or 3x1 cards.
- **Style**: "Compliance Dossier" aesthetic.

| Standard | Requirement | Axiara Solution |
|----------|-------------|-----------------|
| **FCC CPNI** | Protect customer proprietary network info. | differential privacy filters on training data. |
| **GDPR/CCPA** | Right to explanation. | Episteme Logic Maps for retention decisions. |
| **Net Neutrality** | Non-discriminatory traffic management. | Bias audits for traffic shaping algorithms. |

---

## Section 4: Case Study

### Content
> **Client**: Tier-1 North American Carrier
> **Challenge**: 40% false positive rate in fraud detection, leading to customer insults.
> **Solution**: Deployed Axiara Sentinel to govern the fraud model.
> **Result**: 
> - **90% reduction** in false positives.
> - **$14M** annual savings in support costs.
> - **Zero** regulatory penalties.

---

## Telco Specifics

| Property | Default | Telco Override |
|----------|---------|----------------|
| Hero Visual | Abstract | Signal/Waveform animation |
| Icons | Generic | Tower, Signal, Chip, Satellite |
| Accent | Crimson | Crimson + "Signal Blue" (optional, keep Crimson for brand consistency) |
