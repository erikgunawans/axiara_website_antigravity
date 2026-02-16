# Aksara Vector Core — Design Overrides

> Overrides `MASTER.md` for `src/pages/services/aksara.html` only.
> **The Sovereign Memory Engine.**
> Content source: Manual §4.6

---

## Page Structure

```
┌─────────────────────────────────────────────────────┐
│  NAVBAR                                             │
├─────────────────────────────────────────────────────┤
│  HERO — "Total Recall. Zero Leakage."               │
│  Subtitle: "Sovereign RAG Infrastructure."          │
│  Background: Vector Field / Connecting Dots Viz     │
│                                                     │
├─────────────────────────────────────────────────────┤
│  ARCHITECTURE - The Vector Pipeline                 │
│  Ingest -> Chunk -> Embed -> Store -> Retrieve      │
│  Visual: Horizontal flow, crimson data packets      │
├─────────────────────────────────────────────────────┤
│  FEATURE TRIAD (Glass Cards)                        │
│  1. SOVEREIGNTY (Your cloud, your keys)             │
│  2. GRANULARITY (Chunk-level RBAC)                  │
│  3. SCALABILITY (Billion-scale indices)             │
├─────────────────────────────────────────────────────┤
│  INTEGRATION SPECS - Terminal Style                 │
│  Code snippet block showing Python SDK usage        │
│  from axiara import VectorClient                    │
├─────────────────────────────────────────────────────┤
│  DEPLOYMENT OPTIONS - Grid                          │
│  VPC, On-Prem, Dedicated Clusters                   │
├─────────────────────────────────────────────────────┤
│  CTA BAND — "Initialize Core"                       │
│  Link to Contact / Docs                             │
├─────────────────────────────────────────────────────┤
│  FOOTER                                             │
└─────────────────────────────────────────────────────┘
```

---

## Section 1: Hero

### Layout
- **Left-aligned** text.
- **Right-aligned** interactive 3D vector visual (CSS/Canvas placeholder).

### Typography
- **Label:** `JetBrains Mono`, Crimson, uppercase
  - `"SERVICE — VECTOR DATABASE & RAG"`
- **H1:** Outfit 900, White, uppercase
  - `"TOTAL RECALL.\nZERO LEAKAGE."`
- **H2:** Playfair Display 400, italic, Silver
  - `"The memory of the enterprise, secured in obsidian."`

---

## Section 2: Architecture (The Pipeline)

### Visual
- **Flowchart**:
  1. **Ingest** (PDFs, SQL, APIs)
  2. **Chunk** (Semantic Splitting)
  3. **Embed** (High-dim Vectors)
  4. **Store** (Aksara Core)
  5. **Retrieve** (Context Window)

- **Style**: Minimalist, `JetBrains Mono` labels, Crimson arrows.

---

## Section 3: Feature Triad

### Cards
1. **Sovereign**: Icon `lock`. "Data never leaves your VPC. Encryption at rest and in transit (AES-256)."
2. **Granular**: Icon `layers`. "RBAC applied at the document chunk level. Departmental segregation."
3. **Scalable**: Icon `database`. "Horizontal sharding. <50ms P99 latency at 100M vectors."

---

## Section 4: Integration (The Code)

### Visual
- **Terminal Window**:
  - Header: `bash ~ axiara-cli status`
  - Body: Python code snippet.

```python
from axiara import VectorClient

client = VectorClient(api_key="AX_...", region="us-east-1")

# Sovereign Ingest
doc_id = client.ingest(
    file="q3_financials.pdf", 
    encryption="customer_managed_key"
)

# Secure Retrieval
context = client.query(
    "What is our Q3 risk exposure?", 
    filter={"access_level": "executive"}
)
```

---

## Section 5: Deployment

| Option | Description |
|--------|-------------|
| **Managed Cloud** | Fully managed cluster in AWS/GCP/Azure. |
| **VPC Peering** | Data stays in your VPC, compute in ours. |
| **Air-gapped** | Full binary deployment on your metal. |

---

## Aksara Specifics

| Property | Default | Aksara Override |
|----------|---------|-----------------|
| Hero Align | Left | Left (Split with Vector Viz) |
| Code | None | Prominent SDK/API display |
| Icon Set | Lucide | Database/Security focus |
