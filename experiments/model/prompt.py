from abc import ABC

class BasePrompt(ABC):

    def __init__(self, user_message: str, system_message: str = None):
        self.user_message = user_message
        self.system_message = system_message

class QuestionPrompt(BasePrompt):

    def __init__(self, prompt_id: int, user_message: str, system_message: str = None):
        super().__init__(user_message, system_message)
        self.id = prompt_id

class EvaluationPrompt(BasePrompt):

    def __init__(self, batch: str, user_message: str, system_message: str = None):
        super().__init__(user_message, system_message)
        self.batch = batch