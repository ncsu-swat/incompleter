# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57917397/i-get-this-type-of-error-typeerror-not-supported-between-instances-of-in
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.preprocessing import LabelEncoder
    _l_(672730)

except ImportError:
    pass
var_mod = ['Gender','Married','Dependents','Education','Self_Employed','Property_Area']
_l_(672731)
le = _c_(672733, _n_(672732, "LabelEncoder", lambda: LabelEncoder))
_l_(672734)
for i in _n_(672735, "var_mod", lambda: var_mod):
    _l_(672744)

    _n_(672736, "data", lambda: data)[_n_(672737, "i", lambda: i)] = _c_(672742, _a_(672739, _n_(672738, "le", lambda: le), "fit_transform"), _n_(672740, "data", lambda: data)[_n_(672741, "i", lambda: i)])
    _l_(672743)