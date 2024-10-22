from experiments.model.prompt import Prompt
from experiments.model.task import Task

tasks = [
    Task(
        name="data_cleaning",
        prompts=[
            Prompt(
                prompt_id=1,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data cleaning on it?",
            ),
            Prompt(
                prompt_id=2,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data cleaning on it? Let's think step by step.",
            ),
            Prompt(
                prompt_id=3,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data cleaning on it?",
                system_message="You are a data quality expert. For this reason, you help users by providing detailed answers that stick to the task and dataset you are given. Be the most accurate and complete you can.",
            ),
            Prompt(
                prompt_id=4,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data cleaning on it? Let's think step by step.",
                system_message="You are a data quality expert. For this reason, you help users by providing detailed answers that stick to the task and dataset you are given. Be the most accurate and complete you can.",
            )
    ]),
    Task(
        name="data_profiling",
        prompts=[
            Prompt(
                prompt_id=1,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data profiling on it?"
            ),
            Prompt(
                prompt_id=2,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data profiling on it? Let's think step by step."
            ),
            Prompt(
                prompt_id=3,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data profiling on it?",
                system_message="You are a data quality expert. For this reason, you help users by providing detailed answers that stick to the task and dataset you are given. Be the most accurate and complete you can.",
            ),
            Prompt(
                prompt_id=4,
                user_message="Consider this dataset:\n{{csv_text}}\nCan you do data profiling on it? Let's think step by step.",
                system_message="You are a data quality expert. For this reason, you help users by providing detailed answers that stick to the task and dataset you are given. Be the most accurate and complete you can.",
            )
        ]
    )]