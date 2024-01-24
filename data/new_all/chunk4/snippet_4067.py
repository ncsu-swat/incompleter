# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.compose import ColumnTransformer
    _l_(634217)

except ImportError:
    pass
try:
    from sklearn.preprocessing import OneHotEncoder
    _l_(634219)

except ImportError:
    pass

ct  = _c_(634223, _n_(634220, "ColumnTransformer", lambda: ColumnTransformer), transformers = [('encoder', _c_(634222, _n_(634221, "OneHotEncoder", lambda: OneHotEncoder)) , [3])], remainder = 'passthrough')
_l_(634224)

x = _c_(634231, _a_(634226, _n_(634225, "np", lambda: np), "array"), _c_(634230, _a_(634228, _n_(634227, "ct", lambda: ct), "fit_transform"), _n_(634229, "x", lambda: x)))
_l_(634232)

_c_(634235, _n_(634233, "print", lambda: print), _n_(634234, "x", lambda: x))
_l_(634236)