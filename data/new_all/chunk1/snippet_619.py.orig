#Source: https://stackoverflow.com/questions/55407970/how-to-fix-typeerror-the-added-layer-must-be-an-instance-of-class-layer-in-p
import keras
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.utils import shuffle
import tensorflow as tf

seed = 10
np.random.seed(seed)

dataset = np.loadtxt("dataset2.csv",delimiter=',',skiprows=1)
dataset = shuffle(dataset)

X = dataset[:,2:]
Y = dataset[:,1]

(X_train,X_test,Y_train,Y_test) = train_test_split(X, Y, test_size=0.15, random_state=seed)
input_shape = (13,)

model = tf.keras.models.Sequential()
model.add(keras.layers.InputLayer(input_shape))
model.add(keras.layers.core.Dense(128, activation='relu'))
model.add(keras.layers.core.Dense(128, activation='relu'))
model.add(keras.layers.core.Dense(4, activation='sigmoid'))

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(X_train,Y_train,epochs=20)