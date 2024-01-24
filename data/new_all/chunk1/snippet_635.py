# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54974905/attributeerror-numpy-ndarray-object-has-no-attribute-target
#Grid Search Parameter Tuning
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(402706)

except ImportError:
    pass
try:
    from sklearn import datasets
    _l_(402708)

except ImportError:
    pass
try:
    from sklearn.linear_model import Ridge
    _l_(402710)

except ImportError:
    pass
try:
    from sklearn.model_selection import GridSearchCV
    _l_(402712)

except ImportError:
    pass

# datasets
dataset = _c_(402716, _a_(402715, _a_(402714, _n_(402713, "np", lambda: np), "random"), "rand"), 1000,2)
_l_(402717)

#Ridge regression 
alphas = _c_(402720, _a_(402719, _n_(402718, "np", lambda: np), "array"), [1,0.1,0.01,0.001,0.0001,0])
_l_(402721)
model = _c_(402723, _n_(402722, "Ridge", lambda: Ridge))
_l_(402724)
grid = _c_(402730, _n_(402725, "GridSearchCV", lambda: GridSearchCV), estimator=_n_(402726, "model", lambda: model), param_grid=_c_(402729, _n_(402727, "dict", lambda: dict), alpha=_n_(402728, "alphas", lambda: alphas)))
_l_(402731)
_c_(402738, _a_(402733, _n_(402732, "grid", lambda: grid), "fit"), _a_(402735, _n_(402734, "dataset", lambda: dataset), "data"), _a_(402737, _n_(402736, "dataset", lambda: dataset), "target"))
_l_(402739)