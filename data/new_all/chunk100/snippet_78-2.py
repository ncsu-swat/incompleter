# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(120204)

except ImportError:
    pass
_c_(120207, _a_(120206, _n_(120205, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(120208)
_c_(120210, _n_(120209, "print", lambda: print), 'Original Orders DataFrame:')
_l_(120211)
_c_(120214, _n_(120212, "print", lambda: print), _n_(120213, "df", lambda: df))
_l_(120215)
_c_(120217, _n_(120216, "print", lambda: print), "\nSplit the said data on 'salesman_id', 'customer_id' wise:")
_l_(120218)
result = _c_(120221, _a_(120220, _n_(120219, "df", lambda: df), "groupby"), ['salesman_id', 'customer_id'])
_l_(120222)
for name, group in _n_(120223, "result", lambda: result):
    _l_(120235)

    _c_(120225, _n_(120224, "print", lambda: print), '\nGroup:')
    _l_(120226)
    _c_(120229, _n_(120227, "print", lambda: print), _n_(120228, "name", lambda: name))
    _l_(120230)
    _c_(120233, _n_(120231, "print", lambda: print), _n_(120232, "group", lambda: group))
    _l_(120234)
n = 2
_l_(120236)
_c_(120238, _n_(120237, "print", lambda: print), '\nDroping last two records:')
_l_(120239)
result1 = _c_(120249, _a_(120241, _n_(120240, "df", lambda: df), "drop"), _a_(120248, _c_(120247, _a_(120245, _c_(120244, _a_(120243, _n_(120242, "df", lambda: df), "groupby"), ['salesman_id', 'customer_id']), "tail"), _n_(120246, "n", lambda: n)), "index"), axis=0)
_l_(120250)
_c_(120253, _n_(120251, "print", lambda: print), _n_(120252, "result1", lambda: result1))
_l_(120254)