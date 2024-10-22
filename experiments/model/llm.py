from openai import OpenAI
from mistralai import Mistral
import google.generativeai as genai
import os

class LLM:

  def __init__(self, name, model):
    self.name = name
    self.model = model

  def _get_response_from_gpt(self, prompt):

    client = OpenAI(
      api_key=os.getenv('OPEN_AI_KEY'),
    )

    messages = []

    if prompt.system_message is not None:
      messages.append({"role": "system", "content": prompt.system_message})

    messages.append({"role": "user", "content": prompt.user_message})

    chat_completion = client.chat.completions.create(
      messages=messages,
      model=self.model,
      temperature=0,
      max_completion_tokens=16384
    )

    return chat_completion.choices[0].message.content

  def _get_response_from_gemini(self, prompt):

    generation_config = {
      "temperature": 0
    }

    if prompt.system_message is not None:
      model = genai.GenerativeModel(
        model_name=self.model,
        generation_config=generation_config,
        system_instruction=prompt.system_message
      )
    else:
      model = genai.GenerativeModel(
        model_name=self.model,
        generation_config=generation_config
      )

    chat_session = model.start_chat(history=[])

    return chat_session.send_message(prompt.user_message).text

  def _get_response_from_mistral(self, prompt):

    client = Mistral(api_key=os.getenv('MISTRAL_API_KEY'))

    messages = []

    if prompt.system_message is not None:
      messages.append({"role": "system", "content": prompt.system_message})

    messages.append({"role": "user", "content": prompt.user_message})

    chat_response = client.chat.complete(
        model=self.model,
        messages=messages,
        temperature=0,
    )

    return chat_response.choices[0].message.content

  def get_response(self, prompt):

    if self.name == "GPT":
      return self._get_response_from_gpt(prompt)

    elif self.name == "Gemini":
      return self._get_response_from_gemini(prompt)

    elif self.name == "Mistral":
      return self._get_response_from_mistral(prompt)

    else:
      raise ValueError("It was not possible to get an answer from " + self.name + " because no LLM-specific implementation of 'get_response' was provided.")