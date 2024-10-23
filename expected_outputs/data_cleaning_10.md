# Real Estate Dataset Cleaning Procedure

The cleaning procedure involves data standardization, normalization, error correction, missing value imputation, and duplicate detection. Let's clean the dataset column by column:

1. 'brokered_by' column:
   - Replace full names with NaN values, as the majority of values are numerical IDs.
   - Alternatively, create a separate column for full names (though it would be mostly empty).
   - Unable to fill missing values with appropriate data, so we could replace the missing values with 'Unknown'.

2. 'status' column:
   - Replace 's' and 'f' values with 'sold' and 'for_sale' respectively.
   - Missing values could potentially be filled using discovered dependencies, but the support is not strong enough to justify this method. An easy solution would be to replace missing values with 'Unknown'.

3. 'price' column:
   - Replace strings containing price and currency ('$') with the price as an integer (dropping the '$').
   - For missing values, consider using external APIs to estimate the price, or use the mean if necessary. An easy solution would be to replace missing values with NaN.

4. 'bed' column:
   - Replace '9999' values (likely placeholders or outliers) with NaN.
   - Impute missing values using the number of bathrooms and house size. Alternatively, fill missing values using the mean or replacing them with NaN.

5. 'bath' column:
   - Replace '0' values (likely errors) with NaN.
   - Impute missing values using the number of bedrooms and house size. Alternatively, fill missing values using the mean or replacing them with NaN.

6. 'acre_lot' column:
   - Replace negative values (data errors) with the mean value or NaN.
   - Fill missing values using the mean or replacing them with NaN.

7. 'street' column:
   - Standardize addresses by replacing expanded forms (e.g., Street, Boulevard) with abbreviations (e.g., St., Blvd.).
   - Unable to fill missing values with appropriate data, so we could replace the missing values with 'Unknown'.

8. 'city' column:
   - Replace non-USA cities with 'Unknown' or infer the correct city from the zip code when possible.
   - Use the same approach to impute missing values or replace missing values with 'Unknown'.

9. 'state' column:
   - Expand abbreviated state names to their full forms.
   - Impute missing values from the city (if present) or replace them with 'Unknown'.

10. 'zip_code' column:
    - Replace two-digit zip codes with the correct one inferred from the city and state, or with NaN if inference is not possible.
    - Use the same approach to impute missing values or replace them with NaN.

11. 'house_size' column:
    - Convert unit of measure from square miles to square feet for consistency.
    - Impute missing values from the number of bedrooms, bathrooms, and price or replace them with NaN.

12. 'prev_sold_date' column:
    - Standardize all dates to the 'YY-mm-dd' format.
    - If necessary, fill missing values using the mode or bfill/ffill methods. Alternatively, fill missing values replacing them with 'Unknown'.

Lastly, the dataset contains no exact duplicates, but contains ten non-exact duplicates, which differ either in price or in the presence of an extra missing value. The indexes of the duplicated rows are: 12 - 102, 1 - 18, 24 - 76, 41 - 67, 29 - 44, 7 - 85, 39 - 57, 15 - 109, 11 - 88, 74 - 77.