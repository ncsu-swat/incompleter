# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/23319266/using-numpy-genfromtxt-gives-typeerror-cant-convert-bytes-object-to-str-impl
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pandas import read_csv
    _l_(383088)

except ImportError:
    pass
try:
    import numpy as np
    _l_(383090)

except ImportError:
    pass
try:
    from sklearn.linear_model.stochastic_gradient import SGDClassifier
    _l_(383092)

except ImportError:
    pass
try:
    from sklearn import preprocessing
    _l_(383094)

except ImportError:
    pass
try:
    import sklearn.metrics as metrics
    _l_(383096)

except ImportError:
    pass
try:
    from sklearn.cross_validation import train_test_split
    _l_(383098)

except ImportError:
    pass

#d = pd.read_csv("data.csv", dtype={'A': np.str(), 'B': np.str(), 'S': np.str()})

dataset = _c_(383103, _a_(383100, _n_(383099, "np", lambda: np), "genfromtxt"), _c_(383102, _n_(383101, "open", lambda: open), 'data.csv','r'), delimiter=',', dtype='f8')[1:]
_l_(383104)
target = _c_(383109, _a_(383106, _n_(383105, "np", lambda: np), "array"), [_n_(383107, "x", lambda: x)[19] for x in _n_(383108, "dataset", lambda: dataset)])
_l_(383110)
train = _c_(383115, _a_(383112, _n_(383111, "np", lambda: np), "array"), [_n_(383113, "x", lambda: x)[1:] for x in _n_(383114, "dataset", lambda: dataset)])
_l_(383116)

_c_(383119, _n_(383117, "print", lambda: print), _n_(383118, "target", lambda: target))
_l_(383120)