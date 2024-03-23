# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(14361)

except ImportError:
    pass
_c_(14363, _n_(14362, "print", lambda: print), 'Original dataframe:')
_l_(14364)
_c_(14367, _n_(14365, "print", lambda: print), _n_(14366, "df", lambda: df))
_l_(14368)
result = _c_(14372, _a_(14370, _n_(14369, "pd", lambda: pd), "to_datetime"), _n_(14371, "df", lambda: df))
_l_(14373)
_c_(14375, _n_(14374, "print", lambda: print), '\nSeries of Timestamps from the said dataframe:')
_l_(14376)
_c_(14379, _n_(14377, "print", lambda: print), _n_(14378, "result", lambda: result))
_l_(14380)
_c_(14382, _n_(14381, "print", lambda: print), '\nSeries of Timestamps using specified columns:')
_l_(14383)
_c_(14389, _n_(14384, "print", lambda: print), _c_(14388, _a_(14386, _n_(14385, "pd", lambda: pd), "to_datetime"), _n_(14387, "df", lambda: df)[['year', 'month', 'day']]))
_l_(14390)