from data.batches import DataCleaningBatch
from data.checklists.data_cleaning.item_ids import DataCleaningItemId
from experiments.model.checklist import BaseChecklist
from experiments.model.checklist_item import DataCleaningChecklistItem
from experiments.model.prompt import EvaluationPrompt


class DataCleaningConsequentialityChecklist(BaseChecklist):

    def __init__(self) -> None:
        items = [
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION_BROKERED_BY,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION,
                content="'brokered_by' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION_STATUS,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION,
                content="'status' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION_PRICE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION,
                content="'price' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION_BED,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION,
                content="'bed' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION_BATH,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION,
                content="'bath' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION_ACRE_LOT,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION,
                content="'acre_lot' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION_STREET,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION,
                content="'street' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION_CITY,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION,
                content="'city' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION_STATE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION,
                content="'state' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION_ZIP_CODE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION,
                content="'zip_code' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION_HOUSE_SIZE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION,
                content="'house_size' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION_PREV_SOLD_DATE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION,
                content="'prev_sold_date' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS_BROKERED_BY,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS,
                content="'brokered_by' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS_STATUS,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS,
                content="'status' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS_PRICE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS,
                content="'price' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS_BED,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS,
                content="'bed' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS_BATH,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS,
                content="'bath' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS_ACRE_LOT,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS,
                content="'acre_lot' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS_STREET,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS,
                content="'street' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS_CITY,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS,
                content="'city' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS_STATE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS,
                content="'state' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS_ZIP_CODE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS,
                content="'zip_code' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS_HOUSE_SIZE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS,
                content="'house_size' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS_PREV_SOLD_DATE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS,
                content="'prev_sold_date' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_DIRTY_SOLUTION_BROKERED_BY,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="'brokered_by' column: presence of full names (strings) in a list of numerical IDs."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_DIRTY_SOLUTION_STATUS,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="'status' column: presence of format inconsistencies ('s' stands for 'sold', 'f' stands for 'for_sale', which need standardizing)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_DIRTY_SOLUTION_PRICE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="'price' column: presence of format inconsistencies (the presence of '$' in a numerical column)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_DIRTY_SOLUTION_BED,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="'bed' column: presence of outliers/placeholders (specifically, '9999')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_DIRTY_SOLUTION_BATH,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="'bath' column: presence of data errors (specifically, '0')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_DIRTY_SOLUTION_ACRE_LOT,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="'acre_lot' column: the presence of negative values (which need to be replaced)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_DIRTY_SOLUTION_STREET,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="'street' column: presence of format inconsistencies (e.g. 'Boulevard' instead of 'Blvd')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_DIRTY_SOLUTION_CITY,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="'city' column: presence of data errors (European cities in a USA dataset)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_DIRTY_SOLUTION_STATE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="'state' column: presence of format inconsistencies (some states are abbreviated while others are not, so there is the need for standardization)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_DIRTY_SOLUTION_ZIP_CODE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="'zip_code' column: presence of data errors (some zip codes are partial)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_DIRTY_SOLUTION_HOUSE_SIZE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="'house_size' column: presence of values in a different unit of measure (some values are in square miles, while the majority is in square feet, so there are extremely small values that need to be replaced)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_DIRTY_SOLUTION_PREV_SOLD_DATE,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="'prev_sold_date' column: presence of different date formats (which need to be standardized)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_SOLUTION_NON_EXACT_DUPLICATES,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="presence of non-exact duplicate rows."
            ),
        ]
        prompts = [
            EvaluationPrompt(
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_SOLUTION.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You must consider a proposed solution to a problem as CLEAR, if the provided solution addresses the problem in a clear way. A clear solution must be graded with a score of 1.
           
Keep in mind that if a piece of text wants to solve the problem of missing values for a specific column by performing a data type conversion with the parameter "errors='coerce'" (this parameter must be EXPLICIT for this condition to apply), the corresponding statement MUST be graded as 0. This condition MUST prevail on the other ones. 
  
If the solution does NOT specifically address missing values for a specific column (unless a general approach is used, where there are operations performed on the whole dataset/dataframe), the corresponding statements must be graded as 0.
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a clear solution for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataCleaningBatch.CONSEQUENTIALITY_MISSING_VALUES_ALL_KINDS.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

Keep in mind that there are only three types of missing values: '-', '' and NaN. Any other character or combination of characters must not be considered a missing value (for example, negative values are NOT to be considered missing values).

Keep also in mind that if there are actions that are computed on the whole dataset and that address each one of the three types of missing values, you must evaluate each statement with a score of 1. Examples of such table-wise actions are replacements of '-' and '' with NaN performed on an entire dataframe in a single or a few lines of code.

Keep also in mind that if there are actions that convert the data type of a column with functions that explicitly mention the "errors='coerce'" parameter (e.g. to_numeric, to_datetime, etc. and NOT astype), then all the types of missing values are handled for that specific column.

You must consider a proposed solution to a problem as CLEAR, if the provided solution addresses the problem in a clear way. A clear solution must be graded with a score of 1.
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a clear solution that encompasses all the three types of missing values for the following columns:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You must consider a proposed solution to a problem as CLEAR, if the provided solution addresses the problem in a clear way. A clear solution must be graded with a score of 1.       
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a clear solution for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered} 
                """
            ),
        ]
        super().__init__("Consequentiality", items, prompts)