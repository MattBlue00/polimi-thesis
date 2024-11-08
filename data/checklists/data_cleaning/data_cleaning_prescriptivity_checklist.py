from data.batches import DataCleaningBatch
from data.checklists.data_cleaning.item_ids import DataCleaningItemId
from experiments.model.checklist import BaseChecklist
from experiments.model.checklist_item import DataCleaningChecklistItem
from experiments.model.prompt import EvaluationPrompt


class DataCleaningPrescriptivityChecklist(BaseChecklist):

    def __init__(self) -> None:
        items = [
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION_BROKERED_BY,
                batch=DataCleaningBatch.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION,
                content="'brokered_by' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION_STATUS,
                batch=DataCleaningBatch.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION,
                content="'status' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION_PRICE,
                batch=DataCleaningBatch.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION,
                content="'price' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION_BED,
                batch=DataCleaningBatch.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION,
                content="'bed' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION_BATH,
                batch=DataCleaningBatch.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION,
                content="'bath' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION_ACRE_LOT,
                batch=DataCleaningBatch.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION,
                content="'acre_lot' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION_STREET,
                batch=DataCleaningBatch.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION,
                content="'street' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION_CITY,
                batch=DataCleaningBatch.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION,
                content="'city' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION_STATE,
                batch=DataCleaningBatch.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION,
                content="'state' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION_ZIP_CODE,
                batch=DataCleaningBatch.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION,
                content="'zip_code' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION_HOUSE_SIZE,
                batch=DataCleaningBatch.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION,
                content="'house_size' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION_PREV_SOLD_DATE,
                batch=DataCleaningBatch.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION,
                content="'prev_sold_date' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_DIRTY_SOLUTION_BROKERED_BY,
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION,
                content="'brokered_by' column: presence of full names in a list of numerical IDs."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_DIRTY_SOLUTION_STATUS,
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION,
                content="'status' column: presence of format inconsistencies ('s' stands for 'sold', 'f' stands for 'for_sale')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_DIRTY_SOLUTION_PRICE,
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION,
                content="'price' column: presence of format inconsistencies (the presence of '$' in a numerical column)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_DIRTY_SOLUTION_BED,
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION,
                content="'bed' column: presence of outliers/placeholders (specifically, ‘9999')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_DIRTY_SOLUTION_BATH,
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION,
                content="'bath' column: presence of data errors (specifically, ‘0')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_DIRTY_SOLUTION_ACRE_LOT,
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION,
                content="'acre_lot' column: presence of negative values (which need to be removed)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_DIRTY_SOLUTION_STREET,
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION,
                content="'street' column: presence of format inconsistencies (e.g. 'Boulevard' instead of ‘Blvd')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_DIRTY_SOLUTION_CITY,
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION,
                content="'city' column: presence of data errors (European cities in a USA dataset)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_DIRTY_SOLUTION_STATE,
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION,
                content="'state' column: presence of format inconsistencies (some states are abbreviated)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_DIRTY_SOLUTION_ZIP_CODE,
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION,
                content="'zip_code' column: presence of data errors (some zip codes are partial)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_DIRTY_SOLUTION_HOUSE_SIZE,
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION,
                content="'house_size' column: presence of values in a different unit of measure (some values are in square miles, while the majority is in square feet, so there are extremely small values that need to be handled)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_DIRTY_SOLUTION_PREV_SOLD_DATE,
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION,
                content="'prev_sold_date' column: presence of different date formats (which need to be standardized in a unique format/date type)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.PRESCRIPTIVITY_SOLUTION_NON_EXACT_DUPLICATES,
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION,
                content="presence of non-exact duplicates."
            )
        ]
        prompts = [
            EvaluationPrompt(
                batch=DataCleaningBatch.PRESCRIPTIVITY_MISSING_VALUES_SOLUTION.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

Keep in mind that there are only three types of missing values: '-', '' and NaN. Any other character or combination of characters must not be considered a missing value (for example, negative values are NOT to be considered missing values).

Keep also in mind that a 'prescriptive resolution strategy' means that the text will provide only ONE precise, well-defined and prescriptive strategy to solve a problem (i.e. it will NOT propose more than ONE solution for a problem and that solution will NOT be vague). Also, if a solution strategy comprises the choice between two alternatives, the solution is prescriptive if and only if the user is given a clear criteria to choose with.
For example, given the text "For numerical columns like 'price', 'bed', 'bath', 'acre_lot', and 'house_size, decide whether to fill missing values with a central tendency measure (mean, median) or leave them as NaN if they are significant", the statements relative to the addressed columns must be evaluated with the score of 0, since there is more than one solution provided (there are two solutions: "fill with mean/median" AND "leave as NaN") and no criteria to choose with is provided.
Also, if there is a piece of text that describes how to resolve a problem and then there is the code, relative to that problem, that propose a different solution (to the same problem), the statements relative to that problem must be evaluated with a score of 0.
Please, keep in mind that using "Unknown", "Not Available" or any other kind of placeholder must NOT be considered as an alternative solution as they mean the same thing (so, if a piece of code uses "Unknown" instead of "Not Available" it must not be penalized). The same applies to solutions like "replace with mean or median", as choosing between mean and median requires knowing the context of analysis, which you will never be given. Hence, if the text proposes only one solution to a problem and such solution is clear and precise, it must be considered as prescriptive even if it lets you choose between "Unknown", "Not Available", NaN, and so on, or between mean and median.
Please, FOCUS and PAY ATTENTION on this part as it's quite important.

Keep also in mind you that you must consider a fact as true even if only ONE kind of missing value is handled (i.e. if there is an EXPLICIT solution for handling only a type of missing values, but not for the other ones, the solution is still valid and must be evaluated with a score of 1, provided that it presents a precise strategy).
Also, if the text mentions to fix the missing values in general (and does not distinguish between the three kinds), but the code addresses only one kind of missing value, the related statements must be evaluated with the score of 1 (provided that they present a precise strategy).
Also, even if the text mentions to fix the missing values in general (i.e. without addressing each type of missing value), the related statements must be evaluated with a score of 1 (provided that the proposed solution comprises a precise strategy).
Keep also in mind that, if the text proposes a textual solution (or more than one) and then there is a piece of code that proposes ANOTHER solution (i.e. it's not the implementation of the textual solutions) to address the same problem, the statement relative to that specific problem must be evaluated with a score of 0.

Keep also in mind that if there are actions that are performed on the whole dataset and that address AT LEAST one kind of missing value, you must evaluate each statement (for each column) with a score of 1 (provided that the solution presents a precise strategy). Examples of such table-wise actions are replacements of '-' and/or '' with NaN performed on an entire dataframe in a single line of code.
                
Keep also in mind that if the text provided is composed ONLY by code, every statement MUST be evaluated as true.
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a prescriptive resolution strategy for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

Keep also in mind that a 'prescriptive resolution strategy' means that the text will provide only ONE precise, well-defined and prescriptive strategy to solve a problem (i.e. it will NOT propose more than ONE solution for a problem and that solution will NOT be vague). Also, if a solution strategy comprises the choice between two alternatives, the solution is prescriptive if and only if the user is given a clear criteria to choose with.
For example, given the text "For numerical columns like 'price', 'bed', 'bath', 'acre_lot', and 'house_size, decide whether to fill missing values with a central tendency measure (mean, median) or leave them as NaN if they are significant", the statements relative to the addressed columns must be evaluated with the score of 0, since there is more than one solution provided (there are two solutions: "fill with mean/median" AND "leave as NaN") and no criteria to choose with is provided.
Also, vague solutions must be evaluated with a score of 0. For example, given "Ensure that the `status` column has consistent values (e.g., "for_sale", "sold", "pending")" is a vague solution since it does not directly suggest a practical way to solve the problem. However, if the text is vague but then some code is provided to address the same problem, the solution must be evaluated with a score of 1 (provided that it presents a precise strategy).
Please, FOCUS and pay attention on this part as it's quite important.

Keep in mind that handling non-exact duplicates means finding pairs of rows that are slightly different but share the same values for a meaningful subset of columns that acts as a unique column combination.
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a prescriptive resolution strategy for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
        ]
        super().__init__("Data Cleaning - Prescriptivity", items, prompts)