from data.batches import DataProfilingBatch
from data.checklists.data_profiling.item_ids import DataProfilingItemId
from experiments.model.checklist import BaseChecklist
from experiments.model.checklist_item import DataProfilingChecklistItem
from experiments.model.prompt import EvaluationPrompt

class DataProfilingAccuracyChecklist(BaseChecklist):

    def __init__(self) -> None:
        items = [
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_GENERAL_DATASET_DESCRIPTION,
                batch=DataProfilingBatch.ACCURACY_GENERAL,
                content="general dataset description: real estate transactions dataset."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_GENERAL_COLUMNS,
                batch=DataProfilingBatch.ACCURACY_GENERAL,
                content="columns number: 12."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_GENERAL_ROWS,
                batch=DataProfilingBatch.ACCURACY_GENERAL,
                content="rows number: {content_value}.",
                content_values={
                    "df_dirty_10": "110"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_GENERAL_MISSING_VALUES,
                batch=DataProfilingBatch.ACCURACY_GENERAL,
                content="total missing values number/percentage: {content_value}.",
                content_values={
                    "df_dirty_10": "134 - 10%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_GENERAL_DUPLICATES,
                batch=DataProfilingBatch.ACCURACY_GENERAL,
                content="duplicate rows number: {content_value}.",
                content_values={
                    "df_dirty_10": "0"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_GENERAL_SOME_DEPENDENCIES,
                batch=DataProfilingBatch.ACCURACY_GENERAL,
                content="found SOME inter-columns dependencies. Here is the list of ALL dependencies in the dataset: functional dependencies between location-related variables, such as 'street', 'city', 'state', and 'zip_code'. A notable trend observed in the dataset is that properties with 3 bedrooms and 2 bathrooms are more likely to be marked as \"sold\" compared to those that are still \"for sale\"."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_GENERAL_ALL_DEPENDENCIES,
                batch=DataProfilingBatch.ACCURACY_GENERAL,
                content="found ALL inter-columns dependencies. Here is the list of ALL dependencies in the dataset: functional dependencies between location-related variables, such as 'street', 'city', 'state', and 'zip_code'. A notable trend observed in the dataset is that properties with 3 bedrooms and 2 bathrooms are more likely to be marked as \"sold\" compared to those that are still \"for sale\"."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_MISSING_VALUES_BROKERED_BY,
                batch=DataProfilingBatch.ACCURACY_MISSING_VALUES,
                content="'brokered_by' column: {content_value}.",
                content_values={
                    "df_dirty_10": "5 - 4,55%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_MISSING_VALUES_STATUS,
                batch=DataProfilingBatch.ACCURACY_MISSING_VALUES,
                content="'status' column: {content_value}.",
                content_values={
                    "df_dirty_10": "6 - 5,45%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_MISSING_VALUES_PRICE,
                batch=DataProfilingBatch.ACCURACY_MISSING_VALUES,
                content="'price' column: {content_value}.",
                content_values={
                    "df_dirty_10": "10 - 9,09%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_MISSING_VALUES_BED,
                batch=DataProfilingBatch.ACCURACY_MISSING_VALUES,
                content="'bed' column: {content_value}.",
                content_values={
                    "df_dirty_10": "13 - 11,82%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_MISSING_VALUES_BATH,
                batch=DataProfilingBatch.ACCURACY_MISSING_VALUES,
                content="'bath' column: {content_value}.",
                content_values={
                    "df_dirty_10": "12 - 11%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_MISSING_VALUES_ACRE_LOT,
                batch=DataProfilingBatch.ACCURACY_MISSING_VALUES,
                content="'acre_lot' column: {content_value}.",
                content_values={
                    "df_dirty_10": "13 - 11,82%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_MISSING_VALUES_STREET,
                batch=DataProfilingBatch.ACCURACY_MISSING_VALUES,
                content="'street' column: {content_value}.",
                content_values={
                    "df_dirty_10": "13 - 11,82%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_MISSING_VALUES_CITY,
                batch=DataProfilingBatch.ACCURACY_MISSING_VALUES,
                content="'city' column: {content_value}.",
                content_values={
                    "df_dirty_10": "11 - 10%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_MISSING_VALUES_STATE,
                batch=DataProfilingBatch.ACCURACY_MISSING_VALUES,
                content="'state' column: {content_value}.",
                content_values={
                    "df_dirty_10": "41 - 37,27%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_MISSING_VALUES_ZIP_CODE,
                batch=DataProfilingBatch.ACCURACY_MISSING_VALUES,
                content="'zip_code' column: {content_value}.",
                content_values={
                    "df_dirty_10": "15 - 13,64%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_MISSING_VALUES_HOUSE_SIZE,
                batch=DataProfilingBatch.ACCURACY_MISSING_VALUES,
                content="'house_size' column: {content_value}.",
                content_values={
                    "df_dirty_10": "14 - 12,73%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_MISSING_VALUES_PREV_SOLD_DATE,
                batch=DataProfilingBatch.ACCURACY_MISSING_VALUES,
                content="'prev_sold_date' column: {content_value}.",
                content_values={
                    "df_dirty_10": "10 - 9,09%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DISTINCT_VALUES_BROKERED_BY,
                batch=DataProfilingBatch.ACCURACY_DISTINCT_VALUES,
                content="'brokered_by' column: {content_value}.",
                content_values={
                    "df_dirty_10": "93 - 84,55%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DISTINCT_VALUES_STATUS,
                batch=DataProfilingBatch.ACCURACY_DISTINCT_VALUES,
                content="'status' column: {content_value}.",
                content_values={
                    "df_dirty_10": "5 - 4,55%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DISTINCT_VALUES_PRICE,
                batch=DataProfilingBatch.ACCURACY_DISTINCT_VALUES,
                content="'price' column: {content_value}.",
                content_values={
                    "df_dirty_10": "76 - 69,09%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DISTINCT_VALUES_BED,
                batch=DataProfilingBatch.ACCURACY_DISTINCT_VALUES,
                content="'bed' column: {content_value}.",
                content_values={
                    "df_dirty_10": "7 - 6,36%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DISTINCT_VALUES_BATH,
                batch=DataProfilingBatch.ACCURACY_DISTINCT_VALUES,
                content="'bath' column: {content_value}.",
                content_values={
                    "df_dirty_10": "7 - 6,36%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DISTINCT_VALUES_ACRE_LOT,
                batch=DataProfilingBatch.ACCURACY_DISTINCT_VALUES,
                content="'acre_lot' column: {content_value}.",
                content_values={
                    "df_dirty_10": "53 - 48,18%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DISTINCT_VALUES_STREET,
                batch=DataProfilingBatch.ACCURACY_DISTINCT_VALUES,
                content="'street' column: {content_value}.",
                content_values={
                    "df_dirty_10": "89 - 80,91%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DISTINCT_VALUES_CITY,
                batch=DataProfilingBatch.ACCURACY_DISTINCT_VALUES,
                content="'city' column: {content_value}.",
                content_values={
                    "df_dirty_10": "84 - 76,36%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DISTINCT_VALUES_STATE,
                batch=DataProfilingBatch.ACCURACY_DISTINCT_VALUES,
                content="'state' column: {content_value}.",
                content_values={
                    "df_dirty_10": "41 - 37,27%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DISTINCT_VALUES_ZIP_CODE,
                batch=DataProfilingBatch.ACCURACY_DISTINCT_VALUES,
                content="'zip_code' column: {content_value}.",
                content_values={
                    "df_dirty_10": "88 - 80.0%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DISTINCT_VALUES_HOUSE_SIZE,
                batch=DataProfilingBatch.ACCURACY_DISTINCT_VALUES,
                content="'house_size' column: {content_value}.",
                content_values={
                    "df_dirty_10": "88 - 80.0%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DISTINCT_VALUES_PREV_SOLD_DATE,
                batch=DataProfilingBatch.ACCURACY_DISTINCT_VALUES,
                content="'prev_sold_date' column: {content_value}.",
                content_values={
                    "df_dirty_10": "85 - 77,27%"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DATA_TYPES_BROKERED_BY,
                batch=DataProfilingBatch.ACCURACY_DATA_TYPES,
                content="'brokered_by' column: Text/String/Mixed (it's a list of numerical IDs, with some full names as strings)."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DATA_TYPES_STATUS,
                batch=DataProfilingBatch.ACCURACY_DATA_TYPES,
                content="'status' column: Categorical."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DATA_TYPES_PRICE,
                batch=DataProfilingBatch.ACCURACY_DATA_TYPES,
                content="'price' column: Numerical (however, sometimes there are numerical values with \"$\", so they could be considered as strings)."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DATA_TYPES_BED,
                batch=DataProfilingBatch.ACCURACY_DATA_TYPES,
                content="'bed' column: Numerical."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DATA_TYPES_BATH,
                batch=DataProfilingBatch.ACCURACY_DATA_TYPES,
                content="'bath' column: Numerical."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DATA_TYPES_ACRE_LOT,
                batch=DataProfilingBatch.ACCURACY_DATA_TYPES,
                content="'acre_lot' column: Numerical."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DATA_TYPES_STREET,
                batch=DataProfilingBatch.ACCURACY_DATA_TYPES,
                content="'street' column: Categorical."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DATA_TYPES_CITY,
                batch=DataProfilingBatch.ACCURACY_DATA_TYPES,
                content="'city' column: Categorical."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DATA_TYPES_STATE,
                batch=DataProfilingBatch.ACCURACY_DATA_TYPES,
                content="'state' column: Categorical."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DATA_TYPES_ZIP_CODE,
                batch=DataProfilingBatch.ACCURACY_DATA_TYPES,
                content="'zip_code' column: Categorical."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DATA_TYPES_HOUSE_SIZE,
                batch=DataProfilingBatch.ACCURACY_DATA_TYPES,
                content="'house_size' column: Numerical"
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_DATA_TYPES_PREV_SOLD_DATE,
                batch=DataProfilingBatch.ACCURACY_DATA_TYPES,
                content="'prev_sold_date' column: Date."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_COLUMN_DESCRIPTIONS_BROKERED_BY,
                batch=DataProfilingBatch.ACCURACY_COLUMN_DESCRIPTIONS,
                content="'brokered_by' column: ID or name of the broker handling the property."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_COLUMN_DESCRIPTIONS_STATUS,
                batch=DataProfilingBatch.ACCURACY_COLUMN_DESCRIPTIONS,
                content="'status' column: listing status (i.e. \"for_sale\" or \"sold\")."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_COLUMN_DESCRIPTIONS_PRICE,
                batch=DataProfilingBatch.ACCURACY_COLUMN_DESCRIPTIONS,
                content="'price' column: listing price."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_COLUMN_DESCRIPTIONS_BED,
                batch=DataProfilingBatch.ACCURACY_COLUMN_DESCRIPTIONS,
                content="'bed' column: number of bedrooms."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_COLUMN_DESCRIPTIONS_BATH,
                batch=DataProfilingBatch.ACCURACY_COLUMN_DESCRIPTIONS,
                content="'bath' column: number of bathrooms."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_COLUMN_DESCRIPTIONS_ACRE_LOT,
                batch=DataProfilingBatch.ACCURACY_COLUMN_DESCRIPTIONS,
                content="'acre_lot' column: lot size in acres."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_COLUMN_DESCRIPTIONS_STREET,
                batch=DataProfilingBatch.ACCURACY_COLUMN_DESCRIPTIONS,
                content="'street' column: street address."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_COLUMN_DESCRIPTIONS_CITY,
                batch=DataProfilingBatch.ACCURACY_COLUMN_DESCRIPTIONS,
                content="'city' column: city of the property."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_COLUMN_DESCRIPTIONS_STATE,
                batch=DataProfilingBatch.ACCURACY_COLUMN_DESCRIPTIONS,
                content="'state' column: state of the property."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_COLUMN_DESCRIPTIONS_ZIP_CODE,
                batch=DataProfilingBatch.ACCURACY_COLUMN_DESCRIPTIONS,
                content="'zip_code' column: zip code of the property."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_COLUMN_DESCRIPTIONS_HOUSE_SIZE,
                batch=DataProfilingBatch.ACCURACY_COLUMN_DESCRIPTIONS,
                content="'house_size' column: house size in square feet."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_COLUMN_DESCRIPTIONS_PREV_SOLD_DATE,
                batch=DataProfilingBatch.ACCURACY_COLUMN_DESCRIPTIONS,
                content="'prev_sold_date' column: date of previous sale."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_CALCULATE_FREQUENCIES_BROKERED_BY,
                batch=DataProfilingBatch.ACCURACY_FREQUENCIES,
                content="'brokered_by' column: describes how to calculate the frequencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_CALCULATE_FREQUENCIES_STATUS,
                batch=DataProfilingBatch.ACCURACY_FREQUENCIES,
                content="'status' column: describes how to calculate the frequencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_CALCULATE_FREQUENCIES_STREET,
                batch=DataProfilingBatch.ACCURACY_FREQUENCIES,
                content="'street' column: describes how to calculate the frequencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_CALCULATE_FREQUENCIES_CITY,
                batch=DataProfilingBatch.ACCURACY_FREQUENCIES,
                content="'city' column: describes how to calculate the frequencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_CALCULATE_FREQUENCIES_STATE,
                batch=DataProfilingBatch.ACCURACY_FREQUENCIES,
                content="'state' column: describes how to calculate the frequencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_CALCULATE_FREQUENCIES_ZIP_CODE,
                batch=DataProfilingBatch.ACCURACY_FREQUENCIES,
                content="'zip_code' column: describes how to calculate the frequencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_CALCULATE_FREQUENCIES_PREV_SOLD_DATE,
                batch=DataProfilingBatch.ACCURACY_FREQUENCIES,
                content="'prev_sold_date' column: describes how to calculate the frequencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VISUALIZE_FREQUENCIES_BROKERED_BY,
                batch=DataProfilingBatch.ACCURACY_FREQUENCIES,
                content="'brokered_by' column: describes how to visualize the frequencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VISUALIZE_FREQUENCIES_STATUS,
                batch=DataProfilingBatch.ACCURACY_FREQUENCIES,
                content="'status' column: describes how to visualize the frequencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VISUALIZE_FREQUENCIES_STREET,
                batch=DataProfilingBatch.ACCURACY_FREQUENCIES,
                content="'street' column: describes how to visualize the frequencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VISUALIZE_FREQUENCIES_CITY,
                batch=DataProfilingBatch.ACCURACY_FREQUENCIES,
                content="'city' column: describes how to visualize the frequencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VISUALIZE_FREQUENCIES_STATE,
                batch=DataProfilingBatch.ACCURACY_FREQUENCIES,
                content="'state' column: describes how to visualize the frequencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VISUALIZE_FREQUENCIES_ZIP_CODE,
                batch=DataProfilingBatch.ACCURACY_FREQUENCIES,
                content="'zip_code' column: describes how to visualize the frequencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VISUALIZE_FREQUENCIES_PREV_SOLD_DATE,
                batch=DataProfilingBatch.ACCURACY_FREQUENCIES,
                content="'prev_sold_date' column: describes how to visualize the frequencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_PRICE_MIN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'price' column: minimum value is {content_value}.",
                content_values={
                    "df_dirty_10": "69900"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_PRICE_MAX,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'price' column: maximum value is {content_value}.",
                content_values={
                    "df_dirty_10": "2450000"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_PRICE_MEAN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'price' column: mean value is {content_value}.",
                content_values={
                    "df_dirty_10": "481344.375"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_PRICE_MEDIAN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'price' column: median value is {content_value}.",
                content_values={
                    "df_dirty_10": "375000"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_BED_MIN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'bed' column: minimum value is {content_value}.",
                content_values={
                    "df_dirty_10": "1"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_BED_MAX,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'bed' column: maximum value is {content_value}.",
                content_values={
                    "df_dirty_10": "9999 (even 6 is acceptable)"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_BED_MEAN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'bed' column: mean value is {content_value}.",
                content_values={
                    "df_dirty_10": "1033.814"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_BED_MEDIAN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'bed' column: median value is {content_value}.",
                content_values={
                    "df_dirty_10": "3"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_BATH_MIN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'bath' column: minimum value is {content_value}.",
                content_values={
                    "df_dirty_10": "0 (even 1 is acceptable)"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_BATH_MAX,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'bath' column: maximum value is {content_value}.",
                content_values={
                    "df_dirty_10": "6"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_BATH_MEAN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'bath' column: mean value is {content_value}.",
                content_values={
                    "df_dirty_10": "2.265"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_BATH_MEDIAN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'bath' column: median value is {content_value}.",
                content_values={
                    "df_dirty_10": "2"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_ACRE_LOT_MIN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'acre_lot' column: minimum value is {content_value}.",
                content_values={
                    "df_dirty_10": "-1,56"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_ACRE_LOT_MAX,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'acre_lot' column: maximum value is {content_value}.",
                content_values={
                    "df_dirty_10": "35"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_ACRE_LOT_MEAN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'acre_lot' column: mean value is {content_value}.",
                content_values={
                    "df_dirty_10": "1.265"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_ACRE_LOT_MEDIAN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'acre_lot' column: median value is {content_value}.",
                content_values={
                    "df_dirty_10": "0.21"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MIN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'house_size' column: minimum value is {content_value}.",
                content_values={
                    "df_dirty_10": "4.699e-05"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MAX,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'house_size' column: maximum value is {content_value}.",
                content_values={
                    "df_dirty_10": "5828"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MEAN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'house_size' column: mean value is {content_value}.",
                content_values={
                    "df_dirty_10": "1965.375"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MEDIAN,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY,
                content="'house_size' column: median value is {content_value}.",
                content_values={
                    "df_dirty_10": "1879.5"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_PRICE_QUARTILES,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'price' column: {content_value}.",
                content_values={
                    "df_dirty_10": "first quartile is 263725, second quartile is 375000 and third quartile is 540341"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_PRICE_STD_DEV,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'price' column: {content_value}.",
                content_values={
                    "df_dirty_10": "standard deviation is 421099.879 or variance is 177325108023.731"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_PRICE_PLOT,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'price' column: distribution plots are present.",
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_BED_QUARTILES,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'bed' column: {content_value}.",
                content_values={
                    "df_dirty_10": "first quartile is 3, second quartile is 3 and third quartile is 4"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_BED_STD_DEV,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'bed' column: {content_value}.",
                content_values={
                    "df_dirty_10": "standard deviation is 3055.272 or variance is 9334688.944"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_BED_PLOT,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'bed' column: distribution plots are present."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_BATH_QUARTILES,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'bath' column: {content_value}.",
                content_values={
                    "df_dirty_10": "first quartile is 2, second quartile is 2 and third quartile is 3"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_BATH_STD_DEV,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'bath' column: {content_value}.",
                content_values={
                    "df_dirty_10": "standard deviation is 1.24 or variance is 1.537"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_BATH_PLOT,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'bath' column: distribution plots are presents."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_ACRE_LOT_QUARTILES,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'acre_lot' column: {content_value}.",
                content_values={
                    "df_dirty_10": "first quartile is 0.15, second quartile is 0.21 and third quartile id 0.34"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_ACRE_LOT_STD_DEV,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'acre_lot' column: {content_value}.",
                content_values={
                    "df_dirty_10": "standard deviation is 4.828 or variance is 23.307"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_ACRE_LOT_PLOT,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'acre_lot' column: distribution plots are present."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_QUARTILES,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'house_size' column: {content_value}.",
                content_values={
                    "df_dirty_10": "first quartile is 1331.75, second quartile is 1879.5 and third quartile is 2437"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_STD_DEV,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'house_size' column: {content_value}.",
                content_values={
                    "df_dirty_10": "standard deviation is 1120.44 or variance is 1255385.046"
                }
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.ACCURACY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_PLOT,
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD,
                content="'house_size' column: distribution plots are present."
            ),
        ]
        prompts = [
            EvaluationPrompt(
                batch=DataProfilingBatch.ACCURACY_GENERAL.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are true or false.

Keep in mind that any information that is requested can be given in any form, be it a number/datum, a piece of text, or a code snippet that helps obtain that information, but is MUST be accurate and correct.

Keep also in mind that a general description of the dataset must not depend on any column and must stand alone per se, giving an overview of the dataset and not of the columns.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to EACH ONE of the above statements based on the fact that they are false (0) or true (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.ACCURACY_MISSING_VALUES.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are true or false.

Keep in mind that any information that is requested can be given in any form, be it a number/datum, a piece of text, or a code snippet that helps obtain that information, but is MUST be accurate and correct.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to EACH ONE of the above statements based on the fact that they are false (0) or true (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.ACCURACY_DISTINCT_VALUES.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are true or false.

Keep in mind that any information that is requested can be given in any form, be it a number/datum, a piece of text, or a code snippet that helps obtain that information, but is MUST be accurate and correct.  
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to EACH ONE of the above statements based on the fact that they are false (0) or true (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.ACCURACY_DATA_TYPES.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are true or false.

Keep in mind that any information that is requested can be given in any form, be it a number/datum, a piece of text, or a code snippet that helps obtain that information, but is MUST be accurate and correct.
              """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to EACH ONE of the above statements based on the fact that they are false (0) or true (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.ACCURACY_COLUMN_DESCRIPTIONS.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are true or false.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to EACH ONE of the above statements based on the fact that they are false (0) or true (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_EASY.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are true or false.

Keep in mind that any information that is requested can be given in any form, be it a number/datum, a piece of text, or a code snippet that helps obtain that information, but is MUST be accurate and correct.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to EACH ONE of the above statements based on the fact that they are true (0) or false (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.ACCURACY_VALUE_DISTRIBUTIONS_HARD.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are mentioned or not.

Keep in mind that any information that is requested can be given in any form, be it a number/datum, a piece of text, or a code snippet that helps obtain that information, but is MUST be accurate and correct.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to EACH ONE of the above statements based on the fact that they are false or true (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            )
        ]
        super().__init__("Accuracy", items, prompts)