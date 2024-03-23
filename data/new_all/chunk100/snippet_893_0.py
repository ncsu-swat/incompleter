# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(87847)

except ImportError:
    pass
_c_(87849, _n_(87848, "print", lambda: print), 'Original Series:')
_l_(87850)
_c_(87853, _n_(87851, "print", lambda: print), _n_(87852, "date_series", lambda: date_series))
_l_(87854)
_c_(87856, _n_(87855, "print", lambda: print), '\nSeries of date strings to a timeseries:')
_l_(87857)
_c_(87863, _n_(87858, "print", lambda: print), _c_(87862, _a_(87860, _n_(87859, "pd", lambda: pd), "to_datetime"), _n_(87861, "date_series", lambda: date_series)))
_l_(87864)