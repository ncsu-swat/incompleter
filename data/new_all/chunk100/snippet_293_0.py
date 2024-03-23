# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(24936)

except ImportError:
    pass
_c_(24939, _a_(24938, _n_(24937, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(24940)
_c_(24943, _a_(24942, _n_(24941, "pd", lambda: pd), "set_option"), 'display.max_columns', None)
_l_(24944)
_c_(24946, _n_(24945, "print", lambda: print), 'Original Orders DataFrame:')
_l_(24947)
_c_(24950, _n_(24948, "print", lambda: print), _n_(24949, "df", lambda: df))
_l_(24951)
_c_(24953, _n_(24952, "print", lambda: print), '\\Result after group on salesman_id and apply different aggregate functions:')
_l_(24954)
df = _c_(24967, _a_(24958, _c_(24957, _a_(24956, _n_(24955, "df", lambda: df), "groupby"), 'salesman_id'), "agg"), lambda x: _c_(24961, _a_(24960, _n_(24959, "x", lambda: x), "sum")) if _a_(24963, _n_(24962, "x", lambda: x), "name") in ['sale_jan', 'sale_feb', 'sale_mar'] else _c_(24966, _a_(24965, _n_(24964, "x", lambda: x), "mean")))
_l_(24968)
_c_(24971, _n_(24969, "print", lambda: print), _n_(24970, "df", lambda: df))
_l_(24972)