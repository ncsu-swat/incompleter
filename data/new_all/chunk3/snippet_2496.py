# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74920325/dtreeviz-attributeerror-dataframe-object-has-no-attribute-dtype-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.model_selection import train_test_split
    _l_(568365)

except ImportError:
    pass
X_train, X_test, y_train, y_test = _c_(568369, _n_(568366, "train_test_split", lambda: train_test_split), _n_(568367, "X", lambda: X), _n_(568368, "Y", lambda: Y), test_size=0.4, random_state=101)
_l_(568370)