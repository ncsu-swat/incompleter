# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(48571)

except ImportError:
    pass
try:
    import re as re
    _l_(48573)

except ImportError:
    pass
_c_(48576, _a_(48575, _n_(48574, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(48577)
df = _c_(48580, _a_(48579, _n_(48578, "pd", lambda: pd), "DataFrame"), {'company_code': ['c0001', 'c0002', 'c0003', 'c0003', 'c0004'], 'address': ['72 Surrey Ave.11', '92 N. Bishop Ave.', '9910 Golden Star St.', '102 Dunbar St.', '17 West Livingston Court']})
_l_(48581)
_c_(48583, _n_(48582, "print", lambda: print), 'Original DataFrame:')
_l_(48584)
_c_(48587, _n_(48585, "print", lambda: print), _n_(48586, "df", lambda: df))
_l_(48588)

def test_num_less(n):
    _l_(48608)

    nums = []
    _l_(48589)
    for i in _c_(48592, _a_(48591, _n_(48590, "n", lambda: n), "split")):
        _l_(48603)

        result = _c_(48596, _a_(48594, _n_(48593, "re", lambda: re), "findall"), '\\b(0*(?:[1-9][0-9]?|100))\\b', _n_(48595, "i", lambda: i))
        _l_(48597)
        _c_(48601, _a_(48599, _n_(48598, "nums", lambda: nums), "append"), _n_(48600, "result", lambda: result))
        _l_(48602)
    aux = _c_(48606, _a_(48604, ' ', "join"), _n_(48605, "all_num", lambda: all_num))
    _l_(48607)
    return aux
_n_(48609, "df", lambda: df)['num_less'] = _c_(48615, _a_(48611, _n_(48610, "df", lambda: df)['address'], "apply"), lambda x: _c_(48614, _n_(48612, "test_num_less", lambda: test_num_less), _n_(48613, "x", lambda: x)))
_l_(48616)
_c_(48618, _n_(48617, "print", lambda: print), '\nNumber less than 100:')
_l_(48619)
_c_(48622, _n_(48620, "print", lambda: print), _n_(48621, "df", lambda: df))
_l_(48623)