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
