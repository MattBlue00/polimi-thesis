from abc import ABC, abstractmethod

from openai import OpenAI
from mistralai import Mistral as MistralClient
import google.generativeai as genai
from huggingface_hub import login
import os

import transformers
import torch

from scripts.utils.path import get_directory_from_root


class LLM(ABC):

    def __init__(self, name, model_name):
        self.name = name
        self.model_name = model_name

    @abstractmethod
    def get_response(self, prompt):
        pass

class GPT(LLM):

    def __init__(self, model_name):
        super().__init__(name="GPT", model_name=model_name)

    def get_response(self, prompt):

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


class Gemini(LLM):

    def __init__(self, model_name):
        super().__init__(name="Gemini", model_name=model_name)

    def get_response(self, prompt):

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


class Mistral(LLM):

    def __init__(self, model_name):
        super().__init__(name="Mistral", model_name=model_name)

    def get_response(self, prompt):

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


class Llama(LLM):

    def __init__(self, model_name):
        super().__init__(name="Llama", model_name=model_name)

        token = os.getenv('HUGGING_FACE_TOKEN')

        try:
            print("Logging into HuggingFace...")
            login(token=token)
            print("Logged in successfully!")

        except Exception as e:
            print(f"Error while logging into HuggingFace: {e}")

        self.pipeline = transformers.pipeline(
            "text-generation",
            model=self.model_name,
            model_kwargs={"torch_dtype": torch.bfloat16},
            device_map="auto",
        )

    def get_response(self, prompt):

        messages = []

        if prompt.system_message is not None:
            messages.append({"role": "system", "content": prompt.system_message})

        messages.append({"role": "user", "content": prompt.user_message})

        outputs = self.pipeline(
            messages,
            temperature=0.0,
        )
        return outputs[0]["generated_text"][-1]