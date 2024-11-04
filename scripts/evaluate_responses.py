import os

from data.llms import get_llm
from data.task_evaluation_handlers.data_cleaning_evaluation_handler import DataCleaningEvaluationHandler
from scripts.utils.fetch_datasets import load_dirty_datasets
from scripts.utils.path import get_directory_from_root, get_directory_from_dir_name
from scripts.utils.setup import setup
from scripts.utils.text_filter import filter_llm_response

print("Setting up the environment...")
setup(dotenv=True)

responses_dir = get_directory_from_root(__file__, 'responses')  # responses directory

# if responses directory does not exist, create it
if not os.path.exists(responses_dir):
    raise Exception(
        "There is no 'responses' directory to work with. Consider running 'python -m scripts.get_responses_from_llms' before running this script.")

datasets = [d for d in os.listdir(responses_dir) if os.path.isdir(os.path.join(responses_dir, d))]

for dataset in datasets:

    dataset_dir = get_directory_from_dir_name(responses_dir, dataset)
    if not os.path.exists(dataset_dir):
        raise Exception(
            "There is no dataset directory to work with. Consider running 'python -m scripts.get_responses_from_llms' before running this script.")

    datasets_dir = get_directory_from_root(__file__, os.path.join("datasets", "dirty"))  # datasets directory
    if not os.path.exists(datasets_dir):
        raise Exception(
            "There is no 'datasets/dirty' directory to work with. Consider running 'python -m scripts.get_dirty_datasets' before running this script.")

    dataset_obj = None
    ds = load_dirty_datasets(datasets_dir, "df_dirty_10") # FIXME: aggiustare secondo parametro quando avremo più datasets
    for d in ds:
        if d.id == dataset:
            dataset_obj = d
            break
    if dataset_obj is None:
        raise Exception("Dataset not found")

    print("Evaluating dataset " + os.path.basename(dataset_dir))

    tasks = [t for t in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, t))]

    for task in tasks:

        if task == "data_profiling": #FIXME
            continue

        task_dir = get_directory_from_dir_name(dataset_dir, task)
        if not os.path.exists(task_dir):
            raise Exception(
                "There is no task directory to work with. Consider running 'python -m scripts.get_responses_from_llms' before running this script.")

        print("Evaluating task " + os.path.basename(task_dir))

        prompts = [p for p in os.listdir(task_dir) if os.path.isdir(os.path.join(task_dir, p))]

        for prompt in prompts:

            prompt_dir = get_directory_from_dir_name(task_dir, prompt)
            if not os.path.exists(prompt_dir):
                raise Exception(
                    "There is no prompt directory to work with. Consider running 'python -m scripts.get_responses_from_llms' before running this script.")

            print("-" * 50)
            print("Evaluating prompt " + os.path.basename(prompt_dir))

            response_files = [r for r in os.listdir(prompt_dir) if os.path.isfile(os.path.join(prompt_dir, r))]

            cleaning_handler = DataCleaningEvaluationHandler()
            for rf in response_files:
                with open(os.path.join(prompt_dir, rf), 'r', encoding='utf-8') as file:
                    print("Evaluating response: " + rf)
                    file_content = file.read()
                    llm_response_filtered = filter_llm_response(file_content)
                    cleaning_handler.evaluate(llm_response_filtered, get_llm("GPT"))
                    print(cleaning_handler.get_scores())
                    cleaning_handler.reset()

            '''
            evaluations_dir = get_directory_from_root(__file__, 'evaluations')  # responses directory
    
            # if evaluations directory does not exist, create it
            if not os.path.exists(evaluations_dir):
                os.makedirs(evaluations_dir)
    
            dataset_eval_dir = get_directory_from_dir_name(evaluations_dir, dataset)
            if not os.path.exists(dataset_eval_dir):
                os.makedirs(dataset_eval_dir)
    
            task_eval_dir = get_directory_from_dir_name(dataset_eval_dir, task)
            if not os.path.exists(task_eval_dir):
                os.makedirs(task_eval_dir)
    
            prompt_eval_dir = get_directory_from_dir_name(task_eval_dir, prompt)
            if not os.path.exists(prompt_eval_dir):
                os.makedirs(prompt_eval_dir)
    
            print("Evaluating responses...")
            '''

