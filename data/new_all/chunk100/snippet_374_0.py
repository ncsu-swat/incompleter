# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(36969)

except ImportError:
    pass
try:
    import numpy as np
    _l_(36971)

except ImportError:
    pass
_c_(36975, _a_(36974, _a_(36973, _n_(36972, "np", lambda: np), "random"), "seed"), 24)
_l_(36976)
df = _c_(36989, _a_(36978, _n_(36977, "pd", lambda: pd), "concat"), [_n_(36979, "df", lambda: df), _c_(36988, _a_(36981, _n_(36980, "pd", lambda: pd), "DataFrame"), _c_(36985, _a_(36984, _a_(36983, _n_(36982, "np", lambda: np), "random"), "randn"), 10, 4), columns=_c_(36987, _n_(36986, "list", lambda: list), 'BCDE'))], axis=1)
_l_(36990)
_a_(36992, _n_(36991, "df", lambda: df), "iloc")[0, 2] = _a_(36994, _n_(36993, "np", lambda: np), "nan")
_l_(36995)
_a_(36997, _n_(36996, "df", lambda: df), "iloc")[3, 3] = _a_(36999, _n_(36998, "np", lambda: np), "nan")
_l_(37000)
_a_(37002, _n_(37001, "df", lambda: df), "iloc")[4, 1] = _a_(37004, _n_(37003, "np", lambda: np), "nan")
_l_(37005)
_a_(37007, _n_(37006, "df", lambda: df), "iloc")[9, 4] = _a_(37009, _n_(37008, "np", lambda: np), "nan")
_l_(37010)
_c_(37012, _n_(37011, "print", lambda: print), 'Original array:')
_l_(37013)
_c_(37016, _n_(37014, "print", lambda: print), _n_(37015, "df", lambda: df))
_l_(37017)
_c_(37019, _n_(37018, "print", lambda: print), '\nBackground:black - fontcolor:yelow')
_l_(37020)
_c_(37024, _a_(37023, _a_(37022, _n_(37021, "df", lambda: df), "style"), "set_properties"), **{'background-color': 'black', 'color': 'yellow'})
_l_(37025)