from data.checklists.data_profiling.data_profiling_completeness_checklist import DataProfilingCompletenessChecklist
from experiments.model.task_evaluation_handler import BaseTaskEvaluationHandler


class DataProfilingEvaluationHandler(BaseTaskEvaluationHandler):

    def __init__(self) -> None:
        dependencies = []
        checklists = [
            DataProfilingCompletenessChecklist()
            #DataProfilingAccuracyChecklist()
        ]
        super().__init__(checklists, dependencies)