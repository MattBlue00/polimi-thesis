import os
import re
import pandas as pd

from experiments.model.dataset import Dataset


def get_dirtiness_from_filename(filename):
  match = re.search(r'df_dirty_(\d+)', filename)
  if match:
    return match.group(1)
  else:
    raise ValueError("There is no percentage in: " + filename)

def load_dirty_datasets(directory, starts_with):
  """
  Loads all CSV files starting with "df_dirty_" into a list of DataFrames.

  Args:
    directory: The directory containing the CSV files.
    starts_with: The prefix that the CSV filenames must start with to be loaded.

  Returns:
    A list of DataFrames, each representing a loaded CSV file.
  """

  dirty_datasets = []
  for filename in os.listdir(directory):
    if filename.startswith(starts_with) and filename.endswith(".csv"):
      filepath = os.path.join(directory, filename)
      df = pd.read_csv(filepath)
      percentage = get_dirtiness_from_filename(filename)
      dataset = Dataset(
          dataset_id="df_dirty_" + percentage,
          df=df,
          dirty_percentage=percentage
      )
      dirty_datasets.append(dataset)
  return dirty_datasets
