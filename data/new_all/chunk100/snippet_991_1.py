# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(98489)

except ImportError:
    pass
_c_(98492, _a_(98491, _n_(98490, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(98493)
_c_(98495, _n_(98494, "print", lambda: print), 'Original Orders DataFrame:')
_l_(98496)
_c_(98499, _n_(98497, "print", lambda: print), _n_(98498, "orders_data", lambda: orders_data))
_l_(98500)
result = _c_(98505, _a_(98504, _c_(98503, _a_(98502, _n_(98501, "orders_data", lambda: orders_data), "groupby"), 'customer_id'), "agg"), {'purch_amt': ['mean', 'min', 'max']})
_l_(98506)
_c_(98508, _n_(98507, "print", lambda: print), '\nMean, min, and max values of purchase amount (purch_amt) group by customer id  (customer_id).')
_l_(98509)
_c_(98512, _n_(98510, "print", lambda: print), _n_(98511, "result", lambda: result))
_l_(98513)