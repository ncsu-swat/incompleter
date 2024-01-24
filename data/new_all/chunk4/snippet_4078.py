# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
y_pred = _c_(626118, _a_(626116, _n_(626115, "regressor", lambda: regressor), "predict"), _n_(626117, "x_test", lambda: x_test))
_l_(626119)

_c_(626122, _a_(626121, _n_(626120, "np", lambda: np), "set_printoptions"), precision=2)
_l_(626123)

_c_(626140, _n_(626124, "print", lambda: print), _c_(626139, _a_(626126, _n_(626125, "np", lambda: np), "concatenate"), (_c_(626132, _a_(626128, _n_(626127, "y_pred", lambda: y_pred), "reshape"), _c_(626131, _n_(626129, "len", lambda: len), _n_(626130, "y_pred", lambda: y_pred)),1), _c_(626138, _a_(626134, _n_(626133, "y_test", lambda: y_test), "reshape"), _c_(626137, _n_(626135, "len", lambda: len), _n_(626136, "y_test", lambda: y_test)),1)),1))
_l_(626141)