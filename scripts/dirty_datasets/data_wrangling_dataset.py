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

# merge columns
df['address'] = df['street'] + ', ' + df['city'] + ', ' + df['state']
df.drop(columns=['street', 'city', 'state'], inplace=True)

df['bedrooms_bathrooms'] = df['bed'].astype(str) + ', ' + df['bath'].astype(str)
df.drop(columns=['bed', 'bath'], inplace=True)

# directories
dirty_datasets_dir = os.path.join(datasets_dir, 'dirty')
os.makedirs(dirty_datasets_dir, exist_ok=True)

data_wrangling_dir = os.path.join(dirty_datasets_dir, 'data_wrangling')
os.makedirs(data_wrangling_dir, exist_ok=True)

# create dirty datasets
for perc in PERCENTAGES:
    # copy the original dataset
    df_modified = df.copy()

    # number of rows to replace
    n_rows_to_replace = int(len(df_modified) * (perc / 100))

    # randomly chooses the rows to replace
    indices_to_replace = df_modified.sample(n=n_rows_to_replace, random_state=RANDOM_SEED).index

    # replacing the selected rows with empty rows
    df_modified.loc[indices_to_replace] = ''

    # save to CSV
    wrangling_path = os.path.join(data_wrangling_dir, f'data_wrangling_{str(perc)}.csv')
    df_modified.to_csv(wrangling_path, index=False)

    print(f"Data Wrangling {perc}% dataset was created.")