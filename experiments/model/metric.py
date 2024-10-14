from deepeval.metrics import GEval


class Metric:

  def __init__(self, name, weight, evaluation_steps, evaluation_params):
    self.name = name
    self.weight = weight
    self.scorer = GEval(
        name=name,
        model="gpt-4o",
        evaluation_steps=evaluation_steps,
        evaluation_params=evaluation_params,
    )