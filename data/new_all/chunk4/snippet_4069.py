# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.linear_model import LinearRegression
    _l_(611996)

except ImportError:
    pass

regressor = _c_(611998, _n_(611997, "LinearRegression", lambda: LinearRegression))
_l_(611999)

_c_(612004, _a_(612001, _n_(612000, "regressor", lambda: regressor), "fit"), _n_(612002, "x_train", lambda: x_train) ,_n_(612003, "y_train", lambda: y_train))
_l_(612005)