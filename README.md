# SCMS Delivery Performance Analysis

A reproducible supply-chain analytics project investigating delivery performance across shipment modes, fulfillment strategies, vendors, destination countries, product groups, and manufacturing sites.

The project combines data preparation, shipment-level analysis, non-parametric statistical testing, clustered regression, visual reporting, and a publication-ready PDF export. It is designed to be understandable to another analyst, reproducible from the supplied source data, and suitable for a professional analytics portfolio.

---

## Project at a glance

| Item | Result |
|---|---:|
| Original source records | 10,324 line items |
| Analytical records after cleaning | 9,783 line items |
| Unique shipment identifiers | 6,669 |
| Rows excluded by complete-case filtering | 541 |
| Shipment-level late rate | 12.0% |
| Shipment-level on-time rate | 61.5% |
| Shipment-level early rate | 26.5% |
| Hypotheses tested | 6 |

> **Important:** The shipment-level delivery rates above use one median-delay observation per shipment. They are not line-item rates.

## Research objectives

The analysis examines whether delivery-delay outcomes differ across the following supply-chain dimensions:

| Hypothesis | Research question | Method |
|---|---|---|
| **H1 — Shipment mode** | Do delivery-delay distributions differ by transportation mode? | Kruskal–Wallis; pairwise Mann–Whitney tests with Holm correction |
| **H2 — Fulfillment strategy** | Do Direct Drop and From RDC shipments have different delay distributions? | Mann–Whitney U |
| **H3 — Vendor performance** | Do delivery-delay distributions differ across vendors? | Kruskal–Wallis; pairwise comparisons with Holm correction |
| **H4 — Destination geography** | Do delivery-delay distributions differ across destination countries? | Kruskal–Wallis; pairwise comparisons with Holm correction |
| **H5 — Product group** | Do ARV and HRDT shipments have different delay distributions? | Mann–Whitney U |
| **H10 — Manufacturing origin** | Are delivery-delay outcomes associated with manufacturing site? | Gaussian GEE with shipment-clustered robust covariance |

H6–H9 are documented in the original hypothesis framework but are **not tested** in this analysis because the required source fields were excluded from the agreed analytical scope. They must not be interpreted as rejected hypotheses.

## Key findings

The cleaned analytical population contains **9,783 line-item records representing 6,669 unique shipments**. At shipment level, approximately 12.0% of shipments were late, 61.5% were on time, and 26.5% were early. The median shipment delay was zero days, while the mean was approximately −4.98 days.

The inferential tests found statistically significant differences or associations across all six tested dimensions:

| Hypothesis | Test result | Effect / interpretation |
|---|---|---|
| **H1 — Shipment mode** | H = 554.999, p = 5.73 × 10⁻¹²⁰ | ε² = 0.0828; all six pairwise mode comparisons were significant after Holm correction |
| **H2 — Fulfillment strategy** | U = 7,217,153.5, p = 6.70 × 10⁻¹³⁰ | Rank-biserial correlation = 0.3007 |
| **H3 — Vendor performance** | H = 269.527, p = 2.10 × 10⁻⁴⁷ | ε² = 0.0782; 31 of 153 Holm-adjusted vendor pairs were significant |
| **H4 — Destination geography** | H = 328.665, p = 1.80 × 10⁻⁵⁶ | ε² = 0.0470; 54 of 253 Holm-adjusted country pairs were significant |
| **H5 — Product group** | U = 3,019,437, p = 8.63 × 10⁻³⁴ | Rank-biserial correlation = −0.1837 for ARV relative to HRDT |
| **H10 — Manufacturing origin** | Wald χ² = 192.114, df = 26, p = 2.82 × 10⁻²⁷ | Manufacturing-site association detected using clustered GEE |

These findings indicate differences in delivery-delay distributions or statistical associations. They do **not** establish that any dimension causes late delivery. Statistical significance should be considered alongside effect sizes, operational context, and the limitations below.

---

## Repository contents

Keep the following files together in one project directory:

```text
SCMS-Delivery-Performance/
├── SCMS_Executive_Research_Notebook.ipynb
├── SCMS_Delivery_History_Dataset_20150929.csv
├── export_scms_report.py
├── SCMS_Report_Requirements.txt
├── README.md
├── SCMS_Executive_Research_Report.html   # generated
└── SCMS_Executive_Research_Report.pdf    # generated
```

The HTML and PDF reports are generated outputs; they do not need to exist before the first run.

The source CSV is expected to be available locally and is not embedded in the notebook. If you redistribute the project, confirm that you have the right to share the source dataset and include it in the project folder, or provide clear instructions for obtaining it.

## Requirements

- Python 3.9 or later recommended
- Jupyter Notebook or JupyterLab
- The Python packages listed in `SCMS_Report_Requirements.txt`
- The source CSV file named exactly `SCMS_Delivery_History_Dataset_20150929.csv`

## Setup and execution

### 1. Clone or download the project

Keep the notebook, source CSV, export script, and requirements file together in one directory.

