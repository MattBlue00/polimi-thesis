import random

def generate_random_indices(df, percentage):
  return random.sample(df.index.tolist(), int(percentage * len(df)))