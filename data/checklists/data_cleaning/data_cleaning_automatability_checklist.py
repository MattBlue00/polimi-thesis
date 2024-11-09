from data.batches import DataCleaningBatch
from data.checklists.data_cleaning.item_ids import DataCleaningItemId
from experiments.model.checklist import BaseChecklist
from experiments.model.checklist_item import DataCleaningChecklistItem
from experiments.model.prompt import EvaluationPrompt

class DataCleaningAutomatabilityChecklist(BaseChecklist):

    def __init__(self) -> None:
        items = [
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_MISSING_VALUES_SOLUTION_BROKERED_BY,
                batch=DataCleaningBatch.AUTOMATABILITY_MISSING_VALUES_SOLUTION,
                content="'brokered_by' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_MISSING_VALUES_SOLUTION_STATUS,
                batch=DataCleaningBatch.AUTOMATABILITY_MISSING_VALUES_SOLUTION,
                content="'status' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_MISSING_VALUES_SOLUTION_PRICE,
                batch=DataCleaningBatch.AUTOMATABILITY_MISSING_VALUES_SOLUTION,
                content="'price' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_MISSING_VALUES_SOLUTION_BED,
                batch=DataCleaningBatch.AUTOMATABILITY_MISSING_VALUES_SOLUTION,
                content="'bed' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_MISSING_VALUES_SOLUTION_BATH,
                batch=DataCleaningBatch.AUTOMATABILITY_MISSING_VALUES_SOLUTION,
                content="'bath' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_MISSING_VALUES_SOLUTION_ACRE_LOT,
                batch=DataCleaningBatch.AUTOMATABILITY_MISSING_VALUES_SOLUTION,
                content="'acre_lot' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_MISSING_VALUES_SOLUTION_STREET,
                batch=DataCleaningBatch.AUTOMATABILITY_MISSING_VALUES_SOLUTION,
                content="'street' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_MISSING_VALUES_SOLUTION_CITY,
                batch=DataCleaningBatch.AUTOMATABILITY_MISSING_VALUES_SOLUTION,
                content="'city' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_MISSING_VALUES_SOLUTION_STATE,
                batch=DataCleaningBatch.AUTOMATABILITY_MISSING_VALUES_SOLUTION,
                content="'state' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_MISSING_VALUES_SOLUTION_ZIP_CODE,
                batch=DataCleaningBatch.AUTOMATABILITY_MISSING_VALUES_SOLUTION,
                content="'zip_code' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_MISSING_VALUES_SOLUTION_HOUSE_SIZE,
                batch=DataCleaningBatch.AUTOMATABILITY_MISSING_VALUES_SOLUTION,
                content="'house_size' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_MISSING_VALUES_SOLUTION_PREV_SOLD_DATE,
                batch=DataCleaningBatch.AUTOMATABILITY_MISSING_VALUES_SOLUTION,
                content="'prev_sold_date' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_DIRTY_SOLUTION_BROKERED_BY,
                batch=DataCleaningBatch.AUTOMATABILITY_DIRTY_SOLUTION,
                content="'brokered_by' column: presence of full names in a list of numerical IDs."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_DIRTY_SOLUTION_STATUS,
                batch=DataCleaningBatch.AUTOMATABILITY_DIRTY_SOLUTION,
                content="'status' column: presence of format inconsistencies ('s' stands for 'sold', 'f' stands for 'for_sale')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_DIRTY_SOLUTION_PRICE,
                batch=DataCleaningBatch.AUTOMATABILITY_DIRTY_SOLUTION,
                content="'price' column: presence of format inconsistencies (the presence of '$' in a numerical column)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_DIRTY_SOLUTION_BED,
                batch=DataCleaningBatch.AUTOMATABILITY_DIRTY_SOLUTION,
                content="'bed' column: presence of outliers/placeholders (specifically, '9999')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_DIRTY_SOLUTION_BATH,
                batch=DataCleaningBatch.AUTOMATABILITY_DIRTY_SOLUTION,
                content="'bath' column: presence of data errors (specifically, '0')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_DIRTY_SOLUTION_ACRE_LOT,
                batch=DataCleaningBatch.AUTOMATABILITY_DIRTY_SOLUTION,
                content="'acre_lot' column: the presence of negative values (which need to be replaced)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_DIRTY_SOLUTION_STREET,
                batch=DataCleaningBatch.AUTOMATABILITY_DIRTY_SOLUTION,
                content="'street' column: presence of format inconsistencies (e.g. 'Boulevard' instead of 'Blvd')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_DIRTY_SOLUTION_CITY,
                batch=DataCleaningBatch.AUTOMATABILITY_DIRTY_SOLUTION,
                content="'city' column: presence of data errors (European cities in a USA dataset)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_DIRTY_SOLUTION_STATE,
                batch=DataCleaningBatch.AUTOMATABILITY_DIRTY_SOLUTION,
                content="'state' column: presence of format inconsistencies (some states are abbreviated)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_DIRTY_SOLUTION_ZIP_CODE,
                batch=DataCleaningBatch.AUTOMATABILITY_DIRTY_SOLUTION,
                content="'zip_code' column: presence of data errors (some zip codes are partial)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_DIRTY_SOLUTION_HOUSE_SIZE,
                batch=DataCleaningBatch.AUTOMATABILITY_DIRTY_SOLUTION,
                content="'house_size' column: presence of values in a different unit of measure (some values are in square miles, while the majority is in square feet, so there are extremely small values that need to be replaced)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_DIRTY_SOLUTION_PREV_SOLD_DATE,
                batch=DataCleaningBatch.AUTOMATABILITY_DIRTY_SOLUTION,
                content="'prev_sold_date' column: presence of different date formats (which need to be standardized)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.AUTOMATABILITY_SOLUTION_NON_EXACT_DUPLICATES,
                batch=DataCleaningBatch.AUTOMATABILITY_DIRTY_SOLUTION,
                content="presence of non-exact duplicate rows."
            ),
        ]
        prompts = [
            EvaluationPrompt(
                batch=DataCleaningBatch.AUTOMATABILITY_MISSING_VALUES_SOLUTION.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

Keep in mind that there are only three types of missing values: '-', '' and NaN. Any other character or combination of characters must not be considered a missing value (for example, negative values are NOT to be considered missing values).

You will be given a text that should contain some solutions for various problems and you have to evaluate whether, for each of the problems you will be given, the solution that you can find in the text, as it is in the text, is automatable or not.

A solution for a problem is said to be AUTOMATABLE if some code that (at least partially) implements it is provided. However, if the text does not provide a solution strategy but directly the cleaned row/column/dataset, then you must evaluate with a score of 1 all the statements that deal with some of the data that have been given in the cleaned (portion of) dataset.
Therefore, if a text is made of ONLY lines of code (including the eventual Python comments), then you can safely evaluate all the statements with a score of 1.
Analogously, if a text is made of ONLY text and NO line of code, EXCLUDING the case in which some cleaned row/column/dataset is provided, then you can safely evaluate all the statements with a score of 0.
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a solution that is automatable for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are not automatable or automatable. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataCleaningBatch.AUTOMATABILITY_DIRTY_SOLUTION.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

Keep in mind that handling non-exact duplicates means finding pairs of rows that are slightly different but share the same values for a meaningful subset of columns that acts as a unique column combination.

You will be given a text that should contain some solutions for various problems and you have to evaluate whether, for each of the problems you will be given, the solution that you can find in the text, as it is in the text, is automatable or not.

A solution for a problem is said to be AUTOMATABLE if some code that (at least partially) implements it is provided. However, if the text does not provide a solution strategy but directly the cleaned row/column/dataset, then you must evaluate with a score of 1 all the statements that deal with some of the data that have been given in the cleaned (portion of) dataset.
Therefore, if a text is made of ONLY lines of code (including the eventual Python comments), then you can safely evaluate all the statements with a score of 1.
Analogously, if a text is made of ONLY text and NO line of code, EXCLUDING the case in which some cleaned row/column/dataset is provided, then you can safely evaluate all the statements with a score of 0.
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a solution that is automatable for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are not automatable or automatable. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            )
        ]
        super().__init__("Data Cleaning - Automatability", items, prompts)