### 2. Create a virtual environment (recommended)

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r SCMS_Report_Requirements.txt
```

### 4. Run the notebook

```bash
jupyter lab
```

Open `SCMS_Executive_Research_Notebook.ipynb`, then select **Restart Kernel and Run All Cells**.

Run the notebook from top to bottom. This loads the source data, performs the cleaning and validation steps, constructs the analytical populations, executes the statistical tests, and generates the report content and charts.

### 5. Export the report without Python code

After the notebook has run successfully and its outputs are saved, execute:

```bash
python export_scms_report.py
```

The script creates:

- `SCMS_Executive_Research_Report.html`
- `SCMS_Executive_Research_Report.pdf`

The export excludes notebook input cells and hides code blocks. The resulting report is intended to contain the written analysis, tables, statistical findings, and charts—not Python source code.

If PDF generation fails because WeasyPrint or one of its system dependencies is unavailable, open the generated HTML report in a browser and use **Print → Save as PDF**.

**Re-export after changing the data or notebook:** Run all notebook cells again, save the notebook with its updated outputs, and then rerun the export script. The PDF is generated from the notebook's saved outputs.

---

## Data preparation and analytical design

### Source and cleaning

The source file contains 10,324 line-item records. The agreed cleaning workflow:

1. Loads the CSV using the `latin-1` encoding.
2. Preserves the original data in `raw_data`.
3. Performs transformations on a separate `analysis_data` copy.
4. Standardizes field names and data types.
5. Excludes six fields from the analytical scope:
   - `po_sent_to_vendor_date`
   - `freight_cost_(usd)`
   - `weight_(kilograms)`
   - `pq_first_sent_to_client_date`
   - `dosage`
   - `item_description`
6. Applies complete-case filtering to the remaining analytical columns.
7. Creates delivery-delay and delivery-status fields.

The resulting analytical line-item dataset contains 9,783 rows and 29 columns before derived metrics. Complete-case filtering removed 541 rows.

### Delivery outcome definition

Delivery delay is calculated as:

```text
delivery_delay_days = delivered_to_client_date - scheduled_delivery_date
```

| Delay | Classification |
|---|---|
| Greater than 0 | Late |
| Equal to 0 | On Time |
| Less than 0 | Early |

A negative delay means delivery occurred before the scheduled date.

### Unit of analysis and repeated shipments

The source is structured at line-item level, not one row per shipment. Multiple item records can share the same `asn_dn` shipment identifier.

To avoid treating repeated lines from the same shipment as independent observations:

- H1–H5 use one median-delay observation per shipment.
- H10 retains line-level observations because manufacturing site can vary within a shipment. It uses a Generalized Estimating Equation (GEE) with robust covariance clustered by shipment identifier (`asn_dn`).

This distinction is essential when interpreting sample sizes and statistical results.

## Statistical approach

- **Kruskal–Wallis:** tests whether rank distributions differ across multiple independent groups.
- **Mann–Whitney U:** compares rank distributions between two independent groups.
- **Holm correction:** controls family-wise error across pairwise comparisons.
- **Effect sizes:** epsilon-squared and rank-biserial correlation are reported where applicable.
- **Gaussian GEE:** models the line-level delivery-delay outcome while accounting for within-shipment clustering through robust covariance estimation.

The notebook reports test statistics, p-values, effect sizes, pairwise results, and visual summaries. A small p-value is evidence against the relevant null hypothesis; it is not proof of causality or, by itself, proof of operational importance.

## Important methodological limitations

1. **Complete-case selection:** Removing rows with missing values may introduce selection bias if missingness is related to delivery performance or operational characteristics.
2. **Minimum group-size rule:** The threshold of 30 observations is a practical screening convention used for selected vendor, country, and manufacturing-site analyses. It is not a universal guarantee of statistical power.
3. **Skew and tied values:** Delivery delays include many zero values and a highly asymmetric distribution. Means should be interpreted alongside medians, rates, and distribution plots.
4. **Extreme values:** Extreme delays are not automatically removed. They should be investigated against source records and operational evidence before any exclusion.
5. **Confounding:** Vendor, country, mode, product, manufacturing site, and time may be related. The reported group differences are not automatically independent effects.
6. **H10 interpretation:** The manufacturing-site GEE is an association analysis and is not adjusted for every potential confounder, including shipment mode, destination, vendor, product, and time.
7. **RDC category:** `SCMS from RDC` is treated as a fulfillment-channel label rather than an ordinary external vendor and is excluded from the vendor comparison.
8. **Untested hypotheses:** H6–H9 are not tested because their required fields are outside the retained analytical scope.

## Reproducibility notes

- Keep the source CSV filename unchanged unless you also update the notebook's data-loading logic.
- Run all notebook cells in order; do not rely on stale outputs from an earlier execution.
- Save the notebook after execution before exporting.
- The executive summary contains figures for the supplied historical extract. If you replace the source dataset with a different extract, review and update any fixed summary text as well as the generated analysis.
- Package versions may affect rendering or statistical-library behavior. For strict long-term reproducibility, consider recording the exact environment used for the final release.

## Intended use

This project is an analytical case study and portfolio demonstration. It is intended to show a transparent workflow for cleaning historical supply-chain data, selecting an appropriate unit of analysis, testing operational hypotheses, interpreting statistical evidence, and communicating findings in an executive-ready format.

It should not be used as a live operational control system or as a causal evaluation without additional data, validation, and modeling.

## Author

Prepared as a supply-chain delivery performance analytics project.
