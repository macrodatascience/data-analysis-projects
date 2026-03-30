""" This script is for conducting correlation analysis. """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # Set a random seed for reproducibility
data = pd.DataFrame({'ad_spend': np.random.normal(loc=1000, scale=200, size=100),  # Simulate advertising spend data
                     'revenue': np.random.normal(loc=5000, scale=1000, size=100)  # Simulate revenue data
                     })
correlation = data['ad_spend'].corr(data['revenue'])  # Calculate the correlation coefficient
print(f"Correlation coefficient between advertising spend and revenue: {correlation:.2f}")  
plt.scatter(data['ad_spend'], data['revenue'], color='blue', alpha=0.5)  # Create a scatter plot of ad spend vs revenue
plt.xlabel('Advertising Spend') 
plt.ylabel('Revenue')
plt.title('Correlation between Advertising Spend and Revenue')
plt.show()

data2 = pd.DataFrame({'time_spent_minutes': np.random.normal(loc=60, scale=5, size=100),  # Simulate time spent on website data from a random normal distribution
                      'purchases': np.random.normal(loc=3, scale=0.5, size=100)})  # Simulate purchase data from another random normal distribution
correlation2 = data2['time_spent_minutes'].corr(data2['purchases'])  # Calculate the correlation coefficient
print(f"Correlation coefficient between time spent and purchases: {correlation2:.2f}")  
plt.scatter(data2['time_spent_minutes'], data2['purchases'], color='green', alpha=0.7)  # Create a scatter plot of time spent vs purchases
plt.xlabel('Time Spent (minutes)') 
plt.ylabel('Purchases')
plt.title('Correlation between Time Spent and Purchases')
plt.show()

# Note: The correlation coefficients in this example are based on simulated data and may not reflect real-world relationships. 
# Since they are independent random variables from random normal distributions, the correlation coefficients are likely to be close to zero, indicating little to no linear relationship between the variables.
# In practice, you would use actual data to conduct correlation analysis.

# Lets make the data more correlated by adding a linear relationship between ad spend and revenue
data['revenue'] = data['ad_spend'] * 5 + np.random.normal(loc=0, scale=500, size=100)  # Create a linear relationship with some noise
correlation = data['ad_spend'].corr(data['revenue'])  # Recalculate the correlation coefficient
print(f"Correlation coefficient between advertising spend and revenue (with linear relationship): {correlation:.2f}")
plt.scatter(data['ad_spend'], data['revenue'], color='red', alpha=0.5)  # Create a scatter plot of ad spend vs revenue with the linear relationship
plt.xlabel('Advertising Spend')
plt.ylabel('Revenue')
plt.title('Correlation between Advertising Spend and Revenue (with Linear Relationship)')   
plt.show()

# Note: The correlation coefficient should be higher in this case due to the linear relationship we introduced between ad spend and revenue.

# Lets make the data more correlated by adding a linear relationship between time spent and purchases
data2['purchases'] = data2['time_spent_minutes'] * 0.05 + np.random.normal(loc=0, scale=0.5, size=100)  # Create a linear relationship with some noise
correlation2 = data2['time_spent_minutes'].corr(data2['purchases'])
print(f"Correlation coefficient between time spent and purchases (with linear relationship): {correlation2:.2f}")
plt.scatter(data2['time_spent_minutes'], data2['purchases'], color='orange', alpha=0.7)  # Create a scatter plot of time spent vs purchases with the linear relationship
plt.xlabel('Time Spent (minutes)')
plt.ylabel('Purchases')
plt.title('Correlation between Time Spent and Purchases (with Linear Relationship)')
plt.show()