Data standardization is a process of transforming data to have a mean of zero and a standard deviation of one. This is often done to ensure that each feature contributes equally to the analysis. To standardize the dataset, we need to focus on the numerical columns. Here's a step-by-step guide on how to standardize the numerical columns in the dataset:

1. **Identify Numerical Columns**: 
   - `price`
   - `acre_lot`
   - `house_size`

2. **Calculate Mean and Standard Deviation** for each numerical column.

3. **Standardize Each Value**: 
   - For each value in a numerical column, subtract the mean of that column and then divide by the standard deviation of that column.

Let's perform these steps:

### Step 1: Calculate Mean and Standard Deviation

#### Price
- Mean: \( \mu_{\text{price}} \)
- Standard Deviation: \( \sigma_{\text{price}} \)

#### Acre Lot
- Mean: \( \mu_{\text{acre\_lot}} \)
- Standard Deviation: \( \sigma_{\text{acre\_lot}} \)

#### House Size
- Mean: \( \mu_{\text{house\_size}} \)
- Standard Deviation: \( \sigma_{\text{house\_size}} \)

### Step 2: Standardize Each Value

For each numerical column, apply the formula:
\[ \text{Standardized Value} = \frac{\text{Original Value} - \mu}{\sigma} \]

### Example Calculation

Let's assume the following hypothetical means and standard deviations for illustration purposes (you would calculate these from the actual data):

- \( \mu_{\text{price}} = 500000 \), \( \sigma_{\text{price}} = 200000 \)
- \( \mu_{\text{acre\_lot}} = 1.0 \), \( \sigma_{\text{acre\_lot}} = 5.0 \)
- \( \mu_{\text{house\_size}} = 0.0001 \), \( \sigma_{\text{house\_size}} = 0.00005 \)

For a house with:
- `price = 409900`
- `acre_lot = 2.12`
- `house_size = 3.640811524334252e-05`

The standardized values would be:
- Standardized `price`: \( \frac{409900 - 500000}{200000} = -0.451 \)
- Standardized `acre_lot`: \( \frac{2.12 - 1.0}{5.0} = 0.224 \)
- Standardized `house_size`: \( \frac{3.640811524334252e-05 - 0.0001}{0.00005} = -1.272 \)

### Note
To perform this on the entire dataset, you would need to calculate the actual mean and standard deviation for each numerical column using the dataset values, and then apply the standardization formula to each value in those columns.

If you have access to a programming environment like Python, you can use libraries like Pandas and Scikit-learn to automate this process efficiently.