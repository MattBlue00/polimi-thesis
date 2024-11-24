from scripts.utils.data_pollution import make_outlier_detection_dirty
from scripts.utils.math import round_to_significant_figures
from scripts.utils.setup import setup
setup()

import os
import pandas as pd
import random
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

outlier_detection_dir = os.path.join(dirty_datasets_dir, 'outlier_detection')
os.makedirs(outlier_detection_dir, exist_ok=True)

for perc in PERCENTAGES:
    # copy the original dataset
    df_modified = df.copy()

    make_outlier_detection_dirty(df_modified, perc/100)

    # save to CSV
    outlier_path = os.path.join(outlier_detection_dir, f'outlier_detection_{str(perc)}.csv')
    df_modified.to_csv(outlier_path, index=False)

    print(f"Outlier Detection {perc}% dataset was created.")