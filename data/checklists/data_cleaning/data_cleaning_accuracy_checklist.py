from data.batches import DataCleaningBatch
from data.checklists.data_cleaning.item_ids import DataCleaningItemId
from experiments.model.checklist import BaseChecklist
from experiments.model.checklist_item import DataCleaningChecklistItem
from experiments.model.prompt import EvaluationPrompt

class DataCleaningAccuracyChecklist(BaseChecklist):

    def __init__(self) -> None:
        items = [
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_SOLUTION_BROKERED_BY,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_SOLUTION,
                content="'brokered_by' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_SOLUTION_STATUS,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_SOLUTION,
                content="'status' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_SOLUTION_PRICE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_SOLUTION,
                content="'price' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_SOLUTION_BED,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_SOLUTION,
                content="'bed' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_SOLUTION_BATH,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_SOLUTION,
                content="'bath' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_SOLUTION_ACRE_LOT,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_SOLUTION,
                content="'acre_lot' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_SOLUTION_STREET,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_SOLUTION,
                content="'street' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_SOLUTION_CITY,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_SOLUTION,
                content="'city' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_SOLUTION_STATE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_SOLUTION,
                content="'state' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_SOLUTION_ZIP_CODE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_SOLUTION,
                content="'zip_code' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_SOLUTION_HOUSE_SIZE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_SOLUTION,
                content="'house_size' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_SOLUTION_PREV_SOLD_DATE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_SOLUTION,
                content="'prev_sold_date' column: presence of missing values."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_SOLUTION_BROKERED_BY,
                batch=DataCleaningBatch.ACCURACY_DIRTY_SOLUTION,
                content="'brokered_by' column: presence of full names in a list of numerical IDs."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_SOLUTION_STATUS,
                batch=DataCleaningBatch.ACCURACY_DIRTY_SOLUTION,
                content="'status' column: presence of format inconsistencies ('s' stands for 'sold', 'f' stands for 'for_sale')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_SOLUTION_PRICE,
                batch=DataCleaningBatch.ACCURACY_DIRTY_SOLUTION,
                content="'price' column: presence of format inconsistencies (the presence of '$' in a numerical column)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_SOLUTION_BED,
                batch=DataCleaningBatch.ACCURACY_DIRTY_SOLUTION,
                content="'bed' column: presence of outliers/placeholders (specifically, '9999')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_SOLUTION_BATH,
                batch=DataCleaningBatch.ACCURACY_DIRTY_SOLUTION,
                content="'bath' column: presence of data errors (specifically, '0')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_SOLUTION_ACRE_LOT,
                batch=DataCleaningBatch.ACCURACY_DIRTY_SOLUTION,
                content="'acre_lot' column: the presence of negative values (which need to be replaced)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_SOLUTION_STREET,
                batch=DataCleaningBatch.ACCURACY_DIRTY_SOLUTION,
                content="'street' column: presence of format inconsistencies (e.g. 'Boulevard' instead of 'Blvd')."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_SOLUTION_CITY,
                batch=DataCleaningBatch.ACCURACY_DIRTY_SOLUTION,
                content="'city' column: presence of data errors (European cities in a USA dataset)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_SOLUTION_STATE,
                batch=DataCleaningBatch.ACCURACY_DIRTY_SOLUTION,
                content="'state' column: presence of format inconsistencies (some states are abbreviated)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_SOLUTION_ZIP_CODE,
                batch=DataCleaningBatch.ACCURACY_DIRTY_SOLUTION,
                content="'zip_code' column: presence of data errors (some zip codes are partial)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_SOLUTION_HOUSE_SIZE,
                batch=DataCleaningBatch.ACCURACY_DIRTY_SOLUTION,
                content="'house_size' column: presence of values in a different unit of measure (some values are in square miles, while the majority is in square feet)."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_SOLUTION_PREV_SOLD_DATE,
                batch=DataCleaningBatch.ACCURACY_DIRTY_SOLUTION,
                content="'prev_sold_date' column: presence of different date formats."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_SOLUTION_NON_EXACT_DUPLICATES,
                batch=DataCleaningBatch.ACCURACY_DIRTY_SOLUTION,
                content="presence of non-exact duplicate rows."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_ALL_KINDS_BROKERED_BY,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_ALL_KINDS,
                content="'brokered_by' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_ALL_KINDS_STATUS,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_ALL_KINDS,
                content="'status' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_ALL_KINDS_PRICE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_ALL_KINDS,
                content="'price' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_ALL_KINDS_BED,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_ALL_KINDS,
                content="'bed' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_ALL_KINDS_BATH,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_ALL_KINDS,
                content="'bath' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_ALL_KINDS_ACRE_LOT,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_ALL_KINDS,
                content="'acre_lot' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_ALL_KINDS_STREET,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_ALL_KINDS,
                content="'street' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_ALL_KINDS_CITY,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_ALL_KINDS,
                content="'city' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_ALL_KINDS_STATE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_ALL_KINDS,
                content="'state' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_ALL_KINDS_ZIP_CODE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_ALL_KINDS,
                content="'zip_code' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_ALL_KINDS_HOUSE_SIZE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_ALL_KINDS,
                content="'house_size' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_ALL_KINDS_PREV_SOLD_DATE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_ALL_KINDS,
                content="'prev_sold_date' column."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_OPTIMAL_BROKERED_BY,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_OPTIMAL,
                content="'brokered_by' column. The list of solutions is: “Replace the missing values with 'Unknown'\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_OPTIMAL_STATUS,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_OPTIMAL,
                content="'status' column. The list of solutions is: \"Replace the missing values with 'Unknown'\", \"Missing values could potentially be filled using discovered dependencies\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_OPTIMAL_PRICE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_OPTIMAL,
                content="'price' column. The list of solutions is: \"Use external APIs to estimate the price\", \"Use the mean/median to estimate the price\", \"Replace missing values with NaN\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_OPTIMAL_BED,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_OPTIMAL,
                content="'bed' column. The list of solutions is: \"Impute missing values using the number of bathrooms and house size\", \"Fill using the mean/median/mode\", \"Replace with NaN\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_OPTIMAL_BATH,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_OPTIMAL,
                content="'bath' column. The list of solutions is: \"Impute missing values using the number of bedrooms and house size\", \"Fill using the mean/median/mode\", \"Replace with NaN\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_OPTIMAL_ACRE_LOT,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_OPTIMAL,
                content="'acre_lot' column. The list of solutions is: \"Replace missing values with the mean/median/mode\", \"Replace with NaN\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_OPTIMAL_STREET,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_OPTIMAL,
                content="'street' column. The list of solutions is: \"Replace missing values with 'Unknown'\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_OPTIMAL_CITY,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_OPTIMAL,
                content="'city' column. The list of solutions is: \"Infer the correct city from the zip code. If no zip code is available, replace with 'Unknown'\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_OPTIMAL_STATE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_OPTIMAL,
                content="'state' column. The list of solutions is: \"Infer the correct city from the zip code. If no zip code is available, replace with 'Unknown'\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_OPTIMAL_ZIP_CODE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_OPTIMAL,
                content="'zip_code' column. The list of solutions is: \"Infer the correct zip code from the city/state. If no city or state is available, replace with 'Unknown'\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_OPTIMAL_HOUSE_SIZE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_OPTIMAL,
                content="'house_size' column. The list of solutions is: \"Impute missing values from the number of bedrooms, bathrooms, and price\", \"Replace with NaN\", \"Fill with mean/median/mode\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_MISSING_VALUES_OPTIMAL_PREV_SOLD_DATE,
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_OPTIMAL,
                content="'prev_sold_date' column. The list of solutions is: \"Fill using the mode\", \"Use bfill/ffill methods\", \"Fill replacing with 'Unknown'/NaN/NaT\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_OPTIMAL_BROKERED_BY,
                batch=DataCleaningBatch.ACCURACY_DIRTY_OPTIMAL,
                content="'brokered_by' column: the presence of full names in a list of numerical IDs. The list of solutions is: \"Replace full names with NaN values\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_OPTIMAL_STATUS,
                batch=DataCleaningBatch.ACCURACY_DIRTY_OPTIMAL,
                content="'status' column: the presence of format inconsistencies ('s' stands for 'sold', 'f' stands for 'for_sale'). The list of solutions is: \"Replace 's' and 'f' values with 'sold' and 'for_sale' respectively. Other categorical values that are not semantically equivalent to 'sold' and 'for_sale' must not be accepted. Adding other categorical values must not be accepted as well\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_OPTIMAL_PRICE,
                batch=DataCleaningBatch.ACCURACY_DIRTY_OPTIMAL,
                content="'price' column: the presence of format inconsistencies (the presence of '$' in a numerical column). The list of solutions is: \"Drop the '$'\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_OPTIMAL_BED,
                batch=DataCleaningBatch.ACCURACY_DIRTY_OPTIMAL,
                content="'bed' column: the presence of outliers/placeholders (specifically, '9999'). The list of solutions is: \"Replace '9999' using the number of bathrooms and house size\", \"Replace '9999' using the mean/median/mode\", \"Replace '9999' with NaN\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_OPTIMAL_BATH,
                batch=DataCleaningBatch.ACCURACY_DIRTY_OPTIMAL,
                content="'bath' column: the presence of data errors (specifically, '0'). The list of solutions is: \"Replace '0' using the number of bedrooms and house size\", \"Replace '0' using the mean/mode/median\", \"Replace '0' with NaN\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_OPTIMAL_ACRE_LOT,
                batch=DataCleaningBatch.ACCURACY_DIRTY_OPTIMAL,
                content="'acre_lot' column: the presence of negative values (which need to be replaced). The list of solutions is: \"Replace negative values with the mean/mode/median value\", \"Replace negative values with NaN\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_OPTIMAL_STREET,
                batch=DataCleaningBatch.ACCURACY_DIRTY_OPTIMAL,
                content="'street' column: the presence of format inconsistencies (e.g. 'Boulevard' instead of 'Blvd'). The list of solutions is: \"Standardize addresses by replacing expanded forms (e.g., Street, Boulevard) with abbreviations (e.g., St, Blvd)\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_OPTIMAL_CITY,
                batch=DataCleaningBatch.ACCURACY_DIRTY_OPTIMAL,
                content="'city' column: the presence of data errors (European cities in a USA dataset). The list of solutions is: \"Infer the correct city from the zip code. If no zip code is available, replace with 'Unknown'\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_OPTIMAL_STATE,
                batch=DataCleaningBatch.ACCURACY_DIRTY_OPTIMAL,
                content="'state' column: the presence of format inconsistencies (some states are abbreviated). The list of solutions is: \"Expand the abbreviated states with the corresponding full names\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_OPTIMAL_ZIP_CODE,
                batch=DataCleaningBatch.ACCURACY_DIRTY_OPTIMAL,
                content="'zip_code' column: the presence of data errors (some zip codes are partial). The list of solutions is: \"Infer the correct zip code from the city or state. If no city or state is available, replace with 'Unknown'\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_OPTIMAL_HOUSE_SIZE,
                batch=DataCleaningBatch.ACCURACY_DIRTY_OPTIMAL,
                content="'house_size' column: the presence of extremely small values (some values are in a different unit of measurement). The list of solutions is: \"Convert the extremely small values from square miles to square feet\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_DIRTY_OPTIMAL_PREV_SOLD_DATE,
                batch=DataCleaningBatch.ACCURACY_DIRTY_OPTIMAL,
                content="'prev_sold_date' column: the presence of different date formats. The list of solutions is: \"Standardize all dates to a common format\", \"Convert all dates to a datetime type\"."
            ),
            DataCleaningChecklistItem(
                item=DataCleaningItemId.ACCURACY_OPTIMAL_NON_EXACT_DUPLICATES,
                batch=DataCleaningBatch.ACCURACY_DIRTY_OPTIMAL,
                content="the presence of non-exact duplicate rows. The list of solutions is: \"Merge the duplicates\"."
            ),
        ]
        prompts = [
            EvaluationPrompt(
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_SOLUTION.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.
Keep in mind that there are only three types of missing values: '-', '' and NaN. Any other character or combination of characters must not be considered a missing value (for example, negative values are NOT to be considered missing values).

A solution is valid if it addresses and solves a given problem. Notice that the fact that a solution is not explicitly mentioned but is implicit in some actions does not affect the fact that it is valid.
Dropping rows or columns must not be considered a valid solution to the problem of missing values, unless you cannot think of at least one other alternative that does not involve dropping rows or columns. However, if the text suggests to drop rows or columns ONLY in particular settings and offers another alternative, you must consider the solution as valid.
Keep in mind that you should not care about the fact that a specific column is mentioned or not while handling missing values: you may consider a fact as true as long as there is some piece of text that implicitly, but correctly, takes care about them, and you may consider a fact as true even if only one kind of missing value is handled correctly.
Keep also in mind that if there are actions that are computed on the whole dataset and that address at least one kind of missing value correctly, you must evaluate each statement with a score of 1. Examples of such table-wise actions are replacements of '-' and/or '' with NaN performed on an entire dataframe in a single line of code.
                """,
                user_message=
                """
Consider if the piece of text provides a VALID solution for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataCleaningBatch.ACCURACY_DIRTY_SOLUTION.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

Keep in mind that handling non-exact duplicates means finding pairs of rows that are slightly different but share the same values for a meaningful subset of columns that acts as a unique column combination.
Keep also in mind that you should not care about the fact that a specific column is mentioned or not: you may consider a fact as true as long as there is some piece of text that correctly takes care about it.

The user will ask you to evaluate the validity of some solutions in a piece of text that should address a user-given list of problems in the form of statements. A solution is valid if it effectively addresses and solves the specific problem that is described in each statement, regardless of the fact that the problem is implicitly or explicitly solved. A solution that provides code that is syntactically correct and does not raise any errors must NOT be considered as valid if it does NOT solve the problem it has to address. Hence, you must pay particular attention to what each line of code does and reason on whether the specific problem is actually solved or not.
Keep in mind that if a valid solution is provided for multiple columns without explicitly mentioning the column-specific problems that such solution is solving, the solution must be considered as valid for all the involved columns. For example, if the text provides a single solution that is valid for the problems of three columns and mentions those three columns without mentioning all the specific problems, the solution must be considered valid for all the three columns. 

Keep also in mind that for the 'acre_lot' and 'house_size' columns it's not enough to individually replace all the dirty values with something else. Such a solution must not be considered as valid. Instead, a valid solution would be crafting an approach that is able to handle the wrong values without mentioning them.

Keep also in mind that, for categorical columns, solutions that are different from the ones that will be provided but are semantically equivalent must be accepted.
                """,
                user_message=
                """
Consider if the piece of text provides a VALID solution for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_ALL_KINDS.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.
Keep in mind that there are only three types of missing values: '-', '' and NaN. Any other character or combination of characters must not be considered a missing value (for example, negative values are NOT to be considered missing values).

Keep also in mind that if there are actions that are computed on the whole dataset and that address each one of the three types of missing values, you must evaluate each statement with a score of 1. Examples of such table-wise actions are replacements of '-' and/or '' with NaN performed on an entire dataframe in a single line of code.

Keep also in mind that if there are actions that convert the data type of a column with functions that explicitly mention the \"errors='coerce'\" parameter (e.g. to_numeric, to_datetime, etc. and NOT astype), then all the types of missing values are handled for that specific column.
                """,
                user_message=
                """
Consider if the piece of text provides a solution that encompasses all the three types of missing values for the following columns:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataCleaningBatch.ACCURACY_MISSING_VALUES_OPTIMAL.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

Keep in mind that there are only three types of missing values: '-', '' and NaN. Any other character or combination of characters must not be considered a missing value (for example, negative values are NOT to be considered missing values).

Keep also in mind that if there are actions that are performed on the whole dataset and that address at least one of the three types of missing values, you must evaluate each statement for which such a table-wise action can be considered among the list of solutions that will be provided with a score of 1. Examples of such table-wise actions are replacements of '-' and/or '' with NaN performed on an entire dataframe in a single line of code. 
Keep also in mind that if there are actions that convert the data type of a column with functions that EXPLICITLY mention the "errors='coerce'" parameter (e.g. to_numeric, to_datetime, etc. and NOT astype), then all the types of missing values are handled for that specific column. Hence, you must consider if that solution among the candidate solutions that will be provided for that column.

Keep also in mind that solutions that are different from the ones that will be provided but are semantically equivalent must be accepted, as long as the different solution encompasses ALL the aspects of the other solution. For example, if one of the candidate solutions states "Infer the correct state from the zip code. If no zip code is available, replace with 'Unknown'" and the text you are evaluating says \"Fill missing states with 'Unknown'\", the solution provided by the text is only partially equivalent and thus must not be considered equivalent.
                """,
                user_message=
                """
Consider if the piece of text provides at least one of the following solutions for the problem of the presence of missing values for the:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataCleaningBatch.ACCURACY_DIRTY_OPTIMAL.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

Keep in mind that handling non-exact duplicates means finding pairs of rows that are slightly different but share the same values for a meaningful subset of columns that acts as a unique column combination. Notice that removing duplicates is NOT equivalent to merging duplicates, as the latter involves combining the two non-exact duplicates into a new, reconciled row.
Keep also in mind that you should not care about the fact that a specific column is mentioned or not: you may consider a fact as true as long as there is some piece of text that correctly takes care about it.

Keep also in mind that solutions that are different from the ones that will be provided but are semantically equivalent must be accepted, as long as the different solution encompasses ALL the aspects of the other solution.

Keep also in mind that NaN and None are equivalent and acceptable as long as the text makes a consistent use of them, i.e. chooses one and only one of them.

Keep also in mind that if a solution replaces some values because they are not in a specific range, and the values to fix (placeholders, data errors, outliers, etc) lie out of range, they will be replaced even if not explicitly mentioned and the solution must be considered as a valid solution. 
                """,
                user_message=
                """
Consider if the piece of text provides at least one of the following solutions for the following problems:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            )
        ]
        super().__init__("Data Cleaning - Accuracy", items, prompts)