import os
from abc import ABC, abstractmethod

import torch
from transformers import LlamaTokenizer, LlamaForCausalLM

from scripts.utils.path import get_directory_from_root
from scripts.utils.tabular_llm_utils import format_dataset_for_tablellama


class BaseTabularLLM(ABC):

    def __init__(self, name, model_name):
        self.name = name
        self.model_name = model_name

    @abstractmethod
    def get_response(self, instruction: str, dataset: str, question: str) -> str:
        pass


class TableLlama(BaseTabularLLM):

    def __init__(self, model_name):
        super().__init__(name="TableLlama", model_name=model_name)

        # Creazione del modello e tokenizer
        model_dir = get_directory_from_root(__file__, "models")
        os.makedirs(model_dir, exist_ok=True)

        # Controllo se CUDA è disponibile, altrimenti uso la CPU
        if torch.cuda.is_available():
            device = torch.device("cuda")
            torch_dtype = torch.float16  # Float16 per prestazioni migliori su GPU
        else:
            device = torch.device("cpu")
            torch_dtype = torch.float32  # Manteniamo float32 per stabilità su CPU
            print("CUDA unavailable, using CPU.")

        self.tokenizer = LlamaTokenizer.from_pretrained(model_name, use_fast=False)
        self.model = LlamaForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch_dtype,
            device_map="auto",  # Permette una gestione automatica del device
            offload_folder=model_dir
        ).to(device)

    def get_response(self, instruction: str, dataset: str, question: str) -> str:

        base_prompt = """"
        Below is an instruction that describes a task, paired with an input that provides further context. Write a response that
        appropriately completes the request.

        ### Instruction:
        {instruction}

        ### Input:
        {input}

        ### Question:
        {question}

        ### Response:
        """

        formatted_dataset = format_dataset_for_tablellama(dataset)

        formatted_prompt = base_prompt.replace("{instruction}", instruction).replace("{input}", formatted_dataset).replace("{question}", question)

        '''
        inputs = self.tokenizer(formatted_prompt, return_tensors="pt").to(self.model.device)
        device = self.model.device
        inputs = inputs.to(device)
        outputs = self.model.generate(inputs.input_ids, max_new_tokens=4096)
        return self.tokenizer.decode(outputs[0])
        '''

        print(formatted_prompt)