# . Generate 1000 random samples from a standard normal distribution and plot their histogram using Matplotlib.

import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random samples from a standard normal distribution
samples = np.random.standard_normal(1000)

# Create a histogram of the samples
plt.hist(samples, bins=30, edgecolor='yellow')

# Set the title and labels
plt.title('Histogram of 1000 random samples from a standard normal distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show the plot
plt.show()
