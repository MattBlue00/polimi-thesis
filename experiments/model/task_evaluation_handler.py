from abc import ABC
from typing import List, Dict

from experiments.model.checklist import BaseChecklist
from experiments.model.llm import BaseLLM


class BaseTaskEvaluationHandler(ABC):

    def __init__(self, checklists: List[BaseChecklist]) -> None:
        self.checklists = checklists

    def evaluate(self, text: str, llm: BaseLLM):
        for checklist in self.checklists:
            print("Evaluating " + checklist.name)
            checklist.evaluate(text, llm)

    def get_scores(self) -> Dict[str, float]:
        scores = {}
        for checklist in self.checklists:
            scores[checklist.name] = checklist.get_score()
        return scores