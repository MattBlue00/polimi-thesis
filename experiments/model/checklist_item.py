from abc import ABC

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

class DataCleaningChecklistItem(BaseChecklistItem):

    def __init__(self, item: DataCleaningItemId, batch: DataCleaningBatch, content: str) -> None:
        super().__init__(item.name, batch.name, content)
        self.item = item

class DataProfilingChecklistItem(BaseChecklistItem):

    def __init__(self, item: DataProfilingItemId, batch: DataProfilingBatch, content: str) -> None:
        super().__init__(item.name, batch.name, content)
        self.item = item