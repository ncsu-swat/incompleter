# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(72889)

except ImportError:
    pass
_c_(72891, _n_(72890, "print", lambda: print), 'Original DataFrame:')
_l_(72892)
_c_(72895, _n_(72893, "print", lambda: print), _n_(72894, "df", lambda: df))
_l_(72896)
_c_(72898, _n_(72897, "print", lambda: print), '\nDefault Index Range:')
_l_(72899)
_c_(72903, _n_(72900, "print", lambda: print), _a_(72902, _n_(72901, "df", lambda: df), "index"))
_l_(72904)
_n_(72905, "df", lambda: df).index += 10
_l_(72906)
_c_(72908, _n_(72907, "print", lambda: print), '\nNew Index Range:')
_l_(72909)
_c_(72913, _n_(72910, "print", lambda: print), _a_(72912, _n_(72911, "df", lambda: df), "index"))
_l_(72914)
_c_(72916, _n_(72915, "print", lambda: print), '\nDataFrame with new index:')
_l_(72917)
_c_(72920, _n_(72918, "print", lambda: print), _n_(72919, "df", lambda: df))
_l_(72921)