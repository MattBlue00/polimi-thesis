from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict

from data.batches import DataCleaningBatch, DataProfilingBatch
from data.checklists.data_cleaning.item_ids import DataCleaningItemId
from data.checklists.data_profiling.item_ids import DataProfilingItemId

from experiments.errors.check_item_error import CheckItemError
from experiments.errors.disable_item_error import DisableItemError


class BaseChecklistItem(ABC):

    def __init__(self, item_id: str, batch: str, content: str) -> None:
        self.id = item_id
        self.batch = batch
        self.content = content
        self.value = False
        self.enabled = True

    def prepare(self, dataset_id: str) -> None:
        pass

    def check(self) -> None:
        if self.is_enabled():
            if not self.is_checked():
                self.value = True
            else:
                raise CheckItemError(self.id, "it has already been checked")
        else:
            raise CheckItemError(self.id, "it has been disabled")

    def disable(self) -> None:
        if not self.is_checked() and self.is_enabled():
            self.enabled = False
            #print("Disabled: " + self.id)
        else:
            if self.is_checked():
                raise DisableItemError(self.id, "it has been checked")
            else:
                raise DisableItemError(self.id, "it has already been disabled")

    def get_id(self) -> str:
        return self.id

    def is_enabled(self) -> bool:
        return self.enabled

    def is_checked(self) -> bool:
        return self.value

    def get_batch(self) -> str:
        return self.batch

    @abstractmethod
    def copy(self) -> BaseChecklistItem:
        pass

class DataCleaningChecklistItem(BaseChecklistItem):

    def __init__(self, item: DataCleaningItemId, batch: DataCleaningBatch, content: str) -> None:
        super().__init__(item.name, batch.name, content)
        self.item = item
        self.data_cleaning_batch = batch

    def copy(self) -> DataCleaningChecklistItem:
        return DataCleaningChecklistItem(self.item, self.data_cleaning_batch, self.content)

class DataProfilingChecklistItem(BaseChecklistItem):

    def __init__(self, item: DataProfilingItemId, batch: DataProfilingBatch, content: str, content_values: Dict[str, str] = None) -> None:
        super().__init__(item.name, batch.name, content)
        self.item = item
        self.data_profiling_batch = batch
        self.content_values = content_values

    def copy(self) -> DataProfilingChecklistItem:
        return DataProfilingChecklistItem(self.item, self.data_profiling_batch, self.content, self.content_values)

    def prepare(self, dataset_id: str) -> None:
        if self.content_values is not None:
            self.content = self.content.replace("{content_value}", self.content_values[dataset_id])