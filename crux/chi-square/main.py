# ###
# import pandas as pd
# from scipy.stats import chi2_contingency

# import pandas as pd
# from scipy.stats import chi2_contingency

# # Create a contingency table (observed frequencies)
# observed = pd.DataFrame({
#     'Action': [50, 30],  # 50 Males prefer Action, 30 Females prefer Action
#     'Comedy': [20, 40]   # 20 Males prefer Comedy, 40 Females prefer Comedy
# }, index=['Male', 'Female'])

# print("Observed Contingency Table:\n", observed)

# chi2, p, dof, expected = chi2_contingency(observed)

# print("\nChi-Square Test of Independence:")
# print(f"Chi-square statistic: {chi2}")
# print(f"P-value: {p}")
# print(f"Degrees of freedom: {dof}")
# print("Expected Contingency Table:\n", expected)

# # Interpretation:
# alpha = 0.05  # Significance level
# if p < alpha:
#     print("There is a significant association between gender and movie preference.")
# else:
#     print("There is no significant association between gender and movie preference.")