import json
from experiments.model.experiment import Experiment
from experiments.model.prompt import Prompt


def init_experiments(datasets):

  with open('prompts/prompts.json', 'r') as file:
    json_data = file.read()

  # Parse the JSON data
  tasks_init_data = json.loads(json_data)

  experiments = []

  for dataset in datasets:

    for task_init_data in tasks_init_data:

      incremental_number = 0

      for prompt_data in task_init_data["prompts"]:

        with open('expected_outputs/' + task_init_data["task"] + "_" + dataset.dirty_percentage + '.md', 'r') as file:
          expected_output = file.read()

        prompt = Prompt(
          prompt_id="prompt_"+str(incremental_number),
          json_object=prompt_data
        )

        experiment = Experiment(
          name=task_init_data["task"],
          prompt=prompt,
          dataset=dataset,
          expected_output=expected_output
        )

        experiments.append(experiment)

        incremental_number += 1

  return experiments