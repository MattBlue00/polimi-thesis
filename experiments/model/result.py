class Result:

  def __init__(self, dataset_id, task_name, prompt_id, llm_name, accuracy, completeness, consistency, relevance, fluency, overall_score):
    self.llm_name = llm_name
    self.dataset_id = dataset_id
    self.task_name = task_name
    self.prompt_id = prompt_id
    self.llm_name = llm_name
    self.accuracy = accuracy
    self.completeness = completeness
    self.consistency = consistency
    self.relevance = relevance
    self.fluency = fluency
    self.overall_score = overall_score