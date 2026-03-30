""" This script is for conducting A/B testing analysis. """
from scipy import stats
import numpy as np  

np.random.seed(42)  # Set a random seed for reproducibility

control_revenue = np.random.normal(loc=100, scale=10, size=100)  # Simulate revenue data for control group
feature_treatment_revenue = np.random.normal(loc=110, scale=10, size=100)  # Simulate revenue data for treatment group

t_stat, p_value = stats.ttest_ind(control_revenue, feature_treatment_revenue)  # Perform t-test
print(f"t-statistic: {t_stat: .2f}")
print(f"p-value: {p_value: .3f}")   

if p_value < 0.05:
    print("Reject the null hypothesis: There is a significant difference between the control and feature treatment groups")
    print("This suggests that the new feature has a significant impact on revenue.")
else:    
    print("Fail to reject the null hypothesis: There is no significant difference between the control and feature treatment groups.")
    print("This suggests that the new feature does not have a significant impact on revenue.")