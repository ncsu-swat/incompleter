# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(120932)

except ImportError:
    pass
_c_(120935, _a_(120934, _n_(120933, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(120936)
_c_(120938, _n_(120937, "print", lambda: print), 'Original Orders DataFrame:')
_l_(120939)
_c_(120942, _n_(120940, "print", lambda: print), _n_(120941, "df", lambda: df))
_l_(120943)
_n_(120944, "df", lambda: df)['ord_date'] = _c_(120948, _a_(120946, _n_(120945, "pd", lambda: pd), "to_datetime"), _n_(120947, "df", lambda: df)['ord_date'])
_l_(120949)
_c_(120951, _n_(120950, "print", lambda: print), '\nMonth wise purchase amount:')
_l_(120952)
result = _c_(120963, _a_(120961, _c_(120960, _a_(120956, _c_(120955, _a_(120954, _n_(120953, "df", lambda: df), "set_index"), 'ord_date'), "groupby"), _c_(120959, _a_(120958, _n_(120957, "pd", lambda: pd), "Grouper"), freq='M')), "agg"), {'purch_amt': _n_(120962, "sum", lambda: sum)})
_l_(120964)
_c_(120967, _n_(120965, "print", lambda: print), _n_(120966, "result", lambda: result))
_l_(120968)