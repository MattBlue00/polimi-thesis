from abc import ABC

from data.batch import Batch

class BasePrompt(ABC):

    def __init__(self, user_message: str, system_message: str = None):
        self.user_message = user_message
        self.system_message = system_message

class QuestionPrompt(BasePrompt):

    def __init__(self, prompt_id: int, user_message: str, system_message: str = None):
        super().__init__(user_message, system_message)
        self.id = prompt_id

class EvaluationPrompt(BasePrompt):

    def __init__(self, batch: Batch, system_message: str = None):
        user_message ="""
Consider if the piece of text I will give you provides a solution for the following problems:
{problems_list}

Assign a score of 0 or 1 to each of the above statements based on the fact that they are false or true. Answer with only a list of ordered, whitespace-separated numbers. 
The answer must be given considering this text:

{llm_response_filtered}"""
        super().__init__(user_message, system_message)
        self.batch = batch