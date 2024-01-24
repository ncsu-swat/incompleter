# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66364406/attributeerror-smote-object-has-no-attribute-fit-sample
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from imblearn.over_sampling import SMOTE
    _l_(411407)

except ImportError:
    pass
smt = _c_(411409, _n_(411408, "SMOTE", lambda: SMOTE), random_state=0)
_l_(411410)
X_train_SMOTE, y_train_SMOTE = _c_(411415, _a_(411412, _n_(411411, "smt", lambda: smt), "fit_sample"), _n_(411413, "X_train", lambda: X_train), _n_(411414, "y_train", lambda: y_train))
_l_(411416)