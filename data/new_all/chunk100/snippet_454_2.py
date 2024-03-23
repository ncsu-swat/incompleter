# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(48512)

except ImportError:
    pass
try:
    import re as re
    _l_(48514)

except ImportError:
    pass
_c_(48517, _a_(48516, _n_(48515, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(48518)
df = _c_(48521, _a_(48520, _n_(48519, "pd", lambda: pd), "DataFrame"), {'company_code': ['c0001', 'c0002', 'c0003', 'c0003', 'c0004'], 'address': ['72 Surrey Ave.11', '92 N. Bishop Ave.', '9910 Golden Star St.', '102 Dunbar St.', '17 West Livingston Court']})
_l_(48522)
_c_(48524, _n_(48523, "print", lambda: print), 'Original DataFrame:')
_l_(48525)
_c_(48528, _n_(48526, "print", lambda: print), _n_(48527, "df", lambda: df))
_l_(48529)

def test_num_less(n):
    _l_(48554)

    for i in _c_(48532, _a_(48531, _n_(48530, "n", lambda: n), "split")):
        _l_(48549)

        result = _c_(48536, _a_(48534, _n_(48533, "re", lambda: re), "findall"), '\\b(0*(?:[1-9][0-9]?|100))\\b', _n_(48535, "i", lambda: i))
        _l_(48537)
        _c_(48541, _a_(48539, _n_(48538, "nums", lambda: nums), "append"), _n_(48540, "result", lambda: result))
        _l_(48542)
        all_num = [_c_(48545, _a_(48543, ',', "join"), _n_(48544, "x", lambda: x)) for x in _n_(48546, "nums", lambda: nums) if _n_(48547, "x", lambda: x) != []]
        _l_(48548)
    aux = _c_(48552, _a_(48550, ' ', "join"), _n_(48551, "all_num", lambda: all_num))
    _l_(48553)
    return aux
_n_(48555, "df", lambda: df)['num_less'] = _c_(48561, _a_(48557, _n_(48556, "df", lambda: df)['address'], "apply"), lambda x: _c_(48560, _n_(48558, "test_num_less", lambda: test_num_less), _n_(48559, "x", lambda: x)))
_l_(48562)
_c_(48564, _n_(48563, "print", lambda: print), '\nNumber less than 100:')
_l_(48565)
_c_(48568, _n_(48566, "print", lambda: print), _n_(48567, "df", lambda: df))
_l_(48569)