from data.batches import DataCleaningBatch
from data.checklists.data_cleaning.item_ids import DataCleaningItemId
from experiments.model.checklist import BaseChecklist, DataCleaningChecklistItem
from experiments.model.prompt import EvaluationPrompt

class DataCleaningCompletenessChecklist(BaseChecklist):

    def __init__(self) -> None:
        items = [
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_MISSING_VALUES_SOLUTION_BROKERED_BY,
                batch=DataCleaningBatch.COMPLETENESS_MISSING_VALUES_SOLUTION,
                content="'brokered_by' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_MISSING_VALUES_SOLUTION_STATUS,
                batch=DataCleaningBatch.COMPLETENESS_MISSING_VALUES_SOLUTION,
                content="'status' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_MISSING_VALUES_SOLUTION_PRICE,
                batch=DataCleaningBatch.COMPLETENESS_MISSING_VALUES_SOLUTION,
                content="'price' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_MISSING_VALUES_SOLUTION_BED,
                batch=DataCleaningBatch.COMPLETENESS_MISSING_VALUES_SOLUTION,
                content="'bed' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_MISSING_VALUES_SOLUTION_BATH,
                batch=DataCleaningBatch.COMPLETENESS_MISSING_VALUES_SOLUTION,
                content="'bath' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_MISSING_VALUES_SOLUTION_ACRE_LOT,
                batch=DataCleaningBatch.COMPLETENESS_MISSING_VALUES_SOLUTION,
                content="'acre_lot' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_MISSING_VALUES_SOLUTION_STREET,
                batch=DataCleaningBatch.COMPLETENESS_MISSING_VALUES_SOLUTION,
                content="'street' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_MISSING_VALUES_SOLUTION_CITY,
                batch=DataCleaningBatch.COMPLETENESS_MISSING_VALUES_SOLUTION,
                content="'city' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_MISSING_VALUES_SOLUTION_STATE,
                batch=DataCleaningBatch.COMPLETENESS_MISSING_VALUES_SOLUTION,
                content="'state' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_MISSING_VALUES_SOLUTION_ZIP_CODE,
                batch=DataCleaningBatch.COMPLETENESS_MISSING_VALUES_SOLUTION,
                content="'zip_code' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_MISSING_VALUES_SOLUTION_HOUSE_SIZE,
                batch=DataCleaningBatch.COMPLETENESS_MISSING_VALUES_SOLUTION,
                content="'house_size' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_MISSING_VALUES_SOLUTION_PREV_SOLD_DATE,
                batch=DataCleaningBatch.COMPLETENESS_MISSING_VALUES_SOLUTION,
                content="'prev_sold_date' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_DIRTY_SOLUTION_BROKERED_BY,
                batch=DataCleaningBatch.COMPLETENESS_DIRTY_SOLUTION,
                content="'brokered_by' column: presence of full names in a list of numerical IDs."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_DIRTY_SOLUTION_STATUS,
                batch=DataCleaningBatch.COMPLETENESS_DIRTY_SOLUTION,
                content="'status' column: presence of format inconsistencies ('s' stands for 'sold', 'f' stands for 'for_sale')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_DIRTY_SOLUTION_PRICE,
                batch=DataCleaningBatch.COMPLETENESS_DIRTY_SOLUTION,
                content="'price' column: presence of format inconsistencies (the presence of '$' in a numerical column)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_DIRTY_SOLUTION_BED,
                batch=DataCleaningBatch.COMPLETENESS_DIRTY_SOLUTION,
                content="'bed' column: presence of outliers/placeholders (specifically, '9999')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_DIRTY_SOLUTION_BATH,
                batch=DataCleaningBatch.COMPLETENESS_DIRTY_SOLUTION,
                content="'bath' column: presence of data errors (specifically, '0')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_DIRTY_SOLUTION_ACRE_LOT,
                batch=DataCleaningBatch.COMPLETENESS_DIRTY_SOLUTION,
                content="'acre_lot' column: the presence of negative values (which need to be replaced)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_DIRTY_SOLUTION_STREET,
                batch=DataCleaningBatch.COMPLETENESS_DIRTY_SOLUTION,
                content="'street' column: presence of format inconsistencies (e.g. 'Boulevard' instead of 'Blvd')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_DIRTY_SOLUTION_CITY,
                batch=DataCleaningBatch.COMPLETENESS_DIRTY_SOLUTION,
                content="'city' column: presence of data errors (European cities in a USA dataset)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_DIRTY_SOLUTION_STATE,
                batch=DataCleaningBatch.COMPLETENESS_DIRTY_SOLUTION,
                content="'state' column: presence of format inconsistencies (some states are abbreviated)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_DIRTY_SOLUTION_ZIP_CODE,
                batch=DataCleaningBatch.COMPLETENESS_DIRTY_SOLUTION,
                content="'zip_code' column: presence of data errors (some zip codes are partial)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_DIRTY_SOLUTION_HOUSE_SIZE,
                batch=DataCleaningBatch.COMPLETENESS_DIRTY_SOLUTION,
                content="'house_size' column: presence of values in a different unit of measure (some values are in square miles, while the majority is in square feet, so there are extremely small values that need to be replaced)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_DIRTY_SOLUTION_PREV_SOLD_DATE,
                batch=DataCleaningBatch.COMPLETENESS_DIRTY_SOLUTION,
                content="'prev_sold_date' column: presence of different date formats (which need to be standardized)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.COMPLETENESS_SOLUTION_NON_EXACT_DUPLICATES,
                batch=DataCleaningBatch.COMPLETENESS_DIRTY_SOLUTION,
                content="presence of non-exact duplicate rows."
            ),
        ]
        prompts = [
            EvaluationPrompt(
                batch=DataCleaningBatch.COMPLETENESS_MISSING_VALUES_SOLUTION.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

Keep in mind that there are only three types of missing values: '-', '' and NaN. Any other character or combination of characters must not be considered a missing value (for example, negative values are NOT to be considered missing values).

Keep also in mind that you should not care about the fact that a specific column is mentioned or not while handling missing values: you may consider a fact as true as long as there is some piece of text that implicitly takes care about them.

Keep also in mind you that you must consider a fact as true even if only ONE kind of missing value is handled (i.e. if there is an EXPLICIT solution for handling NaN values, but not other types of missing values, the solution is still valid and must be evaluated as true).

Keep also in mind that if there are actions that are performed on the whole dataset and that address AT LEAST one kind of missing value, you must evaluate each statement with a score of 1. Examples of such table-wise actions are replacements of '-' and/or '' with NaN performed on an entire dataframe in a single line of code.
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a solution for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataCleaningBatch.COMPLETENESS_DIRTY_SOLUTION.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

Keep in mind that handling non-exact duplicates means finding pairs of rows that are slightly different but share the same values for a meaningful subset of columns that acts as a unique column combination.

Keep also in mind that you should not care about the fact that a specific column is mentioned or not: you may consider a fact as true as long as there is some piece of text that takes care about it.
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a solution for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            )
        ]
        super().__init__("Data Cleaning - Completeness", items, prompts)