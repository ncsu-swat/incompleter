# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58985632/attributeerror-module-tensorflow-core-keras-layers-has-no-attribute-conv1d
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
 import tensorflow as tf
 _l_(547801)

except ImportError:
 pass
_c_(547805, _n_(547802, "print", lambda: print), _a_(547804, _n_(547803, "tf", lambda: tf), "__version__"))
_l_(547806)

(mnist_train, minst_train_label), (mnist_test, mnist_test_label) = _c_(547812, _a_(547811, _a_(547810, _a_(547809, _a_(547808, _n_(547807, "tf", lambda: tf), "keras"), "datasets"), "mnist"), "load_data"))
_l_(547813)

train_label_batch_int = _c_(547819, _a_(547815, _n_(547814, "tf", lambda: tf), "cast"), _n_(547816, "minst_train_label", lambda: minst_train_label), _a_(547818, _n_(547817, "tf", lambda: tf), "int32")) ## This is important because one tf.one_hot does not accept float
_l_(547820) ## This is important because one tf.one_hot does not accept float
train_label_batch_onehot = _c_(547824, _a_(547822, _n_(547821, "tf", lambda: tf), "one_hot"), _n_(547823, "train_label_batch_int", lambda: train_label_batch_int), depth = 10)
_l_(547825)
test_label_batch_int = _c_(547831, _a_(547827, _n_(547826, "tf", lambda: tf), "cast"), _n_(547828, "mnist_test_label", lambda: mnist_test_label), _a_(547830, _n_(547829, "tf", lambda: tf), "int32")) ## This is important because one tf.one_hot does not accept float
_l_(547832) ## This is important because one tf.one_hot does not accept float
test_label_batch_onehot = _c_(547836, _a_(547834, _n_(547833, "tf", lambda: tf), "one_hot"), _n_(547835, "test_label_batch_int", lambda: test_label_batch_int), depth = 10) 
_l_(547837) 
## converting to ndarray
if _a_(547841, _c_(547840, _n_(547838, "type", lambda: type), _n_(547839, "train_label_batch_onehot", lambda: train_label_batch_onehot)), "__name__") != 'ndarray' :
 _l_(547850)

 train_label_batch_onehot = _c_(547844, _a_(547843, _n_(547842, "train_label_batch_onehot", lambda: train_label_batch_onehot), "numpy"))
 _l_(547845)
 test_label_batch_onehot = _c_(547848, _a_(547847, _n_(547846, "test_label_batch_onehot", lambda: test_label_batch_onehot), "numpy"))
 _l_(547849)
try:
 from tensorflow import keras
 _l_(547852)

except ImportError:
 pass
try:
 from tensorflow.keras import layers
 _l_(547854)

except ImportError:
 pass
try:
 from tensorflow.keras.layers import Conv1D
 _l_(547856)

except ImportError:
 pass

model = _c_(547928, _a_(547859, _a_(547858, _n_(547857, "tf", lambda: tf), "keras"), "Sequential"), [
_c_(547867, _a_(547863, _a_(547862, _a_(547861, _n_(547860, "tf", lambda: tf), "keras"), "layers"), "Conv1D"), 32,5,activation=_a_(547866, _a_(547865, _n_(547864, "tf", lambda: tf), "nn"), "relu")),
_c_(547875, _a_(547871, _a_(547870, _a_(547869, _n_(547868, "tf", lambda: tf), "keras"), "layers"), "Conv1D"), 32,5,activation=_a_(547874, _a_(547873, _n_(547872, "tf", lambda: tf), "nn"), "relu")),
_c_(547880, _a_(547879, _a_(547878, _a_(547877, _n_(547876, "tf", lambda: tf), "keras"), "layers"), "MaxPooling1D"), 2,2),

_c_(547888, _a_(547884, _a_(547883, _a_(547882, _n_(547881, "tf", lambda: tf), "keras"), "layers"), "Conv1d"), 64,3,activation=_a_(547887, _a_(547886, _n_(547885, "tf", lambda: tf), "nn"), "relu")),
_c_(547893, _a_(547892, _a_(547891, _a_(547890, _n_(547889, "tf", lambda: tf), "keras"), "layers"), "MaxPooling1D"), 2,2),

_c_(547901, _a_(547897, _a_(547896, _a_(547895, _n_(547894, "tf", lambda: tf), "keras"), "layers"), "Conv1d"), 128,3,activation=_a_(547900, _a_(547899, _n_(547898, "tf", lambda: tf), "nn"), "relu")),
_c_(547906, _a_(547905, _a_(547904, _a_(547903, _n_(547902, "tf", lambda: tf), "keras"), "layers"), "flatten")),
_c_(547914, _a_(547910, _a_(547909, _a_(547908, _n_(547907, "tf", lambda: tf), "keras"), "layers"), "Dense"), 1024,activation=_a_(547913, _a_(547912, _n_(547911, "tf", lambda: tf), "nn"), "relu")),
_c_(547922, _a_(547918, _a_(547917, _a_(547916, _n_(547915, "tf", lambda: tf), "keras"), "layers"), "Dense"), 256,activation=_a_(547921, _a_(547920, _n_(547919, "tf", lambda: tf), "nn"), "relu")),
_c_(547927, _a_(547926, _a_(547925, _a_(547924, _n_(547923, "tf", lambda: tf), "keras"), "layers"), "Dense"), 10,activation=None)])
_l_(547929)