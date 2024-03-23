# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(37382)

except ImportError:
    pass
try:
    import numpy as np
    _l_(37384)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(37385)
sales_index = _c_(37390, _a_(37388, _a_(37387, _n_(37386, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(37389, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(37391)
_c_(37394, _n_(37392, "print", lambda: print), _n_(37393, "sales_tuples", lambda: sales_tuples))
_l_(37395)
_c_(37397, _n_(37396, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(37398)
df = _c_(37406, _a_(37400, _n_(37399, "pd", lambda: pd), "DataFrame"), _c_(37404, _a_(37403, _a_(37402, _n_(37401, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(37405, "sales_index", lambda: sales_index))
_l_(37407)
_c_(37410, _n_(37408, "print", lambda: print), _n_(37409, "df", lambda: df))
_l_(37411)
_c_(37413, _n_(37412, "print", lambda: print), '\nSort on MultiIndex DataFrame:')
_l_(37414)
df1 = _c_(37417, _a_(37416, _n_(37415, "df", lambda: df), "sort_index"))
_l_(37418)
_c_(37420, _n_(37419, "print", lambda: print), '\nSort on Index level=0 of the DataFrame:')
_l_(37421)
df2 = _c_(37424, _a_(37423, _n_(37422, "df", lambda: df), "sort_index"), level=0)
_l_(37425)
_c_(37428, _n_(37426, "print", lambda: print), _n_(37427, "df2", lambda: df2))
_l_(37429)
_c_(37431, _n_(37430, "print", lambda: print), '\nSort on Index level=1 of the DataFrame:')
_l_(37432)
df2 = _c_(37435, _a_(37434, _n_(37433, "df", lambda: df), "sort_index"), level=1)
_l_(37436)
_c_(37439, _n_(37437, "print", lambda: print), _n_(37438, "df2", lambda: df2))
_l_(37440)
_c_(37442, _n_(37441, "print", lambda: print), '\nPass a level name to sort the DataFrame:')
_l_(37443)
df3 = _c_(37446, _a_(37445, _n_(37444, "df", lambda: df), "sort_index"), level='city')
_l_(37447)
_c_(37450, _n_(37448, "print", lambda: print), _n_(37449, "df3", lambda: df3))
_l_(37451)