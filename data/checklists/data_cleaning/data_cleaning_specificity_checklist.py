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

A set of solutions is said to be SPECIFIC if and only if, for the same kind of problem that is present for n columns, ALL n columns are given a different solution, tailored for the needs of that specific column. Otherwise, i.e. in the case at least two columns are being handled, for the same problem, with the same solution, the solutions for a given kind of problem are said to be GENERAL.
Notice that if the solution for a problem is split into multiple parts, they ALL need to be specific for the set of solutions to be considered specific. This means that, for example, if there's a line of code that handles a certain type of missing value for all the columns and then all the columns' other missing values are handled specifically, the set of solutions must still be considered GENERAL.
Keep also in mind that, typically, for loops that encompass different columns are clear signals of GENERAL solutions.               """,
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
        super().__init__("Data Cleaning - Specificity", items, prompts)