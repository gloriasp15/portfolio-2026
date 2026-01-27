# E-Cards & Shared Operational Backlog  
**Operational Event Orchestration – The Commercial Babel Tower**

---

## Purpose

E-cards are the operational interface through which prioritized events are surfaced, reviewed and acted upon by teams.

They transform automated event detection and tiering into **shared, actionable decision units**, ensuring that operational attention is focused on what matters most while preserving traceability and ownership.

This artefact supports **Section B.4 – E-Cards & Shared Operational Backlog** of the main business case.

---

## Design Principles

The e-card mechanism is designed around a small set of operational principles:

- **Priority-driven visibility**  
  Only events that exceed relevance thresholds are surfaced.

- **Shared ownership**  
  Visibility is collective, even when execution is local.

- **Minimal cognitive load**  
  Information is concise, structured and decision-oriented.

- **Traceability by default**  
  Every card is linked to a persistent operational record.

---

## E-Card Lifecycle

E-cards follow a simple and repeatable operational lifecycle:

1. **Creation**  
   Automatically generated after event scoring and tiering.

2. **Surface**  
   Posted into a shared operational channel (e.g. Teams) as a priority-based card.

3. **Triage**  
   Reviewed during daily or periodic operational routines.

4. **Assignment / Routing**  
   Assigned locally or routed downstream when execution is required.

5. **Resolution or Revisit**  
   Closed, escalated or revisited based on outcome and recurrence.

This lifecycle ensures consistency without enforcing rigid workflows.

---

## E-Card Structure

Each e-card contains a standardized set of fields to support rapid understanding and decision-making:

- **Event type**  
- **Priority tier** (High / Medium / Low)  
- **Affected entity** (store, SKU, channel, region)  
- **Timestamp**  
- **Current status**  
- **Link to shared operational backlog**

![Illustrative e-card surfaced in Teams](assets/visuals/ecard-example.png)

*Illustrative example of a priority-based e-card surfaced in a shared operational channel.*

The structure is intentionally minimal, balancing context with speed.

---

## Teams as Shared Operational Backlog

E-cards are surfaced through a shared Teams channel acting as the **operational attention layer**.

Teams is not treated as a ticketing system, but as:
- a shared visibility surface
- a triage environment
- a coordination space across functions

Priority tiers determine which cards are surfaced and how frequently, preventing alert fatigue and uncontrolled escalation.

![Shared operational backlog of e-cards](assets/visuals/ecards-backlog-example.png)

*Illustrative view of a shared backlog enabling collective triage, prioritization and status tracking.*

---

## Relationship to Execution Systems (ServiceNow)

Not all e-cards require downstream execution.

Only events meeting predefined conditions (e.g. High priority, recurring patterns) are routed to execution systems such as ServiceNow.

In this model:
- e-cards manage **attention and prioritization**
- ServiceNow manages **execution and resolution**

This separation preserves operational flexibility while maintaining system-of-record integrity.

---

## Relationship to the Operating Model

E-cards enable the operating model to function in practice by:
- materializing the shared operational backlog
- enforcing objective prioritization through tiering
- reducing manual handoffs and ad-hoc escalations
- maintaining decision traceability across teams

Without e-cards, orchestration collapses back into fragmented communication.

---

## Notes

- Tooling examples are illustrative and non-prescriptive  
- The model scales from lightweight Teams-based coordination to enterprise execution environments  
- Detailed ingestion and scoring logic are documented separately  

🔗 Related artefacts:  
- Low-Code Event Ingestion  
- Event Scoring & Tiering Logic
