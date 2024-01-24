# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.model_selection import train_test_split
    _l_(622558)

except ImportError:
    pass

x_train, x_test, y_train, y_test = _c_(622562, _n_(622559, "train_test_split", lambda: train_test_split), _n_(622560, "x", lambda: x), _n_(622561, "y", lambda: y), test_size = 0.2, random_state = 0)
_l_(622563)

_c_(622566, _n_(622564, "print", lambda: print), _n_(622565, "x_train", lambda: x_train))
_l_(622567)

_c_(622570, _n_(622568, "print", lambda: print), _n_(622569, "x_test", lambda: x_test))
_l_(622571)

_c_(622574, _n_(622572, "print", lambda: print), _n_(622573, "y_train", lambda: y_train))
_l_(622575)

_c_(622578, _n_(622576, "print", lambda: print), _n_(622577, "y_test", lambda: y_test))
_l_(622579)