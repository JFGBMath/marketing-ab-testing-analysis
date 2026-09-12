import pandas as pd
from statsmodels.stats.proportion import (
    proportions_ztest,
    confint_proportions_2indep,
    proportion_effectsize,
)
from statsmodels.stats.power import NormalIndPower
from scipy.stats import chi2_contingency, chi2
import statsmodels.formula.api as smf


def two_proportion_ztest(df, group_col, outcome_col, group1, group2, alternative="larger"):
    converted = df.groupby(group_col)[outcome_col].sum()
    n_obs = df.groupby(group_col)[outcome_col].count()
    count = [converted[group1], converted[group2]]
    nobs = [n_obs[group1], n_obs[group2]]
    return proportions_ztest(count, nobs, alternative=alternative)


def confidence_interval_two_proportions(df, group_col, outcome_col, group1, group2, method="wald"):
    converted = df.groupby(group_col)[outcome_col].sum()
    n_obs = df.groupby(group_col)[outcome_col].count()
    return confint_proportions_2indep(
        count1=converted[group1], nobs1=n_obs[group1],
        count2=converted[group2], nobs2=n_obs[group2],
        method=method
    )


def required_sample_size(rate1, rate2, alpha=0.05, power=0.8, alternative="larger"):
    effect_size = proportion_effectsize(rate1, rate2)
    analysis = NormalIndPower()
    return analysis.solve_power(effect_size=effect_size, alpha=alpha, power=power, alternative=alternative)


def chi_square_validation(df, group_col, outcome_col):
    contingency_table = pd.crosstab(df[group_col], df[outcome_col])
    return chi2_contingency(contingency_table)


def interaction_test(df, outcome_col, treatment_col, segment_col):
    formula_with = f"{outcome_col} ~ {treatment_col} * C(Q('{segment_col}'))"
    formula_without = f"{outcome_col} ~ {treatment_col} + C(Q('{segment_col}'))"

    interaction_model = smf.logit(formula_with, data=df).fit()
    model_no_interaction = smf.logit(formula_without, data=df).fit()

    llr_stat = 2 * (interaction_model.llf - model_no_interaction.llf)
    df_diff = interaction_model.df_model - model_no_interaction.df_model
    p_value = chi2.sf(llr_stat, df_diff)

    return interaction_model, llr_stat, df_diff, p_value