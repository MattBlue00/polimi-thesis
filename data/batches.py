from enum import Enum, auto

class DataCleaningBatch(Enum):
    COMPLETENESS_MISSING_VALUES_SOLUTION = auto()
    ACCURACY_MISSING_VALUES_SOLUTION = auto()
    ACCURACY_MISSING_VALUES_ALL_KINDS = auto()
    ACCURACY_MISSING_VALUES_OPTIMAL = auto()
    COMPLETENESS_DIRTY_SOLUTION = auto()
    ACCURACY_DIRTY_SOLUTION = auto()
    ACCURACY_DIRTY_OPTIMAL = auto()
    PRESCRIPTIVITY_MISSING_VALUES_SOLUTION = auto()
    PRESCRIPTIVITY_DIRTY_SOLUTION = auto()
    CONSEQUENTIALITY_MISSING_VALUES_SOLUTION = auto()
    CONSEQUENTIALITY_DIRTY_SOLUTION = auto()

class DataProfilingBatch(Enum):
    COMPLETENESS_GENERAL = auto()
    COMPLETENESS_MISSING_VALUES = auto()
    COMPLETENESS_DISTINCT_VALUES = auto()
    COMPLETENESS_DATA_TYPES = auto()
    COMPLETENESS_COLUMN_DESCRIPTIONS = auto()
    COMPLETENESS_VALUE_DISTRIBUTIONS = auto()