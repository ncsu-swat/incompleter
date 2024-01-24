# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.model_selection import train_test_split
    _l_(639785)

except ImportError:
    pass

x_train, x_test, y_train, y_test = _c_(639789, _n_(639786, "train_test_split", lambda: train_test_split), _n_(639787, "x", lambda: x), _n_(639788, "y", lambda: y), test_size = 0.2, random_state = 0)
_l_(639790)

_c_(639793, _n_(639791, "print", lambda: print), _n_(639792, "x_train", lambda: x_train))
_l_(639794)

_c_(639797, _n_(639795, "print", lambda: print), _n_(639796, "x_test", lambda: x_test))
_l_(639798)

_c_(639801, _n_(639799, "print", lambda: print), _n_(639800, "y_train", lambda: y_train))
_l_(639802)

_c_(639805, _n_(639803, "print", lambda: print), _n_(639804, "y_test", lambda: y_test))
_l_(639806)