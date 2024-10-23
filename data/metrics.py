from deepeval.test_case import LLMTestCaseParams

from experiments.model.metric import Metric

metrics = {
    "data_cleaning": [
        # Completeness
        Metric(
            name="Completeness",
            evaluation_steps=[
              "Check whether all relevant facts in 'actual output' are contained in the 'expected output'.",
              "Penalize omission of any key facts that are present in the 'expected output' but missing from the 'actual output'.",
              "Heavily penalize inclusion of incorrect facts in 'actual output'.",
              "Consider paraphrased facts or alternate representations (e.g. code snippets) as valid, provided they convey the same meaning as those in the 'expected output'.",
            ],
            evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
        ),
        # Accuracy
        Metric(
            name="Accuracy",
            evaluation_steps=[
              "Compare each element in 'actual output' to the corresponding element in 'expected output'",
              "Penalize any mismatches between 'actual output' and 'expected output' based on content accuracy",
              "If 'actual output' is entirely accurate, assign a full score",
              "Penalize partial correctness based on the degree of deviation (e.g., wrong values, format inconsistencies, etc.)",
              "If 'actual output' contains incorrect data, penalize heavily",
              "Ensure that both precision and recall aspects are considered to avoid over-penalizing minor errors",
              "Consider paraphrased facts or alternate representations (e.g. code snippets) as valid, provided they convey the same meaning as those in the 'expected output'.",
            ],
            evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
        )
    ],
    "data_profiling": [
# Completeness
        Metric(
            name="Completeness",
            evaluation_steps=[
              "Check whether all relevant facts in 'actual output' are contained in the 'expected output'.",
              "Penalize omission of any key facts that are present in the 'expected output' but missing from the 'actual output'.",
              "Heavily penalize inclusion of incorrect facts in 'actual output'.",
              "Consider paraphrased facts or alternate representations (e.g. code snippets) as valid, provided they convey the same meaning as those in the 'expected output'.",
            ],
            evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
        ),
        # Accuracy
        Metric(
            name="Accuracy",
            evaluation_steps=[
              "Compare each element in 'actual output' to the corresponding element in 'expected output'",
              "Penalize any mismatches between 'actual output' and 'expected output' based on content accuracy",
              "If 'actual output' is entirely accurate, assign a full score",
              "Penalize partial correctness based on the degree of deviation (e.g., wrong values, format inconsistencies, etc.)",
              "If 'actual output' contains incorrect data, penalize heavily",
              "Ensure that both precision and recall aspects are considered to avoid over-penalizing minor errors",
              "Consider paraphrased facts or alternate representations (e.g. code snippets) as valid, provided they convey the same meaning as those in the 'expected output'.",
            ],
            evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
        )
    ]
}