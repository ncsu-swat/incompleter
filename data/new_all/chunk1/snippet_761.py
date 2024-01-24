# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59013531/typeerror-singleton-array-0-cannot-be-considered-a-valid-collection
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
  import numpy as np
  _l_(407738)

except ImportError:
  pass
try:
  import tensorflow as tf
  _l_(407740)

except ImportError:
  pass
try:
  from keras.datasets import cifar10
  _l_(407742)

except ImportError:
  pass

(x_train, y_train), (x_test, y_test) = _c_(407745, _a_(407744, _n_(407743, "cifar10", lambda: cifar10), "load_data"))
_l_(407746)
try:
  from keras.utils import np_utils
  _l_(407748)

except ImportError:
  pass
y_train=_c_(407752, _a_(407750, _n_(407749, "np_utils", lambda: np_utils), "to_categorical"), _n_(407751, "y_train", lambda: y_train), 10)
_l_(407753)
y_test=_c_(407757, _a_(407755, _n_(407754, "np_utils", lambda: np_utils), "to_categorical"), _n_(407756, "y_test", lambda: y_test), 10)
_l_(407758)
x_train = _c_(407761, _a_(407760, _n_(407759, "x_train", lambda: x_train), "astype"), 'float32')/255
_l_(407762)
y_train=_c_(407765, _a_(407764, _n_(407763, "y_train", lambda: y_train), "astype"), 'float32')/255
_l_(407766)
y_train_labels=_c_(407770, _a_(407768, _n_(407767, "np", lambda: np), "argmax"), _n_(407769, "y_train", lambda: y_train), axis=1)
_l_(407771)
try:
  from keras.models import Sequential
  _l_(407773)

except ImportError:
  pass
try:
  from keras.layers import Dense, Conv2D, Flatten
  _l_(407775)

except ImportError:
  pass
def mod(activation):
  _l_(407805)

  model=_c_(407777, _n_(407776, "Sequential", lambda: Sequential))
  _l_(407778)

  _c_(407783, _a_(407780, _n_(407779, "model", lambda: model), "add"), _c_(407782, _n_(407781, "Conv2D", lambda: Conv2D), 3,kernel_size=3,activation='relu',input_shape=(32,32,3)))
  _l_(407784)
  _c_(407789, _a_(407786, _n_(407785, "model", lambda: model), "add"), _c_(407788, _n_(407787, "Conv2D", lambda: Conv2D), 3,kernel_size=3,activation='relu'))
  _l_(407790)
  _c_(407795, _a_(407792, _n_(407791, "model", lambda: model), "add"), _c_(407794, _n_(407793, "Flatten", lambda: Flatten)))
  _l_(407796)
  _c_(407801, _a_(407798, _n_(407797, "model", lambda: model), "add"), _c_(407800, _n_(407799, "Dense", lambda: Dense), 10,activation='softmax'))
  _l_(407802)
  aux = _n_(407803, "model", lambda: model)
  _l_(407804)

  return aux
try:
  import sklearn.metrics as metrics
  _l_(407807)

except ImportError:
  pass

for activations in ["relu", "tanh", "sigmoid"]:
  _l_(407837)

  for epochs in [1,10,15]:
    _l_(407836)

    model_eval=_c_(407810, _n_(407808, "mod", lambda: mod), _n_(407809, "activations", lambda: activations))
    _l_(407811)


    _c_(407814, _a_(407813, _n_(407812, "model_eval", lambda: model_eval), "compile"), optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
    _l_(407815)
    y_pred=_c_(407823, _a_(407817, _n_(407816, "model_eval", lambda: model_eval), "fit"), _n_(407818, "x_train", lambda: x_train),_n_(407819, "y_train", lambda: y_train),validation_data=(_n_(407820, "x_test", lambda: x_test),_n_(407821, "y_test", lambda: y_test)),epochs=_n_(407822, "epochs", lambda: epochs))
    _l_(407824)
    y_pred_labels=_c_(407828, _a_(407826, _n_(407825, "np", lambda: np), "argmax"), _n_(407827, "y_pred", lambda: y_pred), axis=-1)
    _l_(407829)
    confusion_matrix = _c_(407834, _a_(407831, _n_(407830, "metrics", lambda: metrics), "confusion_matrix"), y_true=_n_(407832, "y_train_labels", lambda: y_train_labels), y_pred=_n_(407833, "y_pred_labels", lambda: y_pred_labels))
    _l_(407835)