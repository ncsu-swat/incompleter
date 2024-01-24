# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49869413/python-list-comprehension-with-zip-typeerror-numpy-float64-object-cannot-be
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(659984)

except ImportError:
    pass
try:
    import numpy as np
    _l_(659986)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(659988)

except ImportError:
    pass
try:
    from sklearn.tree import DecisionTreeClassifier
    _l_(659990)

except ImportError:
    pass

data = _c_(659993, _a_(659992, _n_(659991, "pd", lambda: pd), "read_csv"), '/iris1.csv')
_l_(659994)
df = _c_(659998, _a_(659996, _n_(659995, "pd", lambda: pd), "DataFrame"), _n_(659997, "data", lambda: data))
_l_(659999)

X=_a_(660001, _n_(660000, "df", lambda: df), "iloc")[:,0:4]
_l_(660002)
y=_a_(660004, _n_(660003, "df", lambda: df), "iloc")[:,4]
_l_(660005)
try:
    from sklearn.model_selection import train_test_split
    _l_(660007)

except ImportError:
    pass
X_train, X_test, y_train, y_test = _c_(660011, _n_(660008, "train_test_split", lambda: train_test_split), _n_(660009, "X", lambda: X), _n_(660010, "y", lambda: y), test_size=0.2)
_l_(660012)

# Calculate Error Rate
def calc_error_rate(pred, Y):
    _l_(660023)

    aux = _c_(660016, _n_(660013, "sum", lambda: sum), _n_(660014, "pred", lambda: pred) != _n_(660015, "Y", lambda: Y)) / _c_(660021, _n_(660017, "float", lambda: float), _c_(660020, _n_(660018, "len", lambda: len), _n_(660019, "Y", lambda: Y)))
    _l_(660022)
    return aux


