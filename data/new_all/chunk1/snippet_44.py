# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35996970/typeerror-fit-missing-1-required-positional-argument-y
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.naive_bayes import GaussianNB
    _l_(380766)

except ImportError:
    pass
try:
    from sklearn import metrics
    _l_(380768)

except ImportError:
    pass
try:
    from sklearn.cross_validation import train_test_split
    _l_(380770)

except ImportError:
    pass
X = _n_(380771, "data", lambda: data)
_l_(380772)
Y = _n_(380773, "target", lambda: target)
_l_(380774)
model = _n_(380775, "GaussianNB", lambda: GaussianNB)
_l_(380776)
X_train, X_test, Y_train, Y_test = _c_(380780, _n_(380777, "train_test_split", lambda: train_test_split), _n_(380778, "X", lambda: X),_n_(380779, "Y", lambda: Y))
_l_(380781)
_c_(380786, _a_(380783, _n_(380782, "model", lambda: model), "fit"), _n_(380784, "X_train", lambda: X_train), _n_(380785, "Y_train", lambda: Y_train))
_l_(380787)