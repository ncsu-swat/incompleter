# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(22037)

except ImportError:
    pass
_c_(22040, _a_(22039, _n_(22038, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(22041)
_c_(22043, _n_(22042, "print", lambda: print), 'Original Orders DataFrame:')
_l_(22044)
_c_(22047, _n_(22045, "print", lambda: print), _n_(22046, "df", lambda: df))
_l_(22048)
_n_(22049, "df", lambda: df)['ord_date'] = _c_(22053, _a_(22051, _n_(22050, "pd", lambda: pd), "to_datetime"), _n_(22052, "df", lambda: df)['ord_date'])
_l_(22054)
_c_(22056, _n_(22055, "print", lambda: print), '\nYear wise Month wise purchase amount:')
_l_(22057)
result = _c_(22069, _a_(22067, _c_(22066, _a_(22059, _n_(22058, "df", lambda: df), "groupby"), [_a_(22062, _a_(22061, _n_(22060, "df", lambda: df)['ord_date'], "dt"), "year"), _a_(22065, _a_(22064, _n_(22063, "df", lambda: df)['ord_date'], "dt"), "month")]), "agg"), {'purch_amt': _n_(22068, "sum", lambda: sum)})
_l_(22070)
_c_(22073, _n_(22071, "print", lambda: print), _n_(22072, "result", lambda: result))
_l_(22074)