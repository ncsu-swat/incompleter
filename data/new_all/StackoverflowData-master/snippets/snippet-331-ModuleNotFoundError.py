#Source: https://stackoverflow.com/questions/51876460/getting-tensorflow-s-is-not-valid-scope-name-error-while-i-am-trying-to-creat
import pandas as pd
import tensorflow as tf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import metrics
from IPython import display
from tensorflow.python.data import Dataset
tf.logging.set_verbosity(tf.logging.ERROR)
pd.options.display.max_rows = 5
pd.options.display.float_format = '{:.1f}'.format

housing_data = pd.read_csv("train.csv")
housing_data = housing_data.reindex(
np.random.permutation(housing_data.index))
housing_data = pd.get_dummies(
housing_data).dropna()