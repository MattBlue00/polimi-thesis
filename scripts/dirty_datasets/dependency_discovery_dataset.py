from scripts.utils.constants import RANDOM_SEED
from scripts.utils.setup import setup
setup()

import os
import pandas as pd
import numpy as np
from scripts.utils.path import get_directory_from_root

# paths
datasets_dir = get_directory_from_root(__file__, 'datasets')
clean_dataset_path = os.path.join(datasets_dir, 'df_clean.csv')

# read clean dataset
df = pd.read_csv(clean_dataset_path)

# Definizione delle città target con stati e zip code corrispondenti
target_cities = [
    ("Houston", "Texas", 77030),
    ("Saratoga Springs", "Utah", 84043),
    ("Orlando", "Florida", 32828),
    ("Los Angeles", "California", 90064)
]

# Ripetizione ciclica delle città target per bilanciare il dataset
n = len(df)
repeated_cities = (target_cities * (n // len(target_cities) + 1))[:n]

# Aggiornamento delle colonne city, state e zip_code
df['city'], df['state'], df['zip_code'] = zip(*repeated_cities)

# Define a single x and y coefficient for all cities
coefficients = {
    "x": 0.0001,
    "y": 0.1
}

# Randomly select 10% of rows to remain unchanged
np.random.seed(RANDOM_SEED)
unchanged_indices = np.random.choice(df.index, size=int(0.1 * n), replace=False)

# Create new columns for acre_lot and house_size with conditions
acre_lot = []
house_size = []

for idx, row in df.iterrows():
    if idx in unchanged_indices:
        acre_lot.append(row.get('acre_lot', np.nan))  # Preserve existing value or NaN if missing
        house_size.append(row.get('house_size', np.nan))
    else:
        acre_lot.append(row['price'] * coefficients['x'])
        house_size.append(int(row['price'] * coefficients['y']))

# Update the dataframe
df['acre_lot'] = acre_lot
df['house_size'] = house_size

# Shuffle del dataset
df_shuffled = df.sample(frac=1, random_state=RANDOM_SEED+1).reset_index(drop=True)

# directories
dirty_datasets_dir = os.path.join(datasets_dir, 'dirty')
os.makedirs(dirty_datasets_dir, exist_ok=True)

data_wrangling_dir = os.path.join(dirty_datasets_dir, 'dependency_discovery')
os.makedirs(data_wrangling_dir, exist_ok=True)

# save to CSV
wrangling_path = os.path.join(data_wrangling_dir, f'dependency_discovery.csv')
df_shuffled.to_csv(wrangling_path, index=False)

print(f"Dependency discovery dataset was created.")