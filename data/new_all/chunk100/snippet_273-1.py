# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(108015)

except ImportError:
    pass
_c_(108018, _a_(108017, _n_(108016, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(108019)
_c_(108021, _n_(108020, "print", lambda: print), 'Original Orders DataFrame:')
_l_(108022)
_c_(108025, _n_(108023, "print", lambda: print), _n_(108024, "df", lambda: df))
_l_(108026)
_n_(108027, "df", lambda: df)['ord_date'] = _c_(108031, _a_(108029, _n_(108028, "pd", lambda: pd), "to_datetime"), _n_(108030, "df", lambda: df)['ord_date'])
_l_(108032)
_c_(108034, _n_(108033, "print", lambda: print), '\nYear wise Month wise purchase amount:')
_l_(108035)
result = _c_(108047, _a_(108045, _c_(108044, _a_(108037, _n_(108036, "df", lambda: df), "groupby"), [_a_(108040, _a_(108039, _n_(108038, "df", lambda: df)['ord_date'], "dt"), "year"), _a_(108043, _a_(108042, _n_(108041, "df", lambda: df)['ord_date'], "dt"), "month")]), "agg"), {'purch_amt': _n_(108046, "sum", lambda: sum)})
_l_(108048)
_c_(108051, _n_(108049, "print", lambda: print), _n_(108050, "result", lambda: result))
_l_(108052)