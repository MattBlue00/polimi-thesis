from scripts.utils.constants import RANDOM_SEED
from scripts.utils.setup import setup
setup()

import os
import pandas as pd
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

# Define x and y coefficients for each city
coefficients = {
    "Houston": {"x": 0.0001, "y": 0.1},
    "Saratoga Springs": {"x": 0.00012, "y": 0.11},
    "Orlando": {"x": 0.00009, "y": 0.095},
    "Los Angeles": {"x": 0.00008, "y": 0.105}
}

# Apply coefficients based on city
df['acre_lot'] = df.apply(lambda row: row['price'] * coefficients[row['city']]['x'], axis=1)
df['house_size'] = df.apply(lambda row: int(row['price'] * coefficients[row['city']]['y']), axis=1)

# Shuffle del dataset
df_shuffled = df.sample(frac=1, random_state=RANDOM_SEED+1).reset_index(drop=True)

# directories
dirty_datasets_dir = os.path.join(datasets_dir, 'dirty')
os.makedirs(dirty_datasets_dir, exist_ok=True)

data_wrangling_dir = os.path.join(dirty_datasets_dir, 'dependency_discovery')
os.makedirs(data_wrangling_dir, exist_ok=True)

# save to CSV
wrangling_path = os.path.join(data_wrangling_dir, f'dependency_discovery.csv')
df.to_csv(wrangling_path, index=False)

print(f"Dependency discovery dataset was created.")