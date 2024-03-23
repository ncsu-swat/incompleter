# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(5988)

except ImportError:
    pass
_c_(5991, _a_(5990, _n_(5989, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(5992)
_c_(5994, _n_(5993, "print", lambda: print), 'Original DataFrame:')
_l_(5995)
_c_(5998, _n_(5996, "print", lambda: print), _n_(5997, "df", lambda: df))
_l_(5999)
_c_(6001, _n_(6000, "print", lambda: print), '\nGroup by with multiple aggregations:')
_l_(6002)
result = _c_(6007, _a_(6006, _c_(6005, _a_(6004, _n_(6003, "df", lambda: df), "groupby"), ['school_code', 'class']), "agg"), {'height': ['max', 'mean'], 'weight': ['sum', 'min', 'count']})
_l_(6008)
_c_(6011, _n_(6009, "print", lambda: print), _n_(6010, "result", lambda: result))
_l_(6012)