# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/77095936/nameerror-name-np-array-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(602220)

except ImportError:
    pass
def y_true():
    _l_(602227)

    np_array= _c_(602225, _a_(602222, _n_(602221, "np", lambda: np), "add"), _n_(602223, "y_true", lambda: y_true),_n_(602224, "y_pred", lambda: y_pred))
    _l_(602226)

no_of_pred =24
_l_(602228)
ind=72
_l_(602229)
y_pred= _c_(602234, _n_(602230, "forecast", lambda: forecast), _n_(602231, "x_val", lambda: x_val),_n_(602232, "no_of_pred", lambda: no_of_pred),_n_(602233, "ind", lambda: ind))
_l_(602235)
y_true = _n_(602236, "y_val", lambda: y_val)[_n_(602237, "ind", lambda: ind):_n_(602238, "ind", lambda: ind)+_n_(602239, "no_of_pred", lambda: (no_of_pred))]
_l_(602240)

# Lets convert back the normalized values to the original dimensional space
y_true = _c_(602243, _a_(602242, _n_(602241, "np_array", lambda: np_array), "reshape"), 1, -1)
_l_(602244)
y_true= _c_(602248, _a_(602246, _n_(602245, "y_scaler", lambda: y_scaler), "inverse_transform"), _n_(602247, "y_true", lambda: y_true))
_l_(602249)

y_pred = _c_(602252, _a_(602251, _n_(602250, "np_array", lambda: np_array), "reshape"), 1, -1)
_l_(602253)
y_pred= _c_(602257, _a_(602255, _n_(602254, "y_scaler", lambda: y_scaler), "inverse_transform"), _n_(602256, "y_pred", lambda: y_pred))
_l_(602258)