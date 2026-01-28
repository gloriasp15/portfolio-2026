# Applied Example — Cross-country Operational Incident Backlog

This applied example accompanies the business case and illustrates how the proposed **AI-Driven Planning & Forecast model** can be applied to a concrete operational scenario.

Due to confidentiality constraints, real operational data cannot be exposed. All datasets used in this example are **synthetic**, deliberately constructed to reflect typical patterns, frictions and constraints observed in real-world environments. The objective is illustrative rather than exhaustive.

---

## Context

The example is grounded in a cross-country operational setting where incidents are logged by Operations, IT and Business teams across Spain and Brazil. Historically, the backlog has been maintained in Excel (stored in a common SharePoint) and manually consolidated on a monthly basis into C-level dashboard reporting.

This process introduces delays, inconsistencies and interpretation risk, limiting the usefulness of the backlog as a reliable input for decision-making.

---

## Purpose of the Example

This example demonstrates how an existing, imperfect operational backlog can be reused as an input to a decision intelligence loop.

Specifically, it shows how:
- Operational inputs can be minimally normalised and structured  
- Simple logic can be applied to test backlog evolution and prioritisation choices  
- AI-enabled interpretation can support executive sense-making  
- Outputs can evolve continuously rather than being rebuilt manually each month  

The focus is on **decision relevance and reliability**, not on automation or technical optimisation.

---

## Scope

This applied example focuses on:
- A monthly snapshot of an operational incident backlog  
- Lightweight, explainable logic applied to ageing and prioritisation  
- Narrative outputs designed for executive consumption  

Out of scope:
- Real-time system integration  
- Advanced predictive modelling  
- Tool-specific implementations or vendor-dependent implementations 

---

## Structure

The example is organised as a simple pipeline aligned with the solution model:

### A. Input: [Synthetic Backlog Snapshot](backlog_synthetic.csv)


> All data used in this example has been synthetically generated using AI, based on patterns observed in a real operational case. No confidential or proprietary data has been exposed, in line with data protection and confidentiality policies.

**Common Frictions Observed**

- **Duplicate incidents** reported independently by different teams, reflecting lack of cross-team coordination and shared visibility
- Inconsistent **date formats and missing timestamps**, complicating ageing analysis and prioritisation
- Ambiguous **ownership**, with incidents assigned to individuals, teams or high-level roles interchangeably
- Heterogeneous descriptions, **mixing languages and levels of detail**, increasing interpretation effort
- Incomplete or undefined **root causes**, limiting the ability to distinguish tactical fixes from structural problems
- **Limited or absent data quality indicators**, despite data reliability being critical for decision-making

These frictions reduce the reliability of manual reporting and explain why executive decisions are often taken with partial or delayed insight.

---
  
### B. Logic: [Logic Pipeline](logic_pipeline.py)

Starting from a manually maintained backlog file with inconsistent formats, missing information and duplicated entries, the **script loads the data AS-IS** and applies a best-effort approach to date parsing. Rather than correcting invalid or missing dates, it **flags** them and **uses available information** to calculate simple ageing indicators.

Basic quality signals are derived by identifying missing timestamps, ambiguous ownership and inconsistent or overly brief descriptions. Potential duplicate incidents are highlighted through lightweight text normalisation and similarity grouping, without enforcing automatic de-duplication.

The output of this layer is not a cleaned dataset, but a small **set of structured signals that make operational frictions explicit** and comparable. These signals are designed to support prioritisation and discussion, not to produce definitive conclusions.

- Python-based logic applied to exported backlog snapshots
- Owned by Finance (FP&A) teams, with close involvement from Operations and selective support from Analytics and IT
- Designed to run in standard analytics environments, such as local Python setups, shared notebook-based workflows or enterprise analytics platforms (e.g. Databricks)

**Logic outputs** made by the script: 

🔗 [Signals Summary](script01-signals_summary.csv): Structured snapshot of the backlog state. It captures volume, ageing, priority pressure, cross-geo exposure and backlog tension at a given point in time.

🔗 [Suspected Duplicates](script02-suspected_duplicates.csv): List of incident clusters with high semantic similarity. It surfaces potential duplicated work caused by lack of coordination across teams and geographies.

---
### C. Interpretation: [Narrative Layer](narrative_layer.py)

#### C.1. Interpretation — How Narrative Is Generated

The interpretation layer consumes the structured outputs produced by the logic layer (`signals_summary.csv` and `suspected_duplicates.csv`) and uses **Large Language Models to convert them into executive-ready narrative**.

Unlike traditional reporting approaches, the LLM does not:
- Access raw operational data
- Perform calculations and does not automate prioritisation.

Its role is to **interpret pre-defined signals, identify patterns and tensions, and express their implications** in clear, decision-oriented language.

This separation between logic and narrative introduces traceability and control, while significantly reducing the manual effort previously required to transform fragmented operational data into executive insight.

---

#### C.2. From Manual Interpretation to LLM-based Narrative  

| Stage | How narrative was generated | Limitations |
|---|---|---|
| Manual reporting | Analysts reviewed Excel files and wrote PowerPoint slides by hand | Time-consuming, inconsistent, highly dependent on individual judgement |
| Rule-based summaries | Static KPIs and filters in Excel or BI tools | Effective for numbers, ineffective for unstructured text |
| Keyword search & heuristics | Basic text filters in ticketing systems | No semantic understanding, high risk of missing duplicates |
| LLM-based interpretation | LLMs interpret structured signals and generate narrative | Scales interpretation while preserving human decision ownership |

**Key shift:**  
Narrative creation moves from a manual, person-dependent activity to a reproducible interpretation layer grounded in explicit signals.

--- 

#### C.3. Why LLMs Change the Game Here

| Capability | Before | With LLMs |
|---|---|---|
| Unstructured text handling | Manual reading | Semantic interpretation |
| Multi-language understanding | Manual translation or ignored | Native cross-language reasoning |
| Duplicate detection | Memory or intuition | Semantic similarity |
| Narrative consistency | Analyst-dependent | Systematically reproducible |
| Executive readiness | High manual effort | Low marginal cost per iteration |

**LLMs reduce cognitive load, not decision accountability.**

---

#### C.4. LLM Technologies Used (Illustrative)

| Layer | Technology | Purpose |
|---|---|---|
| Narrative synthesis | GPT-4 / GPT-4.1 | Executive-grade reasoning and structured narrative |
| Fast iteration | GPT-4o or smaller GPT variants | Low-latency drafting and iteration |
| Semantic similarity | Embedding models (e.g. `text-embedding-3-large`) | Detection of duplicate or related incidents |
| Enterprise access | Internal GenAI platforms or governed APIs | Security, auditability and access control |

> The example remains vendor-agnostic. Technologies listed illustrate typical enterprise-grade choices rather than fixed implementation requirements.

**One-line anchor**

LLMs replace manual synthesis with semantic interpretation, transforming structured signals into consistent executive narrative without automating decisions or altering underlying data.

---

## D. Output: [Executive Intelligence Dashboard](executive_summary.md) 

The main value of this example lies in the applied logic and outputs, which demonstrate how the decision intelligence loop operates in practice.

The (`executive_summary.md`) is derived from an interpreted signal layer (`executive_decision-snapshot.csv`), generated through *LLM-based synthesis* rather than directly from operational data.

🔗 [Executive Interpretation](executive-decision-snapshot.csv):  Structured executive interpretation of backlog signals. It captures AI-synthesised insights on backlog pressure, execution risk, coordination frictions and ownership clarity, derived from structured logic outputs at a given point in time.



