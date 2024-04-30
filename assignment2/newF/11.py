
import pandas as pd

df = pd.read_csv('data.csv')

cols_with_missing = [col for col in df.columns if df[col].isnull().any()]


for col in cols_with_missing:
    if df[col].dtype == 'object': 
        mode = df[col].mode()[0] 
        df.loc[:, col] = df.loc[:, col].fillna(mode)  
    else: 
        mean = df[col].mean() 
        df.loc[:, col] = df.loc[:, col].fillna(mean)  


print(df)