def AdaBoost(y_train, X_train, y_test, X_test, M, clf):
    _l_(660148)


    n_train = _c_(660026, _n_(660024, "len", lambda: len), _n_(660025, "X_train", lambda: X_train))
    _l_(660027)
    n_test = _c_(660030, _n_(660028, "len", lambda: len), _n_(660029, "X_test", lambda: X_test))
    _l_(660031)

    # Initialize weights
    w = _c_(660035, _a_(660033, _n_(660032, "np", lambda: np), "ones"), _n_(660034, "n_train", lambda: n_train)) / _n_(660036, "n_train", lambda: n_train)
    _l_(660037)


    pred_train = _c_(660041, _a_(660039, _n_(660038, "np", lambda: np), "zeros"), _n_(660040, "n_train", lambda: n_train))
    _l_(660042)
    pred_test = _c_(660046, _a_(660044, _n_(660043, "np", lambda: np), "zeros"), _n_(660045, "n_test", lambda: n_test))
    _l_(660047)

    for i in _c_(660050, _n_(660048, "range", lambda: range), _n_(660049, "M", lambda: M)):
        _l_(660128)


    # Fit a classifier with the specific weights
        _c_(660056, _a_(660052, _n_(660051, "clf", lambda: clf), "fit"), _n_(660053, "X_train", lambda: X_train), _n_(660054, "y_train", lambda: y_train), sample_weight = _n_(660055, "w", lambda: w))
        _l_(660057)
        pred_train_i = _c_(660061, _a_(660059, _n_(660058, "clf", lambda: clf), "predict"), _n_(660060, "X_train", lambda: X_train))
        _l_(660062)
        pred_test_i = _c_(660066, _a_(660064, _n_(660063, "clf", lambda: clf), "predict"), _n_(660065, "X_test", lambda: X_test))
        _l_(660067)

        # Indicator function
        miss = [_c_(660070, _n_(660068, "int", lambda: int), _n_(660069, "x", lambda: x)) for x in (_n_(660071, "pred_train_i", lambda: pred_train_i) != _n_(660072, "y_train", lambda: y_train))]
        _l_(660073)

        # Equivalent with 1/-1 to update weights
        miss2 = [_n_(660074, "x", lambda: x) if _n_(660075, "x", lambda: x)==1 else -1 for x in _n_(660076, "miss", lambda: miss)]
        _l_(660077)

        # Compute the error
        err_m = _c_(660082, _a_(660079, _n_(660078, "np", lambda: np), "dot"), _n_(660080, "w", lambda: w),_n_(660081, "miss", lambda: miss)) / _c_(660085, _n_(660083, "sum", lambda: sum), _n_(660084, "w", lambda: w))
        _l_(660086)

        # wi
        wi = 0.5 * _c_(660093, _a_(660088, _n_(660087, "np", lambda: np), "log"), (1 - _n_(660089, "err_m", lambda: err_m)) / _c_(660092, _n_(660090, "float", lambda: float), _n_(660091, "err_m", lambda: err_m)))
        _l_(660094)

        # New weights
        w = _c_(660106, _a_(660096, _n_(660095, "np", lambda: np), "multiply"), _n_(660097, "w", lambda: w), _c_(660105, _a_(660099, _n_(660098, "np", lambda: np), "exp"), [_c_(660102, _n_(660100, "float", lambda: float), _n_(660101, "x", lambda: x)) * _n_(660103, "wi", lambda: wi) for x in _n_(660104, "miss2", lambda: miss2)]))
        _l_(660107)

        # Add to prediction
        pred_train = [_c_(660110, _n_(660108, "sum", lambda: sum), _n_(660109, "x", lambda: x)) for x in _c_(660116, _n_(660111, "zip", lambda: zip), _n_(660112, "pred_train", lambda: pred_train), [_n_(660113, "x", lambda: x) * _n_(660114, "wi", lambda: wi) for x in _n_(660115, "pred_train_i", lambda: pred_train_i)])]
        _l_(660117)
        pred_test = [_c_(660120, _n_(660118, "sum", lambda: sum), _n_(660119, "x", lambda: x)) for x in _c_(660126, _n_(660121, "zip", lambda: zip), _n_(660122, "pred_test", lambda: pred_test), [_n_(660123, "x", lambda: x) * _n_(660124, "wi", lambda: wi) for x in _n_(660125, "pred_test_i", lambda: pred_test_i)])]
        _l_(660127)

    pred_train = _c_(660132, _a_(660130, _n_(660129, "np", lambda: np), "sign"), _n_(660131, "pred_train", lambda: pred_train))
    _l_(660133)
    pred_test = _c_(660137, _a_(660135, _n_(660134, "np", lambda: np), "sign"), _n_(660136, "pred_test", lambda: pred_test))
    _l_(660138)
    aux = _c_(660142, _n_(660139, "calc_error_rate", lambda: calc_error_rate), _n_(660140, "pred_train", lambda: pred_train), _n_(660141, "y_train", lambda: y_train)), _c_(660146, _n_(660143, "calc_error_rate", lambda: calc_error_rate), _n_(660144, "pred_test", lambda: pred_test), _n_(660145, "y_test", lambda: y_test))
    _l_(660147)

    # Return error rate in train and test set
    return aux

# Use the Decision Tree Classifier for model, M
clf_tree = _c_(660150, _n_(660149, "DecisionTreeClassifier", lambda: DecisionTreeClassifier))
_l_(660151)

x_range = _c_(660153, _n_(660152, "range", lambda: range), 1, 500, 1)
_l_(660154)

for i in _n_(660155, "x_range", lambda: x_range):
    _l_(660165)

    classifier = _c_(660163, _n_(660156, "AdaBoost", lambda: AdaBoost), _n_(660157, "y_train", lambda: y_train), _n_(660158, "X_train", lambda: X_train), _n_(660159, "y_test", lambda: y_test), _n_(660160, "X_test", lambda: X_test), _n_(660161, "i", lambda: i), _n_(660162, "clf_tree", lambda: clf_tree))
    _l_(660164)