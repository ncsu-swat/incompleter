# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.linear_model import LinearRegression
    _l_(634710)

except ImportError:
    pass

regressor = _c_(634712, _n_(634711, "LinearRegression", lambda: LinearRegression))
_l_(634713)

_c_(634718, _a_(634715, _n_(634714, "regressor", lambda: regressor), "fit"), _n_(634716, "x_train", lambda: x_train) ,_n_(634717, "y_train", lambda: y_train))
_l_(634719)