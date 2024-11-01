import re
from abc import ABC
from typing import List, Optional

from data.batches import DataCleaningBatch
from data.checklists.data_cleaning.item_ids import DataCleaningItemId
from experiments.errors.bad_response_error import BadResponseError
from experiments.errors.check_item_error import CheckItemError
from experiments.errors.disable_item_error import DisableItemError
from experiments.model.dependency import BaseDependency
from experiments.model.llm import BaseLLM
from experiments.model.prompt import EvaluationPrompt

class BaseChecklistItem(ABC):

    def __init__(self, item_id: str, batch: DataCleaningBatch, content: str, dependencies: Optional[List[str]] = None) -> None:
        self.id = item_id
        self.batch = batch
        self.content = content
        self.value = False
        self.enabled = True
        self.dependencies = dependencies

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
        return self.batch.name

class DataCleaningChecklistItem(BaseChecklistItem):

    def __init__(self, item: DataCleaningItemId, batch: DataCleaningBatch, content: str, dependencies: Optional[List[str]] = None) -> None:
        super().__init__(item.name, batch, content, dependencies)
        self.item = item


def _build_bullet_list_from_items(enabled_items: List[BaseChecklistItem]) -> str:
    return "\n".join(f"- {item.content}" for item in enabled_items).strip()


class BaseChecklist(ABC):

    def __init__(self, name: str, items: List[BaseChecklistItem], prompts: List[EvaluationPrompt], dependencies: Optional[List[BaseDependency]] = None) -> None:
        super().__init__()
        self.name = name
        self.items = items
        self.prompts = prompts
        self.dependencies = dependencies

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

    def _build_enabled_items_list(self, prompt_batch: str) -> List[BaseChecklistItem]:
        return [item for item in self.items if prompt_batch == item.get_batch() and item.is_enabled()]

    def _solve_dependencies(self, batch_str: str):
        print("Solving dependencies...")
        for dependency in self.dependencies:
            if dependency.get_batch() == batch_str:
                causing_dependency = dependency.get_causing_dependency()
                causing_dependency_items = [item for item in self.items if item.get_id() == causing_dependency.name]
                if not len(causing_dependency_items) == 0:
                    if not causing_dependency_items[0].is_checked():
                        dependent = dependency.get_dependent()
                        dependent_str = [d.name for d in dependent]
                        dependent_items = [item for item in self.items if item.get_id() in dependent_str]
                        for dependent_item in dependent_items:
                            dependent_item.disable()

    def evaluate(self, text: str, llm: BaseLLM):
        for prompt in self.prompts:
            print("Evaluating batch: " + prompt.batch)
            if self.dependencies is not None:
                self._solve_dependencies(prompt.batch)
            enabled_items = self._build_enabled_items_list(prompt.batch)
            bullet_checklist = _build_bullet_list_from_items(enabled_items)
            prompt.user_message = prompt.user_message.replace("{bullet_checklist}", bullet_checklist).replace("{llm_response_filtered}", text)
            response = llm.get_response(prompt).strip()
            if not re.fullmatch(r"^[01](?: [01])*$", response):
                raise BadResponseError(response)
            results = [int(x) for x in response.split()]
            for idx, result in enumerate(results):
                if result == 1:
                    enabled_items[idx].check()
            for enabled_item in enabled_items:
                print(f"Item: {enabled_item.id}, Score: {enabled_item.is_checked()}")