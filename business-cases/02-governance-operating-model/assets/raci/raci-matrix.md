# RACI Matrix – Data Quality Governance

This RACI matrix operationalizes the Governance Operating Model by mapping
defined governance roles to key Data Quality lifecycle activities.

The objective is to translate ownership and roles into **clear execution
responsibilities, decision rights and visibility**, ensuring governance
operates as an execution framework rather than a policy layer.

The RACI framework is applied across:
- One-off Data Quality validations
- Business-as-usual (BAU) Data Quality activities

---

## RACI Definitions

- **R – Responsible**: Executes the activity
- **A – Accountable**: Owns the decision and outcome *(single-point accountability)*
- **C – Consulted**: Provides expert input prior to decision-making
- **I – Informed**: Receives visibility on progress and outcomes

> **Principle:** Each activity has a single accountable owner to avoid
decision ambiguity and execution delays.

---

## RACI Matrix – Data Quality Lifecycle

### One-off Validations

| Activity                      | CDO / Governance | Process Owner | System Owner | Data Owner | Data Steward | Data Engineer | Data Consumer |
|-------------------------------|------------------|---------------|--------------|------------|--------------|---------------|---------------|
| Data definition               | A                | R             | I            | R          | C            | I             | I             |
| Functional control definition | C                | A             | I            | R          | C            | C             | I             |
| Technical control definition  | C                | C             | I            | R          | C            | A             | I             |
| Control validation            | I                | C             | I            | C          | R            | A             | I             |
| Control implementation        | I                | I             | C            | I          | R            | A             | I             |

---

### BAU Activities

| Activity               | CDO / Governance | Process Owner | System Owner | Data Owner | Data Steward | Data Engineer | Data Consumer |
|------------------------|------------------|---------------|--------------|------------|--------------|---------------|---------------|
| Detection & monitoring | I                | C             | I            | C          | R            | C             | I             |
| Issue opening          | I                | C             | I            | C          | R            | I             | I             |
| Monitoring execution   | I                | C             | I            | C          | R            | C             | I             |
| Issue resolution       | I                | A             | C            | A          | R            | R             | I             |
| Governance alignment   | A                | C             | I            | C          | R            | I             | I             |

---

## Data Quality Lifecycle – Extended Description

This section provides detailed clarification of each lifecycle phase to
support consistent interpretation of the RACI matrix and enable
effective execution.

### One-off Validations

**Data definition**  
Definition of the business meaning, structure and criticality of key data
elements within a given domain.

**Functional control definition**  
Specification of business rules and expected conditions data must meet to be
considered fit for use.

**Technical control definition**  
Translation of functional rules into technical logic and validations that can
be automated within systems and data pipelines.

**Control validation**  
Testing and confirmation that defined controls effectively detect data
quality issues and are aligned with business expectations.

**Control implementation**  
Deployment of validated controls into productive systems, ensuring integration
into monitoring and operational processes.

---

### BAU Activities

**Detection & monitoring**  
Identification of potential data quality issues through automated rules,
checks, anomaly detection and proactive monitoring mechanisms.

**Issue opening**  
Logging of detected issues into the Data Quality backlog, assigning ownership,
priority and required metadata for resolution.

**Monitoring execution**  
Ongoing oversight of active issues to ensure ownership, SLA compliance,
proper escalation and trend identification.

**Issue resolution**  
Remediation of data quality issues at source or downstream layers, including
implementation of fixes and validation of outcomes.

**Governance alignment**  
Continuous alignment with governance standards, reporting expectations and
corporate policies, reinforcing Data Quality culture across the organization.

---

## Notes & Governance Principles

- Accountability may be **temporarily shared** during early rollout stages
  (e.g. between CDO and domain representatives) until governance is fully embedded.
- Responsibility assignments may vary depending on the **nature of the issue**
  (functional vs technical), while accountability remains stable.
- The RACI matrix is designed as a **living artefact**, evolving as governance
  maturity increases.

---

*This RACI matrix supports the Governance Operating Model and serves as the
foundation for defining execution KPIs and monitoring governance effectiveness.*

