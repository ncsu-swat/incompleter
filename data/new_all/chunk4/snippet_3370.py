# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75197660/python-attributeerror-bool-object-has-no-attribute-any-when-fitting-regres
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.linear_model import LinearRegression
    _l_(621709)

except ImportError:
    pass
lm = _c_(621711, _n_(621710, "LinearRegression", lambda: LinearRegression))
_l_(621712)

_c_(621717, _a_(621714, _n_(621713, "lm", lambda: lm), "fit"), _n_(621715, "X_train", lambda: X_train), _n_(621716, "y_train", lambda: y_train))
_l_(621718)