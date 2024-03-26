# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(103836)

except ImportError:
    pass
_c_(103838, _n_(103837, "print", lambda: print), 'Original dataframe:')
_l_(103839)
_c_(103842, _n_(103840, "print", lambda: print), _n_(103841, "df", lambda: df))
_l_(103843)
result = _c_(103847, _a_(103845, _n_(103844, "pd", lambda: pd), "to_datetime"), _n_(103846, "df", lambda: df))
_l_(103848)
_c_(103850, _n_(103849, "print", lambda: print), '\nSeries of Timestamps from the said dataframe:')
_l_(103851)
_c_(103854, _n_(103852, "print", lambda: print), _n_(103853, "result", lambda: result))
_l_(103855)
_c_(103857, _n_(103856, "print", lambda: print), '\nSeries of Timestamps using specified columns:')
_l_(103858)
_c_(103864, _n_(103859, "print", lambda: print), _c_(103863, _a_(103861, _n_(103860, "pd", lambda: pd), "to_datetime"), _n_(103862, "df", lambda: df)[['year', 'month', 'day']]))
_l_(103865)