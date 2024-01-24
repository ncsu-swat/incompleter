# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51125475/typeerror-fit-transform-missing-1-required-positional-argument-x
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(415443)

except ImportError:
    pass

# Importing the dataset
dataset = _c_(415446, _a_(415445, _n_(415444, "pd", lambda: pd), "read_csv"), 'Data.csv')
_l_(415447)
X = _a_(415450, _a_(415449, _n_(415448, "dataset", lambda: dataset), "iloc")[:, :-1], "values")
_l_(415451)
y = _a_(415454, _a_(415453, _n_(415452, "dataset", lambda: dataset), "iloc")[:, 3], "values")
_l_(415455)
try:
    from sklearn.preprocessing import Imputer
    _l_(415457)

except ImportError:
    pass
imputer = _c_(415459, _n_(415458, "Imputer", lambda: Imputer), missing_values="NaN", strategy="mean", axis=0)
_l_(415460)
imputer = _c_(415465, _a_(415462, _n_(415461, "Imputer", lambda: Imputer), "fit"), _n_(415463, "imputer", lambda: imputer),_n_(415464, "X", lambda: X)[:,1:3])
_l_(415466)
_n_(415467, "X", lambda: X)[:, 1:3] = _c_(415472, _a_(415469, _n_(415468, "Imputer", lambda: Imputer), "transform"), _n_(415470, "imputer", lambda: imputer),_n_(415471, "X", lambda: X)[:, 1:3])
_l_(415473)
try:
    from sklearn.cross_validation import train_test_split
    _l_(415475)

except ImportError:
    pass

x_train, x_test, y_train, y_test = _c_(415479, _n_(415476, "train_test_split", lambda: train_test_split), _n_(415477, "X", lambda: X), _n_(415478, "y", lambda: y), test_size= 0.2, random_state= 0)
_l_(415480)
try:
    from sklearn.preprocessing import StandardScaler
    _l_(415482)

except ImportError:
    pass
sc_X = _n_(415483, "StandardScaler", lambda: StandardScaler)
_l_(415484)
x_train = _c_(415488, _a_(415486, _n_(415485, "sc_X", lambda: sc_X), "fit_transform"), _n_(415487, "x_train", lambda: x_train))
_l_(415489)
x_test = _c_(415493, _a_(415491, _n_(415490, "sc_X", lambda: sc_X), "transform"), _n_(415492, "x_test", lambda: x_test))
_l_(415494)