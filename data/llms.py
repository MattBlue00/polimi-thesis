from experiments.model.llm import GPT, Gemini, Mistral, Llama, Claude, TableLlama

llms = [
        #GPT(
        #    model_name="gpt-4o-2024-08-06"
        #),
        #Gemini(
        #    model_name="gemini-1.5-pro"
        #),
        #Claude(
        #    model_name="claude-3-5-sonnet-latest"
        #)
        #Mistral(
        #  model_name="mistral-large-2407"
        #),
        #Llama(
        #    model_name="meta-llama/Meta-Llama-3.1-8B-Instruct"
        #),
        TableLlama(
            model_name="osunlp/TableLlama"
        )
    ]

def get_llm(llm_name):

    for llm in llms:
        if llm.name == llm_name:
            return llm

    raise ValueError(f"No such llm: {llm_name}")