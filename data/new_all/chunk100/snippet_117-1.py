# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(101087)

except ImportError:
    pass
_c_(101090, _a_(101089, _n_(101088, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(101091)
_c_(101093, _n_(101092, "print", lambda: print), 'Original DataFrame:')
_l_(101094)
_c_(101097, _n_(101095, "print", lambda: print), _n_(101096, "df", lambda: df))
_l_(101098)
_c_(101100, _n_(101099, "print", lambda: print), '\nGroup by with multiple aggregations:')
_l_(101101)
result = _c_(101106, _a_(101105, _c_(101104, _a_(101103, _n_(101102, "df", lambda: df), "groupby"), ['school_code', 'class']), "agg"), {'height': ['max', 'mean'], 'weight': ['sum', 'min', 'count']})
_l_(101107)
_c_(101110, _n_(101108, "print", lambda: print), _n_(101109, "result", lambda: result))
_l_(101111)