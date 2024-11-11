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
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

Keep in mind that there are only three types of missing values: '-', '' and NaN. Any other character or combination of characters must not be considered a missing value (for example, negative values are NOT to be considered missing values).

You will be given a text that should contain some solutions for some given problems. You will have to evaluate the given text based on whether the proposed solution strategies are prescriptive or not.

A PRESCRIPTIVE solution strategy is defined as a solution strategy that allows the user to clearly follow one solution path. This means that if the solution proposes two different strategies with no criteria that allow users to choose one solution over another, such a solution strategy is NOT prescriptive and must be evaluated with a score of 0. However, if a solution path lets user choose between two SIMILAR concepts, such as between "Unknown", NaN, None, or any other placeholder, or between mean and median, then the solution is still prescriptive (and must be evaluated with a score of 1) as the user is entitled to choose between the different nuances that such proposals bring with themselves.
Examples of valid criteria that allow users to choose between two alternatives within a solution are: "if data is crucial", "if a large percentage of missing values is missing", "if a few missing values are missing, "if data is sparse". In these cases, the user has the information they need to make a decision, thus the solution MUST be considered prescriptive and must be evaluated with a score of 1.
An example of criterion that would not allow users to make an informed choice between two alternatives within a solution is: "if appropriate". It is not the user's task to define appropriateness of a solution, so the solution is NOT prescriptive and must be evaluated with a score of 0.
Please, do not look for perfection and penalize the text too much: you should assign a score of 0 to proposed solutions only if they significantly violate the above rules.
Also, don't penalize the prescriptiveness of a solution for missing values just because the words "missing values" are not mentioned: if the text/code is prescriptive in telling to remove at least one kind of missing value (even if it doesn't mention the fact that it is removing missing values), then assign that solution a score of 1.

Keep also in mind you that you may evaluate a statement with a score of 1 even if it refers to a solution that handles only ONE kind of missing values: you must not care about the accuracy of the solution, because you must care about whether it is prescriptive or not.
Also, if the text mentions to fix the missing values in general (i.e. without addressing each type of missing value), the related statements have to be evaluated with a score of 1 if the proposed solution consists of a prescriptive strategy.
Keep also in mind that, if the text proposes a textual solution that you consider prescriptive but then there is a piece of code that proposes ANOTHER solution (i.e. it's not the implementation of the textual solution) to address the same problem, the statement related to that specific problem must be evaluated with a score of 0. This means that if there are lines of code that represent a solution to a problem but the textual part that comes before or after the code tell the user another different resolution strategy or possibly the one shown in the code plus a brand new one with NO criteria that help the user choose, you must evaluate the related statements with a score of 0.
Notice also that if at least one of the proposed solutions is vague and does not provide a level of detail that allows the user to actually implement that solution, you must evaluate the related statements with a score of 0.

Keep also in mind that if there are actions that are performed on the whole dataset and that address AT LEAST one kind of missing value, you must evaluate each statement (for each column) with a score of 1 provided that the presented solution is prescriptive. Examples of such table-wise actions are replacements of '-' and/or '' with NaN performed on an entire dataframe in a single line of code.
                
Keep also in mind that if a solution is provided ONLY with code and with no textual description (aside from Python comments), as well as with no other textual part in which solutions are discussed, you are sure that the related statement MUST be evaluated with a score of 1.

REMEMBER: a code-only solution makes the solution prescriptive, but a solution does not require code to be prescriptive! If the solution is text-only, make sure that it follows the prescriptive rule: it must provide the user with one, unambiguous strategy to solve the problem.

REMEMBER: if the text lets the user decide a solution among a set of solutions while giving no criteria to do so, then the statement related to that set of solutions must be evaluated with a score of 0!
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a prescriptive resolution strategy for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that the following text proposes a not prescriptive (0) or prescriptive (1) solution. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataCleaningBatch.PRESCRIPTIVITY_DIRTY_SOLUTION.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text that should contain some solutions for some given problems. You will have to evaluate the given text based on whether the proposed solution strategies are prescriptive or not.

A PRESCRIPTIVE solution strategy is defined as a solution strategy that allows the user to clearly follow one solution path. This means that if the solution proposes two different strategies with no criteria that allow users to choose one solution over another, such a solution strategy is NOT prescriptive and must be evaluated with a score of 0. However, if a solution path lets user choose between two SIMILAR concepts, such as between "Unknown", NaN, None, or any other placeholder, or between mean and median, then the solution is still prescriptive as the user is entitled to choose between the different nuances that such proposals bring with themselves.
Examples of valid criteria that allow users to choose between two alternatives within a solution are: "if data is crucial", "if a large percentage is missing". In this case, the user has the information they need to make a decision, thus the solution MUST be considered prescriptive.
An example of criterion that would not allow users to make an informed choice between two alternatives within a solution is: "if appropriate". It is not the user's task to define appropriateness of a solution, so the solution is NOT prescriptive.
Please, do not look for perfection and penalize the text too much: you should assign a score of 0 to proposed solutions only if they significantly violate the above rules.

Keep also in mind that, if the text proposes a textual solution that you consider prescriptive but then there is a piece of code that proposes ANOTHER solution (i.e. it's not the implementation of the textual solution) to address the same problem, the statement related to that specific problem must be evaluated with a score of 0. This means that if there are lines of code that represent a solution to a problem but the textual part that comes before or after the code tell the user another different resolution strategy or possibly the one shown in the code plus a brand new one with NO criteria that help the user choose, you must evaluate the related statements with a score of 0.
Notice also that if at least one of the proposed solutions is vague and does not provide a level of detail that allows the user to actually implement that solution, you must evaluate the related statements with a score of 0.
                
Keep also in mind that if a solution is provided ONLY with code and with no textual description (aside from Python comments), as well as with no other textual part in which solutions are discussed, you are sure that the related statement MUST be evaluated with a score of 1.

Keep in mind that handling non-exact duplicates means finding pairs of rows that are slightly different but share the same values for a meaningful subset of columns that acts as a unique column combination.

REMEMBER: a code-only solution makes the solution prescriptive, but a solution does not require code to be prescriptive! If the solution is text-only, make sure that it follows the prescriptive rule: it must provide the user with one, unambiguous strategy to solve the problem.

REMEMBER: if the text lets the user decide a solution among a set of solutions while giving no criteria to do so, then the statement related to that set of solutions must be evaluated with a score of 0!
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a prescriptive resolution strategy for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that the following text proposes a not prescriptive (0) or prescriptive (1) solution. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
        ]
        super().__init__("Prescriptivity", items, prompts)