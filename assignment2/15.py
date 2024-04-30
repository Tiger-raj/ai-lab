# . Create a scatter plot with two numerical columns from a DataFrame, customizing markers, colors, and labels.

import pandas as pd
import matplotlib.pyplot as plt

# create a sample dataframe for demonstration
df = pd.DataFrame({
    'Column1': [4,7,2,4,6],
    'Column2': [5,7,3,6,4]
})

# create a scatter plot
plt.scatter(df['Column1'], df['Column2'], marker='o', color='red')

# customize labels
plt.xlabel('Column1')
plt.ylabel('Column2')
plt.title('Scatter Plot of Column1 vs Column2')

# show the plot
plt.show()
