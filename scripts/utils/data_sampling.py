import random

def generate_random_indices(df, percentage, seed=None):
  if seed is not None:
    random.seed(seed)
  return random.sample(df.index.tolist(), int(percentage * len(df)))