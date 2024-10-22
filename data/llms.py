from experiments.model.llm import LLM

llms = [
      LLM(
        name="GPT",
        model="gpt-4o-2024-08-06"
      ),
      LLM(
        name="Gemini",
        model="gemini-1.5-pro"
      ),
      #LLM(
      #  name="Mistral",
      #  model="mistral-large-2407"
      #)
    ]