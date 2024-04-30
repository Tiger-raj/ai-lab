# Group a dataset by a categorical column and calculate the sum, mean, and count for each group

import pandas as pd

# create a sample dataframe for demonstration
df = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'A', 'B', 'B', 'A', 'B'],
    'Value': [23, 56, 43, 78, 34, 23, 21, 32]
})

# group by 'Category' column
grouped = df.groupby('Category')

# calculate sum, mean, and count for each group
sum_df = grouped.sum()  # calculate sum
mean_df = grouped.mean()  # calculate mean
count_df = grouped.count()  # calculate count

print("Sum:\n", sum_df)
print("\nMean:\n", mean_df)
print("\nCount:\n", count_df)
