# Low-Code Event Ingestion  
**Operational Event Orchestration – Commercial Babel Tower**

---

## Purpose

The low-code ingestion layer enables **automated, scalable capture of operational events** across heterogeneous source systems without requiring deep system refactoring or centralized ownership.

Its role is not to replace existing tools, but to **orchestrate operational signals** into a consistent, event-driven flow that feeds scoring, tiering and shared decision-making.

This artefact supports:
- Multi-source event ingestion  
- Event normalization and enrichment  
- Decoupling event capture from prioritization logic  

---

## Design Principles

The ingestion approach is guided by the following principles:

- **Low-friction integration**  
  Source systems remain unchanged. Events are captured where they occur.

- **Automation by default**  
  No manual handoffs are required to surface operational events.

- **Schema consistency**  
  All ingested events conform to a shared operational event structure.

- **Incremental extensibility**  
  New sources can be added without redesigning the operating model.

---

## Typical Source Systems (Illustrative)

Operational events may originate from multiple environments, including:

- Retail systems (store actions, stock adjustments)  
- E-commerce platforms (sales velocity, availability signals)  
- Supply and planning tools (demand deviations, lead-time risks)  
- Ticketing systems (e.g. ServiceNow, when already in use)  

Each source produces events with its own semantics, frequency and data structure.

---

## Ingestion Pattern

Low-code automation (e.g. Power Automate) is used to ingest events through a combination of:

- Event-based triggers  
- Scheduled polling  
- API-based connectors  

The ingestion layer acts as a **translation boundary**, separating source-specific logic from downstream prioritization and decision flows.

---

## Event Normalization

Upon ingestion, events are normalized into a **common operational event model**, ensuring consistency across sources.

Typical normalized attributes include:
- Event type  
- Source system  
- Timestamp  
- Affected entity (store, SKU, channel, region)  
- Contextual metadata  

Normalization ensures that downstream scoring and tiering logic operates on a **shared language**, regardless of origin.

---

## Metadata Enrichment

Where available, additional metadata may be appended during ingestion, such as:
- Commercial relevance indicators  
- Channel classification  
- Historical reference keys  

Enrichment is intentionally lightweight and non-blocking, preserving ingestion speed and reliability.

---

## Relationship to Event Scoring

The low-code ingestion layer does not assign priority.  
Its sole responsibility is to ensure that events are:
- Captured reliably  
- Structured consistently  
- Delivered downstream with sufficient context  

Priority and relevance are determined exclusively by the **Event Scoring & Tiering Logic**, maintaining separation of concerns.

---

## Operational Benefits

This ingestion approach enables:
- Rapid onboarding of new operational event sources  
- Reduced dependency on IT-heavy integrations  
- Faster time-to-value for operational coordination  
- Scalable evolution from fragmented to mature environments  

---

## Relationship to the Operating Model

Low-code ingestion directly supports:
- Event Scoring & Tiering  
- Shared Operational Backlog formation  
- E-card creation and triage  
- Execution routing to downstream systems  

Without automated ingestion, orchestration collapses into manual coordination.

---

## Reference

This artefact supports **Section B.2 – Low-Code Ingestion** of the main business case README.

