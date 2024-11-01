from abc import ABC
from typing import List

from data.batch import Batch
from experiments.errors.check_item_error import CheckItemError
from experiments.errors.disable_item_error import DisableItemError
from experiments.model.prompt import EvaluationPrompt

class ChecklistItem:

    def __init__(self, item_id: str, batch: Batch, content: str) -> None:
        self.id = item_id
        self.batch_id = batch
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

    def is_enabled(self) -> bool:
        return self.enabled

    def is_checked(self) -> bool:
        return self.value

class BaseChecklist(ABC):

    def __init__(self, items: List[ChecklistItem], prompts: List[EvaluationPrompt]) -> None:
        super().__init__()
        self.items = items
        self.prompts = prompts

    def get_score(self) -> float:
        checked_items_count = 0
        enabled_items_count = 0
        for item in self.items:
            if item.is_enabled():
                enabled_items_count += 1
                if item.is_checked():
                    checked_items_count += 1
        if enabled_items_count == 0:
            return 0.0
        else:
            return checked_items_count / enabled_items_count

    def _build_bullet_list_from_items(self):
        return "\n".join(f"- {item.content}" for item in self.items).strip()

    def evaluate(self, text: str):

        pass #todo