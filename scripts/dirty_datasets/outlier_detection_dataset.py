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

# create dirty datasets
for perc in PERCENTAGES:
    # copy the original dataset
    df_modified = df.copy()

    # number of rows to replace
    n_rows_to_replace = int(len(df_modified) * (perc / 100))

    indices_to_replace = {}
    for i, col in enumerate(['price', 'bed', 'bath', 'acre_lot', 'house_size']):
        # randomly chooses the rows to replace
        indices_to_replace[col] = df_modified.sample(n=n_rows_to_replace, random_state=RANDOM_SEED+i).index

    # PRICE OUTLIERS

    # indices of low and high price outliers
    indices_to_replace_low = indices_to_replace['price'][:len(indices_to_replace['price']) // 2]
    indices_to_replace_high = indices_to_replace['price'][len(indices_to_replace['price']) // 2:]

    # price outliers injection
    min_value = df_modified['price'].min()
    max_value = df_modified['price'].max()
    price_outliers_low = [random.randint(0, int(min_value // 100)) * 100 for _ in range(len(indices_to_replace_low))]
    df_modified.loc[indices_to_replace_low, 'price'] = price_outliers_low
    price_outliers_high = [random.randint(int(max_value // 100), int(max_value * 10 // 100)) * 100 for _ in range(len(indices_to_replace_high))]
    df_modified.loc[indices_to_replace_high, 'price'] = price_outliers_high

    # BED OUTLIERS

    max_value = df_modified['bed'].max()
    bed_outliers = [random.randint(max_value + 1, max_value * 2) for _ in range(len(indices_to_replace['bed']))]
    df_modified.loc[indices_to_replace['bed'], 'bed'] = bed_outliers

    # BATH OUTLIERS

    max_value = df_modified['bath'].max()
    bath_outliers = [random.randint(max_value + 1, max_value * 2) for _ in range(len(indices_to_replace['bath']))]
    df_modified.loc[indices_to_replace['bath'], 'bath'] = bath_outliers

    # ACRE_LOT OUTLIERS

    # indices of low and high acre_lot outliers
    indices_to_replace_low = indices_to_replace['acre_lot'][:len(indices_to_replace['acre_lot']) // 2]
    indices_to_replace_high = indices_to_replace['acre_lot'][len(indices_to_replace['acre_lot']) // 2:]

    # acre_lot outliers injection
    min_value = df_modified['acre_lot'].min()
    max_value = df_modified['acre_lot'].max()
    acre_lot_outliers_low = [
        round_to_significant_figures(random.uniform(0, min_value / 2), sig_figs=2)
        for _ in range(len(indices_to_replace_low))
    ]
    df_modified.loc[indices_to_replace_low, 'acre_lot'] = acre_lot_outliers_low
    acre_lot_outliers_high = [
        round_to_significant_figures(random.uniform(max_value * 1.25, max_value * 2), sig_figs=2)
        for _ in range(len(indices_to_replace_high))
    ]
    df_modified.loc[indices_to_replace_high, 'acre_lot'] = acre_lot_outliers_high

    # HOUSE_SIZE OUTLIERS

    # indices of low and high house_size outliers
    indices_to_replace_low = indices_to_replace['house_size'][:len(indices_to_replace['house_size']) // 2]
    indices_to_replace_high = indices_to_replace['house_size'][len(indices_to_replace['house_size']) // 2:]

    # house_size outliers injection
    min_value = df_modified['house_size'].min()
    max_value = df_modified['house_size'].max()
    house_size_outliers_low = [
        round_to_significant_figures(random.uniform(0, min_value / 2), sig_figs=2)
        for _ in range(len(indices_to_replace_low))
    ]
    df_modified.loc[indices_to_replace_low, 'house_size'] = house_size_outliers_low
    house_size_outliers_high = [
        round_to_significant_figures(random.uniform(max_value * 1.25, max_value * 2), sig_figs=4)
        for _ in range(len(indices_to_replace_high))
    ]
    df_modified.loc[indices_to_replace_high, 'house_size'] = house_size_outliers_high

    # save to CSV
    outlier_path = os.path.join(outlier_detection_dir, f'outlier_detection_{str(perc)}.csv')
    df_modified.to_csv(outlier_path, index=False)

    print(f"Outlier Detection {perc}% dataset was created.")

