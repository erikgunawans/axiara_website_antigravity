# End-to-End Audit (E2E) — Design Overrides

> Overrides `MASTER.md` for `src/pages/services/e2e.html` only.
> **Primary technical deep-dive page.**
> Content source: Manual §4.0–§4.5

---

## Page Structure

```
┌─────────────────────────────────────────────────────┐
│  NAVBAR                                             │
├─────────────────────────────────────────────────────┤
│                                                     │
│  HERO — "The Glass Box Protocol"                    │
│  Subtitle: "Audit. Monitor. Insure."                │
│  Background: Cinematic Model Weights Viz            │
│                                                     │
├─────────────────────────────────────────────────────┤
│  THE E2E MODEL — Diagrammatic Flow                  │
│  Interactive SVG/HTML diagram of the 3 steps        │
│  1. Audit (Static) -> 2. Monitor (Dynamic) -> 3. Insure (Transfer)
├─────────────────────────────────────────────────────┤
│  PHASE 1: AUDIT (Deep Dive)                         │
│  Technical details on weights analysis, data lineage│
│  "The Static Snapshot"                              │
├─────────────────────────────────────────────────────┤
│  PHASE 2: MONITOR (Deep Dive)                       │
│  Episteme Integration, drift detection, real-time   │
│  "The Dynamic Pulse"                                │
├─────────────────────────────────────────────────────┤
│  PHASE 3: INSURE (Deep Dive)                        │
│  Actuarial backing, residual risk transfer          │
│  "The Liability Shield"                             │
├─────────────────────────────────────────────────────┤
│  TECHNICAL SPECIFICATIONS — Accordion/Grid          │
│  Supported Models (Llama 3, GPT-4, Claude 3)        │
│  Scan Types (Bias, Poisoning, PII, hallucination)   │
├─────────────────────────────────────────────────────┤
│  CTA BAND — "Deploy the Protocol"                   │
│  Links to Sprint (Step 1) or Contact (Custom)       │
├─────────────────────────────────────────────────────┤
│  FOOTER                                             │
└─────────────────────────────────────────────────────┘
```

---

## Section 1: Hero

### Layout
- **Center-aligned** technical manifesto.
- **Background**: `obsidian` with a slow-moving "Matrix code" or "Weights" visualization (CSS/Canvas).

### Typography
- **Label:** `JetBrains Mono`, Crimson, uppercase, spacing 3px
  - `"SERVICE — END-TO-END RISK MANAGEMENT"`
- **H1:** Outfit 900, White, uppercase
  - `"THE GLASS BOX PROTOCOL"`
- **H2:** Playfair Display 400, italic, Silver
  - `"Total algorithmic transparency. From weights to warranty."`

### CTAs
- Primary: `"INITIATE AUDIT"` (border-crimson)
- Secondary: `"VIEW ARCHITECTURE"` (ghost)

---

## Section 2: The E2E Model (Diagram)

### Layout
- **Horizontal Process Flow** on desktop.
- **Vertical Stack** on mobile.
- Connected by **animated crimson data pipes**.

### Components (Glass Cards)
1. **AUDIT**: Icon `file-search`. "Static Inspection."
2. **MONITOR**: Icon `activity`. "Real-time Telemetry."
3. **INSURE**: Icon `shield`. "Residual Risk Transfer."

---

## Section 3, 4, 5: Deep Dives

### Style: "The Dossier"
- Alternating layout (Left Text/Right Graphic, then swapped).
- **Graphics**: High-fidelity, technical wireframes (using CSS borders/grid).
- **Typography**: `JetBrains Mono` for data points, `Outfit` for headers.

#### Phase 1: Audit
- **Focus**: Weights & Biases inspection.
- **Data Points**:
  - "Model Weights Analysis"
  - "Training Data Lineage"
  - "Adversarial Stress Testing"

#### Phase 2: Monitor
- **Focus**: Episteme Platform.
- **Data Points**:
  - "Drift Detection (< 0.05%)"
  - "Prompt Injection Firewalls"
  - "Latency: 24ms overhead"

#### Phase 3: Insure
- **Focus**: Liability wrapper.
- **Data Points**:
  - "Underwritten by Lloyds A+"
  - "Hallucination Coverage"
  - "IP Infringement Defense"

---

## Section 6: Technical Specs

### Layout
- **4-Column Grid** of specs.
- Minimalist, `JetBrains Mono` 10px text.

| Category | Specs |
|----------|-------|
| **Models** | Llama 3, GPT-4o, Claude 3.5, Mistral Large |
| **Vectors** | Pinecone, Milvus, Weaviate, Qdrant |
| **Compliance** | EU AI Act, NIST AI RMF, ISO 42001, NYC 144 |
| **Deployment** | On-Prem (Airgapped), VPC, Hybrid Edge |

---

## E2E Specifics

| Property | Default | E2E Override |
|----------|---------|--------------|
| Hero Align | Left | Center (Technical Manifesto) |
| Diagram | None | Animated SVG/CSS Process Flow |
| Content | Marketing | Technical/Engineering focus |
