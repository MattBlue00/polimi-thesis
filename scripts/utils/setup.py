import random
import numpy as np

from scripts.utils.constants import RANDOM_SEED

def setup():
    _setup_seed()

def _setup_seed():
    random.seed(RANDOM_SEED)
    np.random.seed(RANDOM_SEED)