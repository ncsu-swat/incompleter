# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49869413/python-list-comprehension-with-zip-typeerror-numpy-float64-object-cannot-be
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(674407)

except ImportError:
    pass
try:
    import numpy as np
    _l_(674409)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(674411)

except ImportError:
    pass
try:
    from sklearn.tree import DecisionTreeClassifier
    _l_(674413)

except ImportError:
    pass

data = _c_(674416, _a_(674415, _n_(674414, "pd", lambda: pd), "read_csv"), '/iris1.csv')
_l_(674417)
df = _c_(674421, _a_(674419, _n_(674418, "pd", lambda: pd), "DataFrame"), _n_(674420, "data", lambda: data))
_l_(674422)

X=_a_(674424, _n_(674423, "df", lambda: df), "iloc")[:,0:4]
_l_(674425)
y=_a_(674427, _n_(674426, "df", lambda: df), "iloc")[:,4]
_l_(674428)
try:
    from sklearn.model_selection import train_test_split
    _l_(674430)

except ImportError:
    pass
X_train, X_test, y_train, y_test = _c_(674434, _n_(674431, "train_test_split", lambda: train_test_split), _n_(674432, "X", lambda: X), _n_(674433, "y", lambda: y), test_size=0.2)
_l_(674435)

# Calculate Error Rate
def calc_error_rate(pred, Y):
    _l_(674446)

    aux = _c_(674439, _n_(674436, "sum", lambda: sum), _n_(674437, "pred", lambda: pred) != _n_(674438, "Y", lambda: Y)) / _c_(674444, _n_(674440, "float", lambda: float), _c_(674443, _n_(674441, "len", lambda: len), _n_(674442, "Y", lambda: Y)))
    _l_(674445)
    return aux


