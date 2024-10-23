# Real Estate Dataset Profiling

This report presents a comprehensive analysis of a real estate dataset, which contains 110 records across 12 variables. The analysis includes cardinality assessment, value distribution, data type classification, domain analysis, and dependency discovery.

## 1. Cardinality Analysis

### 1.1 Dataset Overview
The dataset consists of 110 records, with a total of 12 variables. There are 134 missing values in the dataset, which account for 10% of the total data points. Additionally, no exact duplicate records were found.

### 1.2 Missing Values Analysis
Several variables in the dataset have missing values. The breakdown is as follows:
- 'zip_code' has 15 missing values, accounting for 13.64% of its total entries.
- 'house_size' has 14 missing values, which is 12.73%.
- 'bed' has 13 missing values, also making up 11.82%.
- 'acre_lot', 'street', and 'bath' each have 13 missing values, representing 11.82%.
- 'state' has 12 missing values (10.91%).
- 'city' has 11 missing values (10%).
- 'price' and 'prev_sold_date' both have 10 missing values (9.09% each).
- 'status' has 6 missing values, representing 5.45%.
- 'brokered_by' has 5 missing values, accounting for 4.55%.

### 1.3 Distinct Values Analysis
The total number of distinct values across the dataset is 754. Here is the distinct value count for each variable:
- 'brokered_by' has 94 distinct values (85.50%).
- 'house_size' and street each have 91 distinct values (82.73%).
- 'zip_code' has 90 distinct values (81.82%).
- 'price' has 89 distinct values (80.91%).
- 'city' has 87 distinct values (79.10%).
- 'prev_sold_date' has 85 distinct values (77.27%).
- 'acre_lot' has 57 distinct values (51.82%).
- 'state' has 44 distinct values (40%).
- 'bed' and 'bath' both have 10 distinct values (9.10% each).
- 'status' has 6 distinct values (5.50%).

## 2. Value Distribution Analysis

The variable 'price' ranges from a minimum of $69,900 to a maximum of $2,450,000, with an average value of $510,263.70. The variable 'bed' has a minimum of 1 and a maximum of 9,999 bedrooms, with an average of 724.68 bedrooms. The number of bathrooms ('bath') ranges from 0 to 6, with an average of 2.18. The 'acre_lot' variable has values between -1.92 and 35, with an average of 1.27 acres. 'house_size' ranges from 0.001015 square feet to 5,828 square feet, with an average size of 2,021.13 square feet.

Note: Statistics for 'brokered_by' and 'zip_code' are omitted as these variables serve as identifiers.

## 3. Data Type Classification

Each variable in the dataset is categorized by its data type:
- 'brokered_by': This variable contains mixed data types, including both integers and strings.
- 'status': This variable is classified as a string.
- 'price': This variable contains mixed data types, including both integers and strings.
- 'bed': This variable is an integer.
- 'bath': This variable is an integer.
- 'acre_lot': This variable is a float.
- 'street': This variable is a string.
- 'city': This variable is a string.
- 'state': This variable is a string.
- 'zip_code': This variable is an integer.
- 'house_size': This variable is a float.
- 'prev_sold_date': This variable is classified as a date.

## 4. Domain Classification/Column Description

The dataset pertains to real estate transactions, and each variable represents a specific aspect of these transactions:
- 'brokered_by': Identifier for the real estate agent or broker.
- 'status': The current sale status of the property, indicating whether it is sold or for sale.
- 'price': The price of the property in US dollars.
- 'bed': The number of bedrooms in the property.
- 'bath': The number of bathrooms in the property.
- 'acre_lot': The size of the lot in acres.
- 'street': The street address of the property.
- 'city': The city in which the property is located.
- 'state': The state in which the property is located.
- 'zip_code': The ZIP code for the property's location.
- 'house_size': The size of the house in square feet.
- 'prev_sold_date': The date on which the property was previously sold.

## 5. Dependency Discovery

It is expected that there may be functional dependencies between location-related variables, such as 'street', 'city', 'state', and 'zip_code', although there is insufficient evidence in the dataset to confirm these relationships conclusively.

A notable trend observed in the dataset is that properties with 3 bedrooms and 2 bathrooms are more likely to be marked as "sold" compared to those that are still "for sale".