from deepeval.models import DeepEvalBaseLLM

from data.llms import get_llm
from experiments.model.llm import BaseLLM
from experiments.model.prompt import QuestionPrompt


class GeminiEvaluator(DeepEvalBaseLLM):

    def __init__(self):
        super().__init__()
        self.cost = 0.0

    def load_model(self):
        return get_llm("Gemini")

    def generate(self, prompt: str) -> str:
        chat_model = self.load_model()
        model_response = chat_model.get_response(
            QuestionPrompt(
                prompt_id="evaluator",
                user_message=prompt
            )
        )
        # self.cost += model_response.cost
        return model_response

    async def a_generate(self, prompt: str) -> str:
        raise Exception("Async evaluation is not permitted here.")

    def get_model_name(self):
        return "Gemini (gemini-1.5-pro) Evaluator"


class LlamaEvaluator(DeepEvalBaseLLM):

    def __init__(self):
        super().__init__()
        self.cost = 0.0

    def load_model(self):
        return get_llm("Llama")

    def generate(self, prompt: str) -> str:
        chat_model = self.load_model()
        model_response = chat_model.get_response(
            QuestionPrompt(
                prompt_id="evaluator",
                user_message=prompt
            )
        )
        # self.cost += model_response.cost
        return model_response

    async def a_generate(self, prompt: str) -> str:
        raise Exception("Async evaluation is not permitted here.")

    def get_model_name(self):
        return "Llama (llama-3.2-40B) Evaluator"

class GPTEvaluator(DeepEvalBaseLLM):
    def __init__(self):
        self.cost = 0.0
        super().__init__()

    def load_model(self):
        return get_llm("GPT")

    def generate(self, prompt: str) -> str:
        chat_model = self.load_model()
        model_response = chat_model.get_response(
            QuestionPrompt(
                prompt_id="evaluator",
                user_message=prompt
            )
        )
        #self.cost += model_response.cost
        return model_response

    async def a_generate(self, prompt: str) -> str:
        raise Exception("Async evaluation is not permitted here.")

    def get_model_name(self):
        return "GPT (gpt-4o) Evaluator"