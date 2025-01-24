from scipy import stats
import pandas as pd
import numpy as np

def anova_test(alpha=0.05, *args):
    try:
        f_statistic, p_value = stats.f_oneway(*args)
        if p_value<alpha:
            return {'f_statistic: ':f_statistic, 'p_value: ':p_value, 'crux: ': 'There is statistically significant difference between the groups'}
        else:
            return {'f_statistic: ':f_statistic, 'p_value: ':p_value, 'crux: ': "There's not enough statistically significant difference"}
    except Exception as e:
        raise ValueError(e)

# # Example usage:
# np.random.seed(0)
# group1 = np.random.normal(10, 2, 50)
# group2 = np.random.normal(12, 2, 50)
# group3 = np.random.normal(11, 2, 50)

# r = anova_test(group1, group2, group3)
# print(r)