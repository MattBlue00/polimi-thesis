To perform outlier detection on the given dataset, we'll use the Interquartile Range (IQR) method and the Z-score method. We'll focus on the numerical columns: `price`, `bed`, `bath`, `acre_lot`, `house_size`.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Visualize the data
for col in numerical_cols:
    plt.figure(figsize=(10, 6))
    plt.boxplot(df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()
```

This code will print the number of outliers in each column using both the IQR and Z-score methods. It will also display boxplots for each column to visualize the data.

**Interpretation:**

* The IQR method is more robust to non-normal data and is often used for outlier detection in skewed distributions.
* The Z-score method assumes a normal distribution and is more sensitive to outliers.
* The boxplots provide a visual representation of the data, showing the median, quartiles, and outliers.

**Example Output:**

```
Outliers in price using IQR method: 10
Outliers in bed using IQR method: 5
Outliers in bath using IQR method: 3
Outliers in acre_lot using IQR method: 12
Outliers in house_size using IQR method: 8
Outliers in price using Z-score method: 15
Outliers in bed using Z-score method: 2
Outliers in bath using Z-score method: 1
Outliers in acre_lot using Z-score method: 10
Outliers in house_size using Z-score method: 5
```

Note that the actual output will depend on the specific data and may vary.