from scripts.utils.setup import setup
print("Setting up the environment...")
setup(dotenv=True)

from data.llms import get_llm
from experiments.model.prompt import Prompt

llm = get_llm("Llama")
prompt = Prompt(1, "Who are you?")
print(llm.get_response(prompt))