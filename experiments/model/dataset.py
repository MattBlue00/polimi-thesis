class Dataset:

  def __init__(self, dataset_id, df, dirty_percentage):
    self.id = dataset_id
    self.df = df
    self.dirty_percentage = dirty_percentage
