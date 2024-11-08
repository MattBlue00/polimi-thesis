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
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.
Keep in mind that there are only three types of missing values: '-', '' and NaN. Any other character or combination of characters must not be considered a missing value (for example, negative values are NOT to be considered missing values).

A solution is said to be GENERAL if and only if the SAME solution for a problem that is present for n columns is given to ALL n columns. Otherwise, i.e. in the case at least two different solutions are provided for the same kind of problem that is present for more than one column, the solutions are said to be SPECIFIC.

Keep also in mind that applying the same solution to a subset of columns (e.g. thanks to a for loop) counts as a specific solution, and not as a general one, only if not all the columns that have the problem that is being solved are targeted. For example, if there are outliers in 4 columns and the for loop targets only 3, and the remaining has a different solution, the solutions are to be considered specific.
                """,
                user_message=
                """
Consider if the piece of text I will give you provides a solution that is specific for the various columns of the dataset or general for every column of the dataset for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that the solutions are general (0) or specific (1). Answer with only a list of ordered, whitespace-separated numbers.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
        ]
        super().__init__("Data Cleaning - Specificity", items, prompts)