# Group a dataset by a categorical column and calculate the sum, mean, and count for each group

import pandas as pd


df = pd.DataFrame({
    'Category': ['A', 'A', 'A', 'A', 'B', 'B', 'A', 'B'],
    'Value': [10,20,30,40,50,60,70,80]
})


grouped = df.groupby('Category')


sum_df = grouped.sum()  
mean_df = grouped.mean()  
count_df = grouped.count()  

print("Sum:\n", sum_df)
print("\nMean:\n", mean_df)
print("\nCount:\n", count_df)
