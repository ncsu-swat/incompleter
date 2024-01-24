# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63224642/while-predicting-the-test-result-the-reshape-function-is-causing-an-error-attri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.compose import ColumnTransformer
    _l_(581971)

except ImportError:
    pass
try:
    from sklearn.preprocessing import OneHotEncoder
    _l_(581973)

except ImportError:
    pass

ct  = _c_(581977, _n_(581974, "ColumnTransformer", lambda: ColumnTransformer), transformers = [('encoder', _c_(581976, _n_(581975, "OneHotEncoder", lambda: OneHotEncoder)) , [3])], remainder = 'passthrough')
_l_(581978)

x = _c_(581985, _a_(581980, _n_(581979, "np", lambda: np), "array"), _c_(581984, _a_(581982, _n_(581981, "ct", lambda: ct), "fit_transform"), _n_(581983, "x", lambda: x)))
_l_(581986)

_c_(581989, _n_(581987, "print", lambda: print), _n_(581988, "x", lambda: x))
_l_(581990)