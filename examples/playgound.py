from __future__ import print_function
import example_helper
import json
from deepmoji.model_def import deepmoji_transfer
from deepmoji.global_variables import PRETRAINED_PATH
from deepmoji.finetuning import (
    load_benchmark,
    finetune)

DATASET_PATH = '../data/SS-Youtube/raw.pickle'
nb_classes = 2

with open('../model/vocabulary.json', 'r') as f:
    vocab = json.load(f)

# Load dataset.
data = load_benchmark(DATASET_PATH, vocab)
print(len(data))
print(type(data))
