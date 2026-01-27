# Low-Code Event Ingestion  
**Operational Event Orchestration – The Commercial Babel Tower**

---

## Purpose

The low-code ingestion layer enables the automated capture of operational events across heterogeneous source systems without requiring deep system refactoring or centralized ownership.

Its role is to orchestrate operational signals into a consistent, event-driven flow that feeds scoring, tiering and shared decision-making, while keeping execution systems and local workflows unchanged.

This artefact supports **Section B.2 – Low-Code Ingestion** of the main business case.

---

## Design Principles

The ingestion approach follows a small set of operational principles:

- **Low-friction integration**  
  Events are captured at source without forcing upstream system consolidation.

- **Automation by default**  
  Operational signals are surfaced without manual intervention or escalation.

- **Shared operational language**  
  All ingested events are translated into a common operational event schema.

- **Separation of concerns**  
  Ingestion, prioritization and execution remain decoupled.

---

## Ingestion Pattern

Low-code automation (e.g. Power Automate) is used to ingest operational events through flexible triggers such as forms, APIs or system signals.

The ingestion flow intentionally consolidates multiple operational phases into a minimal number of automated steps, acting as a translation boundary between fragmented source systems and downstream prioritization logic.

---

### 1.Power Automate Workflow (Illustrative)

![Power Automate – Event Ingestion Workflow](../visuals/power-automate-event-ingestion-workflow.png)

The workflow illustrates how operational events are captured, normalized and persisted using low-code automation.

Power Automate acts as the orchestration layer, translating heterogeneous inputs into a standardized operational event and routing them downstream for scoring, tiering and shared visibility.

Typical normalized attributes include:
- Event type  
- Source system  
- Timestamp  
- Affected entity (store, SKU, channel, region)  
- Contextual metadata  

Normalization ensures that downstream scoring and tiering logic operates on a **shared language**, regardless of origin.

---

### 2.Implementation Snapshot (Illustrative)

The following JSON snapshot illustrates the **end-to-end execution pattern** implemented within the low-code ingestion workflow, from event normalization to scoring and backlog persistence.

The example is intentionally simplified and focuses on execution logic rather than full Power Automate flow definitions.

```json
{
  "normalizedEvent": {
    "eventId": "uuid",
    "eventType": "StockOut",
    "sourceSystem": "Retail",
    "entity": {
      "storeId": "ES045",
      "sku": "SKU-1234"
    },
    "timestamp": "2026-01-27T10:15:00Z",
    "status": "New"
  },
  "scoringResult": {
    "priorityTier": "High",
    "score": 87
  },
  "backlogRecord": {
    "eventId": "uuid",
    "priorityTier": "High",
    "status": "Open",
    "createdAt": "2026-01-27T10:15:05Z"
  }
}

```

This snapshot shows how:
- heterogeneous inputs are translated into a shared operational event
- scoring and tiering are applied downstream
- prioritized events are persisted into a common operational backlog

---

## Traceability to the Operating Model

| Workflow responsibility | Operating model capability |
|------------------------|----------------------------|
| Event normalization    | Shared operational language |
| Automated scoring call | Objective priority tiering |
| Backlog persistence   | Centralized operational visibility |

---

Additional contextual metadata may be appended during ingestion when available, without affecting the core event structure.

Scoring and tiering are invoked downstream from ingestion, ensuring that prioritization logic remains independent from event capture and source systems.

This artefact demonstrates how the ingestion phase of the operating model can be executed using low-code automation, enabling standardized event capture, objective prioritization and shared operational visibility.

🔗 Related artefact:  
Event Scoring & Tiering Logic

---

## Reference

This artefact supports **Section B.2 – Low-Code Ingestion** of the main business case README.

