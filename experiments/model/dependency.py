from abc import ABC, abstractmethod
from typing import List

from data.batches import DataCleaningBatch
from data.checklists.data_cleaning.item_ids import DataCleaningItemId
from experiments.errors.generic_error import GenericError


class BaseDependency(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_batches(self) -> List[str]:
        raise GenericError("You should not be here.")

    @abstractmethod
    def get_causing_dependency(self):
        raise GenericError("You should not be here.")

    @abstractmethod
    def get_dependent(self):
        raise GenericError("You should not be here.")


class DataCleaningDependency(BaseDependency):

    def __init__(self, batches: List[DataCleaningBatch], causing_dependency: DataCleaningItemId, dependent: List[DataCleaningItemId]) -> None:
        super().__init__()
        self.batches = batches
        self.causing_dependency = causing_dependency
        self.dependent = dependent

    def get_batches(self) -> List[str]:
        return [batch.name for batch in self.batches]

    def get_causing_dependency(self) -> DataCleaningItemId:
        return self.causing_dependency

    def get_dependent(self) -> List[DataCleaningItemId]:
        return self.dependent