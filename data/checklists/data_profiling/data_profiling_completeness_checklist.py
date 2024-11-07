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
                content="explicit columns number."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_GENERAL_ROWS,
                batch=DataProfilingBatch.COMPLETENESS_GENERAL,
                content="explicit rows number."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_GENERAL_MISSING_VALUES,
                batch=DataProfilingBatch.COMPLETENESS_GENERAL,
                content="explicit total missing values number."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_GENERAL_DUPLICATES,
                batch=DataProfilingBatch.COMPLETENESS_GENERAL,
                content="explicit exact duplicate rows number."
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
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_MIN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'price' column: minimum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_MEAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'price' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_MAX,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'price' column: maximum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BED_MIN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'bed' column: minimum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BED_MEAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'bed' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BED_MAX,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'bed' column: maximum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_MIN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'bath' column: minimum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_MEAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'bath' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_MAX,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'bath' column: maximum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_MIN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'acre_lot' column: minimum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_MEAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'acre_lot' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_MAX,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'acre_lot' column: maximum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MIN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'house_size' column: minimum value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MEAN,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'house_size' column: mean value."
            ),
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MAX,
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS,
                content="'house_size' column: maximum value."
            )
        ]
        prompts = [
            EvaluationPrompt(
                batch=DataProfilingBatch.COMPLETENESS_GENERAL.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.
                
Keep in mind that a general description of the dataset must not depend on any column and must stand alone per se, giving an overview of the dataset and not of the columns.

Keep also in mind that general numbers about the dataset (i.e. columns number, rows number, total missing values number, exact duplicate rows number) must be EXPLICITLY given and MUST NOT be inferred from other pieces of information.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.COMPLETENESS_DISTINCT_VALUES.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.COMPLETENESS_DATA_TYPES.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.COMPLETENESS_COLUMN_DESCRIPTIONS.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            ),
            EvaluationPrompt(
                batch=DataProfilingBatch.COMPLETENESS_VALUE_DISTRIBUTIONS.name,
                system_message=
                """
You are working on a dataset with 12 columns: brokered_by, status, price, bed, bath, acre_lot, street, city, state, zip_code, house_size, prev_sold_date. Assume that there is a dataframe containing the whole dataset.
                """,
                user_message=
                """
Consider if the piece of text I will give you mentions these facts:
{bullet_checklist}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. You MUST answer with ONLY a list of ordered, whitespace-separated numbers. You MUST avoid any textual comment.
The answer must be given considering this text:

{llm_response_filtered}
                """
            )
        ]
        super().__init__("Data Profiling - Completeness", items, prompts)