# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(38559)

except ImportError:
    pass
_c_(38562, _a_(38561, _n_(38560, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(38563)
_c_(38565, _n_(38564, "print", lambda: print), 'Original Orders DataFrame:')
_l_(38566)
_c_(38569, _n_(38567, "print", lambda: print), _n_(38568, "df", lambda: df))
_l_(38570)
df_agg = _c_(38576, _a_(38574, _c_(38573, _a_(38572, _n_(38571, "df", lambda: df), "groupby"), ['customer_id', 'salesman_id']), "agg"), {'purch_amt': _n_(38575, "sum", lambda: sum)})
_l_(38577)
result = _c_(38580, _a_(38579, _n_(38578, "df_agg", lambda: df_agg)['purch_amt'], "groupby"), level=0, group_keys=False)
_l_(38581)
_c_(38583, _n_(38582, "print", lambda: print), "\nGroup on 'customer_id', 'salesman_id' and then sort sum of purch_amt within the groups:")
_l_(38584)
_c_(38589, _n_(38585, "print", lambda: print), _c_(38588, _a_(38587, _n_(38586, "result", lambda: result), "nlargest")))
_l_(38590)