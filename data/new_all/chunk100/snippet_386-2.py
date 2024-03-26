# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(114004)

except ImportError:
    pass
_c_(114007, _a_(114006, _n_(114005, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(114008)
_c_(114010, _n_(114009, "print", lambda: print), 'Original Orders DataFrame:')
_l_(114011)
_c_(114014, _n_(114012, "print", lambda: print), _n_(114013, "df", lambda: df))
_l_(114015)
df_agg = _c_(114021, _a_(114019, _c_(114018, _a_(114017, _n_(114016, "df", lambda: df), "groupby"), ['customer_id', 'salesman_id']), "agg"), {'purch_amt': _n_(114020, "sum", lambda: sum)})
_l_(114022)
result = _c_(114025, _a_(114024, _n_(114023, "df_agg", lambda: df_agg)['purch_amt'], "groupby"), level=0, group_keys=False)
_l_(114026)
_c_(114028, _n_(114027, "print", lambda: print), "\nGroup on 'customer_id', 'salesman_id' and then sort sum of purch_amt within the groups:")
_l_(114029)
_c_(114034, _n_(114030, "print", lambda: print), _c_(114033, _a_(114032, _n_(114031, "result", lambda: result), "nlargest")))
_l_(114035)