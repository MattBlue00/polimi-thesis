from abc import ABC, abstractmethod
from typing import List

from data.batches import DataCleaningBatch
from data.checklists.data_cleaning.item_ids import DataCleaningItemId
from experiments.errors.solve_dependency_error import SolveDependencyError
from experiments.model.checklist_item import BaseChecklistItem


class BaseDependency(ABC):

    def __init__(self, batches: List[str], causing_dependency_ids: List[str], dependent_ids: List[str]):
        self.batches = batches
        self.causing_dependency_ids = causing_dependency_ids
        self.dependent_ids = dependent_ids
        self.solved = False
        pass

    def get_batches(self) -> List[str]:
        return self.batches

    def get_causing_dependency_ids(self) -> List[str]:
        return self.causing_dependency_ids

    def get_dependent_ids(self) -> List[str]:
        return self.dependent_ids

    def is_solved(self) -> bool:
        return self.solved

    @abstractmethod
    def solve(self, causing_dependency_items: List[BaseChecklistItem], dependent_items: List[BaseChecklistItem]):
        self.solved = True

    def reset(self):
        self.solved = False


class DataCleaningDependency(BaseDependency):

    def __init__(self, batches: List[DataCleaningBatch], causing_dependency: DataCleaningItemId, dependents: List[DataCleaningItemId]) -> None:
        batches_str = [batch.name for batch in batches]
        causing_dependency_ids = [causing_dependency.name]
        dependent_ids = [dependent.name for dependent in dependents]
        super().__init__(batches_str, causing_dependency_ids, dependent_ids)

    def solve(self, causing_dependency_items: List[BaseChecklistItem], dependent_items: List[BaseChecklistItem]) -> None:
        if not self.is_solved():
            causing_dependency = True
            for causing_dependency_item in causing_dependency_items:
                causing_dependency = causing_dependency and (not causing_dependency_item.is_checked())
            if causing_dependency:
                for dependent_item in dependent_items:
                    dependent_item.disable()
                super().solve(causing_dependency_items, dependent_items)
        else:
            raise SolveDependencyError(
                causing_dependency_ids=self.causing_dependency_ids,
                dependent_ids=self.dependent_ids,
                reason="you already solved this dependency"
            )

class DataCleaningSpecificityDependency(BaseDependency):

    def __init__(self, batches: List[DataCleaningBatch], causing_dependencies: List[DataCleaningItemId], dependent: DataCleaningItemId) -> None:
        batches_str = [batch.name for batch in batches]
        causing_dependency_ids = [causing_dependency.name for causing_dependency in causing_dependencies]
        dependent_ids = [dependent.name]
        super().__init__(batches_str, causing_dependency_ids, dependent_ids)

    def solve(self, causing_dependency_items: List[BaseChecklistItem], dependent_items: List[BaseChecklistItem]) -> None:
        if not self.is_solved():
            should_disable = True
            for causing_dependency_item in causing_dependency_items:
                if causing_dependency_item.is_checked():
                    should_disable = False
            if len(causing_dependency_items) != 0 and should_disable:
                for dependent_item in dependent_items:
                    dependent_item.disable()
                super().solve(causing_dependency_items, dependent_items)
        else:
            raise SolveDependencyError(
                causing_dependency_ids=self.causing_dependency_ids,
                dependent_ids=self.dependent_ids,
                reason="you already solved this dependency"
            )