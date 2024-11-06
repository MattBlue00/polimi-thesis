from data.batches import DataProfilingBatch
from data.checklists.data_profiling.item_ids import DataProfilingItemId
from experiments.model.checklist import BaseChecklist, DataProfilingChecklistItem
from experiments.model.prompt import EvaluationPrompt

class DataProfilingCompletenessChecklist(BaseChecklist):

    def __init__(self) -> None:
        items = [
            DataProfilingChecklistItem(
                item=DataProfilingItemId.COMPLETENESS_MISSING_VALUES_BROKERED_BY,
                batch=DataProfilingBatch.COMPLETENESS_MISSING_VALUES_SOLUTION,
                content="'brokered_by' column: presence of missing values."
            ),