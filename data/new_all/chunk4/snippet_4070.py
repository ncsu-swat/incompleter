# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
y_pred = _c_(591769, _a_(591767, _n_(591766, "regressor", lambda: regressor), "predict"), _n_(591768, "x_test", lambda: x_test))
_l_(591770)

_c_(591773, _a_(591772, _n_(591771, "np", lambda: np), "set_printoptions"), precision=2)
_l_(591774)

_c_(591791, _n_(591775, "print", lambda: print), _c_(591790, _a_(591777, _n_(591776, "np", lambda: np), "concatenate"), (_c_(591783, _a_(591779, _n_(591778, "y_pred", lambda: y_pred), "reshape"), _c_(591782, _n_(591780, "len", lambda: len), _n_(591781, "y_pred", lambda: y_pred)),1), _c_(591789, _a_(591785, _n_(591784, "y_test", lambda: y_test), "reshape"), _c_(591788, _n_(591786, "len", lambda: len), _n_(591787, "y_test", lambda: y_test)),1)),1))
_l_(591792)