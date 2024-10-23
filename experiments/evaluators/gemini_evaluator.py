from deepeval.models import DeepEvalBaseLLM

from experiments.model.prompt import Prompt


class GeminiEvaluator(DeepEvalBaseLLM):

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.cost = 0.0

    def load_model(self):
        return self.model

    def generate(self, prompt: str) -> str:
        chat_model = self.load_model()
        model_response = chat_model.get_response(
            Prompt(
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