from scripts.utils.constants import RANDOM_SEED
from scripts.utils.setup import setup
setup()

import pandas as pd
import os

from scripts.utils.path import get_directory_from_root

'''
Questo script genera un dataset uguale all'originale, ma shuffled.
Rimane la colonna 'duplicate' per tenere traccia di quale riga è duplicato di un'altra.
'''

percentages = [0.1, 0.3, 0.5]

datasets_dir = get_directory_from_root(__file__, 'datasets')  # datasets directory

# if datasets directory does not exist, raise an exception
if not os.path.exists(datasets_dir):
    raise Exception("There is no 'datasets' directory to work with. Consider running 'python -m scripts.get_clean_dataset' before running this script.")

dirty_dir = os.path.join(datasets_dir, 'dirty')

# if dirty directory does not exist, raise an exception
if not os.path.exists(datasets_dir):
    raise Exception("There is no 'dirty' directory to work with. Consider running 'python -m scripts.data_deduplication_dataset' before running this script.")


task_dir = os.path.join(dirty_dir, 'data_deduplication')

# if task directory does not exist, raise an exception
if not os.path.exists(datasets_dir):
    raise Exception("There is no 'task' directory to work with. Consider running 'python -m scripts.data_deduplication_dataset' before running this script.")

# make duplicates dirty shuffled folder
shuffled_dataset_dir = os.path.join(task_dir, 'duplicates_dirty_shuffled_with_duplicate_column')

# make duplicates dirty shuffled if it does not exist
if not os.path.exists(shuffled_dataset_dir):
    os.makedirs(shuffled_dataset_dir)

dirty_datasets_dir = os.path.join(task_dir, 'duplicates_dirty_no_shuffle')

# if dirty datasets directory does not exist, raise an exception
if not os.path.exists(datasets_dir):
    raise Exception("There is no 'duplicates_dirty_no_shuffle' directory to work with. Consider running 'python -m scripts.data_deduplication_dataset' before running this script.")

for percentage in percentages:
    # Legge il dataset originale
    csv_file = f"data_deduplication_dirty_no_shuffling_{int(percentage * 100)}.csv"
    file_path = os.path.join(dirty_datasets_dir, csv_file)
    df = pd.read_csv(file_path, delimiter=';')

    # Aggiunge una nuova colonna 'old_index' che contiene gli indici originali
    df['old_index'] = df.index

    # Effettua lo shuffle casuale del dataset
    shuffled_df = df.sample(frac=1, random_state=RANDOM_SEED).reset_index(drop=True)

    # Creiamo una mappatura tra vecchi indici e nuovi indici
    old_to_new_index = {row['old_index']: new_index for new_index, row in shuffled_df.iterrows()}

    # Funzione per aggiornare la colonna 'duplicate' utilizzando 'old_index'
    def update_duplicates(value):
        if value == -1 or value == "-1":  # Nessun duplicato
            return -1
        else:
            # Traduci i vecchi indici in nuovi indici
            indices = map(int, str(value).split(','))
            updated_indices = [old_to_new_index[i] for i in indices]
            return ','.join(map(str, updated_indices))

    # Applica la funzione alla colonna 'duplicate'
    shuffled_df['duplicate'] = shuffled_df['duplicate'].apply(update_duplicates)

    # Rimuove la colonna temporanea 'old_index'
    shuffled_df.drop(columns=['old_index'], inplace=True)

    # Salva il dataset aggiornato
    output_file = f"shuffled_dirty_dataset_{int(percentage * 100)}.csv"
    output_path = os.path.join(shuffled_dataset_dir, output_file)
    shuffled_df.to_csv(output_path, sep=';', index=False)

    print(f"Dataset riorganizzato e salvato in {output_path}")

    # Crea una copia del dataset senza la colonna 'duplicate'
    df_without_duplicates = shuffled_df.drop(columns=['duplicate'])

    # Salva il nuovo dataset senza 'duplicate'
    output_file_without_duplicates = f"data_deduplication_{int(percentage * 100)}.csv"
    output_path_without_duplicates = os.path.join(task_dir, output_file_without_duplicates)
    df_without_duplicates.to_csv(output_path_without_duplicates, sep=';', index=False)

    print(f"Dataset senza 'duplicate' salvato in {output_path_without_duplicates}")