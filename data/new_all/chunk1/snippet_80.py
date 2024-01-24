# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38646040/attributeerror-linearregression-object-has-no-attribute-coef
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(410681)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(410683)

except ImportError:
    pass
try:
    import scipy.stats as stats
    _l_(410685)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(410687)

except ImportError:
    pass
try:
    import sklearn
    _l_(410689)

except ImportError:
    pass
try:
    from sklearn.datasets import load_boston
    _l_(410691)

except ImportError:
    pass
try:
    from sklearn.linear_model import LinearRegression
    _l_(410693)

except ImportError:
    pass

boston = _c_(410695, _n_(410694, "load_boston", lambda: load_boston))
_l_(410696)
bos = _c_(410701, _a_(410698, _n_(410697, "pd", lambda: pd), "DataFrame"), _a_(410700, _n_(410699, "boston", lambda: boston), "data"))
_l_(410702)
_n_(410703, "bos", lambda: bos).columns = _a_(410705, _n_(410704, "boston", lambda: boston), "feature_names")
_l_(410706)
_n_(410707, "bos", lambda: bos)['PRICE'] = _a_(410709, _n_(410708, "boston", lambda: boston), "target")
_l_(410710)

X = _c_(410713, _a_(410712, _n_(410711, "bos", lambda: bos), "drop"), 'PRICE', axis = 1)
_l_(410714)

lm = _c_(410716, _n_(410715, "LinearRegression", lambda: LinearRegression))
_l_(410717)