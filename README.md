# Marketing A/B Test: Does Showing an Ad Increase Conversion?

## Business Context

A mid-sized e-commerce company runs a marketing campaign and wants to know whether showing users an **ad** actually drives more conversions compared to showing a neutral **Public Service Announcement (PSA)** — the standard practice before rolling out the campaign at full scale.

The marketing team needs a data-backed answer before committing the full ad budget: is the lift in conversion large enough, and statistically reliable enough, to justify the spend?

## Business Question

> Does exposure to the ad campaign produce a statistically and practically significant increase in conversion rate compared to the PSA (control) group?

## Dataset

- **Source:** [Marketing A/B Testing](https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing) (Kaggle)
- **Size:** ~588,000 user records
- **Key columns:** treatment group (`ad` / `psa`), conversion (binary), day, hour, total ads seen
- **Note:** the raw CSV is not included in this repo (see `data/raw/README.md` for download instructions). Class and treatment-group sizes are imbalanced by design — handling that correctly is part of the analysis.

1. **Exploratory analysis** — data overview, treatment/control group sizes (~96% ad / ~4% psa by design, not a sample ratio mismatch), and conversion rate by group.
2. **Experiment design** — null/alternative hypotheses, choice of test (one-sided two-proportion z-test), and significance level.
3. **Hypothesis testing** — two-proportion z-test for the primary conversion metric.
4. **Effect size, confidence interval & sample size check** — 95% CI for the difference in conversion rate, and a retrospective power analysis to check how much sample size was actually required.
5. **Validation** — chi-square test on the same contingency table, confirming the z-test result.
6. **Business interpretation** — translating the statistical result into a go/no-go recommendation with estimated impact.

*Note: a segment-level heterogeneity check (by day/hour) is a natural next step, not yet included in this version.*

## Key Results

- Users exposed to the ad converted at **2.55%** vs. **1.79%** for the control (PSA) group — an absolute lift of **0.60–0.94 percentage points** (95% CI).
- The result is statistically significant (**p < 0.0001**), confirmed by both a one-sided two-proportion z-test and a chi-square test.
- A retrospective power analysis shows only **~4,401 users per group (~8,800 total)** were needed to detect this effect with 80% power — the experiment ran with **~588,000 users, roughly 67x more than required**. This suggests the test could have concluded faster or with a smaller traffic allocation, freeing capacity to test additional variants.
- **Recommendation:** roll out the ad campaign — the lift is both statistically robust and practically meaningful.

## Repository Structure

```
├── data/
│   ├── raw/            # original dataset (not tracked in git — see download instructions)
│   └── processed/      # cleaned data used for analysis
├── notebooks/
│   └── ab_test_analysis.ipynb   # full analysis, organized in clearly labeled markdown sections
├── src/
│   ├── data_cleaning.py
│   ├── stats_functions.py
│   └── visualization.py
├── sql/                 # queries used for any data extraction/transformation
├── requirements.txt
└── README.md
```

## How to Reproduce

```bash
git clone https://github.com/JFGBMath/<repo-name>.git
cd <repo-name>
pip install -r requirements.txt
# Download the dataset from Kaggle into data/raw/ (see instructions there)
jupyter notebook notebooks/ab_test_analysis.ipynb
```

## Tools

Python, pandas, numpy, scipy, statsmodels, matplotlib/seaborn, Jupyter

## Author

Jesús Fernando Gómez Brito ([GitHub](https://github.com/JFGBMath)) — Mathematician transitioning into Data Science, background in applied statistics and deep learning (see [Master's thesis work](#) on SAR image processing).
