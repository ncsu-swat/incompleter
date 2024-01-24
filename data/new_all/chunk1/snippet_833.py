# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67552839/kds-library-gives-attributeerror-module-kds-has-no-attribute-metrics
# REPRODUCABLE EXAMPLE
# Load Dataset and train-test split
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.datasets import load_iris
    _l_(407592)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(407594)

except ImportError:
    pass
try:
    from sklearn import tree
    _l_(407596)

except ImportError:
    pass

X, y = _c_(407598, _n_(407597, "load_iris", lambda: load_iris), return_X_y=True)
_l_(407599)
X_train, X_test, y_train, y_test = _c_(407603, _n_(407600, "train_test_split", lambda: train_test_split), _n_(407601, "X", lambda: X), _n_(407602, "y", lambda: y), test_size=0.33,random_state=3)
_l_(407604)
clf = _c_(407607, _a_(407606, _n_(407605, "tree", lambda: tree), "DecisionTreeClassifier"), max_depth=1,random_state=3)
_l_(407608)
clf = _c_(407613, _a_(407610, _n_(407609, "clf", lambda: clf), "fit"), _n_(407611, "X_train", lambda: X_train), _n_(407612, "y_train", lambda: y_train))
_l_(407614)
y_prob = _c_(407618, _a_(407616, _n_(407615, "clf", lambda: clf), "predict_proba"), _n_(407617, "X_test", lambda: X_test))
_l_(407619)
try:
    import kds
    _l_(407621)

except ImportError:
    pass
_c_(407627, _a_(407624, _a_(407623, _n_(407622, "kds", lambda: kds), "metrics"), "report"), _n_(407625, "y_test", lambda: y_test), _n_(407626, "y_prob", lambda: y_prob))
_l_(407628)