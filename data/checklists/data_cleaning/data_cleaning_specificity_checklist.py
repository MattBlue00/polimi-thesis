from data.batches import DataCleaningBatch
from data.checklists.data_cleaning.item_ids import DataCleaningItemId
from experiments.model.checklist import BaseChecklist
from experiments.model.checklist_item import DataCleaningChecklistItem
from experiments.model.prompt import EvaluationPrompt


class DataCleaningSpecificityChecklist(BaseChecklist):

    def __init__(self) -> None:
        items = [
            DataCleaningChecklistItem(
                item=DataCleaningItemId.SPECIFICITY_MISSING_VALUES_SOLUTIONS,
                batch=DataCleaningBatch.SPECIFICITY_BATCH,
                content="presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.SPECIFICITY_MISSING_VALUES_ALL_KINDS,
                batch=DataCleaningBatch.SPECIFICITY_BATCH,
                content="presence of different kinds of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.SPECIFICITY_OUTLIERS_SOLUTIONS,
                batch=DataCleaningBatch.SPECIFICITY_BATCH,
                content="presence of outliers or extreme values."
            ),
        ]
        prompts = [
            EvaluationPrompt(
                batch=DataCleaningBatch.SPECIFICITY_BATCH.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.
Keep in mind that there are only three types of missing values: '-', '' and NaN. Any other character or combination of characters must not be considered a missing value (for example, negative values are NOT to be considered missing values).
Remember that data type conversions with the parameter "errors='coerce'" handle ALL the mentioned kinds of missing values.
You will be given a text that you will have to evaluate based on the fact that some proposed solutions are specific (score of 1) or general (score of 0).

Please, from now on consider the meaning of the word SPECIFIC as it is discussed in a moment. Also, consider the meaning of the word GENERAL as the opposite of SPECIFIC.

A problem is said to be handled in a SPECIFIC way if, for all the columns for which the text proposes a solution, the solution is given individually for each column.

This means that if you have code that is similar to:
for col in [col1, col2, col3]:
    df[col] = do_something()
Then, the solution 'do_something' is GENERAL, because it is applied to a set of more than one column in the exact same way.

On the other hand, if you have code that is similar to:
df[col1] = do_something()
df[col2] = do_something()
df[col3] = do_something()
which is the case of a single solution applied indiviually to more than one column, or similar to:
df[col1] = do_something()
df[col2] = do_something_else()
df[col3] = do_something_different()
which is the case of different solutions applied individually each to a column.
Either way, the set of solutions is SPECIFIC, because the text analyzes the problem for each column. Please PAY ATTENTION to the fact that you must not care if the proposed solutions, for each column, are the same or are different. The important thing to notice is whether they are individually mentioned (SPECIFIC) or not (GENERAL) for each column.
Notice that the fact that there are different lines of code or different sentences for each column is an indicator of a SPECIFIC solution.

Notice that, if there is AT LEAST one solution to a problem that is applied to all columns, then the problem is handled in a GENERAL way. IT DOES NOT MATTER if there are other alternative/complementary solutions that are specific for each column: as long as there's even one part of a problem that is handled in a general way, then the problem is said to be handled in a general way.
Notice that if a problem is handled with for loop that involves more than one column, then the problem is handled in a GENERAL way.
Analogously, if the same solution is given in a textual form for a subset of columns, then the problem is handled in a GENERAL way, even if more subsets, each with its own solution, are defined.
For example, if the text says:
For categorical columns like col1 and col2, do something. For numerical columns like col3 and col4, do something else.
Then the problem is handled in a GENERAL way.

REMEMBER: do not reason with the meaning/accuracy of the solution. Reason only with the criteria I gave you.
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a set of solutions that are specific for the various columns of the dataset or general for every column of the dataset for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that the solutions are general (0) or specific (1). Answer with only a list of ordered, whitespace-separated numbers.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
        ]
        super().__init__("Specificity", items, prompts)