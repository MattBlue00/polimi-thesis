from data.batches import DataProfilingBatch
from data.checklists.data_profiling.item_ids import DataProfilingItemId
from experiments.model.checklist import BaseChecklist
from experiments.model.checklist_item import DataProfilingChecklistItem
from experiments.model.prompt import EvaluationPrompt

class DataProfilingCompletenessChecklist(BaseChecklist):

    def __init__(self) -> None:
        items = [
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_GENERAL_DATASET_DESCRIPTION,
                batch=DataProfilingBatch.COMPLETENESS_GENERAL,
                content="general dataset description."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_GENERAL_COLUMNS,
                batch=DataProfilingBatch.COMPLETENESS_GENERAL,
                content="columns number."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_GENERAL_ROWS,
                batch=DataProfilingBatch.COMPLETENESS_GENERAL,
                content="rows number."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_GENERAL_MISSING_VALUES,
                batch=DataProfilingBatch.COMPLETENESS_GENERAL,
                content="total missing values number."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_GENERAL_DUPLICATES,
                batch=DataProfilingBatch.COMPLETENESS_GENERAL,
                content="exact duplicate rows number."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_GENERAL_DEPENDENCIES,
                batch=DataProfilingBatch.COMPLETENESS_GENERAL,
                content="inter-columns dependencies."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_MISSING_VALUES_BROKERED_BY,
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES,
                content="'brokered_by' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_MISSING_VALUES_STATUS,
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES,
                content="'status' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_MISSING_VALUES_PRICE,
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES,
                content="'price' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_MISSING_VALUES_BED,
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES,
                content="'bed' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_MISSING_VALUES_BATH,
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES,
                content="'bath' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_MISSING_VALUES_ACRE_LOT,
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES,
                content="'acre_lot' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_MISSING_VALUES_STREET,
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES,
                content="'street' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_MISSING_VALUES_CITY,
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES,
                content="'city' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_MISSING_VALUES_STATE,
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES,
                content="'state' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_MISSING_VALUES_ZIP_CODE,
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES,
                content="'zip_code' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_MISSING_VALUES_HOUSE_SIZE,
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES,
                content="'house_size' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_MISSING_VALUES_PREV_SOLD_DATE,
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES,
                content="'prev_sold_date' column: missing values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DISTINCT_VALUES_BROKERED_BY,
                batch=DataProfilingBatch.COMPLETENESS_DISTINCT_VALUES,
                content="'brokered_by' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DISTINCT_VALUES_STATUS,
                batch=DataProfilingBatch.COMPLETENESS_DISTINCT_VALUES,
                content="'status' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DISTINCT_VALUES_PRICE,
                batch=DataProfilingBatch.COMPLETENESS_DISTINCT_VALUES,
                content="'price' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DISTINCT_VALUES_BED,
                batch=DataProfilingBatch.COMPLETENESS_DISTINCT_VALUES,
                content="'bed' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DISTINCT_VALUES_BATH,
                batch=DataProfilingBatch.COMPLETENESS_DISTINCT_VALUES,
                content="'bath' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DISTINCT_VALUES_ACRE_LOT,
                batch=DataProfilingBatch.COMPLETENESS_DISTINCT_VALUES,
                content="'acre_lot' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DISTINCT_VALUES_STREET,
                batch=DataProfilingBatch.COMPLETENESS_DISTINCT_VALUES,
                content="'street' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DISTINCT_VALUES_CITY,
                batch=DataProfilingBatch.COMPLETENESS_DISTINCT_VALUES,
                content="'city' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DISTINCT_VALUES_STATE,
                batch=DataProfilingBatch.COMPLETENESS_DISTINCT_VALUES,
                content="'state' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DISTINCT_VALUES_ZIP_CODE,
                batch=DataProfilingBatch.COMPLETENESS_DISTINCT_VALUES,
                content="'zip_code' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DISTINCT_VALUES_HOUSE_SIZE,
                batch=DataProfilingBatch.COMPLETENESS_DISTINCT_VALUES,
                content="'house_size' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DISTINCT_VALUES_PREV_SOLD_DATE,
                batch=DataProfilingBatch.COMPLETENESS_DISTINCT_VALUES,
                content="'prev_sold_date' column: distinct/unique values."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DATA_TYPES_BROKERED_BY,
                batch=DataProfilingBatch.COMPLETENESS_DATA_TYPES,
                content="'brokered_by' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DATA_TYPES_STATUS,
                batch=DataProfilingBatch.COMPLETENESS_DATA_TYPES,
                content="'status' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DATA_TYPES_PRICE,
                batch=DataProfilingBatch.COMPLETENESS_DATA_TYPES,
                content="'price' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DATA_TYPES_BED,
                batch=DataProfilingBatch.COMPLETENESS_DATA_TYPES,
                content="'bed' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DATA_TYPES_BATH,
                batch=DataProfilingBatch.COMPLETENESS_DATA_TYPES,
                content="'bath' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DATA_TYPES_ACRE_LOT,
                batch=DataProfilingBatch.COMPLETENESS_DATA_TYPES,
                content="'acre_lot' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DATA_TYPES_STREET,
                batch=DataProfilingBatch.COMPLETENESS_DATA_TYPES,
                content="'street' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DATA_TYPES_CITY,
                batch=DataProfilingBatch.COMPLETENESS_DATA_TYPES,
                content="'city' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DATA_TYPES_STATE,
                batch=DataProfilingBatch.COMPLETENESS_DATA_TYPES,
                content="'state' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DATA_TYPES_ZIP_CODE,
                batch=DataProfilingBatch.COMPLETENESS_DATA_TYPES,
                content="'zip_code' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DATA_TYPES_HOUSE_SIZE,
                batch=DataProfilingBatch.COMPLETENESS_DATA_TYPES,
                content="'house_size' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_DATA_TYPES_PREV_SOLD_DATE,
                batch=DataProfilingBatch.COMPLETENESS_DATA_TYPES,
                content="'prev_sold_date' column: data types."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_COLUMN_DESCRIPTIONS_BROKERED_BY,
                batch=DataProfilingBatch.COMPLETENESS_COLUMN_DESCRIPTIONS,
                content="'brokered_by' column: column description."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_COLUMN_DESCRIPTIONS_STATUS,
                batch=DataProfilingBatch.COMPLETENESS_COLUMN_DESCRIPTIONS,
                content="'status' column: column description."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_COLUMN_DESCRIPTIONS_PRICE,
                batch=DataProfilingBatch.COMPLETENESS_COLUMN_DESCRIPTIONS,
                content="'price' column: column description."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_COLUMN_DESCRIPTIONS_BED,
                batch=DataProfilingBatch.COMPLETENESS_COLUMN_DESCRIPTIONS,
                content="'bed' column: column description."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_COLUMN_DESCRIPTIONS_BATH,
                batch=DataProfilingBatch.COMPLETENESS_COLUMN_DESCRIPTIONS,
                content="'bath' column: column description."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_COLUMN_DESCRIPTIONS_ACRE_LOT,
                batch=DataProfilingBatch.COMPLETENESS_COLUMN_DESCRIPTIONS,
                content="'acre_lot' column: column description."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_COLUMN_DESCRIPTIONS_STREET,
                batch=DataProfilingBatch.COMPLETENESS_COLUMN_DESCRIPTIONS,
                content="'street' column: column description."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_COLUMN_DESCRIPTIONS_CITY,
                batch=DataProfilingBatch.COMPLETENESS_COLUMN_DESCRIPTIONS,
                content="'city' column: column description."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_COLUMN_DESCRIPTIONS_STATE,
                batch=DataProfilingBatch.COMPLETENESS_COLUMN_DESCRIPTIONS,
                content="'state' column: column description."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_COLUMN_DESCRIPTIONS_ZIP_CODE,
                batch=DataProfilingBatch.COMPLETENESS_COLUMN_DESCRIPTIONS,
                content="'zip_code' column: column description."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_COLUMN_DESCRIPTIONS_HOUSE_SIZE,
                batch=DataProfilingBatch.COMPLETENESS_COLUMN_DESCRIPTIONS,
                content="'house_size' column: column description."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_COLUMN_DESCRIPTIONS_PREV_SOLD_DATE,
                batch=DataProfilingBatch.COMPLETENESS_COLUMN_DESCRIPTIONS,
                content ="'prev_sold_date' column: column description."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_RANGE,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'price' column: range (interval between minimum value and maximum value)."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_MEAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'price' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_MEDIAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'price' column: median value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BED_RANGE,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'bed' column: range (interval between minimum value and maximum value)."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BED_MEAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'bed' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BED_MEDIAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'bed' column: median value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_RANGE,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'bath' column: range (interval between minimum value and maximum value)."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_MEAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'bath' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_MEDIAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'bath' column: median value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_RANGE,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'acre_lot' column: range (interval between minimum value and maximum value)."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_MEAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'acre_lot' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_MEDIAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'acre_lot' column: median value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_RANGE,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'house_size' column: range (interval between minimum value and maximum value)."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MEAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'house_size' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MEDIAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY,
                content="'house_size' column: median value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_QUARTILES,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'price' column: quartiles or percentiles."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_STD_DEV,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'price' column: standard deviation or variance."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_PLOT,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'price' column: distribution plots."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BED_QUARTILES,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'bed' column: quartiles or percentiles."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BED_STD_DEV,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'bed' column: standard deviation or variance."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BED_PLOT,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'bed' column: distribution plots."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_QUARTILES,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'bath' column: quartiles or percentiles."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_STD_DEV,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'bath' column: standard deviation or variance."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_PLOT,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'bath' column: distribution plots."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_QUARTILES,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'acre_lot' column: quartiles or percentiles."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_STD_DEV,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'acre_lot' column: standard deviation or variance."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_PLOT,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'acre_lot' column: distribution plots."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_QUARTILES,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'house_size' column: quartiles or percentiles."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_STD_DEV,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'house_size' column: standard deviation or variance."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_PLOT,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD,
                content="'house_size' column: distribution plots."
            ),
        ]
        prompts = [
            EvaluationPrompt(
                batch=DataProfilingBatch.COMPLETENESS_GENERAL.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are mentioned or not.

Keep in mind that any information that is requested can be given in any form to be considered mentioned, be it a number/datum, a piece of text, or a code snippet that helps obtain that information.

Keep also in mind that a general description of the dataset must not depend on any column and must stand alone per se, giving an overview of the dataset and not of the columns.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are not mentioned (0) or mentioned (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are mentioned or not.

Keep in mind that any information that is requested can be given in any form to be considered mentioned, be it a number/datum, a piece of text, or a code snippet that helps obtain that information.

Keep also in mind that it is not necessary to explicitly mention a column in order to evaluate a missing values statement with a score of 1: for example, if the text suggests to calculate the missing values for every column without explicitly mentioning each one of them, then you must still evaluate each missing values statement with a score of 1.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are not mentioned (0) or mentioned (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.COMPLETENESS_DISTINCT_VALUES.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are mentioned or not.

Keep in mind that any information that is requested can be given in any form to be considered mentioned, be it a number/datum, a piece of text, or a code snippet that helps obtain that information.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are not mentioned (0) or mentioned (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.COMPLETENESS_DATA_TYPES.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are mentioned or not.

Keep in mind that any information that is requested can be given in any form to be considered mentioned, be it a number/datum, a piece of text, or a code snippet that helps obtain that information.
Remember that even if data types are often given as clear, standalone information, sometimes it may happen that they are mentioned in a less evident way inside a sentence: if the text states that a column contains a given type of values, without explicitly mentioning that it contains only that kind of values, you can still assume that such type is a valid data type for that column. However, please be sure of the fact that a proper type is provided: you shouldn't infer it by means of other information.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are not mentioned (0) or mentioned (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.COMPLETENESS_COLUMN_DESCRIPTIONS.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are mentioned or not.

Keep also in mind that a column description is a textual description of the semantic meaning of the values contained in that column. For example, valid column descriptions are "number of bedrooms" for the 'bed' column and "lot size in acres" for the 'acre_lot' column.
Other pieces of information about columns, such as data quality issues (e.g. outliers, consistency issues, missing values), data types, and descriptive statistics, MUST NOT be considered column descriptions. Furthermore, information that is related to the values but not strictly related to the "domain" of the column does NOT provide a column description: for example, if the text says that the 'city' column has "various city names across different states", even though the information may be correct and pertain to the domain, the sentence does not provide a valid column description since it is an information that is dataset-dependent and not general with respect to the meaning of the column. 
Plus, a good column description should be clearly identified in the text: so, if you struggle to find a clear sentence that directly describes the meaning of a column, it is likely that there is no column description for that column.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are not mentioned (0) or mentioned (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_EASY.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are mentioned or not.

Keep in mind that any information that is requested can be given in any form to be considered mentioned, be it a number/datum, a piece of text, or a code snippet that helps obtain that information.

Keep also in mind that calculating the range of values for a specific (numeric) column is equivalent to calculating the minimum and maximum values for that column. Hence, if the text suggests to calculate or calculates the minimum and maximum values for a column, the range statement related to that column must be evaluated with a score of 1.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are not mentioned (0) or mentioned (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS_HARD.name,
                system_message=
                """
You are working on a dataset with these columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.

You will be given a text to evaluate based on whether some given facts are mentioned or not.

Keep in mind that any information that is requested can be given in any form to be considered mentioned, be it a number/datum, a piece of text, or a code snippet that helps obtain that information.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are not mentioned (0) or mentioned (1). You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            )
        ]
        super().__init__("Completeness", items, prompts)