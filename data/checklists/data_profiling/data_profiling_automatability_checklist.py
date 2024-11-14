from data.batches import DataProfilingBatch
from data.checklists.data_profiling.item_ids import DataProfilingItemId
from experiments.model.checklist import BaseChecklist
from experiments.model.checklist_item import DataProfilingChecklistItem
from experiments.model.prompt import EvaluationPrompt


class DataProfilingAutomatabilityChecklist(BaseChecklist):

    def __init__(self) -> None:
        items = [
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_GENERAL_COLUMNS,
                batch=DataProfilingBatch.AUTOMATABILITY_GENERAL,
                content="columns number."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_GENERAL_ROWS,
                batch=DataProfilingBatch.AUTOMATABILITY_GENERAL,
                content="rows number."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_GENERAL_MISSING_VALUES,
                batch=DataProfilingBatch.AUTOMATABILITY_GENERAL,
                content="total missing values number."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_GENERAL_DUPLICATES,
                batch=DataProfilingBatch.AUTOMATABILITY_GENERAL,
                content="exact duplicate rows number."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_GENERAL_DEPENDENCIES,
                batch=DataProfilingBatch.AUTOMATABILITY_GENERAL,
                content="inter-columns dependencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_MISSING_VALUES_BROKERED_BY,
                batch=DataProfilingBatch.AUTOMATABILITY_MISSING_VALUES,
                content="'brokered_by' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_MISSING_VALUES_STATUS,
                batch=DataProfilingBatch.AUTOMATABILITY_MISSING_VALUES,
                content="'status' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_MISSING_VALUES_PRICE,
                batch=DataProfilingBatch.AUTOMATABILITY_MISSING_VALUES,
                content="'price' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_MISSING_VALUES_BED,
                batch=DataProfilingBatch.AUTOMATABILITY_MISSING_VALUES,
                content="'bed' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_MISSING_VALUES_BATH,
                batch=DataProfilingBatch.AUTOMATABILITY_MISSING_VALUES,
                content="'bath' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_MISSING_VALUES_ACRE_LOT,
                batch=DataProfilingBatch.AUTOMATABILITY_MISSING_VALUES,
                content="'acre_lot' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_MISSING_VALUES_STREET,
                batch=DataProfilingBatch.AUTOMATABILITY_MISSING_VALUES,
                content="'street' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_MISSING_VALUES_CITY,
                batch=DataProfilingBatch.AUTOMATABILITY_MISSING_VALUES,
                content="'city' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_MISSING_VALUES_STATE,
                batch=DataProfilingBatch.AUTOMATABILITY_MISSING_VALUES,
                content="'state' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_MISSING_VALUES_ZIP_CODE,
                batch=DataProfilingBatch.AUTOMATABILITY_MISSING_VALUES,
                content="'zip_code' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_MISSING_VALUES_HOUSE_SIZE,
                batch=DataProfilingBatch.AUTOMATABILITY_MISSING_VALUES,
                content="'house_size' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_MISSING_VALUES_PREV_SOLD_DATE,
                batch=DataProfilingBatch.AUTOMATABILITY_MISSING_VALUES,
                content="'prev_sold_date' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DISTINCT_VALUES_BROKERED_BY,
                batch=DataProfilingBatch.AUTOMATABILITY_DISTINCT_VALUES,
                content="'brokered_by' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DISTINCT_VALUES_STATUS,
                batch=DataProfilingBatch.AUTOMATABILITY_DISTINCT_VALUES,
                content="'status' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DISTINCT_VALUES_PRICE,
                batch=DataProfilingBatch.AUTOMATABILITY_DISTINCT_VALUES,
                content="'price' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DISTINCT_VALUES_BED,
                batch=DataProfilingBatch.AUTOMATABILITY_DISTINCT_VALUES,
                content="'bed' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DISTINCT_VALUES_BATH,
                batch=DataProfilingBatch.AUTOMATABILITY_DISTINCT_VALUES,
                content="'bath' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DISTINCT_VALUES_ACRE_LOT,
                batch=DataProfilingBatch.AUTOMATABILITY_DISTINCT_VALUES,
                content="'acre_lot' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DISTINCT_VALUES_STREET,
                batch=DataProfilingBatch.AUTOMATABILITY_DISTINCT_VALUES,
                content="'street' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DISTINCT_VALUES_CITY,
                batch=DataProfilingBatch.AUTOMATABILITY_DISTINCT_VALUES,
                content="'city' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DISTINCT_VALUES_STATE,
                batch=DataProfilingBatch.AUTOMATABILITY_DISTINCT_VALUES,
                content="'state' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DISTINCT_VALUES_ZIP_CODE,
                batch=DataProfilingBatch.AUTOMATABILITY_DISTINCT_VALUES,
                content="'zip_code' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DISTINCT_VALUES_HOUSE_SIZE,
                batch=DataProfilingBatch.AUTOMATABILITY_DISTINCT_VALUES,
                content="'house_size' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DISTINCT_VALUES_PREV_SOLD_DATE,
                batch=DataProfilingBatch.AUTOMATABILITY_DISTINCT_VALUES,
                content="'prev_sold_date' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DATA_TYPES_BROKERED_BY,
                batch=DataProfilingBatch.AUTOMATABILITY_DATA_TYPES,
                content="'brokered_by' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DATA_TYPES_STATUS,
                batch=DataProfilingBatch.AUTOMATABILITY_DATA_TYPES,
                content="'status' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DATA_TYPES_PRICE,
                batch=DataProfilingBatch.AUTOMATABILITY_DATA_TYPES,
                content="'price' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DATA_TYPES_BED,
                batch=DataProfilingBatch.AUTOMATABILITY_DATA_TYPES,
                content="'bed' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DATA_TYPES_BATH,
                batch=DataProfilingBatch.AUTOMATABILITY_DATA_TYPES,
                content="'bath' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DATA_TYPES_ACRE_LOT,
                batch=DataProfilingBatch.AUTOMATABILITY_DATA_TYPES,
                content="'acre_lot' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DATA_TYPES_STREET,
                batch=DataProfilingBatch.AUTOMATABILITY_DATA_TYPES,
                content="'street' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DATA_TYPES_CITY,
                batch=DataProfilingBatch.AUTOMATABILITY_DATA_TYPES,
                content="'city' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DATA_TYPES_STATE,
                batch=DataProfilingBatch.AUTOMATABILITY_DATA_TYPES,
                content="'state' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DATA_TYPES_ZIP_CODE,
                batch=DataProfilingBatch.AUTOMATABILITY_DATA_TYPES,
                content="'zip_code' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DATA_TYPES_HOUSE_SIZE,
                batch=DataProfilingBatch.AUTOMATABILITY_DATA_TYPES,
                content="'house_size' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_DATA_TYPES_PREV_SOLD_DATE,
                batch=DataProfilingBatch.AUTOMATABILITY_DATA_TYPES,
                content="'prev_sold_date' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_PRICE_MIN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'price' column: minimum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_PRICE_MIN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'price' column: maximum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_PRICE_MEAN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'price' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_PRICE_MEDIAN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'price' column: median value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_BED_MIN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'bed' column: minimum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_BED_MAX,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'bed' column: maximum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_BED_MEAN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'bed' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_BED_MEDIAN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'bed' column: median value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_BATH_MIN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'bath' column: minimum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_BATH_MAX,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'bath' column: maximum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_BATH_MEAN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'bath' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_BATH_MEDIAN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'bath' column: median value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_ACRE_LOT_MIN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'acre_lot' column: minimum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_ACRE_LOT_MAX,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'acre_lot' column: maximum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_ACRE_LOT_MEAN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'acre_lot' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_ACRE_LOT_MEDIAN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'acre_lot' column: median value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MIN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'house_size' column: minimum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MAX,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'house_size' column: maximum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MEAN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'house_size' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MEDIAN,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY,
                content="'house_size' column: median value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_PRICE_QUARTILES,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'price' column: quartiles or percentiles."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_PRICE_STD_DEV,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'price' column: standard deviation or variance."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_PRICE_PLOT,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'price' column: distribution plots."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_BED_QUARTILES,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'bed' column: quartiles or percentiles."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_BED_STD_DEV,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'bed' column: standard deviation or variance."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_BED_PLOT,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'bed' column: distribution plots."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_BATH_QUARTILES,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'bath' column: quartiles or percentiles."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_BATH_STD_DEV,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'bath' column: standard deviation or variance."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_BATH_PLOT,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'bath' column: distribution plots."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_ACRE_LOT_QUARTILES,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'acre_lot' column: quartiles or percentiles."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_ACRE_LOT_STD_DEV,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'acre_lot' column: standard deviation or variance."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_ACRE_LOT_PLOT,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'acre_lot' column: distribution plots."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_QUARTILES,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'house_size' column: quartiles or percentiles."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_STD_DEV,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'house_size' column: standard deviation or variance."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_PLOT,
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD,
                content="'house_size' column: distribution plots."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_FREQUENCIES_BROKERED_BY,
                batch=DataProfilingBatch.AUTOMATABILITY_FREQUENCIES,
                content="'brokered_by' column."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_FREQUENCIES_STATUS,
                batch=DataProfilingBatch.AUTOMATABILITY_FREQUENCIES,
                content="'status' column."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_FREQUENCIES_STREET,
                batch=DataProfilingBatch.AUTOMATABILITY_FREQUENCIES,
                content="'street' column."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_FREQUENCIES_CITY,
                batch=DataProfilingBatch.AUTOMATABILITY_FREQUENCIES,
                content="'city' column."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_FREQUENCIES_STATE,
                batch=DataProfilingBatch.AUTOMATABILITY_FREQUENCIES,
                content="'state' column."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_FREQUENCIES_ZIP_CODE,
                batch=DataProfilingBatch.AUTOMATABILITY_FREQUENCIES,
                content="'zip_code' column."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.AUTOMATABILITY_FREQUENCIES_PREV_SOLD_DATE,
                batch=DataProfilingBatch.AUTOMATABILITY_FREQUENCIES,
                content="'prev_sold_date' column."
            ),
        ]
        prompts = [
            EvaluationPrompt(
                batch=DataProfilingBatch.AUTOMATABILITY_GENERAL.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are handled only with a natural language description (score of 0) or also with code or an explicit datum that directly corresponds with the desired information (score of 1) - regardless of the fact that the textual description, the code or the datum are accurate or not.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts with a textual description or with code or an explicit datum::
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are mentioned with only a natural language description (0) or with code or an explicit datum that addresses the facts (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.AUTOMATABILITY_MISSING_VALUES.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are handled only with a natural language description (score of 0) or also with code or an explicit datum that directly corresponds with the desired information (score of 1) - regardless of the fact that the textual description, the code or the datum are accurate or not.

Keep also in mind that it is not necessary to explicitly mention a column in order to consider it: for example, if the text suggests to calculate the missing values for every column without explicitly mentioning each one of them, then you must consider the way in which the missing values are generally handled for your evaluation for each statement.
However, if the text does not handle missing values in a general way, you need to have an explicit mention of missing values for a column in order to consider it. This means that just mentioning that a column has "-", "" or NaN values is not enough to say that it handles missing values, as the text needs to explicitly recognize them as missing values.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts with a textual description or with code or an explicit datum::
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are mentioned with only a natural language description (0) or with code or an explicit datum that addresses the facts (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.AUTOMATABILITY_DISTINCT_VALUES.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are handled only with a natural language description (score of 0) or also with code or an explicit datum that directly corresponds with the desired information (score of 1) - regardless of the fact that the textual description, the code or the datum are accurate or not.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts with a textual description or with code or an explicit datum::
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are mentioned with only a natural language description (0) or with code or an explicit datum that addresses the facts (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.AUTOMATABILITY_DATA_TYPES.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are handled only with a natural language description (score of 0) or also with code or an explicit datum that directly corresponds with the desired information (score of 1) - regardless of the fact that the textual description, the code or the datum are accurate or not.

Remember that data types can be found in the "explicit datum" form as single-word strings that clearly represent a data type, such as "object", "numeric", "float", "text", and more.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts with a textual description or with code or an explicit datum::
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are mentioned with only a natural language description (0) or with code or an explicit datum that addresses the facts (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_EASY.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are handled only with a natural language description (score of 0) or also with code or an explicit datum that directly corresponds with the desired information (score of 1) - regardless of the fact that the textual description, the code or the datum are accurate or not.

Keep also in mind that calculating the range of values for a specific (numeric) column is equivalent to calculating the minimum and maximum values for that column.

Pay attention to the fact that you must accept ranges that go from the *actual* minimum to the *actual* maximum: it does not matter if these values are not actually calculated or specified, but you cannot accept ranges that encompass only a subset of values, such as the most common values.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts with a textual description or with code or an explicit datum::
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are mentioned with only a natural language description (0) or with code or an explicit datum that addresses the facts (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.AUTOMATABILITY_VALUE_DISTRIBUTIONS_HARD.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are handled only with a natural language description (score of 0) or also with code or an explicit datum that directly corresponds with the desired information (score of 1) - regardless of the fact that the textual description, the code or the datum are accurate or not.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts with a textual description or with code or an explicit datum::
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are mentioned with only a natural language description (0) or with code or an explicit datum that addresses the facts (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.AUTOMATABILITY_FREQUENCIES.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are handled only with a natural language description (score of 0) or also with code or an explicit datum that directly corresponds with the desired information (score of 1) - regardless of the fact that the textual description, the code or the datum are accurate or not.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions the frequencies of these columns with a textual description or with code or an explicit datum::
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that the frequencies are mentioned with only a natural language description (0) or with code or an explicit datum that addresses the facts (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
        ]
        super().__init__("Automatability", items, prompts)