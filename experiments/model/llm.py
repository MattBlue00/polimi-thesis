from abc import ABC, abstractmethod

import anthropic
from openai import OpenAI
from mistralai import Mistral as MistralClient
import google.generativeai as genai
import os

import transformers
import torch

class BaseLLM(ABC):

    def __init__(self, name, model_name):
        self.name = name
        self.model_name = model_name

    @abstractmethod
    def get_response(self, prompt) -> str:
        pass

class GPT(BaseLLM):

    def __init__(self, model_name):
        super().__init__(name="GPT", model_name=model_name)

    def get_response(self, prompt) -> str:

        client = OpenAI(
            api_key=os.getenv('OPEN_AI_KEY'),
        )

        messages = []

        if prompt.system_message is not None:
            messages.append({"role": "system", "content": prompt.system_message})

        messages.append({"role": "user", "content": prompt.user_message})

        chat_completion = client.chat.completions.create(
            messages=messages,
            model=self.model_name,
            temperature=0,
            max_completion_tokens=16384
            )

        return chat_completion.choices[0].message.content


class Gemini(BaseLLM):

    def __init__(self, model_name):
        super().__init__(name="Gemini", model_name=model_name)

    def get_response(self, prompt) -> str:

        generation_config = {
            "temperature": 0
        }

        if prompt.system_message is not None:
            model = genai.GenerativeModel(
                model_name=self.model_name,
                generation_config=generation_config,
                system_instruction=prompt.system_message
            )
        else:
            model = genai.GenerativeModel(
                model_name=self.model_name,
                generation_config=generation_config
            )

        chat_session = model.start_chat(history=[])

        return chat_session.send_message(prompt.user_message).text


class Mistral(BaseLLM):

    def __init__(self, model_name):
        super().__init__(name="Mistral", model_name=model_name)

    def get_response(self, prompt) -> str:

        client = MistralClient(api_key=os.getenv('MISTRAL_API_KEY'))

        messages = []

        if prompt.system_message is not None:
            messages.append({"role": "system", "content": prompt.system_message})

        messages.append({"role": "user", "content": prompt.user_message})

        chat_response = client.chat.complete(
            model=self.model_name,
            messages=messages,
            temperature=0,
        )

        return chat_response.choices[0].message.content


class Llama(BaseLLM):

    def __init__(self, model_name):
        super().__init__(name="Llama", model_name=model_name)

        token = os.getenv('HUGGING_FACE_TOKEN')
        if not token:
            raise ValueError("Hugging Face token is not set in the environment variables.")

        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_name,
            #model_kwargs={"torch_dtype": torch.float32},
            device_map="auto"
        )

        print("Torch version: " + str(torch.__version__))
        print("CUDA available? " + str(torch.cuda.is_available()))
        print("Llama is active on device:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU")

    def get_response(self, prompt) -> str:

        messages = []

        if prompt.system_message is not None:
            messages.append({"role": "system", "content": prompt.system_message})

        messages.append({"role": "user", "content": prompt.user_message})

        with torch.cuda.amp.autocast(enabled=False):
            torch.cuda.empty_cache()
            outputs = self.pipeline(
                messages,
                do_sample=False,
                temperature=None,
                top_p=None,
                max_new_tokens=1024
            )
        return outputs[0]["generated_text"][-1]


class Claude(BaseLLM):

    def __init__(self, model_name: str) -> None:
        super().__init__(name="Claude", model_name=model_name)

    def get_response(self, prompt) -> str:
        client = anthropic.Anthropic(
            api_key=os.getenv('CLAUDE_API_KEY'),
        )
        system_message = ""
        if prompt.system_message is not None:
            system_message = prompt.system_message
        message = client.messages.create(
            model=self.model_name,
            max_tokens=8192,
            temperature=0,
            system=system_message,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt.user_message
                        }
                    ]
                }
            ]
        )
        return message.content[0].text
