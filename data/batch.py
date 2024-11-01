from enum import Enum, auto

class Batch(Enum):
    MISSING_VALUES_SOLUTION = auto()
    MISSING_VALUES_ALL_KINDS = auto()
    MISSING_VALUES_OPTIMAL = auto()
    DIRTY_SOLUTION = auto()
    DIRTY_OPTIMAL = auto()