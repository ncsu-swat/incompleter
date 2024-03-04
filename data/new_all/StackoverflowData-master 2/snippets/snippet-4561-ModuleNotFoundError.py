#Source: https://stackoverflow.com/questions/55577628/attributeerror-module-gensim-models-word2vec-has-no-attribute-load
import numpy as np
import pandas as pd
import gensim
from matplotlib import pyplot as plt
from gensim.models import word2vec
from collections import defaultdict
from sklearn.cluster import KMeans

model = word2vec.Text8Corpus(r'C:\Users\qlm\Desktop\globalwarming.txt')
model = word2vec.load(r'C:\Users\qlm\Desktop\globalwarming.txt')