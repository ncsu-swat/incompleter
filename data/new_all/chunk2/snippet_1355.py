# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73187115/fit-attributeerror-in-python3-using-imblearn-ensemble-and-balancedrandomfore
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from imblearn.ensemble import BalancedRandomForestClassifier
    _l_(450257)

except ImportError:
    pass

bal_forest = _c_(450259, _n_(450258, "BalancedRandomForestClassifier", lambda: BalancedRandomForestClassifier), n_estimators=100, random_state=1)
_l_(450260)
_c_(450265, _a_(450262, _n_(450261, "bal_forest", lambda: bal_forest), "fit"), _n_(450263, "X_train", lambda: X_train), _n_(450264, "y_train", lambda: y_train))
_l_(450266)