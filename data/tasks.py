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
    ]),
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
        ]
    )]

def get_prompt(task_name, prompt_id):
    for task in tasks:
        if task.name == task_name:
            for prompt in task.prompts:
                if str(prompt.id) == str(prompt_id):
                    return prompt

    raise Exception("Prompt " + str(prompt_id) + " not found for task " + str(task_name))