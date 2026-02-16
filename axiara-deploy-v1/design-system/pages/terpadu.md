# Terpadu — Design Overrides

> Overrides `MASTER.md` for `src/pages/technology/terpadu.html` only.
> **The Integration Layer.**
> Content source: Manual §2.3

---

## Page Structure

```
┌─────────────────────────────────────────────────────┐
│  NAVBAR                                             │
├─────────────────────────────────────────────────────┤
│  HERO — "NTRJ Terpadu" / "The Neural Fabric"       │
│  Visual: Network of connected nodes (CSS/SVG)       │
├─────────────────────────────────────────────────────┤
│  DEFINITION — "Unified Orchestration"               │
│  Data flow architecture                             │
├─────────────────────────────────────────────────────┤
│  CONNECTOR MATRIX — Grid of integrations            │
│  ERP, CRM, Databases, Models                        │
├─────────────────────────────────────────────────────┤
│  ENTERPRISE SECURITY — "Zero Trust"                 │
│  SSO, MFA, Audit Logging                            │
├─────────────────────────────────────────────────────┤
│  ORCHESTRATION — The workflow builder               │
│  Visual: Drag-and-drop interface mock               │
├─────────────────────────────────────────────────────┤
│  API SPECS — Developer focus                        │
│  Code snippet: POST /workflow/execute               │
├─────────────────────────────────────────────────────┤
│  CTA — "Connect Your Enterprise"                    │
├─────────────────────────────────────────────────────┤
│  FOOTER                                             │
└─────────────────────────────────────────────────────┘
```

---

## Section 1: Hero

### Layout
- **Center-aligned** text.
- **Background**: Dynamic node network (CSS/SVG), slowly rotating.

### Typography
- **Label:** `JetBrains Mono`, Crimson, uppercase
  - `"TECHNOLOGY — INTEGRATION HUB"`
- **H1:** Outfit 900, White, uppercase
  - `"NTRJ TERPADU"`
- **H2:** Playfair Display 400, italic, Silver
  - `"The Neural Fabric"`

---

## Section 2: Integration Matrix

### Layout
- **Grid Layout**: 4x4 grid of integration logos/icons.
- **Style**: Monochrome logos, lighting up on hover with crimson accent.

### Categories
1. **Data Sources**: SAP, Salesforce, Snowflake, Oracle.
2. **AI Models**: OpenAI, Anthropic, Llama, Mistral.
3. **Communication**: Slack, Teams, Email.
4. **Security**: Okta, Auth0, Active Directory.

---

## Section 3: Enterprise Security

### Features
1. **Zero Trust Architecture**: "Never trust, always verify."
2. **Single Sign-On (SSO)**: SAML 2.0, OIDC.
3. **Audit Logging**: Immutable logs for every API call.
4. **Encryption**: AES-256 at rest, TLS 1.3 in transit.

---

## Section 4: API & Orchestration

### Visual
- **Split Screen**:
  - Left: Visual Workflow Builder (Mockup).
  - Right: JSON API Request/Response.

```json
POST /api/v1/terpadu/workflow/execute
{
  "workflow_id": "wf_8823_audit",
  "inputs": {
    "document_id": "doc_9912",
    "compliance_check": true
  }
}
```

---

## Terpadu Specifics

| Property | Default | Terpadu Override |
|----------|---------|------------------|
| Hero Visual | None | Network/Node graph |
| Integration | List | Interactive 4x4 Matrix |
| Security | Generic | Specific protocols (SAML, TLS) |
