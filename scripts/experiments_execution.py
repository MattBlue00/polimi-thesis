import os

from scripts.utils.fetch_datasets import load_dirty_datasets
from scripts.utils.init_experiments import init_experiments
from scripts.utils.path import get_directory_from_root
from scripts.utils.results_visualization import get_results, plot_results
from scripts.utils.setup import setup

print("Setting up the environment...")
setup()

# Load the datasets
datasets = load_dirty_datasets("Datasets", "df_dirty_10")

results_dir = get_directory_from_root(__file__, 'results')  # datasets directory

# if datasets directory does not exist, raise an exception
if not os.path.exists(results_dir):
    raise Exception("There is no 'results' directory to work with.")

experiments = init_experiments(datasets)

# Experiment execution
for experiment in experiments:
  experiment.test()

# Results visualization
df_results = get_results(experiments)
print(df_results)
plot_results(df_results)


