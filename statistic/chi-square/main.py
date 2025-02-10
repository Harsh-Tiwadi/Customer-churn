# ###
import pandas as pd
from scipy.stats import chi2_contingency

def chi_square_test(group_of_two:pd.DataFrame, alpha=0.05):
    if not isinstance(group_of_two, pd.DataFrame):
        raise ValueError("not a dataframe")
    if len(group_of_two.index) != 2:
        raise ValueError("not a group of two")

    try:
        chi2, p_value, dof, expected = chi2_contingency(group_of_two)
        if p_value<alpha:
            return {'Chi-square statistic: ':chi2, 'P-value: ':p_value, 'Degrees of freedom: ':dof,
                    'Expected Contingency Table:\n':expected, '\ncrux': 'There is statistically significant difference between two group'}
        else:
            return {'Chi-square statistic: ':chi2, 'P-value: ':p_value, 'Degrees of freedom: ':dof,
                    'Expected Contingency Table:\n':expected, '\ncrux': 'There"s not enough statistically significant difference between two group'}
    except Exception as e:
        raise ValueError(e)

# Create a contingency table (observed frequencies)
group_of_two = pd.DataFrame({
    'Action': [50, 30],  # 50 Males prefer Action, 30 Females prefer Action
    'Comedy': [40, 40]   # 20 Males prefer Comedy, 40 Females prefer Comedy
}, index=['Male', 'Female'])


r = chi_square_test(group_of_two)
print(r)