from data.checklists.data_cleaning.data_cleaning_accuracy_checklist import DataCleaningAccuracyChecklist
from data.checklists.data_cleaning.data_cleaning_automatability_checklist import DataCleaningAutomatabilityChecklist
from data.checklists.data_cleaning.data_cleaning_completeness_checklist import DataCleaningCompletenessChecklist
from data.checklists.data_cleaning.data_cleaning_consequentiality_checklist import DataCleaningConsequentialityChecklist
from data.checklists.data_cleaning.data_cleaning_prescriptivity_checklist import DataCleaningPrescriptivityChecklist
from data.checklists.data_cleaning.data_cleaning_specificity_checklist import DataCleaningSpecificityChecklist
from scripts.utils.setup import setup

setup()

checklists = {
    "data_cleaning": [
        DataCleaningCompletenessChecklist(),
        DataCleaningAccuracyChecklist(),
        DataCleaningConsequentialityChecklist(),
        DataCleaningPrescriptivityChecklist(),
        DataCleaningSpecificityChecklist(),
        DataCleaningAutomatabilityChecklist()
    ],
    "data_profiling": [

    ]
}