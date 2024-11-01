from abc import ABC, abstractmethod
from typing import List

from data.batches import DataCleaningBatch
from data.checklists.data_cleaning.item_ids import DataCleaningItemId
from experiments.errors.generic_error import GenericError


class BaseDependency(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_batch(self) -> str:
        raise GenericError("You should not be here.")

    @abstractmethod
    def get_causing_dependency(self):
        raise GenericError("You should not be here.")

    @abstractmethod
    def get_dependent(self):
        raise GenericError("You should not be here.")


class DataCleaningDependency(BaseDependency):

    def __init__(self, batch: DataCleaningBatch, causing_dependency: DataCleaningItemId, dependent: List[DataCleaningItemId]) -> None:
        super().__init__()
        self.batch = batch
        self.causing_dependency = causing_dependency
        self.dependent = dependent

    def get_batch(self) -> str:
        return self.batch.name

    def get_causing_dependency(self) -> DataCleaningItemId:
        return self.causing_dependency

    def get_dependent(self) -> List[DataCleaningItemId]:
        return self.dependent