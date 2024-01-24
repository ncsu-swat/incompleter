# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74920325/dtreeviz-attributeerror-dataframe-object-has-no-attribute-dtype-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
X = _n_(542668, "df1", lambda: df1)[['age', 'gender', 'portfolio_type', 'platform']]
_l_(542669)
X = _c_(542673, _a_(542671, _n_(542670, "pd", lambda: pd), "get_dummies"), data=_n_(542672, "X", lambda: X), drop_first=True)
_l_(542674)

Y = _n_(542675, "df1", lambda: df1)[[ 'Customer']]
_l_(542676)
Y = _c_(542680, _a_(542678, _n_(542677, "pd", lambda: pd), "get_dummies"), data=_n_(542679, "Y", lambda: Y), drop_first=True)
_l_(542681)