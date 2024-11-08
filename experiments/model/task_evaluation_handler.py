from abc import ABC
from typing import List, Dict, Optional

from experiments.model.checklist import BaseChecklist, BaseChecklistItem
from experiments.model.dependency import BaseDependency
from experiments.model.llm import BaseLLM


class BaseTaskEvaluationHandler(ABC):

    def __init__(self, checklists: List[BaseChecklist], dependencies: Optional[List[BaseDependency]] = None) -> None:
        self.checklists = checklists
        self.dependencies = dependencies

    def _solve_dependencies(self, batches: List[str], may_cause_dependency_items: List[BaseChecklistItem], may_be_dependent_items: List[BaseChecklistItem]) -> None:
        print("Solving dependencies...")
        batches_str = ", ".join(batches)
        print("Batches: " + batches_str)
        for dependency in self.dependencies:
            if (not dependency.is_solved()) and len(set(dependency.get_batches()).intersection(set(batches))) > 0:
                causing_dependency = dependency.get_causing_dependency()
                causing_dependency_items = [item for item in may_cause_dependency_items if item.get_id() == causing_dependency.name]
                if not len(causing_dependency_items) == 0:
                    if not causing_dependency_items[0].is_checked():
                        dependent = dependency.get_dependent()
                        dependent_str = [d.name for d in dependent]
                        dependent_items = [item for item in may_be_dependent_items if item.get_id() in dependent_str]
                        for dependent_item in dependent_items:
                            dependent_item.disable()
                            print("Disabled: " + dependent_item.get_id())
                        dependency.solve()

    def evaluate(self, text: str, llm: BaseLLM) -> None:
        for checklist in self.checklists:
            print("Evaluating " + checklist.name)
            checklist.evaluate(text, llm)
            for other_checklist in self.checklists:
                if not other_checklist.is_evaluated():
                    self._solve_dependencies(other_checklist.get_batches(), checklist.get_items(), other_checklist.get_items())

    def get_scores(self) -> Dict[str, float]:
        scores = {}
        for checklist in self.checklists:
            scores[checklist.name] = checklist.get_score()
        return scores

    def reset(self) -> None:
        for checklist in self.checklists:
            checklist.reset()
        for dependency in self.dependencies:
            dependency.reset()