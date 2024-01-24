#Source: https://stackoverflow.com/questions/59013531/typeerror-singleton-array-0-cannot-be-considered-a-valid-collection
import numpy as np
import tensorflow as tf
from keras.datasets import cifar10

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
from keras.utils import np_utils
y_train=np_utils.to_categorical(y_train, 10)
y_test=np_utils.to_categorical(y_test, 10)
x_train = x_train.astype('float32')/255
y_train=y_train.astype('float32')/255
y_train_labels=np.argmax(y_train, axis=1)
from keras.models import Sequential 
from keras.layers import Dense, Conv2D, Flatten
def mod(activation):
  model=Sequential()

  model.add(Conv2D(3,kernel_size=3,activation='relu',input_shape=(32,32,3)))
  model.add(Conv2D(3,kernel_size=3,activation='relu'))
  model.add(Flatten())
  model.add(Dense(10,activation='softmax'))

  return model
import sklearn.metrics as metrics

for activations in ["relu", "tanh", "sigmoid"]:
  for epochs in [1,10,15]:
    model_eval=mod(activations)


    model_eval.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
    y_pred=model_eval.fit(x_train,y_train,validation_data=(x_test,y_test),epochs=epochs)
    y_pred_labels=np.argmax(y_pred, axis=-1)
    confusion_matrix = metrics.confusion_matrix(y_true=y_train_labels, y_pred=y_pred_labels)