# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(48457)

except ImportError:
    pass
try:
    import re as re
    _l_(48459)

except ImportError:
    pass
_c_(48462, _a_(48461, _n_(48460, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(48463)
df = _c_(48466, _a_(48465, _n_(48464, "pd", lambda: pd), "DataFrame"), {'company_code': ['c0001', 'c0002', 'c0003', 'c0003', 'c0004'], 'address': ['72 Surrey Ave.11', '92 N. Bishop Ave.', '9910 Golden Star St.', '102 Dunbar St.', '17 West Livingston Court']})
_l_(48467)
_c_(48469, _n_(48468, "print", lambda: print), 'Original DataFrame:')
_l_(48470)
_c_(48473, _n_(48471, "print", lambda: print), _n_(48472, "df", lambda: df))
_l_(48474)

def test_num_less(n):
    _l_(48495)

    nums = []
    _l_(48475)
    for i in _c_(48478, _a_(48477, _n_(48476, "n", lambda: n), "split")):
        _l_(48490)

        _c_(48482, _a_(48480, _n_(48479, "nums", lambda: nums), "append"), _n_(48481, "result", lambda: result))
        _l_(48483)
        all_num = [_c_(48486, _a_(48484, ',', "join"), _n_(48485, "x", lambda: x)) for x in _n_(48487, "nums", lambda: nums) if _n_(48488, "x", lambda: x) != []]
        _l_(48489)
    aux = _c_(48493, _a_(48491, ' ', "join"), _n_(48492, "all_num", lambda: all_num))
    _l_(48494)
    return aux
_n_(48496, "df", lambda: df)['num_less'] = _c_(48502, _a_(48498, _n_(48497, "df", lambda: df)['address'], "apply"), lambda x: _c_(48501, _n_(48499, "test_num_less", lambda: test_num_less), _n_(48500, "x", lambda: x)))
_l_(48503)
_c_(48505, _n_(48504, "print", lambda: print), '\nNumber less than 100:')
_l_(48506)
_c_(48509, _n_(48507, "print", lambda: print), _n_(48508, "df", lambda: df))
_l_(48510)