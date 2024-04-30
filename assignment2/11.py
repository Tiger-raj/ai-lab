# . Load a CSV file containing missing values and perform appropriate imputation methods

import pandas as pd

# load the csv file
df = pd.read_csv('example.csv')

# identify columns with missing values
cols_with_missing = [col for col in df.columns if df[col].isnull().any()]

# perform imputation for each column
for col in cols_with_missing:
    if df[col].dtype == 'object':  # if column is categorical
        mode = df[col].mode()[0]  # calculate mode
        df.loc[:, col] = df.loc[:, col].fillna(mode)  # fill missing values with mode
    else:  # if column is numerical
        mean = df[col].mean()  # calculate mean
        df.loc[:, col] = df.loc[:, col].fillna(mean)  # fill missing values with mean

# print the dataframe
print(df)
