from data.batch import Batch
from experiments.model.checklist import BaseChecklist, ChecklistItem
from experiments.model.prompt import EvaluationPrompt

class DataCleaningCompletenessChecklist(BaseChecklist):

    def __init__(self) -> None:
        items = [
            ChecklistItem(
                item_id="data_cleaning_completeness_1",
                batch=Batch.MISSING_VALUES_SOLUTION,
                content="'brokered_by' column: presence of missing values."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_2",
                batch=Batch.MISSING_VALUES_SOLUTION,
                content="'status' column: presence of missing values."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_3",
                batch=Batch.MISSING_VALUES_SOLUTION,
                content="'price' column: presence of missing values."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_4",
                batch=Batch.MISSING_VALUES_SOLUTION,
                content="'bed' column: presence of missing values."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_5",
                batch=Batch.MISSING_VALUES_SOLUTION,
                content="'bath' column: presence of missing values."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_6",
                batch=Batch.MISSING_VALUES_SOLUTION,
                content="'acre_lot' column: presence of missing values."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_7",
                batch=Batch.MISSING_VALUES_SOLUTION,
                content="'street' column: presence of missing values."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_8",
                batch=Batch.MISSING_VALUES_SOLUTION,
                content="'city' column: presence of missing values."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_9",
                batch=Batch.MISSING_VALUES_SOLUTION,
                content="'state' column: presence of missing values."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_10",
                batch=Batch.MISSING_VALUES_SOLUTION,
                content="'zip_code' column: presence of missing values."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_11",
                batch=Batch.MISSING_VALUES_SOLUTION,
                content="'house_size' column: presence of missing values."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_12",
                batch=Batch.MISSING_VALUES_SOLUTION,
                content="'prev_sold_date' column: presence of missing values."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_13",
                batch=Batch.DIRTY_SOLUTION,
                content="'brokered_by' column: presence of full names in a list of numerical IDs."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_14",
                batch=Batch.DIRTY_SOLUTION,
                content="'status' column: presence of format inconsistencies ('s' stands for 'sold', 'f' stands for 'for_sale')."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_15",
                batch=Batch.DIRTY_SOLUTION,
                content="'price' column: presence of format inconsistencies (the presence of '$' in a numerical column)."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_16",
                batch=Batch.DIRTY_SOLUTION,
                content="'bed' column: presence of outliers/placeholders (specifically, '9999')."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_17",
                batch=Batch.DIRTY_SOLUTION,
                content="'bath' column: presence of data errors (specifically, '0')."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_18",
                batch=Batch.DIRTY_SOLUTION,
                content="'acre_lot' column: the presence of negative values (which are nonsensical)."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_19",
                batch=Batch.DIRTY_SOLUTION,
                content="'street' column: presence of format inconsistencies (e.g. 'Boulevard' instead of 'Blvd')."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_20",
                batch=Batch.DIRTY_SOLUTION,
                content="'city' column: presence of data errors (European cities in a USA dataset)."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_21",
                batch=Batch.DIRTY_SOLUTION,
                content="'state' column: presence of format inconsistencies (some states are abbreviated)."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_22",
                batch=Batch.DIRTY_SOLUTION,
                content="'zip_code' column: presence of data errors (some zip codes are partial)."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_23",
                batch=Batch.DIRTY_SOLUTION,
                content="'house_size' column: presence of values in a different unit of measure (some values are in square miles, while the majority is in square feet)."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_24",
                batch=Batch.DIRTY_SOLUTION,
                content="'prev_sold_date' column: presence of different date formats."
            ),
            ChecklistItem(
                item_id="data_cleaning_completeness_25",
                batch=Batch.DIRTY_SOLUTION,
                content="presence of non-exact duplicate rows."
            ),
        ]
        prompts = [
            EvaluationPrompt(
                batch=Batch.MISSING_VALUES_SOLUTION,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.
Keep in mind that there are only three types of missing values: '-', '' and NaN. Any other character or combination of characters must not be considered a missing value (for example, negative values are NOT to be considered missing values).
                """
            ),
            EvaluationPrompt(
                batch=Batch.DIRTY_SOLUTION,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

Keep in mind that handling non-exact duplicates means finding pairs of rows that are slightly different but share the same values for a meaningful subset of columns that acts as a unique column combination.
Keep also in mind that you should not care about the fact that a specific column is mentioned or not: you may consider a fact as true as long as there is some piece of text that takes care about it.
                """
            )
        ]
        super().__init__(items, prompts)