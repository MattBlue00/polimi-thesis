from enum import Enum, auto


class DataProfilingItemId(Enum):
    #completeness
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

    #accuracy
    ACCURACY_GENERAL_DATASET_DESCRIPTION = auto()
    ACCURACY_GENERAL_COLUMNS = auto()
    ACCURACY_GENERAL_ROWS = auto()
    ACCURACY_GENERAL_MISSING_VALUES = auto()
    ACCURACY_GENERAL_DUPLICATES = auto()
    ACCURACY_GENERAL_SOME_DEPENDENCIES = auto()
    ACCURACY_GENERAL_ALL_DEPENDENCIES = auto()

    ACCURACY_MISSING_VALUES_BROKERED_BY = auto()
    ACCURACY_MISSING_VALUES_STATUS = auto()
    ACCURACY_MISSING_VALUES_PRICE = auto()
    ACCURACY_MISSING_VALUES_BED = auto()
    ACCURACY_MISSING_VALUES_BATH = auto()
    ACCURACY_MISSING_VALUES_ACRE_LOT = auto()
    ACCURACY_MISSING_VALUES_STREET = auto()
    ACCURACY_MISSING_VALUES_CITY = auto()
    ACCURACY_MISSING_VALUES_STATE = auto()
    ACCURACY_MISSING_VALUES_ZIP_CODE = auto()
    ACCURACY_MISSING_VALUES_HOUSE_SIZE = auto()
    ACCURACY_MISSING_VALUES_PREV_SOLD_DATE = auto()

    ACCURACY_DISTINCT_VALUES_BROKERED_BY = auto()
    ACCURACY_DISTINCT_VALUES_STATUS = auto()
    ACCURACY_DISTINCT_VALUES_PRICE = auto()
    ACCURACY_DISTINCT_VALUES_BED = auto()
    ACCURACY_DISTINCT_VALUES_BATH = auto()
    ACCURACY_DISTINCT_VALUES_ACRE_LOT = auto()
    ACCURACY_DISTINCT_VALUES_STREET = auto()
    ACCURACY_DISTINCT_VALUES_CITY = auto()
    ACCURACY_DISTINCT_VALUES_STATE = auto()
    ACCURACY_DISTINCT_VALUES_ZIP_CODE = auto()
    ACCURACY_DISTINCT_VALUES_HOUSE_SIZE = auto()
    ACCURACY_DISTINCT_VALUES_PREV_SOLD_DATE = auto()

    ACCURACY_DATA_TYPES_BROKERED_BY = auto()
    ACCURACY_DATA_TYPES_STATUS = auto()
    ACCURACY_DATA_TYPES_PRICE = auto()
    ACCURACY_DATA_TYPES_BED = auto()
    ACCURACY_DATA_TYPES_BATH = auto()
    ACCURACY_DATA_TYPES_ACRE_LOT = auto()
    ACCURACY_DATA_TYPES_STREET = auto()
    ACCURACY_DATA_TYPES_CITY = auto()
    ACCURACY_DATA_TYPES_STATE = auto()
    ACCURACY_DATA_TYPES_ZIP_CODE = auto()
    ACCURACY_DATA_TYPES_HOUSE_SIZE = auto()
    ACCURACY_DATA_TYPES_PREV_SOLD_DATE = auto()

    ACCURACY_COLUMN_DESCRIPTIONS_BROKERED_BY = auto()
    ACCURACY_COLUMN_DESCRIPTIONS_STATUS = auto()
    ACCURACY_COLUMN_DESCRIPTIONS_PRICE = auto()
    ACCURACY_COLUMN_DESCRIPTIONS_BED = auto()
    ACCURACY_COLUMN_DESCRIPTIONS_BATH = auto()
    ACCURACY_COLUMN_DESCRIPTIONS_ACRE_LOT = auto()
    ACCURACY_COLUMN_DESCRIPTIONS_STREET = auto()
    ACCURACY_COLUMN_DESCRIPTIONS_CITY = auto()
    ACCURACY_COLUMN_DESCRIPTIONS_STATE = auto()
    ACCURACY_COLUMN_DESCRIPTIONS_ZIP_CODE = auto()
    ACCURACY_COLUMN_DESCRIPTIONS_HOUSE_SIZE = auto()
    ACCURACY_COLUMN_DESCRIPTIONS_PREV_SOLD_DATE = auto()

    ACCURACY_CALCULATE_FREQUENCIES_BROKERED_BY = auto()
    ACCURACY_CALCULATE_FREQUENCIES_STATUS = auto()
    ACCURACY_CALCULATE_FREQUENCIES_STREET = auto()
    ACCURACY_CALCULATE_FREQUENCIES_CITY = auto()
    ACCURACY_CALCULATE_FREQUENCIES_STATE = auto()
    ACCURACY_CALCULATE_FREQUENCIES_ZIP_CODE = auto()
    ACCURACY_CALCULATE_FREQUENCIES_PREV_SOLD_DATE = auto()

    ACCURACY_VISUALIZE_FREQUENCIES_BROKERED_BY = auto()
    ACCURACY_VISUALIZE_FREQUENCIES_STATUS = auto()
    ACCURACY_VISUALIZE_FREQUENCIES_STREET = auto()
    ACCURACY_VISUALIZE_FREQUENCIES_CITY = auto()
    ACCURACY_VISUALIZE_FREQUENCIES_STATE = auto()
    ACCURACY_VISUALIZE_FREQUENCIES_ZIP_CODE = auto()
    ACCURACY_VISUALIZE_FREQUENCIES_PREV_SOLD_DATE = auto()

    ACCURACY_VALUE_DISTRIBUTIONS_PRICE_MIN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_PRICE_MAX = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_PRICE_MEAN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_PRICE_MEDIAN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_PRICE_QUARTILES = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_PRICE_STD_DEV = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_PRICE_PLOT = auto()

    ACCURACY_VALUE_DISTRIBUTIONS_BED_MIN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_BED_MAX = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_BED_MEAN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_BED_MEDIAN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_BED_QUARTILES = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_BED_STD_DEV = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_BED_PLOT = auto()

    ACCURACY_VALUE_DISTRIBUTIONS_BATH_MIN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_BATH_MAX = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_BATH_MEAN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_BATH_MEDIAN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_BATH_QUARTILES = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_BATH_STD_DEV = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_BATH_PLOT = auto()

    ACCURACY_VALUE_DISTRIBUTIONS_ACRE_LOT_MIN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_ACRE_LOT_MAX = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_ACRE_LOT_MEAN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_ACRE_LOT_MEDIAN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_ACRE_LOT_QUARTILES = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_ACRE_LOT_STD_DEV = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_ACRE_LOT_PLOT = auto()

    ACCURACY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MIN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MAX = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MEAN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MEDIAN = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_QUARTILES = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_STD_DEV = auto()
    ACCURACY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_PLOT = auto()

    # automatability
    AUTOMATABILITY_GENERAL_COLUMNS = auto()
    AUTOMATABILITY_GENERAL_ROWS = auto()
    AUTOMATABILITY_GENERAL_MISSING_VALUES = auto()
    AUTOMATABILITY_GENERAL_DUPLICATES = auto()
    AUTOMATABILITY_GENERAL_DEPENDENCIES = auto()

    AUTOMATABILITY_MISSING_VALUES_BROKERED_BY = auto()
    AUTOMATABILITY_MISSING_VALUES_STATUS = auto()
    AUTOMATABILITY_MISSING_VALUES_PRICE = auto()
    AUTOMATABILITY_MISSING_VALUES_BED = auto()
    AUTOMATABILITY_MISSING_VALUES_BATH = auto()
    AUTOMATABILITY_MISSING_VALUES_ACRE_LOT = auto()
    AUTOMATABILITY_MISSING_VALUES_STREET = auto()
    AUTOMATABILITY_MISSING_VALUES_CITY = auto()
    AUTOMATABILITY_MISSING_VALUES_STATE = auto()
    AUTOMATABILITY_MISSING_VALUES_ZIP_CODE = auto()
    AUTOMATABILITY_MISSING_VALUES_HOUSE_SIZE = auto()
    AUTOMATABILITY_MISSING_VALUES_PREV_SOLD_DATE = auto()

    AUTOMATABILITY_DISTINCT_VALUES_BROKERED_BY = auto()
    AUTOMATABILITY_DISTINCT_VALUES_STATUS = auto()
    AUTOMATABILITY_DISTINCT_VALUES_PRICE = auto()
    AUTOMATABILITY_DISTINCT_VALUES_BED = auto()
    AUTOMATABILITY_DISTINCT_VALUES_BATH = auto()
    AUTOMATABILITY_DISTINCT_VALUES_ACRE_LOT = auto()
    AUTOMATABILITY_DISTINCT_VALUES_STREET = auto()
    AUTOMATABILITY_DISTINCT_VALUES_CITY = auto()
    AUTOMATABILITY_DISTINCT_VALUES_STATE = auto()
    AUTOMATABILITY_DISTINCT_VALUES_ZIP_CODE = auto()
    AUTOMATABILITY_DISTINCT_VALUES_HOUSE_SIZE = auto()
    AUTOMATABILITY_DISTINCT_VALUES_PREV_SOLD_DATE = auto()

    AUTOMATABILITY_DATA_TYPES_BROKERED_BY = auto()
    AUTOMATABILITY_DATA_TYPES_STATUS = auto()
    AUTOMATABILITY_DATA_TYPES_PRICE = auto()
    AUTOMATABILITY_DATA_TYPES_BED = auto()
    AUTOMATABILITY_DATA_TYPES_BATH = auto()
    AUTOMATABILITY_DATA_TYPES_ACRE_LOT = auto()
    AUTOMATABILITY_DATA_TYPES_STREET = auto()
    AUTOMATABILITY_DATA_TYPES_CITY = auto()
    AUTOMATABILITY_DATA_TYPES_STATE = auto()
    AUTOMATABILITY_DATA_TYPES_ZIP_CODE = auto()
    AUTOMATABILITY_DATA_TYPES_HOUSE_SIZE = auto()
    AUTOMATABILITY_DATA_TYPES_PREV_SOLD_DATE = auto()

    AUTOMATABILITY_VALUE_DISTRIBUTIONS_PRICE_MIN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_PRICE_MAX = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_PRICE_MEAN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_PRICE_MEDIAN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_PRICE_QUARTILES = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_PRICE_STD_DEV = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_PRICE_PLOT = auto()

    AUTOMATABILITY_VALUE_DISTRIBUTIONS_BED_MIN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_BED_MAX = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_BED_MEAN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_BED_MEDIAN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_BED_QUARTILES = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_BED_STD_DEV = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_BED_PLOT = auto()

    AUTOMATABILITY_VALUE_DISTRIBUTIONS_BATH_MIN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_BATH_MAX = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_BATH_MEAN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_BATH_MEDIAN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_BATH_QUARTILES = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_BATH_STD_DEV = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_BATH_PLOT = auto()

    AUTOMATABILITY_VALUE_DISTRIBUTIONS_ACRE_LOT_MIN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_ACRE_LOT_MAX = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_ACRE_LOT_MEAN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_ACRE_LOT_MEDIAN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_ACRE_LOT_QUARTILES = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_ACRE_LOT_STD_DEV = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_ACRE_LOT_PLOT = auto()

    AUTOMATABILITY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MIN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MAX = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MEAN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_MEDIAN = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_QUARTILES = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_STD_DEV = auto()
    AUTOMATABILITY_VALUE_DISTRIBUTIONS_HOUSE_SIZE_PLOT = auto()

    AUTOMATABILITY_FREQUENCIES_BROKERED_BY = auto()
    AUTOMATABILITY_FREQUENCIES_STATUS = auto()
    AUTOMATABILITY_FREQUENCIES_STREET = auto()
    AUTOMATABILITY_FREQUENCIES_CITY = auto()
    AUTOMATABILITY_FREQUENCIES_STATE = auto()
    AUTOMATABILITY_FREQUENCIES_ZIP_CODE = auto()
    AUTOMATABILITY_FREQUENCIES_PREV_SOLD_DATE = auto()