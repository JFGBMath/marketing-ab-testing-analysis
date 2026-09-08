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

## Methodology

1. **Exploratory analysis** — treatment/control group sizes, conversion rates, distribution of segmentation variables, outlier checks.
2. **Experiment design** — null/alternative hypotheses, choice of test statistic, minimum detectable effect (MDE) and required sample size given the observed baseline conversion rate.
3. **Hypothesis testing** — two-proportion z-test (or chi-square test) for the primary conversion metric, with a sample ratio mismatch (SRM) check before trusting the result.
4. **Heterogeneity check** — does the effect hold consistently across day/hour segments, or is it concentrated in a subgroup?
5. **Business interpretation** — translating the statistical result into a go/no-go recommendation with an estimated impact.

## Key Results

*(To be filled in once the analysis is complete — headline number, confidence level, and recommendation go here.)*

## Repository Structure

```
├── data/
│   ├── raw/            # original dataset (not tracked in git — see download instructions)
│   └── processed/      # cleaned data used for analysis
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb
│   ├── 02_experiment_design.ipynb
│   └── 03_hypothesis_testing.ipynb
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
jupyter notebook notebooks/01_exploratory_analysis.ipynb
```

## Tools

Python, pandas, numpy, scipy, statsmodels, matplotlib/seaborn, Jupyter

## Author

Jesús Fernando Gómez Brito ([GitHub](https://github.com/JFGBMath)) — Mathematician transitioning into Data Science, background in applied statistics and deep learning (see [Master's thesis work](#) on SAR image processing).
