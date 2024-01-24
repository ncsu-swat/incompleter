# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69051693/is-attributeerror-working-as-it-should-pandas-df
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
"""
creating dict of {symbol:[spot, aggregate]
"""

abn_dict = _c_(542683, _n_(542682, "defaultdict", lambda: defaultdict), lambda: [0, 0])
_l_(542684)

for (col, row) in _c_(542687, _a_(542686, _n_(542685, "abn_df", lambda: abn_df), "iterrows")):
    _l_(542708)

    try:
        _l_(542707)

        _c_(542691, _a_(542690, _a_(542689, _n_(542688, "row", lambda: row), "loc")["Quantity Long"], "isnull"))
        _l_(542692)
        _n_(542693, "abn_dict", lambda: abn_dict)[_a_(542695, _n_(542694, "row", lambda: row), "loc")["Symbol"]][1] += _a_(542697, _n_(542696, "row", lambda: row), "loc")["Quantity Short"]
        _l_(542698)
    except _n_(542699, "AttributeError", lambda: AttributeError):
        _l_(542706)

        _n_(542700, "abn_dict", lambda: abn_dict)[_a_(542702, _n_(542701, "row", lambda: row), "loc")["Symbol"]][1] += _a_(542704, _n_(542703, "row", lambda: row), "loc")["Quantity Long"]
        _l_(542705)