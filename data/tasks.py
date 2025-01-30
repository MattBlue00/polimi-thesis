from experiments.model.prompt import QuestionPrompt
from experiments.model.task import Task

tasks = [
    Task(
        name="data_cleaning",
        prompts=[
            QuestionPrompt(
                prompt_id=1,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data cleaning on it?",
            ),
            QuestionPrompt(
                prompt_id=2,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data cleaning on it? Let's think step by step.",
            ),
            QuestionPrompt(
                prompt_id=3,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data cleaning on it?",
                system_message="You are a data quality expert. For this reason, you help users by providing detailed answers that stick to the task and dataset you are given. Be the most accurate and complete you can.",
            ),
            QuestionPrompt(
                prompt_id=4,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data cleaning on it? Let's think step by step.",
                system_message="You are a data quality expert. For this reason, you help users by providing detailed answers that stick to the task and dataset you are given. Be the most accurate and complete you can.",
            )
        ],
        tab_instruction="This is a Data Cleaning task. The goal of this task is to provide a clean version of the given dataset.",
        tab_question="Can you do Data Cleaning on the given dataset?"
    ),
    Task(
        name="data_profiling",
        prompts=[
            QuestionPrompt(
                prompt_id=1,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data profiling on it?"
            ),
            QuestionPrompt(
                prompt_id=2,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data profiling on it? Let's think step by step."
            ),
            QuestionPrompt(
                prompt_id=3,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data profiling on it?",
                system_message="You are a data quality expert. For this reason, you help users by providing detailed answers that stick to the task and dataset you are given. Be the most accurate and complete you can.",
            ),
            QuestionPrompt(
                prompt_id=4,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data profiling on it? Let's think step by step.",
                system_message="You are a data quality expert. For this reason, you help users by providing detailed answers that stick to the task and dataset you are given. Be the most accurate and complete you can.",
            )
        ],
        tab_instruction="This is a Data Profiling task. The goal of this task is to provide insights and statistics about the given dataset.",
        tab_question="Can you do Data Profiling on the given dataset?"
    ),
    Task(
        name="data_imputation",
        prompts=[
            QuestionPrompt(
                prompt_id=1,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data imputation on it?"
            ),
            QuestionPrompt(
                prompt_id=2,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data imputation on it? Let's think step by step."
            ),
            QuestionPrompt(
                prompt_id=3,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data imputation on it?",
                system_message="You are a data quality expert. For this reason, you help users by providing detailed answers that stick to the task and dataset you are given. Be the most accurate and complete you can.",
            ),
            QuestionPrompt(
                prompt_id=4,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data imputation on it? Let's think step by step.",
                system_message="You are a data quality expert. For this reason, you help users by providing detailed answers that stick to the task and dataset you are given. Be the most accurate and complete you can.",
            )
        ],
        tab_instruction="This is a Data Imputation task. The goal of this task is to provide an imputed version of the given dataset.",
        tab_question="Can you do Data Imputation on the given dataset?"
    ),
    Task(
        name="data_deduplication",
        prompts=[
            QuestionPrompt(
                prompt_id=1,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data deduplication on it?"
            ),
            QuestionPrompt(
                prompt_id=2,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data deduplication on it? Let's think step by step."
            ),
            QuestionPrompt(
                prompt_id=3,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data deduplication on it?",
                system_message="You are a data quality expert. For this reason, you help users by providing detailed answers that stick to the task and dataset you are given. Be the most accurate and complete you can.",
            ),
            QuestionPrompt(
                prompt_id=4,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data deduplication on it? Let's think step by step.",
                system_message="You are a data quality expert. For this reason, you help users by providing detailed answers that stick to the task and dataset you are given. Be the most accurate and complete you can.",
            )
        ],
        tab_instruction="This is a Data Deduplication task. The goal of this task is to provide a deduplicated version of the given dataset.",
        tab_question="Can you do Data Deduplication on the given dataset?"
    ),
    Task(
        name="outlier_detection",
        prompts=[
            QuestionPrompt(
                prompt_id=1,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do outlier detection on it?"
            ),
            QuestionPrompt(
                prompt_id=2,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do outlier detection on it? Let's think step by step."
            ),
            QuestionPrompt(
                prompt_id=3,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do outlier detection on it?",
                system_message="You are a data quality expert. For this reason, you help users by providing detailed answers that stick to the task and dataset you are given. Be the most accurate and complete you can.",
            ),
            QuestionPrompt(
                prompt_id=4,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do outlier detection on it? Let's think step by step.",
                system_message="You are a data quality expert. For this reason, you help users by providing detailed answers that stick to the task and dataset you are given. Be the most accurate and complete you can.",
            )
        ],
        tab_instruction="This is an Outlier Detection task. The goal of this task is to provide the outliers of the given dataset.",
        tab_question="Can you do Outlier Detection on the given dataset?"
    ),
    Task(
        name="data_wrangling",
        prompts=[
            QuestionPrompt(
                prompt_id=1,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data wrangling on it?"
            ),
        ],
        tab_instruction="This is a Data Wrangling task. The goal of this task is to provide a correctly structured version of the given dataset.",
        tab_question="Can you do Data Wrangling on the given dataset?"
    ),
    Task(
        name="data_standardization",
        prompts=[
            QuestionPrompt(
                prompt_id=1,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data standardization on it?"
            ),
        ],
        tab_instruction="This is a Data Standardization task. The goal of this task is to provide a standardized version of the given dataset.",
        tab_question="Can you do Data Standardization on the given dataset?"
    ),
    Task(
        name="dependency_discovery",
        prompts=[
            QuestionPrompt(
                prompt_id=1,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do dependency discovery on it?"
            ),
        ],
        tab_instruction="This is a Dependency Discovery task. The goal of this task is to provide the functional dependencies among the columns of the given dataset.",
        tab_question="Can you do Dependency Discovery on the given dataset?"
    ),
]

def get_prompt(task_name, prompt_id):
    for task in tasks:
        if task.name == task_name:
            for prompt in task.prompts:
                if str(prompt.id) == str(prompt_id):
                    return prompt

    raise ValueError("Prompt " + str(prompt_id) + " not found for task " + str(task_name))