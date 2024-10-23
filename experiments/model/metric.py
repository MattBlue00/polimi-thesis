from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCaseParams

from experiments.evaluators.gpt_evaluator import GPTEvaluator
from experiments.model.llm import LLM


class Metric:

  def __init__(self, name, evaluation_params, criteria=None, evaluation_steps=None):

    if criteria is None and evaluation_steps is None:
      raise ValueError("Either 'criteria' or 'evaluation_steps' must be provided.")
    if criteria is not None and evaluation_steps is not None:
      raise ValueError("Only one of 'criteria' or 'evaluation_steps' can be provided.")

    self.name = name

    evaluator_model = GPTEvaluator(
        model=LLM(
            name="GPT",
            model="gpt-4o"
        )
    )
    #evaluator_model = GeminiEvaluator(
    #    model=LLM(
    #        name="Gemini",
    #        model="gemini-1.5-pro"
    #    )
    #)

    if evaluation_steps is not None and LLMTestCaseParams.ACTUAL_OUTPUT in evaluation_params:
      evaluation_steps.insert(0, "Assign a score of zero if 'actual output' contains only the original dataset (or a portion of it) and there are no changes justified by the prompt.")

    if evaluation_steps is not None:
      self.scorer = GEval(
          name=name,
          model=evaluator_model,
          evaluation_steps=evaluation_steps,
          evaluation_params=evaluation_params,
          async_mode=False
      )
    else:
      self.scorer = GEval(
          name=name,
          model=evaluator_model,
          criteria=criteria,
          evaluation_params=evaluation_params,
          async_mode=False
      )