from scripts.utils.setup import setup
setup()

import pandas as pd
import os

from scripts.utils.path import get_directory_from_root
from scripts.utils.data_pollution import inject_duplicates

'''
Questo script genera un dataset uguale all'originale, ma con tot righe in più duplicate.
Viene aggiunta la colonna 'duplicate' per tenere traccia di quale riga è duplicato di un'altra.
Lo shuffling verrà fatto successivamente.
'''

percentages = [0.1, 0.3, 0.5]

datasets_dir = get_directory_from_root(__file__, 'datasets')  # datasets directory

# if datasets directory does not exist, raise an exception
if not os.path.exists(datasets_dir):
    raise Exception("There is no 'datasets' directory to work with. Consider running 'python -m scripts.get_clean_dataset' before running this script.")

df_clean = pd.read_csv(datasets_dir + '/df_clean.csv')

dirty_dir = os.path.join(datasets_dir, 'dirty')

# make dirty datasets folder if it does not exist
if not os.path.exists(dirty_dir):
    os.makedirs(dirty_dir)

task_dir = os.path.join(dirty_dir, 'data_deduplication')

# make task datasets folder if it does not exist
if not os.path.exists(task_dir):
    os.makedirs(task_dir)

# make duplicates no shuffling folder
duplicates_dir = os.path.join(task_dir, 'duplicates_no_shuffling')

# make duplicates no shuffling folder if it does not exist
if not os.path.exists(duplicates_dir):
    os.makedirs(duplicates_dir)

for percentage in percentages:
    # injects duplicates
    duplicated_df = inject_duplicates(df_clean.copy(), percentage)
    csv_file_path = os.path.join(duplicates_dir, 'data_deduplication_no_shuffling_' + str(int(percentage * 100)) + '.csv')
    duplicated_df.to_csv(csv_file_path, index=False)
    print("Data deduplication dataset (" + str(int(percentage * 100)) + "%) successfully saved in: " + csv_file_path)