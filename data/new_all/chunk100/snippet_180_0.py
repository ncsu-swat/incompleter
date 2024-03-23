# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(14331)

except ImportError:
    pass
df = _c_(14334, _a_(14333, _n_(14332, "pd", lambda: pd), "DataFrame"), {'year': [2018, 2019, 2020], 'month': [2, 3, 4], 'day': [4, 5, 6], 'hour': [2, 3, 4]})
_l_(14335)
_c_(14337, _n_(14336, "print", lambda: print), 'Original dataframe:')
_l_(14338)
_c_(14341, _n_(14339, "print", lambda: print), _n_(14340, "df", lambda: df))
_l_(14342)
_c_(14344, _n_(14343, "print", lambda: print), '\nSeries of Timestamps from the said dataframe:')
_l_(14345)
_c_(14348, _n_(14346, "print", lambda: print), _n_(14347, "result", lambda: result))
_l_(14349)
_c_(14351, _n_(14350, "print", lambda: print), '\nSeries of Timestamps using specified columns:')
_l_(14352)
_c_(14358, _n_(14353, "print", lambda: print), _c_(14357, _a_(14355, _n_(14354, "pd", lambda: pd), "to_datetime"), _n_(14356, "df", lambda: df)[['year', 'month', 'day']]))
_l_(14359)