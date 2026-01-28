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

- **A. Input**: [Synthetic Backlog Snapshot](.../assets/applied-example/backlog_synthetic.csv)

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
  
- B. **Logic**: normalisation and scenario logic



---
- **Interpretation**: narrative synthesis  
- **Output**: executive-ready intelligence summary  

The main value of this example lies in the applied logic and outputs, which demonstrate how the decision intelligence loop operates in practice.
