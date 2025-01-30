from experiments.model.llm import GPT, Gemini, Mistral, Llama, Claude
from experiments.model.tabular_llm import TableLlama

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
    ]

tabular_llms = [
    TableLlama(
        model_name="osunlp/TableLlama"
    ),
    TableGPT(
        model_name="tablegpt/TableGPT2-7B"
    ),
    TableLLM(
        model_name="RUCKBReasoning/TableLLM-13b"
    )
]

def get_llm(llm_name):

    for llm in llms:
        if llm.name == llm_name:
            return llm

    raise ValueError(f"No such LLM: {llm_name}")

def get_tabular_llm(tabular_llm_name):

    for tab_llm in tabular_llms:
        if tab_llm.name == tabular_llm_name:
            return tab_llm

    raise ValueError(f"No such Tabular LLM: {tabular_llm_name}")