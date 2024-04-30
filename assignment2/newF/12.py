
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': np.random.rand(10),
    'B': np.random.rand(10),
    'C': np.random.rand(10)
})

for column in df.select_dtypes(include=[np.number]).columns.tolist():
    mean = df[column].mean()  
    std_dev = df[column].std()  
    quartiles = df[column].quantile([0.25, 0.5, 0.75]) 


    print(f"Column: {column}")
    print(f"Mean: {mean}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Quartiles: {quartiles}\n")
