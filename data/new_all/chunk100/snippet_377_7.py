# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(37599)

except ImportError:
    pass
try:
    import numpy as np
    _l_(37601)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(37602)
sales_tuples = _c_(37607, _n_(37603, "list", lambda: list), _c_(37606, _n_(37604, "zip", lambda: zip), *_n_(37605, "sales_arrays", lambda: sales_arrays)))
_l_(37608)
sales_index = _c_(37613, _a_(37611, _a_(37610, _n_(37609, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(37612, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(37614)
_c_(37617, _n_(37615, "print", lambda: print), _n_(37616, "sales_tuples", lambda: sales_tuples))
_l_(37618)
_c_(37620, _n_(37619, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(37621)
df = _c_(37629, _a_(37623, _n_(37622, "pd", lambda: pd), "DataFrame"), _c_(37627, _a_(37626, _a_(37625, _n_(37624, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(37628, "sales_index", lambda: sales_index))
_l_(37630)
_c_(37633, _n_(37631, "print", lambda: print), _n_(37632, "df", lambda: df))
_l_(37634)
_c_(37636, _n_(37635, "print", lambda: print), '\nSort on MultiIndex DataFrame:')
_l_(37637)
_c_(37639, _n_(37638, "print", lambda: print), '\nSort on Index level=0 of the DataFrame:')
_l_(37640)
df2 = _c_(37643, _a_(37642, _n_(37641, "df", lambda: df), "sort_index"), level=0)
_l_(37644)
_c_(37647, _n_(37645, "print", lambda: print), _n_(37646, "df2", lambda: df2))
_l_(37648)
_c_(37650, _n_(37649, "print", lambda: print), '\nSort on Index level=1 of the DataFrame:')
_l_(37651)
df2 = _c_(37654, _a_(37653, _n_(37652, "df", lambda: df), "sort_index"), level=1)
_l_(37655)
_c_(37658, _n_(37656, "print", lambda: print), _n_(37657, "df2", lambda: df2))
_l_(37659)
_c_(37661, _n_(37660, "print", lambda: print), '\nPass a level name to sort the DataFrame:')
_l_(37662)
df3 = _c_(37665, _a_(37664, _n_(37663, "df", lambda: df), "sort_index"), level='city')
_l_(37666)
_c_(37669, _n_(37667, "print", lambda: print), _n_(37668, "df3", lambda: df3))
_l_(37670)