# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(78975)

except ImportError:
    pass
try:
    import numpy as np
    _l_(78977)

except ImportError:
    pass
_c_(78981, _a_(78980, _a_(78979, _n_(78978, "np", lambda: np), "random"), "seed"), 24)
_l_(78982)
df = _c_(78995, _a_(78984, _n_(78983, "pd", lambda: pd), "concat"), [_n_(78985, "df", lambda: df), _c_(78994, _a_(78987, _n_(78986, "pd", lambda: pd), "DataFrame"), _c_(78991, _a_(78990, _a_(78989, _n_(78988, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(78993, _n_(78992, "list", lambda: list), 'BCDE'))], axis=1)
_l_(78996)
_a_(78998, _n_(78997, "df", lambda: df), "iloc")[0, 2] = _a_(79000, _n_(78999, "np", lambda: np), "nan")
_l_(79001)
_a_(79003, _n_(79002, "df", lambda: df), "iloc")[3, 3] = _a_(79005, _n_(79004, "np", lambda: np), "nan")
_l_(79006)
_a_(79008, _n_(79007, "df", lambda: df), "iloc")[4, 1] = _a_(79010, _n_(79009, "np", lambda: np), "nan")
_l_(79011)
_a_(79013, _n_(79012, "df", lambda: df), "iloc")[9, 4] = _a_(79015, _n_(79014, "np", lambda: np), "nan")
_l_(79016)
_c_(79018, _n_(79017, "print", lambda: print), 'Original array:')
_l_(79019)
_c_(79022, _n_(79020, "print", lambda: print), _n_(79021, "df", lambda: df))
_l_(79023)

def highlight_max(s):
    _l_(79032)

    """
    highlight the maximum in a Series green.
    """
    is_max = _n_(79024, "s", lambda: s) == _c_(79027, _a_(79026, _n_(79025, "s", lambda: s), "max"))
    _l_(79028)
    aux = ['background-color: green' if _n_(79029, "v", lambda: v) else '' for v in _n_(79030, "is_max", lambda: is_max)]
    _l_(79031)
    return aux
_c_(79034, _n_(79033, "print", lambda: print), '\nHighlight the maximum value in last two columns:')
_l_(79035)
_c_(79042, _a_(79038, _a_(79037, _n_(79036, "df", lambda: df), "style"), "apply"), _n_(79039, "highlight_max", lambda: highlight_max), subset=_a_(79041, _n_(79040, "pd", lambda: pd), "IndexSlice")[:, ['D', 'E']])
_l_(79043)