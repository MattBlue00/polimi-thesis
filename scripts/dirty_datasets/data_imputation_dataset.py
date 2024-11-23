from scripts.utils.math import divide_number
from scripts.utils.setup import setup
setup()

import os
import random
import pandas as pd
import numpy as np
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

data_imputation_dir = os.path.join(dirty_datasets_dir, 'data_imputation')
os.makedirs(data_imputation_dir, exist_ok=True)

# create dirty datasets
for perc in PERCENTAGES:
    # copy the original dataset
    df_modified = df.copy()

    # number of rows to replace
    n_rows_to_replace = int(len(df_modified) * (perc / 100))

    distributions = divide_number(perc, 3)

    for i, col in enumerate(df.columns):

        # randomly chooses the rows to replace
        indices_to_replace = df_modified.sample(n=n_rows_to_replace, random_state=RANDOM_SEED+i).index

        missing_values = []

        col_type = df_modified[col].dtype
        if col_type == object:
            # For object columns, we will use a mix of "-","Unknown", and ""
            missing_values.extend(["-" for _ in range(distributions[0])])
            missing_values.extend(["Unknown" for _ in range(distributions[1])])
            missing_values.extend(["" for _ in range(distributions[2])])
        elif col_type == float or col_type == int:
            # For numerical columns, we will use np.nan, -1, and ""
            missing_values.extend([np.nan for _ in range(distributions[0])])
            missing_values.extend([-1 for _ in range(distributions[1])])
            missing_values.extend(["" for _ in range(distributions[2])])
        else:
            raise ValueError(f"Unknown type: {col_type}.")

            # Shuffle the missing values list to distribute them randomly
        random.shuffle(missing_values)

        # Replacing the selected rows with corresponding missing values
        for idx, missing_value in zip(indices_to_replace, missing_values):
            df_modified.loc[idx, col] = missing_value

    # save to CSV
    imputation_path = os.path.join(data_imputation_dir, f'data_imputation_{str(perc)}.csv')
    df_modified.to_csv(imputation_path, index=False)

    print(f"Data Imputation {perc}% dataset was created.")