# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57917397/i-get-this-type-of-error-typeerror-not-supported-between-instances-of-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.preprocessing import LabelEncoder
    _l_(684083)

except ImportError:
    pass
var_mod = ['Gender','Married','Dependents','Education','Self_Employed','Property_Area']
_l_(684084)
le = _c_(684086, _n_(684085, "LabelEncoder", lambda: LabelEncoder))
_l_(684087)
for i in _n_(684088, "var_mod", lambda: var_mod):
    _l_(684097)

    _n_(684089, "data", lambda: data)[_n_(684090, "i", lambda: i)] = _c_(684095, _a_(684092, _n_(684091, "le", lambda: le), "fit_transform"), _n_(684093, "data", lambda: data)[_n_(684094, "i", lambda: i)])
    _l_(684096)