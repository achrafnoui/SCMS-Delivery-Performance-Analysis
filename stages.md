# Supply Chain Analytics Project Architecture

## Overview

This project is structured as an eight-stage analytical workflow designed to move from supply chain domain understanding to advanced statistical, predictive, and geospatial analysis.

The sequence is deliberate: each stage establishes the foundation required for the next, ensuring that analytical conclusions are grounded in both operational context and validated data.

---

## Stage 1 — Supply Chain Domain Understanding

Before analyzing the data, we establish a working understanding of the supply chain process and its terminology.

### Core concepts

- **PQ** — Price Quote
- **PO / SO** — Purchase Order / Sales Order
- **ASN / DN** — Advanced Shipping Notice / Delivery Note
- **Direct Drop** — Fulfillment directly from the vendor
- **RDC** — Regional Delivery Center
- **Incoterms** — International Commercial Terms governing aspects of commercial delivery arrangements
- **Shipment Mode** — Transportation method used to move commodities
- **Delivery Lifecycle** — The sequence of events from procurement through delivery

The objective is not to become a subject-matter expert in every operational area. It is to develop sufficient domain knowledge to correctly interpret the data, understand the underlying process, and ask meaningful analytical questions.

---

## Stage 2 — Data Audit

The second stage establishes whether the dataset is reliable enough for analytical use.

### Areas of investigation

- Dataset shape
- Data types
- Missingness
- Duplicate records
- Unique identifiers
- Categorical distributions
- Date validity
- Numeric anomalies

### Critical focus: Data grain

A central objective is to determine **what each row represents**.

Establishing the dataset grain is essential before calculating metrics, aggregating records, or building analytical models. Incorrect assumptions about grain can produce misleading results even when the underlying calculations are technically correct.

### Tools

- Python
- pandas
- NumPy
- Data-cleaning techniques

---

## Stage 3 — Data Engineering

Once the dataset structure has been validated, the next step is to create analytical variables that make the underlying supply chain processes measurable.

### Candidate engineered variables

- `delivery_delay_days`
- `is_late`
- `order_to_vendor_days`
- `vendor_to_delivery_days`
- `freight_cost_per_kg`
- `freight_cost_pct_of_value`
- `shipment_value`
- `delivery_recording_lag` — where supported by the available data

These engineered features transform raw operational fields into variables that can directly support performance analysis, statistical investigation, and modeling.

---

## Stage 4 — Exploratory Data Analysis

Exploratory analysis is used to identify patterns, differences, and potential operational drivers before formal statistical testing.

### Delivery performance

Key questions include:

- Which countries have the weakest delivery performance?
- Which vendors experience higher levels of late delivery?
- Which shipment modes are associated with longer delivery times?
- Which products or product groups are most affected?

### Freight and cost

The analysis will investigate:

- What factors are associated with freight cost?
- Is shipment weight associated with freight cost?
- Does shipment mode influence freight cost?
- Does destination country influence freight cost?

### Operational structure

Additional comparisons will examine:

- Direct Drop vs. RDC fulfillment
- PMO vs. field-office management
- Vendor-level differences
- Manufacturing-site differences

### Analytical toolkit

The analysis may use:

- pandas
- NumPy
- matplotlib
- seaborn
- Data reshaping
- Grouping and aggregation
- Joining and relational operations

---

## Stage 5 — Statistical Investigation

This stage moves the project beyond descriptive comparisons and into formal hypothesis testing.

Rather than concluding that one group *appears* slower or performs worse, the analysis will test whether observed differences are supported by statistical evidence.

### Example research question

**Does shipment mode significantly affect delivery delay?**

**Null hypothesis (H₀):**  
Mean delivery delay is the same across shipment modes.

**Alternative hypothesis (H₁):**  
At least one shipment mode has a different mean delivery delay.

### Candidate statistical tests

Depending on the structure and assumptions of the data, appropriate methods may include:

- t-test
- ANOVA
- Mann–Whitney U test
- Kruskal–Wallis test

The statistical method will be selected **after inspecting the data and its assumptions**, rather than applying a test simply because it is commonly used in a tutorial.

This distinction is fundamental to rigorous analytical practice.

---

## Stage 6 — Vendor Performance Analysis

Vendor performance analysis provides an opportunity to identify whether delivery delays are concentrated among particular suppliers.

### Core question

**Are delivery delays concentrated among certain vendors?**

A simple late-rate comparison may reveal substantial differences between vendors. However, percentage alone is not sufficient evidence for a strong performance conclusion.

For example:

| Vendor | Shipments | Late Shipments | Late Rate |
|---|---:|---:|---:|
| Vendor A | 100 | 12 | 12% |
| Vendor B | 100 | 31 | 31% |
| Vendor C | 100 | 47 | 47% |

Sample size must always be considered.

A vendor with **4 shipments and 2 late deliveries** also produces a 50% late rate, but that percentage should not automatically be treated as equivalent evidence to a vendor with **400 shipments and 200 late deliveries**.

The analysis will therefore distinguish between:

- Observed performance percentages
- Sample size
- Statistical credibility of observed differences

---

## Stage 7 — Regression Analysis

The project will then move toward multivariable analysis using `statsmodels`.

### Objective

The central question becomes:

**Which observable factors are associated with delivery delay?**

Potential explanatory variables include:

- Shipment Mode
- Fulfill Via
- Country
- Product Group
- Vendor
- Weight
- Line Item Value
- Manufacturing Site

The appropriate regression approach will depend on the target variable and the structure of the data.

### Conceptual model

```text
Delivery Delay
    =
      Shipment Mode
    + Fulfillment Method
    + Product Group
    + Country
    + Vendor
    + Shipment Characteristics
    + Error
```

This approach strengthens the analysis because it moves beyond simple group comparisons.

Instead of asking:

> Does Vendor X have more delivery delays?

the analysis can ask:

> Does vendor performance remain associated with delivery delays after accounting for other observable factors?

This provides a substantially stronger analytical perspective.

---

## Stage 8 — Geospatial Supply Chain Analysis

The final stage applies geospatial analysis to identify geographic patterns in supply chain performance.

The analysis can connect:

```text
Country
   ↓
Average Delay
   ↓
Late Rate
   ↓
Shipment Volume
   ↓
Freight Cost
```

A geographic view can then be used to identify regions associated with:

- Longer delivery lead times
- Higher late-delivery rates
- Greater shipment volumes
- Higher freight-cost exposure

This stage provides an operational perspective on how geographic differences may relate to delivery performance and transportation cost.

---

## Project Progression

The overall analytical progression is:

**Domain Understanding → Data Audit → Data Engineering → Exploratory Analysis → Statistical Investigation → Vendor Analysis → Regression → Geospatial Analysis**

Each stage builds on the previous one, progressively increasing the analytical depth of the project.
