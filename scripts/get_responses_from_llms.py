from experiments.model.dataset import Dataset
from scripts.utils.setup import setup

setup(dotenv=True)

import os

from data.tasks import tasks
from scripts.utils.fetch_datasets import load_dirty_datasets, read_csv_as_string
from scripts.utils.path import get_directory_from_root, get_directory_from_dir_name

# Load the datasets
datasets_dir = get_directory_from_root(__file__, os.path.join("datasets", "dirty"))  # datasets directory
responses_dir = get_directory_from_root(__file__, 'responses')  # responses directory

# if responses directory does not exist, create it
if not os.path.exists(responses_dir):
    os.makedirs(responses_dir)

# Definisce il percorso del file di output
output_file_path = os.path.join(responses_dir, "prompts_output.txt")

# Apre il file in modalità scrittura (sovrascrive se esiste già)
with open(output_file_path, "w") as output_file:
    for task in tasks:
        task_dir = os.path.join(datasets_dir, task.name)
        if not os.path.exists(task_dir):
            os.makedirs(task_dir)

        if task.name == "dependency_discovery":
            datasets = [
                Dataset(
                    "dependency_discovery_dataset",
                    content_string=read_csv_as_string(
                        os.path.join(get_directory_from_root(__file__, "datasets"), "df_clean.csv")),
                    dirty_percentage=0
                )
            ]

        elif task.name == "data_wrangling":
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

            if dataset.dirty_percentage != "10" and dataset.dirty_percentage != 0:
                continue

            dataset_dir = get_directory_from_dir_name(task_dir, dataset.id)
            if not os.path.exists(dataset_dir):
                os.makedirs(dataset_dir)

            for prompt in task.prompts:

                if prompt.id != 1:  # FIXME
                    continue

                prompt_dir = get_directory_from_dir_name(dataset_dir, str(prompt.id))
                if not os.path.exists(prompt_dir):
                    os.makedirs(prompt_dir)

                prompt_copy = prompt.copy()
                prompt_copy.user_message = prompt_copy.user_message.replace("{{csv_text}}", dataset.content_string)

                # Stampa il messaggio
                print(prompt_copy.user_message)
                print()

                # Scrive il messaggio nel file
                output_file.write(prompt_copy.user_message + "\n\n"
                                  + "---------------------------------------------------------------"
                                  + "\n\n")

print(f"Tutti i prompt sono stati salvati in {output_file_path}")