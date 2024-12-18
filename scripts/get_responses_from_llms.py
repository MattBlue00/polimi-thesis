from experiments.model.dataset import Dataset
from scripts.utils.setup import setup

setup(dotenv=True)

import concurrent.futures
import os

from data.llms import llms
from data.tasks import tasks
from scripts.utils.fetch_datasets import load_dirty_datasets, read_csv_as_string
from scripts.utils.path import get_directory_from_root, get_directory_from_dir_name

# Load the datasets
datasets_dir = get_directory_from_root(__file__, os.path.join("datasets", "dirty"))  # datasets directory

responses_dir = get_directory_from_root(__file__, 'responses')  # responses directory

# if responses directory does not exist, create it
if not os.path.exists(responses_dir):
    os.makedirs(responses_dir)

for task in tasks:

    if task.name != "data_cleaning":
        continue

    print("Starting task " + task.name)

    task_dir = os.path.join(datasets_dir, task.name)
    if not os.path.exists(task_dir):
        os.makedirs(task_dir)

    if task.name == "dependency_discovery" :
        datasets = [
            Dataset(
               "dependency_discovery_dataset",
                content_string=read_csv_as_string(os.path.join(get_directory_from_root(__file__, "datasets"), "df_clean.csv")),
                dirty_percentage=0
            )
        ]

    elif task.name == "data_wrangling" :
        datasets = [
            Dataset(
                "data_wrangling_dataset",
                content_string=read_csv_as_string(
                    os.path.join(str(task_dir), "data_wrangling.csv")),
                dirty_percentage=0
            )
        ]

    else:
        datasets = load_dirty_datasets(task_dir)

    task_dir = os.path.join(responses_dir, task.name)

    for dataset in datasets:

        if dataset.dirty_percentage != "10":
            continue

        print("Starting dataset " + str(dataset.id))

        dataset_dir = get_directory_from_dir_name(task_dir, dataset.id)
        if not os.path.exists(dataset_dir):
            os.makedirs(dataset_dir)

        for prompt in task.prompts:

            if prompt.id != 1: # FIXME
                continue

            print("Starting prompt " + str(prompt.id))

            prompt_dir = get_directory_from_dir_name(dataset_dir, str(prompt.id))
            if not os.path.exists(prompt_dir):
                os.makedirs(prompt_dir)

            prompt_copy = prompt.copy()
            prompt_copy.user_message = prompt_copy.user_message.replace("{{csv_text}}", dataset.content_string)

            '''
            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = {}

                print("Asking LLMs...")
                for llm in llms:
                    futures[executor.submit(llm.get_response, prompt_copy)] = llm.name

                responses = []

                for future in concurrent.futures.as_completed(futures):
                    llm_name = futures[future]
                    try:
                        response = future.result()
                        responses.append((llm_name, response))
                    except Exception as e:
                        print(f"Error while asking {llm_name} for a response: {e}")
                        print(f"Error type: {type(e).__name__}")

            print("All LLMs answered")

            for llm_name, response in responses:
                file_path = os.path.join(prompt_dir, f"{llm_name}.txt") # Create a clean filename
                with open(file_path, 'w') as f:
                    f.write(response)
            '''

            print("*" * 50)
            print(prompt_copy.user_message)
            print("*" * 50)

            print("Finished prompt " + str(prompt_copy.id))

        print("Finished dataset " + str(dataset.id))

    print("Finished task " + task.name)