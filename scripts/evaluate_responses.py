import concurrent.futures
import os

from deepeval.test_case import LLMTestCase

from data.tasks import get_prompt
from experiments.model.result import DataCleaningResult, DataProfilingResult
from scripts.utils.metric import evaluate_metric, find_metric_by_name
from scripts.utils.fetch_datasets import load_dirty_datasets
from scripts.utils.path import get_directory_from_root, get_directory_from_dir_name
from scripts.utils.setup import setup
from data.metrics import metrics

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

            print("Evaluating prompt " + os.path.basename(prompt_dir))

            response_files = [r for r in os.listdir(prompt_dir) if os.path.isfile(os.path.join(prompt_dir, r))]
            llm_test_cases = {}

            prompt_eval = get_prompt(task, prompt)
            prompt_eval.user_message = prompt_eval.user_message.replace("{{csv_text}}", dataset_obj.df.to_string())

            expected_output_dir = get_directory_from_root(__file__, "expected_outputs")
            with open(os.path.join(expected_output_dir, task + "_" + dataset_obj.dirty_percentage + ".md"), 'r') as file:
                expected_output = file.read()

            for rf in response_files:
                with open(os.path.join(prompt_dir, rf), 'r', encoding='utf-8') as file:
                    file_content = file.read()
                    llm_test_cases[os.path.splitext(rf)[0]] = LLMTestCase(
                        input=prompt_eval.user_message,
                        actual_output=file_content,
                        expected_output=expected_output
                    )

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

            # è stato commentato su suggerimento dell'IDE, ma potrebbero esserci casini, questo è un reminder
            # metric_results = []

            for llm_name in llm_test_cases:

                with concurrent.futures.ThreadPoolExecutor() as executor:

                    futures = {}

                    for metric in metrics[task]:
                        futures[executor.submit(evaluate_metric, metric, llm_test_cases[llm_name])] = metric.name

                    metric_results = [future.result() for future in concurrent.futures.as_completed(futures)]

                    if task == "data_cleaning":
                        DataCleaningResult(
                            dataset_id = dataset,
                            task_name = task,
                            prompt_id = prompt,
                            llm_name = llm_name,
                            accuracy = find_metric_by_name(metric_results, 'Accuracy').scorer.score,
                            acc_reason = find_metric_by_name(metric_results, 'Accuracy').scorer.reason,
                            completeness = find_metric_by_name(metric_results, 'Completeness').scorer.score,
                            compl_reason = find_metric_by_name(metric_results, 'Completeness').scorer.reason,
                        ).to_csv(os.path.join(prompt_eval_dir, llm_name + ".csv"))

                    elif task == "data_profiling":
                        DataProfilingResult(
                            dataset_id = dataset,
                            task_name = task,
                            prompt_id = prompt,
                            llm_name = llm_name,
                            accuracy=  find_metric_by_name(metric_results, 'Accuracy').scorer.score,
                            acc_reason = find_metric_by_name(metric_results, 'Accuracy').scorer.reason,
                            completeness = find_metric_by_name(metric_results, 'Completeness').scorer.score,
                            compl_reason = find_metric_by_name(metric_results, 'Completeness').scorer.reason,
                        ).to_csv(os.path.join(prompt_eval_dir, llm_name + ".csv"))

                    else:
                        raise Exception("There is no result implementation for the following task: " + task)

