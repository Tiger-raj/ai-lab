# Calculate summary statistics (mean, standard deviation, quartiles) for each numerical column in a pandas DataFrame.

import pandas as pd
import numpy as np

# create a sample dataframe for demonstration
df = pd.DataFrame({
    'A': np.random.rand(10),
    'B': np.random.rand(10),
    'C': np.random.rand(10)
})

# calculate summary statistics for each numerical column
for column in df.select_dtypes(include=[np.number]).columns.tolist():
    mean = df[column].mean()  # calculate mean
    std_dev = df[column].std()  # calculate standard deviation
    quartiles = df[column].quantile([0.25, 0.5, 0.75])  # calculate quartiles

# print results
    print(f"Column: {column}")
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Quartiles: {quartiles}\n")
