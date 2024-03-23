# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(88019)

except ImportError:
    pass
_c_(88022, _a_(88021, _n_(88020, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(88023)
_c_(88025, _n_(88024, "print", lambda: print), 'Original Orders DataFrame:')
_l_(88026)
_c_(88029, _n_(88027, "print", lambda: print), _n_(88028, "df", lambda: df))
_l_(88030)
_n_(88031, "df", lambda: df)['ord_date'] = _c_(88035, _a_(88033, _n_(88032, "pd", lambda: pd), "to_datetime"), _n_(88034, "df", lambda: df)['ord_date'])
_l_(88036)
_c_(88038, _n_(88037, "print", lambda: print), '\nQuartly purchase amount:')
_l_(88039)
result = _c_(88050, _a_(88048, _c_(88047, _a_(88043, _c_(88042, _a_(88041, _n_(88040, "df", lambda: df), "set_index"), 'ord_date'), "groupby"), _c_(88046, _a_(88045, _n_(88044, "pd", lambda: pd), "Grouper"), freq='Q')), "agg"), {'purch_amt': _n_(88049, "sum", lambda: sum)})
_l_(88051)
_c_(88054, _n_(88052, "print", lambda: print), _n_(88053, "result", lambda: result))
_l_(88055)