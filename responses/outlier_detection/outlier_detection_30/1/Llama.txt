To perform outlier detection on the given dataset, we'll use the Interquartile Range (IQR) method and the Z-score method. We'll focus on the numerical columns: `price`, `bed`, `bath`, `acre_lot`, `house_size`.

```python
import pandas as pd
import numpy as np

# Load the dataset
data = {
    # ... your data here ...
}

df = pd.DataFrame(data)

# Select numerical columns
numerical_cols = ['price', 'bed', 'bath', 'acre_lot', 'house_size']

# IQR method
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    print(f"Outliers in {col} using IQR method: {len(outliers)}")

# Z-score method
from scipy import stats

for col in numerical_cols:
    z_scores = np.abs(stats.zscore(df[col]))
    outliers = df[z_scores > 3]
    print(f"Outliers in {col} using Z-score method: {len(outliers)}")
```

This code will print the number of outliers in each numerical column using both the IQR and Z-score methods.

To visualize the outliers, you can use a boxplot or a scatter plot with the outliers highlighted.

```python
import matplotlib.pyplot as plt

for col in numerical_cols:
    plt.figure(figsize=(10, 6))
    plt.boxplot(df[col], vert=False)
    plt.title(f"Boxplot of {col}")
    plt.show()
```

This will create a boxplot for each numerical column, with the outliers represented as individual points outside the whiskers.

Note that the choice of method and the threshold values (e.g., 1.5*IQR, 3*stddev) may vary depending on the specific characteristics of your dataset and the goals of your analysis.

Here is a more detailed analysis of the outliers in the `price` column:

```python
price_outliers_iqr = df[(df['price'] < (df['price'].quantile(0.25) - 1.5 * (df['price'].quantile(0.75) - df['price'].quantile(0.25)))) | 
                       (df['price'] > (df['price'].quantile(0.75) + 1.5 * (df['price'].quantile(0.75) - df['price'].quantile(0.25))))]

price_outliers_zscore = df[np.abs(stats.zscore(df['price'])) > 3]

print("Outliers in price using IQR method:")
print(price_outliers_iqr)

print("\nOutliers in price using Z-score method:")
print(price_outliers_zscore)
```

This code will print the rows of the dataframe that are identified as outliers in the `price` column using both the IQR and Z-score methods.