# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(116952)

except ImportError:
    pass
try:
    import re as re
    _l_(116954)

except ImportError:
    pass
_c_(116957, _a_(116956, _n_(116955, "pd", lambda: pd), "set_option"), 'display.max_columns', 10)
_l_(116958)
_c_(116960, _n_(116959, "print", lambda: print), 'Original DataFrame:')
_l_(116961)
_c_(116964, _n_(116962, "print", lambda: print), _n_(116963, "df", lambda: df))
_l_(116965)

def test_num_less(n):
    _l_(116991)

    nums = []
    _l_(116966)
    for i in _c_(116969, _a_(116968, _n_(116967, "n", lambda: n), "split")):
        _l_(116986)

        result = _c_(116973, _a_(116971, _n_(116970, "re", lambda: re), "findall"), '\\b(0*(?:[1-9][0-9]?|100))\\b', _n_(116972, "i", lambda: i))
        _l_(116974)
        _c_(116978, _a_(116976, _n_(116975, "nums", lambda: nums), "append"), _n_(116977, "result", lambda: result))
        _l_(116979)
        all_num = [_c_(116982, _a_(116980, ',', "join"), _n_(116981, "x", lambda: x)) for x in _n_(116983, "nums", lambda: nums) if _n_(116984, "x", lambda: x) != []]
        _l_(116985)
    aux = _c_(116989, _a_(116987, ' ', "join"), _n_(116988, "all_num", lambda: all_num))
    _l_(116990)
    return aux
_n_(116992, "df", lambda: df)['num_less'] = _c_(116998, _a_(116994, _n_(116993, "df", lambda: df)['address'], "apply"), lambda x: _c_(116997, _n_(116995, "test_num_less", lambda: test_num_less), _n_(116996, "x", lambda: x)))
_l_(116999)
_c_(117001, _n_(117000, "print", lambda: print), '\nNumber less than 100:')
_l_(117002)
_c_(117005, _n_(117003, "print", lambda: print), _n_(117004, "df", lambda: df))
_l_(117006)