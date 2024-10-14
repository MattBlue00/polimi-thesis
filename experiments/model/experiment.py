from deepeval.test_case import LLMTestCaseParams, LLMTestCase
import concurrent.futures
from experiments.model.llm import LLM
from experiments.model.metric import Metric
from experiments.model.result import Result


def _evaluate_metric(metric, test_case):
  metric.scorer.measure(test_case)
  return metric


def _find_metric_by_name(metrics, name):
  for metric in metrics:
    if metric.name == name:
      return metric
  raise ValueError("There's no " + name + " metric in the provided list.")


class Experiment:

  def __init__(self, name, prompt, dataset, expected_output):
    self.name = name
    self.prompt = prompt
    self.dataset = dataset
    self.expected_output = expected_output
    self.llms = [
      LLM(
        name="GPT",
        model="gpt-4o-2024-08-06"
      ),
      LLM(
        name="Gemini",
        model="gemini-1.5-pro"
      ),
      #LLM(
      #  name="Mistral",
      #  model="mistral-large-2407"
      #)
    ]
    self.metrics = [
      # Completeness
      Metric(
        name="Completeness",
        weight=0.35,
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
        weight=0.40,
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
      ),
      # Consistency
      Metric(
        name="Consistency",
        weight=0.10,
        evaluation_steps=[
          "Check whether 'actual output' is internally consistent, ensuring there are no contradictions within the output itself.",
          "Penalize any inconsistencies in logic or flow between different parts of 'actual output' (e.g., conflicting statements or transitions).",
          "Verify consistency in formatting and structure (e.g., date formats, units of measurement, naming conventions) within 'actual output'.",
          "Do not evaluate the factual correctness or completeness of the statements, but focus solely on internal coherence.",
        ],
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT],
      ),
      # Relevance
      Metric(
        name="Relevance",
        weight=0.10,
        evaluation_steps=[
          "Check if 'actual output' directly addresses the question or request made in the input prompt.",
          "Penalize any unnecessary or off-topic information in 'actual output'.",
          "Ensure that the main points of the 'actual output' are aligned with the purpose of the input prompt.",
        ],
        evaluation_params=[LLMTestCaseParams.INPUT, LLMTestCaseParams.ACTUAL_OUTPUT],
      ),
      # Fluency
      Metric(
        name="Fluency",
        weight=0.05,
        evaluation_steps=[
          "Check if 'actual output' is grammatically correct and free of awkward phrasing.",
          "Ensure the language flows naturally and is easy to read and understand.",
          "Penalize any repetitive or unclear sentences in 'actual output'.",
          "Penalize the lack of explanation in the sentences of 'actual output'."
        ],
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT],
      )
    ]
    self.results = []

  def test(self):

    file_path = f"results/{self.name}_{self.prompt.id}.txt"  # Create a clean filename
    with open(file_path, 'w') as f:

      f.write("*" * 50 + "\n")
      f.write("Experiment: " + self.name + "_" + self.prompt.id + "\n")

      if self.prompt.system_message is not None:
        f.write("System Prompt:\n" + self.prompt.system_message + "\n")

      f.write("User Prompt:\n" + self.prompt.user_message + "\n")
      f.write("-" * 50 + "\n")

      print("Experiment: " + self.name + "_" + self.prompt.id + "\n")

      if self.prompt.system_message is not None:
        print("System Prompt:\n" + self.prompt.system_message + "\n")

      print("User Prompt:\n" + self.prompt.user_message + "\n")

      self.prompt.user_message = self.prompt.user_message.replace("{{csv_text}}", self.dataset.df.to_string())

      with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {}

        print("Asking LLMs...")
        for llm in self.llms:
          futures[executor.submit(llm.get_response, self.prompt)] = llm.name

        responses = []

        for future in concurrent.futures.as_completed(futures):
          llm_name = futures[future]
          try:
            response = future.result()
            responses.append((llm_name, response))
          except Exception as e:
            print(f"Error while asking {llm_name} for a response: {e}")

      print("Evaluating responses...")
      for llm_name, response in responses:

        f.write("LLM: " + llm_name + "\n\n")
        f.write("Response:\n" + response + "\n")
        f.write("-" * 50 + "\n")

        f.write("Starting " + llm_name + " evaluation...\n\n")

        test_case = LLMTestCase(
            input=self.prompt.user_message,
            actual_output=response,
            expected_output=self.expected_output
        )

        # è stato commentato su suggerimento dell'IDE, ma potrebbero esserci casini, questo è un reminder
        # metric_results = []

        with concurrent.futures.ThreadPoolExecutor() as executor:

          futures = {}

          for metric in self.metrics:
            futures[executor.submit(_evaluate_metric, metric, test_case)] = metric.name

          metric_results = [future.result() for future in concurrent.futures.as_completed(futures)]

        overall_score = 0.0
        for metric in metric_results:
          f.write("Evaluating " + metric.name + "...\n")
          f.write("Score: " + str(metric.scorer.score) + "\n")
          f.write("Reason: " + metric.scorer.reason + "\n\n")
          overall_score += (metric.scorer.score * metric.weight)

        f.write("Overall performance: " + str(overall_score) + "\n")
        f.write("-" * 50 + "\n")

        final_result = Result(
            dataset_id = self.dataset.id,
            task_name = self.name,
            prompt_id = self.prompt.id,
            llm_name = llm_name,
            accuracy = _find_metric_by_name(metric_results, 'Accuracy').scorer.score,
            completeness = _find_metric_by_name(metric_results, 'Completeness').scorer.score,
            consistency = _find_metric_by_name(metric_results, 'Consistency').scorer.score,
            relevance = _find_metric_by_name(metric_results, 'Relevance').scorer.score,
            fluency = _find_metric_by_name(metric_results, 'Fluency').scorer.score,
            overall_score = overall_score
        )

        self.results.append(final_result)

      f.write("*" * 50 + "\n")
      f.write("\n")