
import pandas as pd


df1 = pd.DataFrame({
    'Key': ['A', 'B', 'C', 'D'],
    'Value': [5,6,7,8]
})

df2 = pd.DataFrame({
    'Key': ['A', 'B', 'E', 'F'],
    'Value': [1,2,3,4]
})

df1.drop_duplicates(subset='Key', keep='first', inplace=True)
df2.drop_duplicates(subset='Key', keep='first', inplace=True)


merged_df = pd.merge(df1, df2, on='Key', how='outer')


merged_df.fillna(0, inplace=True)

print(merged_df)
