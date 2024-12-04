import numpy as np

from scripts.utils.data_pollution import inject_duplicates, make_single_value_outlier_detection_dirty, \
    make_single_value_data_standardization_dirty, make_single_value_data_imputation_dirty
from scripts.utils.setup import setup
setup()

import os
import pandas as pd
from scripts.utils.constants import PERCENTAGES, RANDOM_SEED
from scripts.utils.path import get_directory_from_root

# paths
datasets_dir = get_directory_from_root(__file__, 'datasets')
clean_dataset_path = os.path.join(datasets_dir, 'df_clean.csv')

# read clean dataset
df = pd.read_csv(clean_dataset_path)

# directories
dirty_datasets_dir = os.path.join(datasets_dir, 'dirty')
os.makedirs(dirty_datasets_dir, exist_ok=True)

data_cleaning_dir = os.path.join(dirty_datasets_dir, 'data_cleaning')
os.makedirs(data_cleaning_dir, exist_ok=True)

data_cleaning_no_dirty_duplicates_dir = os.path.join(data_cleaning_dir, 'no_dirty_duplicates')
os.makedirs(data_cleaning_no_dirty_duplicates_dir, exist_ok=True)

# create dirty datasets
for perc in PERCENTAGES:
    # copy the original dataset
    df_modified = df.copy()

    duplicated_df = inject_duplicates(df_modified, perc / 100)

    # Aggiunge una nuova colonna 'old_index' che contiene gli indici originali
    duplicated_df['old_index'] = duplicated_df.index

    # Effettua lo shuffle casuale del dataset
    shuffled_df = duplicated_df.sample(frac=1, random_state=RANDOM_SEED).reset_index(drop=True)

    # Creiamo una mappatura tra vecchi indici e nuovi indici
    old_to_new_index = {row['old_index']: new_index for new_index, row in shuffled_df.iterrows()}

    # Funzione per aggiornare la colonna 'duplicate' utilizzando 'old_index'
    def update_duplicates(value):
        if value == -1 or value == "-1":  # Nessun duplicato
            return -1
        else:
            # Traduci i vecchi indici in nuovi indici
            indices = map(int, str(value).split(','))
            updated_indices = [old_to_new_index[idx] for idx in indices]
            return ','.join(map(str, updated_indices))

    # Applica la funzione alla colonna 'duplicate'
    shuffled_df['duplicate'] = shuffled_df['duplicate'].apply(update_duplicates)

    # Rimuove la colonna temporanea 'old_index'
    shuffled_df.drop(columns=['old_index'], inplace=True)

    negative_duplicates = shuffled_df[shuffled_df['duplicate'] == -1]

    # Seleziona casualmente le righe da rimuovere
    rows_to_remove = negative_duplicates.sample(n=perc, random_state=RANDOM_SEED).index

    # Elimina le righe selezionate dal dataframe
    shuffled_df.drop(index=rows_to_remove, inplace=True)

    col_map = {
        0: "brokered_by",
        1: "status",
        2: "price",
        3: "bed",
        4: "bath",
        5: "acre_lot",
        6: "street",
        7: "city",
        8: "state",
        9: "zip_code",
        10: "house_size",
        11: "prev_sold_date"
    }

    # Genera indici casuali per le celle
    np.random.seed(RANDOM_SEED)
    total_cells = int(shuffled_df.shape[0] * (shuffled_df.shape[1] - 1) * (perc / 100))
    print("Cells to make dirty: " + str(total_cells)) # Numero totale di sporcature richieste
    rows = np.random.randint(0, shuffled_df.shape[0], total_cells)
    cols = np.random.randint(0, shuffled_df.shape[1] - 1, total_cells)

    # Combina righe e colonne in una lista di tuple (maschera)
    mask = list(zip(rows, cols))

    # Definizione dei tipi di sporcature
    noise_types = ['outlier_detection', 'data_standardization', 'data_imputation']

    # Colonne applicabili per ciascun tipo di sporcatura
    outlier_columns = {2, 3, 4, 5, 10}
    standardization_columns = {1, 2, 3, 4, 6, 8, 10, 11}

    # Filtra la maschera in base alle colonne applicabili
    outlier_mask = [cell for cell in mask if cell[1] in outlier_columns]
    standardization_mask = [cell for cell in mask if cell[1] in standardization_columns]

    # Determina il numero di celle da assegnare a ciascun tipo
    cells_per_type = total_cells // 3

    # Assegna celle alle maschere rispettando i limiti
    grouped_masks = {
        'outlier_detection': outlier_mask[:cells_per_type],
        'data_standardization': standardization_mask[:cells_per_type],
    }

    # Rimuovi le celle già assegnate
    remaining_mask = [cell for cell in mask if
                      cell not in grouped_masks['outlier_detection'] and cell not in grouped_masks[
                          'data_standardization']]

    # Assegna le rimanenti celle alla imputation_mask (può includere tutte le colonne)
    grouped_masks['data_imputation'] = remaining_mask[:cells_per_type]

    # Gestisci le celle residue per assicurarti che il totale sia esatto
    remaining_cells = total_cells - sum(len(group) for group in grouped_masks.values())
    if remaining_cells > 0:
        # Distribuisci le celle residue tra le maschere (ad esempio, a round-robin)
        for i, key in enumerate(grouped_masks):
            if remaining_cells == 0:
                break
            grouped_masks[key].append(remaining_mask[cells_per_type + i])
            remaining_cells -= 1

    dirty_df = shuffled_df.copy()

    # Applica le sporcature
    for noise_type, cell_group in grouped_masks.items():
        for row, col in cell_group:
            if noise_type == 'outlier_detection':
                dirty_df.iat[row, col] = make_single_value_outlier_detection_dirty(shuffled_df.iat[row, col], col_map[col], shuffled_df)
            elif noise_type == 'data_standardization':
                dirty_df.iat[row, col] = make_single_value_data_standardization_dirty(shuffled_df.iat[row, col], col_map[col])
            elif noise_type == 'data_imputation':
                dirty_df.iat[row, col] = make_single_value_data_imputation_dirty(shuffled_df.iat[row, col], col_map[col])
            else:
                raise ValueError('Unknown noise type.')

    # save to CSV
    cleaning_path = os.path.join(data_cleaning_no_dirty_duplicates_dir, f'data_cleaning_{str(perc)}.csv')
    dirty_df.to_csv(cleaning_path, index=False)

    print(f"Data Cleaning {perc}% dataset was created.")