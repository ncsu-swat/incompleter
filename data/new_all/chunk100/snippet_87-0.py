# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(120970)

except ImportError:
    pass
_c_(120972, _n_(120971, "print", lambda: print), 'Original dataframe:')
_l_(120973)
df = _c_(120977, _a_(120975, _n_(120974, "pd", lambda: pd), "DataFrame"), _n_(120976, "nums", lambda: nums))
_l_(120978)
_c_(120981, _n_(120979, "print", lambda: print), _n_(120980, "df", lambda: df))
_l_(120982)
_c_(120984, _n_(120983, "print", lambda: print), '\nAdd leading zeros:')
_l_(120985)
_n_(120986, "df", lambda: df)['amount'] = _c_(120994, _n_(120987, "list", lambda: list), _c_(120993, _n_(120988, "map", lambda: map), lambda x: _c_(120991, _a_(120990, _n_(120989, "x", lambda: x), "zfill"), 10), _n_(120992, "df", lambda: df)['amount']))
_l_(120995)
_c_(120998, _n_(120996, "print", lambda: print), _n_(120997, "df", lambda: df))
_l_(120999)