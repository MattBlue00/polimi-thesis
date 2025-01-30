import os
from abc import ABC, abstractmethod

import torch
from transformers import LlamaTokenizer, LlamaForCausalLM, AutoTokenizer, AutoModelForCausalLM

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

        self.device = device
        self.tokenizer = LlamaTokenizer.from_pretrained(model_name, use_fast=False)
        self.model = LlamaForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch_dtype,
            device_map="auto",  # Permette una gestione automatica del device
            offload_folder=model_dir
        ).to(device)

    def get_response(self, instruction: str, dataset: str, question: str) -> str:
        """
        Genera una risposta basata sull'istruzione, dataset e domanda forniti.
        """
        prompt = ("""Below is an instruction that describes a task, paired with an input tabular dataset. "
                  "Write a response that appropriately answers the question.\n\n"
                  "### Instruction:\n{instruction}\n\n"
                  "### Input:\n{input}\n\n"
                  "### Question:\n{question}\n\n"
                  "### Response:""")

        # Format dataset properly
        formatted_dataset = format_dataset_for_tablellama(dataset)

        # Costruzione del prompt finale
        prompt = prompt.format(instruction=instruction, input=formatted_dataset, question=question)

        # Tokenizzazione con troncamento
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=8000
        ).to(self.device)

        # Generazione della risposta con parametri deterministici
        outputs = self.model.generate(
            inputs.input_ids,
            max_new_tokens=8000,
            do_sample=False,  # Disabilitazione del campionamento per massimo determinismo
            top_p=None  # Disabilitato per evitare casualità
        )

        # Decodifica della risposta evitando di includere il prompt originale
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Rimozione della parte di input dalla risposta, mantenendo solo il testo generato
        response = response[len(prompt):].strip()

        return response


class TableGPT(BaseTabularLLM):

    def __init__(self, model_name="tablegpt/TableGPT2-7B"):
        super().__init__(name="TableGPT", model_name=model_name)

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

        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch_dtype,
            device_map="auto",  # Permette una gestione automatica del device
            offload_folder=model_dir
        ).to(device)

    def get_response(self, instruction: str, dataset: str, question: str) -> str:
        """
        Genera una risposta basata sulla tabella pandas e la domanda fornita.
        """
        prompt = ("""Below is an instruction that describes a task, paired with an input tabular dataset. "
                  "Write a response that appropriately answers the question.\n\n"
                  "### Instruction:\n{instruction}\n\n"
                  "### Input:\n{input}\n\n"
                  "### Question:\n{question}\n\n"
                  "### Response:""")

        # Costruzione del prompt finale
        prompt = prompt.format(instruction=instruction, input=dataset, question=question)

        messages = [
            {"role": "user", "content": prompt},
        ]
        text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )

        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)
        generated_ids = self.model.generate(**model_inputs, max_new_tokens=8192)
        generated_ids = [
            output_ids[len(input_ids):]
            for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response