def AdaBoost(y_train, X_train, y_test, X_test, M, clf):
    _l_(674571)


    n_train = _c_(674449, _n_(674447, "len", lambda: len), _n_(674448, "X_train", lambda: X_train))
    _l_(674450)
    n_test = _c_(674453, _n_(674451, "len", lambda: len), _n_(674452, "X_test", lambda: X_test))
    _l_(674454)

    # Initialize weights
    w = _c_(674458, _a_(674456, _n_(674455, "np", lambda: np), "ones"), _n_(674457, "n_train", lambda: n_train)) / _n_(674459, "n_train", lambda: n_train)
    _l_(674460)


    pred_train = _c_(674464, _a_(674462, _n_(674461, "np", lambda: np), "zeros"), _n_(674463, "n_train", lambda: n_train))
    _l_(674465)
    pred_test = _c_(674469, _a_(674467, _n_(674466, "np", lambda: np), "zeros"), _n_(674468, "n_test", lambda: n_test))
    _l_(674470)

    for i in _c_(674473, _n_(674471, "range", lambda: range), _n_(674472, "M", lambda: M)):
        _l_(674551)


    # Fit a classifier with the specific weights
        _c_(674479, _a_(674475, _n_(674474, "clf", lambda: clf), "fit"), _n_(674476, "X_train", lambda: X_train), _n_(674477, "y_train", lambda: y_train), sample_weight = _n_(674478, "w", lambda: w))
        _l_(674480)
        pred_train_i = _c_(674484, _a_(674482, _n_(674481, "clf", lambda: clf), "predict"), _n_(674483, "X_train", lambda: X_train))
        _l_(674485)
        pred_test_i = _c_(674489, _a_(674487, _n_(674486, "clf", lambda: clf), "predict"), _n_(674488, "X_test", lambda: X_test))
        _l_(674490)

        # Indicator function
        miss = [_c_(674493, _n_(674491, "int", lambda: int), _n_(674492, "x", lambda: x)) for x in (_n_(674494, "pred_train_i", lambda: pred_train_i) != _n_(674495, "y_train", lambda: y_train))]
        _l_(674496)

        # Equivalent with 1/-1 to update weights
        miss2 = [_n_(674497, "x", lambda: x) if _n_(674498, "x", lambda: x)==1 else -1 for x in _n_(674499, "miss", lambda: miss)]
        _l_(674500)

        # Compute the error
        err_m = _c_(674505, _a_(674502, _n_(674501, "np", lambda: np), "dot"), _n_(674503, "w", lambda: w),_n_(674504, "miss", lambda: miss)) / _c_(674508, _n_(674506, "sum", lambda: sum), _n_(674507, "w", lambda: w))
        _l_(674509)

        # wi
        wi = 0.5 * _c_(674516, _a_(674511, _n_(674510, "np", lambda: np), "log"), (1 - _n_(674512, "err_m", lambda: err_m)) / _c_(674515, _n_(674513, "float", lambda: float), _n_(674514, "err_m", lambda: err_m)))
        _l_(674517)

        # New weights
        w = _c_(674529, _a_(674519, _n_(674518, "np", lambda: np), "multiply"), _n_(674520, "w", lambda: w), _c_(674528, _a_(674522, _n_(674521, "np", lambda: np), "exp"), [_c_(674525, _n_(674523, "float", lambda: float), _n_(674524, "x", lambda: x)) * _n_(674526, "wi", lambda: wi) for x in _n_(674527, "miss2", lambda: miss2)]))
        _l_(674530)

        # Add to prediction
        pred_train = [_c_(674533, _n_(674531, "sum", lambda: sum), _n_(674532, "x", lambda: x)) for x in _c_(674539, _n_(674534, "zip", lambda: zip), _n_(674535, "pred_train", lambda: pred_train), [_n_(674536, "x", lambda: x) * _n_(674537, "wi", lambda: wi) for x in _n_(674538, "pred_train_i", lambda: pred_train_i)])]
        _l_(674540)
        pred_test = [_c_(674543, _n_(674541, "sum", lambda: sum), _n_(674542, "x", lambda: x)) for x in _c_(674549, _n_(674544, "zip", lambda: zip), _n_(674545, "pred_test", lambda: pred_test), [_n_(674546, "x", lambda: x) * _n_(674547, "wi", lambda: wi) for x in _n_(674548, "pred_test_i", lambda: pred_test_i)])]
        _l_(674550)

    pred_train = _c_(674555, _a_(674553, _n_(674552, "np", lambda: np), "sign"), _n_(674554, "pred_train", lambda: pred_train))
    _l_(674556)
    pred_test = _c_(674560, _a_(674558, _n_(674557, "np", lambda: np), "sign"), _n_(674559, "pred_test", lambda: pred_test))
    _l_(674561)
    aux = _c_(674565, _n_(674562, "calc_error_rate", lambda: calc_error_rate), _n_(674563, "pred_train", lambda: pred_train), _n_(674564, "y_train", lambda: y_train)), _c_(674569, _n_(674566, "calc_error_rate", lambda: calc_error_rate), _n_(674567, "pred_test", lambda: pred_test), _n_(674568, "y_test", lambda: y_test))
    _l_(674570)

    # Return error rate in train and test set
    return aux

# Use the Decision Tree Classifier for model, M
clf_tree = _c_(674573, _n_(674572, "DecisionTreeClassifier", lambda: DecisionTreeClassifier))
_l_(674574)

x_range = _c_(674576, _n_(674575, "range", lambda: range), 1, 500, 1)
_l_(674577)

for i in _n_(674578, "x_range", lambda: x_range):
    _l_(674588)

    classifier = _c_(674586, _n_(674579, "AdaBoost", lambda: AdaBoost), _n_(674580, "y_train", lambda: y_train), _n_(674581, "X_train", lambda: X_train), _n_(674582, "y_test", lambda: y_test), _n_(674583, "X_test", lambda: X_test), _n_(674584, "i", lambda: i), _n_(674585, "clf_tree", lambda: clf_tree))
    _l_(674587)