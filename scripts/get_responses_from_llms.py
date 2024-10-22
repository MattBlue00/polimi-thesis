import concurrent.futures
import os

from data.llms import llms
from data.tasks import tasks
from scripts.utils.fetch_datasets import load_dirty_datasets
from scripts.utils.path import get_directory_from_root, get_directory_from_dir_name
from scripts.utils.setup import setup

print("Setting up the environment...")
setup(dotenv=True)

# Load the datasets
datasets_dir = get_directory_from_root(__file__, os.path.join("datasets", "dirty"))  # datasets directory

# if datasets directory does not exist, raise an exception
if not os.path.exists(datasets_dir):
    raise Exception("There is no 'datasets' directory to work with. Consider running 'python -m scripts.get_clean_dataset' before running this script.")

datasets = load_dirty_datasets(datasets_dir, "df_dirty_10")

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

        print("Starting task " + task.name)

        task_dir = get_directory_from_dir_name(dataset_dir, task.name)
        if not os.path.exists(task_dir):
            os.makedirs(task_dir)

        for prompt in task.prompts:

            print("Starting prompt " + str(prompt.id))

            prompt_dir = get_directory_from_dir_name(task_dir, str(prompt.id))
            if not os.path.exists(prompt_dir):
                os.makedirs(prompt_dir)

            prompt.user_message = prompt.user_message.replace("{{csv_text}}", dataset.df.to_string())

            with concurrent.futures.ThreadPoolExecutor() as executor:
                futures = {}

                print("Asking LLMs...")
                for llm in llms:
                  futures[executor.submit(llm.get_response, prompt)] = llm.name

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

            print("Finished prompt " + str(prompt.id))

        print("Finished task " + task.name)

    print("Finished dataset " + str(dataset.id))