from enum import Enum, auto


class DataProfilingItemId(Enum):

    COMPLETENESS_GENERAL_DATASET_DESCRIPTION = auto()
    COMPLETENESS_GENERAL_COLUMNS = auto()
    COMPLETENESS_GENERAL_ROWS = auto()
    COMPLETENESS_GENERAL_MISSING_VALUES = auto()
    COMPLETENESS_GENERAL_DUPLICATES = auto()
    COMPLETENESS_GENERAL_DEPENDENCIES = auto()

    COMPLETENESS_MISSING_VALUES_BROKERED_BY = auto()
    COMPLETENESS_MISSING_VALUES_STATUS = auto()
    COMPLETENESS_MISSING_VALUES_PRICE = auto()
    COMPLETENESS_MISSING_VALUES_BED = auto()
    COMPLETENESS_MISSING_VALUES_BATH = auto()
    COMPLETENESS_MISSING_VALUES_ACRE_LOT = auto()
    COMPLETENESS_MISSING_VALUES_STREET = auto()
    COMPLETENESS_MISSING_VALUES_CITY = auto()
    COMPLETENESS_MISSING_VALUES_STATE = auto()
    COMPLETENESS_MISSING_VALUES_ZIP_CODE = auto()
    COMPLETENESS_MISSING_VALUES_HOUSE_SIZE = auto()
    COMPLETENESS_MISSING_VALUES_PREV_SOLD_DATE = auto()

    COMPLETENESS_DISTINCT_VALUES_BROKERED_BY = auto()
    COMPLETENESS_DISTINCT_VALUES_STATUS = auto()
    COMPLETENESS_DISTINCT_VALUES_PRICE = auto()
    COMPLETENESS_DISTINCT_VALUES_BED = auto()
    COMPLETENESS_DISTINCT_VALUES_BATH = auto()
    COMPLETENESS_DISTINCT_VALUES_ACRE_LOT = auto()
    COMPLETENESS_DISTINCT_VALUES_STREET = auto()
    COMPLETENESS_DISTINCT_VALUES_CITY = auto()
    COMPLETENESS_DISTINCT_VALUES_STATE = auto()
    COMPLETENESS_DISTINCT_VALUES_ZIP_CODE = auto()
    COMPLETENESS_DISTINCT_VALUES_HOUSE_SIZE = auto()
    COMPLETENESS_DISTINCT_VALUES_PREV_SOLD_DATE = auto()

    COMPLETENESS_DATA_TYPES_BROKERED_BY = auto()
    COMPLETENESS_DATA_TYPES_STATUS = auto()
    COMPLETENESS_DATA_TYPES_PRICE = auto()
    COMPLETENESS_DATA_TYPES_BED = auto()
    COMPLETENESS_DATA_TYPES_BATH = auto()
    COMPLETENESS_DATA_TYPES_ACRE_LOT = auto()
    COMPLETENESS_DATA_TYPES_STREET = auto()
    COMPLETENESS_DATA_TYPES_CITY = auto()
    COMPLETENESS_DATA_TYPES_STATE = auto()
    COMPLETENESS_DATA_TYPES_ZIP_CODE = auto()
    COMPLETENESS_DATA_TYPES_HOUSE_SIZE = auto()
    COMPLETENESS_DATA_TYPES_PREV_SOLD_DATE = auto()

    COMPLETENESS_COLUMN_DESCRIPTIONS_BROKERED_BY = auto()
    COMPLETENESS_COLUMN_DESCRIPTIONS_STATUS = auto()
    COMPLETENESS_COLUMN_DESCRIPTIONS_PRICE = auto()
    COMPLETENESS_COLUMN_DESCRIPTIONS_BED = auto()
    COMPLETENESS_COLUMN_DESCRIPTIONS_BATH = auto()
    COMPLETENESS_COLUMN_DESCRIPTIONS_ACRE_LOT = auto()
    COMPLETENESS_COLUMN_DESCRIPTIONS_STREET = auto()
    COMPLETENESS_COLUMN_DESCRIPTIONS_CITY = auto()
    COMPLETENESS_COLUMN_DESCRIPTIONS_STATE = auto()
    COMPLETENESS_COLUMN_DESCRIPTIONS_ZIP_CODE = auto()
    COMPLETENESS_COLUMN_DESCRIPTIONS_HOUSE_SIZE = auto()
    COMPLETENESS_COLUMN_DESCRIPTIONS_PREV_SOLD_DATE = auto()

    COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_RANGE = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_MEAN = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_MEDIAN = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_QUARTILES = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_STD_DEV = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_PRICE_PLOT = auto()

    COMPLETENESS_VALUE_DISTRIBUTIONS_BED_RANGE = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_BED_MEAN = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_BED_MEDIAN = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_BED_QUARTILES = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_BED_STD_DEV = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_BED_PLOT = auto()

    COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_RANGE = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_MEAN = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_MEDIAN = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_QUARTILES = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_STD_DEV = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_BATH_PLOT = auto()

    COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_RANGE = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_MEAN = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_MEDIAN = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_QUARTILES = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_STD_DEV = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_ACRE_LOT_PLOT = auto()

    COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_RANGE = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MEAN = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MEDIAN = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_QUARTILES = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_STD_DEV = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS_HOUSE_SIZE_PLOT = auto()

    COMPLETENESS_FREQUENCIES_BROKERED_BY = auto()
    COMPLETENESS_FREQUENCIES_STATUS = auto()
    COMPLETENESS_FREQUENCIES_STREET = auto()
    COMPLETENESS_FREQUENCIES_CITY = auto()
    COMPLETENESS_FREQUENCIES_STATE = auto()
    COMPLETENESS_FREQUENCIES_ZIP_CODE = auto()
    COMPLETENESS_FREQUENCIES_PREV_SOLD_DATE = auto()