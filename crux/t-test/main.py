import pandas as pd
import numpy as np
from scipy import stats

def independent_t(group1, group2):
    formula = 't = (x̄₁ - x̄₂) / sqrt(s²ₚ * (1/n₁ + 1/n₂))'
    params = {
        'x1':'Mean of the first sample',
        'x2':'Mean of the second sample',
        's2p':'Pooled variance (an estimate of the common variance of the two populations) = [(n₁ - 1)s₁² + (n₂ - 1)s₂²] / (n₁ + n₂ - 2)',
        'n1':'Sample size of the first group',
        'n2':'Sample size of the second group'
    }
    alpha = 0.05

    try:
        t_statistic, p_value = stats.ttest_ind(group1, group2)
        if p_value<=alpha:
            return {"t_statistic: ":t_statistic, "p_value: ":p_value, "crux: ":"There is statistically significant difference."}
        else:
            return {"t_statistic: ":t_statistic, "p_value: ":p_value, "crux: ":"There's not enough statistically significant difference."}
    except Exception as e:
        raise('something went wrong', e)


def paired_t(group1_pre, group1_post):
    formula = 't = d / (standard deviation / sqrt(n))'
    params = {
        'd': 'Mean of the differences between the paired observations (dᵢ = x₁ᵢ - x₂ᵢ, where x₁ᵢ and x₂ᵢ are the paired measurements for the i-th subject).',
        'standard deviation': 'Standard deviation of the differences.',
        'n': 'Number of pairs (which is also the number of subjects).'
    }
    alpha = 0.05

    try:
        t_statistic, p_value = stats.ttest_rel(group1_pre, group1_post)
        if p_value<=alpha:
            return {"t_statistic: ":t_statistic, "p_value: ":p_value, "crux: ":"There is statistically significant difference."}
        else:
            return {"t_statistic: ":t_statistic, "p_value: ":p_value, "crux: ":"There's not enough statistically significant difference."}
    except Exception as e:
        raise('something went wrong', e)


def onesample_t(sample, pop_mean):
    formula = 't = (x̄ - μ) / (s / sqrt(n))'
    params = {
        'x': 'Mean of the sample.',
        'μ': 'Population mean (the value you"re comparing against).',
        's': 'Standard deviation of the sample.',
        'n': 'Sample size.'
    }
    alpha = 0.05

    try:
        t_statistic, p_value = stats.ttest_1samp(sample, pop_mean)
        if p_value<=alpha:
            return {"t_statistic: ":t_statistic, "p_value: ":p_value, "crux: ":"There is statistically significant difference."}
        else:
            return {"t_statistic: ":t_statistic, "p_value: ":p_value, "crux: ":"There's not enough statistically significant difference."}
    except Exception as e:
        raise('something went wrong', e)
