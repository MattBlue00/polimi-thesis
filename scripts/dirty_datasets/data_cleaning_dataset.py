from scripts.utils.data_pollution import make_data_standardization_dirty, make_outlier_detection_dirty, \
    make_data_imputation_dirty, inject_duplicates
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

data_cleaning_dir = os.path.join(dirty_datasets_dir, 'data_cleaning')
os.makedirs(data_cleaning_dir, exist_ok=True)

# create dirty datasets
for perc in PERCENTAGES:
    # copy the original dataset
    df_modified = df.copy()

    make_outlier_detection_dirty(df_modified, perc / 100)

    make_data_standardization_dirty(df_modified, perc / 100)

    make_data_imputation_dirty(df_modified, perc / 100)

    duplicated_df = inject_duplicates(df_modified, perc / 100)

    # save to CSV
    cleaning_path = os.path.join(data_cleaning_dir, f'data_cleaning_{str(perc)}.csv')
    duplicated_df.to_csv(cleaning_path, index=False)

    print(f"Data Cleaning {perc}% dataset was created.")