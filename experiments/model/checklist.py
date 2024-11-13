import re
import time
from abc import ABC
from typing import List


from experiments.errors.bad_response_error import BadResponseError
from experiments.model.checklist_item import BaseChecklistItem
from experiments.model.llm import BaseLLM
from experiments.model.prompt import EvaluationPrompt


def _build_bullet_list_from_items(enabled_items: List[BaseChecklistItem]) -> str:
    return "\n".join(f"- {item.content}" for item in enabled_items).strip()


class BaseChecklist(ABC):

    def __init__(self, name: str, items: List[BaseChecklistItem], prompts: List[EvaluationPrompt] = None) -> None:
        super().__init__()
        self.name = name
        self.items = items
        self.prompts = prompts
        self.evaluated = False

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

    def reset(self) -> None:
        self.evaluated = False
        for item in self.items:
            item.enabled = True
            item.value = False

    def get_batches(self) -> List[str]:
        batches = []
        for item in self.items:
            if item.get_batch() not in batches:
                batches.append(item.get_batch())
        return batches

    def get_items(self) -> List[BaseChecklistItem]:
        return self.items

    def is_evaluated(self) -> bool:
        return self.evaluated

    def disable_items(self, item_ids: List[str]) -> None:
        for item in self.items:
            if item.get_id() in item_ids:
                item.disable()

    def _build_enabled_items_list(self, prompt_batch: str) -> List[BaseChecklistItem]:
        return [item for item in self.items if prompt_batch == item.get_batch() and item.is_enabled()]


    def evaluate(self, text: str, llm: BaseLLM, dataset_id: str):
        for prompt in self.prompts:
            print("Evaluating batch: " + prompt.batch)
            enabled_items = self._build_enabled_items_list(prompt.batch)
            if len(enabled_items) == 0:
                continue
            enabled_items_copy = []
            for item in enabled_items:
                enabled_items_copy.append(item.copy())
            for item in enabled_items_copy:
                item.prepare(dataset_id)
            bullet_checklist = _build_bullet_list_from_items(enabled_items_copy)
            prompt_copy = prompt.copy()
            prompt_copy.user_message = prompt_copy.user_message.replace("{bullet_checklist}", bullet_checklist).replace("{llm_response_filtered}", text)
            #print(prompt_copy.user_message)
            while True:
                try:
                    response = llm.get_response(prompt_copy).strip()
                    if not re.fullmatch(r"^[01](?: [01])*$", response):
                        raise BadResponseError(response)
                    results = [int(x) for x in response.split()]
                    if len(results) != len(enabled_items):
                        raise BadResponseError(response)
                    break
                except BadResponseError as error:
                    print(error.message)
                    print("Retrying in 10 seconds...")
                    time.sleep(10)
                    print("Retrying now!")
            print(response)
            for idx, result in enumerate(results):
                if result == 1:
                    enabled_items[idx].check()
        self.evaluated = True