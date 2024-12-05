from scripts.utils.setup import setup
setup()

import pandas as pd
import os

from scripts.utils.data_pollution import make_data_standardization_dirty
from scripts.utils.path import get_directory_from_root

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

task_dir = os.path.join(dirty_dir, 'data_standardization')

# make task datasets folder if it does not exist
if not os.path.exists(task_dir):
    os.makedirs(task_dir)

for percentage in percentages:
    df_dirty = df_clean.copy()
    make_data_standardization_dirty(df_dirty, percentage)
    csv_file_path = os.path.join(task_dir, 'data_standardization_' + str(int(percentage * 100)) + '.csv')
    df_dirty.to_csv(csv_file_path, index=False)
    print("Data standardization dataset (" + str(int(percentage * 100)) + "%) successfully saved in: " + csv_file_path)