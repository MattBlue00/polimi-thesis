import time
from abc import ABC, abstractmethod

import anthropic
from anthropic import APIError as AnthropicAPIError
from google.api_core.exceptions import GoogleAPIError
from openai import OpenAI, APIError as OpenAPIError
from mistralai import Mistral as MistralClient
import google.generativeai as genai
import os

from groq import Groq, APITimeoutError, InternalServerError, GroqError


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

        response = ""

        while response == "":
            try:
                response = chat_completion.choices[0].message.content
            except OpenAPIError as e:
                print(f"OpenAI error: {type(e).__name__}. Retrying in a minute.")
                time.sleep(60)
                print("Retrying now!")

        return response


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

        response = ""

        while response == "":
            try:
                response = chat_session.send_message(prompt.user_message).text
            except GoogleAPIError as e:
                print(f"Google AI error: {type(e).__name__}. Retrying in a minute.")
                time.sleep(60)
                print("Retrying now!")

        return response


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

    def get_response(self, prompt) -> str:

        client = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
        )

        messages = []

        if prompt.system_message is not None:
            messages.append({"role": "system", "content": prompt.system_message})

        messages.append({"role": "user", "content": prompt.user_message})

        chat_completion = client.chat.completions.create(
            messages=messages,
            model=self.model_name,
            max_tokens=32768,
            temperature=0
        )

        response = ""

        while response == "":
            try:
                response = chat_completion.choices[0].message.content
            except APITimeoutError:
                print("Request timed out. Retrying in a minute.")
                time.sleep(60)
                print("Retrying now!")
            except InternalServerError:
                print("Groq is temporarily unavailable. Retrying in a minute.")
                time.sleep(60)
                print("Retrying now!")
            except GroqError as e:
                print(f"Groq error: {type(e).__name__}. Retrying in a minute.")
                time.sleep(60)
                print("Retrying now!")

        return chat_completion.choices[0].message.content


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

        response = ""

        while response == "":
            try:
                response = client.messages.create(
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
                ).content[0].text
            except AnthropicAPIError as e:
                print(f"Anthropic error: {type(e).__name__}. Retrying in a minute.")
                time.sleep(60)
                print("Retrying now!")

        return response
