# Merge two DataFrames based on a common column, handling potential duplicates and missing values appropriately.

import pandas as pd

# create two sample dataframes for demonstration
df1 = pd.DataFrame({
    'Key': ['A', 'B', 'C', 'D'],
    'Value': [8, 2, 6, 3]
})

df2 = pd.DataFrame({
    'Key': ['B', 'D', 'E', 'F'],
    'Value': [9, 6, 2, 1]
})

# handle duplicates
df1.drop_duplicates(subset='Key', keep='first', inplace=True)
df2.drop_duplicates(subset='Key', keep='first', inplace=True)

# merge dataframes on 'Key'
merged_df = pd.merge(df1, df2, on='Key', how='outer')

# handle missing values
merged_df.fillna(0, inplace=True)

# print merges dataframe
print(merged_df)
