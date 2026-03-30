""" This script is for calculating descriptive statistics for a dataset. """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  # Set a random seed for reproducibility
data = pd.DataFrame({'day': range(1,31),
                     'user_sessions': np.random.poisson(lam=120, size=30)
                     })  # Simulate user sessions data for 30 days

print("Descriptive Statistics:")
print(data['user_sessions'].describe())  # Calculate and print descriptive statistics
plt.hist(data['user_sessions'], bins=10, color = 'skyblue', edgecolor='black')  # Create a histogram of user sessions
plt.xlabel('User Sessions')
plt.ylabel('Frequency')
plt.title('Distribution of Daily User Sessions')
plt.show()