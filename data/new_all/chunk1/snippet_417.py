# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56303572/how-can-i-solve-this-unknown-label-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.feature_selection import RFE
    _l_(401991)

except ImportError:
    pass
try:
    from sklearn.ensemble import RandomForestClassifier
    _l_(401993)

except ImportError:
    pass

clf =_c_(401995, _n_(401994, "RandomForestClassifier", lambda: RandomForestClassifier), n_jobs = 2)
_l_(401996)

rfe = _c_(401999, _n_(401997, "RFE", lambda: RFE), _n_(401998, "clf", lambda: clf), n_features_to_select=1)
_l_(402000)
_c_(402005, _a_(402002, _n_(402001, "rfe", lambda: rfe), "fit"), _n_(402003, "X_newDoS", lambda: X_newDoS), _n_(402004, "Y_DoS", lambda: Y_DoS))
_l_(402006)