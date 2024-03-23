# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(48401)

except ImportError:
    pass
try:
    import re as re
    _l_(48403)

except ImportError:
    pass
_c_(48406, _a_(48405, _n_(48404, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(48407)
_c_(48409, _n_(48408, "print", lambda: print), 'Original DataFrame:')
_l_(48410)
_c_(48413, _n_(48411, "print", lambda: print), _n_(48412, "df", lambda: df))
_l_(48414)

def test_num_less(n):
    _l_(48440)

    nums = []
    _l_(48415)
    for i in _c_(48418, _a_(48417, _n_(48416, "n", lambda: n), "split")):
        _l_(48435)

        result = _c_(48422, _a_(48420, _n_(48419, "re", lambda: re), "findall"), '\\b(0*(?:[1-9][0-9]?|100))\\b', _n_(48421, "i", lambda: i))
        _l_(48423)
        _c_(48427, _a_(48425, _n_(48424, "nums", lambda: nums), "append"), _n_(48426, "result", lambda: result))
        _l_(48428)
        all_num = [_c_(48431, _a_(48429, ',', "join"), _n_(48430, "x", lambda: x)) for x in _n_(48432, "nums", lambda: nums) if _n_(48433, "x", lambda: x) != []]
        _l_(48434)
    aux = _c_(48438, _a_(48436, ' ', "join"), _n_(48437, "all_num", lambda: all_num))
    _l_(48439)
    return aux
_n_(48441, "df", lambda: df)['num_less'] = _c_(48447, _a_(48443, _n_(48442, "df", lambda: df)['address'], "apply"), lambda x: _c_(48446, _n_(48444, "test_num_less", lambda: test_num_less), _n_(48445, "x", lambda: x)))
_l_(48448)
_c_(48450, _n_(48449, "print", lambda: print), '\nNumber less than 100:')
_l_(48451)
_c_(48454, _n_(48452, "print", lambda: print), _n_(48453, "df", lambda: df))
_l_(48455)