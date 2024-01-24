# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57537474/how-to-fix-attributeerror-list-object-has-no-attribute-shape-error-in-pyt
from __future__ import absolute_import, division, print_function, unicode_literals
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(409519)
try:
    import tensorflow as tf
    _l_(409521)

except ImportError:
    pass
try:
    from tensorflow import keras
    _l_(409523)

except ImportError:
    pass

_c_(409525, _n_(409524, "print", lambda: print), "Tensorflow Version:")
_l_(409526)
_c_(409531, _n_(409527, "print", lambda: print), _a_(409530, _a_(409529, _n_(409528, "tf", lambda: tf), "version"), "VERSION"))
_l_(409532)
_c_(409534, _n_(409533, "print", lambda: print), "Keras Verstion:")
_l_(409535)
_c_(409540, _n_(409536, "print", lambda: print), _a_(409539, _a_(409538, _n_(409537, "tf", lambda: tf), "keras"), "__version__"))
_l_(409541)

minst = _a_(409545, _a_(409544, _a_(409543, _n_(409542, "tf", lambda: tf), "keras"), "datasets"), "mnist") # 28x28 0-9
_l_(409546) # 28x28 0-9

(x_train, y_train), (x_test, y_test) = _c_(409549, _a_(409548, _n_(409547, "minst", lambda: minst), "load_data"))
_l_(409550)

x_train = _c_(409556, _a_(409554, _a_(409553, _a_(409552, _n_(409551, "tf", lambda: tf), "keras"), "utils"), "normalize"), _n_(409555, "x_train", lambda: x_train), axis=1)
_l_(409557)
x__test = _n_(409558, "x_test", lambda: x_test);
_l_(409559)
x_test = _c_(409565, _a_(409563, _a_(409562, _a_(409561, _n_(409560, "tf", lambda: tf), "keras"), "utils"), "normalize"), _n_(409564, "x_test", lambda: x_test), axis=1)
_l_(409566)

model = _c_(409571, _a_(409570, _a_(409569, _a_(409568, _n_(409567, "tf", lambda: tf), "keras"), "models"), "Sequential"))
_l_(409572)
_c_(409580, _a_(409574, _n_(409573, "model", lambda: model), "add"), _c_(409579, _a_(409578, _a_(409577, _a_(409576, _n_(409575, "tf", lambda: tf), "keras"), "layers"), "Flatten")))
_l_(409581)
_c_(409592, _a_(409583, _n_(409582, "model", lambda: model), "add"), _c_(409591, _a_(409587, _a_(409586, _a_(409585, _n_(409584, "tf", lambda: tf), "keras"), "layers"), "Dense"), 128, activation=_a_(409590, _a_(409589, _n_(409588, "tf", lambda: tf), "nn"), "relu")))
_l_(409593)
_c_(409604, _a_(409595, _n_(409594, "model", lambda: model), "add"), _c_(409603, _a_(409599, _a_(409598, _a_(409597, _n_(409596, "tf", lambda: tf), "keras"), "layers"), "Dense"), 128, activation=_a_(409602, _a_(409601, _n_(409600, "tf", lambda: tf), "nn"), "relu")))
_l_(409605)
_c_(409616, _a_(409607, _n_(409606, "model", lambda: model), "add"), _c_(409615, _a_(409611, _a_(409610, _a_(409609, _n_(409608, "tf", lambda: tf), "keras"), "layers"), "Dense"), 10, activation=_a_(409614, _a_(409613, _n_(409612, "tf", lambda: tf), "nn"), "softmax")))
_l_(409617)

_c_(409620, _a_(409619, _n_(409618, "model", lambda: model), "compile"), optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
_l_(409621)

_c_(409626, _a_(409623, _n_(409622, "model", lambda: model), "fit"), _n_(409624, "x_train", lambda: x_train), _n_(409625, "y_train", lambda: y_train), epochs=1)
_l_(409627)

val_loss, val_acc = _c_(409632, _a_(409629, _n_(409628, "model", lambda: model), "evaluate"), _n_(409630, "x_test", lambda: x_test), _n_(409631, "y_test", lambda: y_test))
_l_(409633)
_c_(409637, _n_(409634, "print", lambda: print), _n_(409635, "val_loss", lambda: val_loss), _n_(409636, "val_acc", lambda: val_acc))
_l_(409638)

_c_(409641, _a_(409640, _n_(409639, "model", lambda: model), "save"), 'epic_num.h5')
_l_(409642)
_c_(409644, _n_(409643, "print", lambda: print), "Saved")
_l_(409645)
# Loading

nmodel = _c_(409649, _a_(409648, _a_(409647, _n_(409646, "keras", lambda: keras), "models"), "load_model"), "epic_num.h5")
_l_(409650)
try:
    import numpy as np;
    _l_(409652)

except ImportError:
    pass


# Test
predics = _c_(409656, _a_(409654, _n_(409653, "nmodel", lambda: nmodel), "predict"), [_n_(409655, "x_test", lambda: x_test)])
_l_(409657)
_c_(409660, _n_(409658, "print", lambda: print), _n_(409659, "predics", lambda: predics))
_l_(409661)
try:
    import matplotlib.pyplot as plt
    _l_(409663)

except ImportError:
    pass

_c_(409670, _a_(409665, _n_(409664, "plt", lambda: plt), "imshow"), _n_(409666, "x__test", lambda: x__test)[11], cmap=_a_(409669, _a_(409668, _n_(409667, "plt", lambda: plt), "cm"), "binary"))
_l_(409671)
_c_(409674, _a_(409673, _n_(409672, "plt", lambda: plt), "show"))
_l_(409675)

_c_(409681, _n_(409676, "print", lambda: print), _c_(409680, _a_(409678, _n_(409677, "np", lambda: np), "argmax"), _n_(409679, "predics", lambda: predics)[11]))
_l_(409682)