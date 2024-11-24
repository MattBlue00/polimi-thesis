from scripts.utils.data_pollution import make_data_imputation_dirty
from scripts.utils.setup import setup
setup()

import os
import pandas as pd
from scripts.utils.constants import PERCENTAGES
from scripts.utils.path import get_directory_from_root

# paths
datasets_dir = get_directory_from_root(__file__, 'datasets')
clean_dataset_path = os.path.join(datasets_dir, 'df_clean.csv')

# read clean dataset
df = pd.read_csv(clean_dataset_path)

# directories
dirty_datasets_dir = os.path.join(datasets_dir, 'dirty')
os.makedirs(dirty_datasets_dir, exist_ok=True)

data_imputation_dir = os.path.join(dirty_datasets_dir, 'data_imputation')
os.makedirs(data_imputation_dir, exist_ok=True)

# create dirty datasets
for perc in PERCENTAGES:
    # copy the original dataset
    df_modified = df.copy()

    make_data_imputation_dirty(df_modified, perc / 100)

    # save to CSV
    imputation_path = os.path.join(data_imputation_dir, f'data_imputation_{str(perc)}.csv')
    df_modified.to_csv(imputation_path, index=False)

    print(f"Data Imputation {perc}% dataset was created.")