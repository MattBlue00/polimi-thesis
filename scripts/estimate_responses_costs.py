import os
import pprint

from data.tasks import get_prompt
from scripts.utils.constants import LLM_INPUT_COSTS, LLM_OUTPUT_COSTS
from scripts.utils.fetch_datasets import load_dirty_datasets
from scripts.utils.path import get_directory_from_root, get_directory_from_dir_name
from scripts.utils.setup import setup
from scripts.utils.text_filter import filter_llm_response

setup()

import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4o")

responses_dir = get_directory_from_root(__file__, 'responses')  # responses directory

if not os.path.exists(responses_dir):
    raise Exception(
        "There is no 'responses' directory to work with. Consider running 'python -m scripts.get_responses_from_llms' before running this script.")

datasets = [d for d in os.listdir(responses_dir) if os.path.isdir(os.path.join(responses_dir, d))]

for dataset in datasets:

    dataset_dir = get_directory_from_dir_name(responses_dir, dataset)
    if not os.path.exists(dataset_dir):
        raise Exception(
            "There is no dataset directory to work with. Consider running 'python -m scripts.get_responses_from_llms' before running this script.")

    dataset_name = os.path.basename(dataset_dir)

    datasets_dir = get_directory_from_root(__file__, os.path.join("datasets", "dirty"))  # datasets directory
    if not os.path.exists(datasets_dir):
        raise Exception(
            "There is no 'datasets/dirty' directory to work with. Consider running 'python -m scripts.get_dirty_datasets' before running this script.")

    dataset_obj = None
    ds = load_dirty_datasets(datasets_dir,
                             "df_dirty_10")  # FIXME: aggiustare secondo parametro quando avremo più datasets
    for d in ds:
        if d.id == dataset:
            dataset_obj = d
            break
    if dataset_obj is None:
        raise Exception("Dataset not found")

    tasks = [t for t in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, t))]

    for task in tasks:

        task_dir = get_directory_from_dir_name(dataset_dir, task)
        if not os.path.exists(task_dir):
            raise Exception(
                "There is no task directory to work with. Consider running 'python -m scripts.get_responses_from_llms' before running this script.")

        task_name = os.path.basename(task_dir)

        responses_costs = {}

        prompts = [p for p in os.listdir(task_dir) if os.path.isdir(os.path.join(task_dir, p))]

        for prompt in prompts:

            prompt_dir = get_directory_from_dir_name(task_dir, prompt)
            if not os.path.exists(prompt_dir):
                raise Exception(
                    "There is no prompt directory to work with. Consider running 'python -m scripts.get_responses_from_llms' before running this script.")

            response_files = [r for r in os.listdir(prompt_dir) if os.path.isfile(os.path.join(prompt_dir, r))]

            for rf in response_files:

                with open(os.path.join(prompt_dir, rf), 'r', encoding='utf-8') as file:

                    prompt = get_prompt(os.path.basename(task_dir), os.path.basename(prompt_dir))
                    prompt_copy = prompt.copy()
                    prompt_copy.user_message = prompt_copy.user_message.replace("{{csv_text}}", dataset_obj.df.to_string())
                    if prompt.system_message is not None:
                        prompt_str = prompt_copy.system_message + "\n" + prompt_copy.user_message
                    else:
                        prompt_str = prompt_copy.user_message

                    file_content = file.read()
                    llm_response_filtered = filter_llm_response(file_content)

                    input_tokens = len(encoding.encode(prompt_str))
                    output_tokens = len(encoding.encode(llm_response_filtered))

                    llm_name = os.path.splitext(os.path.basename(rf))[0]
                    responses_costs[llm_name] = responses_costs.get(llm_name, 0) + (input_tokens * LLM_INPUT_COSTS[llm_name]) + (output_tokens * LLM_OUTPUT_COSTS[llm_name])

        print(f"Responses mean costs for {dataset_name}, {task_name}:")
        responses_mean_costs = {k: v / len(prompts) for k, v in responses_costs.items()}
        pprint.pprint(responses_costs)