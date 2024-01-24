# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55150181/attributeerror-module-keras-utils-has-no-attribute-sequence
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy
    _l_(415752)

except ImportError:
    pass
try:
    from keras.datasets import mnist
    _l_(415754)

except ImportError:
    pass
try:
    from keras.models import Sequential
    _l_(415756)

except ImportError:
    pass
try:
    from keras.layers import Dense
    _l_(415758)

except ImportError:
    pass
try:
    from keras.utils import np_utils
    _l_(415760)

except ImportError:
    pass


_c_(415764, _a_(415763, _a_(415762, _n_(415761, "numpy", lambda: numpy), "random"), "seed"), 42)
_l_(415765)


(X_train, y_train), (X_test, y_test) = _c_(415768, _a_(415767, _n_(415766, "mnist", lambda: mnist), "load_data"))
_l_(415769)

X_train = _c_(415772, _a_(415771, _n_(415770, "X_train", lambda: X_train), "reshape"), 60000, 784)
_l_(415773)
X_test = _c_(415776, _a_(415775, _n_(415774, "X_test", lambda: X_test), "reshape"), 10000, 784)
_l_(415777)

X_train = _c_(415780, _a_(415779, _n_(415778, "X_train", lambda: X_train), "astype"), 'float32')
_l_(415781)
X_test = _c_(415784, _a_(415783, _n_(415782, "X_test", lambda: X_test), "astype"), 'float32')
_l_(415785)
X_train /= 255
_l_(415786)
X_test /= 255
_l_(415787)


Y_train = _c_(415791, _a_(415789, _n_(415788, "np_utils", lambda: np_utils), "to_categorical"), _n_(415790, "y_train", lambda: y_train), 10)
_l_(415792)
Y_test = _c_(415796, _a_(415794, _n_(415793, "np_utils", lambda: np_utils), "to_categorical"), _n_(415795, "y_test", lambda: y_test), 10)
_l_(415797)


model = _c_(415799, _n_(415798, "Sequential", lambda: Sequential))
_l_(415800)


_c_(415805, _a_(415802, _n_(415801, "model", lambda: model), "add"), _c_(415804, _n_(415803, "Dense", lambda: Dense), 800, input_dim=784, activation="relu",         
kernel_initializer="normal"))
_l_(415806)
_c_(415811, _a_(415808, _n_(415807, "model", lambda: model), "add"), _c_(415810, _n_(415809, "Dense", lambda: Dense), 10, activation="softmax", kernel_initializer="normal"))
_l_(415812)


_c_(415815, _a_(415814, _n_(415813, "model", lambda: model), "compile"), loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])
_l_(415816)

_c_(415821, _n_(415817, "print", lambda: print), _c_(415820, _a_(415819, _n_(415818, "model", lambda: model), "summary")))
_l_(415822)


_c_(415827, _a_(415824, _n_(415823, "model", lambda: model), "fit"), _n_(415825, "X_train", lambda: X_train), _n_(415826, "Y_train", lambda: Y_train), batch_size=200, epochs=25, validation_split=0.2, verbose=2)
_l_(415828)


scores = _c_(415833, _a_(415830, _n_(415829, "model", lambda: model), "evaluate"), _n_(415831, "X_test", lambda: X_test), _n_(415832, "Y_test", lambda: Y_test), verbose=0)
_l_(415834)
_c_(415837, _n_(415835, "print", lambda: print), "Точность работы на тестовых данных: %.2f%%" % (_n_(415836, "scores", lambda: scores)[1]*100))
_l_(415838)