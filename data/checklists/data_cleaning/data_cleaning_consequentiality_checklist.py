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
                item=DataCleaningItemId.CONSEQUENTIALITY_DIRTY_SOLUTION_BROKERED_BY,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="'brokered_by' column: presence of full names in a list of numerical IDs."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.CONSEQUENTIALITY_DIRTY_SOLUTION_STATUS,
                batch=DataCleaningBatch.CONSEQUENTIALITY_DIRTY_SOLUTION,
                content="'status' column: presence of format inconsistencies ('s' stands for 'sold', 'f' stands for 'for_sale')."
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
                content="'state' column: presence of format inconsistencies (some states are abbreviated)."
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
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You must consider a solution to a problem as CONSEQUENTIAL if there is an obvious cause-effect relationship between a piece of text or a line of code and the effect it is intended to provoke, REGARDLESS of the fact that the proposed solution actually solves the problem and REGARDLESS of the fact that the solution is given in a clear and unambiguous way. For this reason, for example, if a piece of text wants to solve the problem of missing values for a specific column by performing a data type conversion with the parameter "errors='coerce'", the cause-effect relationship is NOT consequential, because only an expert user knows that such a parameter is able to handle also missing or wrong values during a data type conversion (which is a different task with respect to the task of solving the problem of missing values).

Keep in mind that you must consider a solution as CONSEQUENTIAL even if it does NOT provide a DIRECT way to solve a problem, as long that a user can easily link a solution proposal to the effect it is intended to obtain.
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a CONSEQUENTIAL solution for the following problems:
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
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You must consider a solution to a problem as CONSEQUENTIAL if there is an obvious cause-effect relationship between a piece of text or a line of code and the effect it is intended to provoke, REGARDLESS of the fact that the proposed solution actually solves the problem and REGARDLESS of the fact that the solution is given in a clear and unambiguous way. For this reason, for example, if a piece of text wants to solve the fact that some prices have a currency and others don't by performing a data type conversion to a numeric type with the parameter "errors='coerce'", the cause-effect relationship is NOT consequential, because only an expert user knows that such a parameter is able to transform non-numeric values into NaN values during a data type conversion (which is a different task with respect to the task of solving the prices in different formats).
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a CONSEQUENTIAL solution for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
        ]
        super().__init__("Data Cleaning - Consequentiality", items, prompts)