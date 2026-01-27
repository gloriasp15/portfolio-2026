# Event Scoring & Tiering Logic  
**Operational Event Orchestration – Commercial Babel Tower**

---

## Purpose

The event scoring and tiering mechanism is designed to establish a **shared operational prioritization model** across retail, e-commerce and supply functions.

Its objective is to ensure that operational relevance is determined by **event characteristics**, not by local interpretation, hierarchy or escalation behavior.

This scoring logic acts as the foundation for:
- Priority tier assignment  
- Shared operational backlog composition  
- E-card visibility and triage cadence  

---

## Design Principles

The scoring model follows a small set of guiding principles:

- **Objectivity**  
  Prioritization is derived from event attributes, not team perception.

- **Transparency**  
  Scoring rules are explicit and understandable by operational teams.

- **Simplicity**  
  The model avoids overfitting and remains actionable in day-to-day operations.

- **Evolvability**  
  Scoring weights and thresholds can be adjusted over time without redesigning the operating model.

---

## Scoring Dimensions

Each operational event is evaluated across three core dimensions.

### 1. Impact  
Measures the potential business exposure associated with the event.

Typical indicators:
- Revenue or sales impact  
- Stock availability risk  
- Customer experience exposure  

Impact answers the question:  
**“How much does this matter if left unaddressed?”**

---

### 2. Urgency  
Measures the time sensitivity of the event.

Typical indicators:
- Time to stock-out or service degradation  
- Promotional or campaign dependency  
- Operational deadlines  

Urgency answers the question:  
**“How quickly does this require action?”**

---

### 3. Recurrence  
Measures whether the event represents an isolated incident or a repeating pattern.

Typical indicators:
- Frequency of similar events  
- Historical repetition over a defined time window  

Recurrence answers the question:  
**“Is this a symptom or a pattern?”**

---

## Scoring Model (Illustrative)

Each dimension is scored on a normalized scale (e.g. 1–5).

| Dimension  | Low (1) | Medium (3) | High (5) |
|-----------|--------|------------|----------|
| Impact    | Limited local effect | Multi-store or channel impact | Broad commercial exposure |
| Urgency   | No immediate risk | Time-sensitive | Immediate action required |
| Recurrence| One-off | Occasional | Recurrent pattern |

The combined score is calculated as a weighted aggregation of the three dimensions.

> Weights may vary depending on operational context and maturity.

---

## Tier Assignment

Based on the aggregated score, events are assigned to priority tiers.

| Tier | Description | Operational Treatment |
|-----|------------|-----------------------|
| High | Critical operational deviation | Immediate visibility and daily triage |
| Medium | Relevant but non-critical | Included in regular review cadence |
| Low | Informational or minor | Logged for monitoring and pattern detection |

Tier assignment determines:
- Inclusion in the shared operational backlog  
- Visibility through e-cards  
- Review and escalation cadence  

---

## Operational Implications

The tiering mechanism enables:

- Consistent prioritization across functions  
- Reduced subjective escalation behavior  
- Focused operational attention on what matters most  
- Early detection of recurring operational issues  

Priority is no longer negotiated; it is **derived**.

---

## Governance & Evolution

The scoring model is governed as an operational asset.

- Scoring dimensions remain stable  
- Thresholds and weights are reviewed periodically  
- Adjustments are based on observed outcomes, not exceptions  

This ensures continuity while allowing the model to evolve with business needs.

---

## Relationship to the Operating Model

Event scoring and tiering directly support:

- Shared operational backlog composition  
- E-card visibility and triage  
- Execution routing to downstream systems (e.g. ServiceNow)  

Without scoring, orchestration collapses into noise.

---

## Reference

This artefact supports **Section B.3 – Event Scoring & Tiering** of the main business case README.

