# . Create a scatter plot with two numerical columns from a DataFrame, customizing markers, colors, and labels.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Column1': [1,2,3,4,5],
    'Column2': [5,4,3,2,1]
})


plt.scatter(df['Column1'], df['Column2'], marker='o', color='red')

plt.xlabel('Column1')
plt.ylabel('Column2')
plt.title('Scatter Plot of Column1 vs Column2')

plt.show()
