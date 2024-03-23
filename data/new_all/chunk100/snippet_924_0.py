# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(94082)

except ImportError:
    pass
_c_(94085, _a_(94084, _n_(94083, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(94086)
_c_(94088, _n_(94087, "print", lambda: print), 'Original Orders DataFrame:')
_l_(94089)
_c_(94092, _n_(94090, "print", lambda: print), _n_(94091, "df", lambda: df))
_l_(94093)
result = _c_(94099, _a_(94097, _c_(94096, _a_(94095, _n_(94094, "df", lambda: df), "groupby"), 'customer_id')['ord_date'], "apply"), _n_(94098, "list", lambda: list))
_l_(94100)
_c_(94102, _n_(94101, "print", lambda: print), "\nGroup on 'customer_id' and display the list of order dates in group wise:")
_l_(94103)
_c_(94106, _n_(94104, "print", lambda: print), _n_(94105, "result", lambda: result))
_l_(94107)