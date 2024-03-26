# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(103867)

except ImportError:
    pass
df = _c_(103870, _a_(103869, _n_(103868, "pd", lambda: pd), "DataFrame"), {'year': [2018, 2019, 2020], 'month': [2, 3, 4], 'day': [4, 5, 6], 'hour': [2, 3, 4]})
_l_(103871)
_c_(103873, _n_(103872, "print", lambda: print), 'Original dataframe:')
_l_(103874)
_c_(103877, _n_(103875, "print", lambda: print), _n_(103876, "df", lambda: df))
_l_(103878)
_c_(103880, _n_(103879, "print", lambda: print), '\nSeries of Timestamps from the said dataframe:')
_l_(103881)
_c_(103884, _n_(103882, "print", lambda: print), _n_(103883, "result", lambda: result))
_l_(103885)
_c_(103887, _n_(103886, "print", lambda: print), '\nSeries of Timestamps using specified columns:')
_l_(103888)
_c_(103894, _n_(103889, "print", lambda: print), _c_(103893, _a_(103891, _n_(103890, "pd", lambda: pd), "to_datetime"), _n_(103892, "df", lambda: df)[['year', 'month', 'day']]))
_l_(103895)