from scripts.utils.setup import setup

setup(dotenv=True)

import concurrent.futures
import os

from data.llms import llms
from data.tasks import tasks
from scripts.utils.fetch_datasets import load_dirty_datasets
from scripts.utils.path import get_directory_from_root, get_directory_from_dir_name

# Load the datasets
datasets_dir = get_directory_from_root(__file__, os.path.join("datasets", "dirty"))  # datasets directory

# if datasets directory does not exist, raise an exception
if not os.path.exists(datasets_dir):
    raise Exception("There is no 'datasets/dirty' directory to work with. Consider running 'python -m scripts.get_dirty_datasets' before running this script.")

datasets = load_dirty_datasets(datasets_dir, "df_dirty_") # FIXME: aggiustare secondo parametro quando avremo più datasets

responses_dir = get_directory_from_root(__file__, 'responses')  # responses directory

# if responses directory does not exist, create it
if not os.path.exists(responses_dir):
    os.makedirs(responses_dir)

for dataset in datasets:

    print("Starting dataset " + str(dataset.id))

    dataset_dir = get_directory_from_dir_name(responses_dir, dataset.id)
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)

    for task in tasks:

        if task.name == "data_cleaning" or task.name == "data_profiling" : #fixme
            continue

        print("Starting task " + task.name)

        task_dir = get_directory_from_dir_name(dataset_dir, task.name)
        if not os.path.exists(task_dir):
            os.makedirs(task_dir)

        for prompt in task.prompts:

            if prompt.id != 1: # FIXME
                continue

            print("Starting prompt " + str(prompt.id))

            prompt_dir = get_directory_from_dir_name(task_dir, str(prompt.id))
            if not os.path.exists(prompt_dir):
                os.makedirs(prompt_dir)

            prompt_copy = prompt.copy()
            prompt_copy.user_message = prompt_copy.user_message.replace("{{csv_text}}", dataset.df.to_string())

            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = {}

                print("Asking LLMs...")
                for llm in llms:
                    if llm.name != "GPT": #fixme
                        continue
                    futures[executor.submit(llm.get_response, prompt_copy)] = llm.name

                responses = []

                for future in concurrent.futures.as_completed(futures):
                  llm_name = futures[future]
                  try:
                    response = future.result()
                    responses.append((llm_name, response))
                  except Exception as e:
                    print(f"Error while asking {llm_name} for a response: {e}")

            print("All LLMs answered")

            for llm_name, response in responses:
                file_path = os.path.join(prompt_dir, f"{llm_name}.txt") # Create a clean filename
                with open(file_path, 'w') as f:
                    f.write(response)

            print("Finished prompt " + str(prompt_copy.id))

        print("Finished task " + task.name)

    print("Finished dataset " + str(dataset.id))