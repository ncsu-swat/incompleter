# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(37453)

except ImportError:
    pass
try:
    import numpy as np
    _l_(37455)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(37456)
sales_tuples = _c_(37461, _n_(37457, "list", lambda: list), _c_(37460, _n_(37458, "zip", lambda: zip), *_n_(37459, "sales_arrays", lambda: sales_arrays)))
_l_(37462)
sales_index = _c_(37467, _a_(37465, _a_(37464, _n_(37463, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(37466, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(37468)
_c_(37471, _n_(37469, "print", lambda: print), _n_(37470, "sales_tuples", lambda: sales_tuples))
_l_(37472)
_c_(37474, _n_(37473, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(37475)
df = _c_(37483, _a_(37477, _n_(37476, "pd", lambda: pd), "DataFrame"), _c_(37481, _a_(37480, _a_(37479, _n_(37478, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(37482, "sales_index", lambda: sales_index))
_l_(37484)
_c_(37487, _n_(37485, "print", lambda: print), _n_(37486, "df", lambda: df))
_l_(37488)
_c_(37490, _n_(37489, "print", lambda: print), '\nSort on MultiIndex DataFrame:')
_l_(37491)
df1 = _c_(37494, _a_(37493, _n_(37492, "df", lambda: df), "sort_index"))
_l_(37495)
_c_(37497, _n_(37496, "print", lambda: print), '\nSort on Index level=0 of the DataFrame:')
_l_(37498)
df2 = _c_(37501, _a_(37500, _n_(37499, "df", lambda: df), "sort_index"), level=0)
_l_(37502)
_c_(37505, _n_(37503, "print", lambda: print), _n_(37504, "df2", lambda: df2))
_l_(37506)
_c_(37508, _n_(37507, "print", lambda: print), '\nSort on Index level=1 of the DataFrame:')
_l_(37509)
df2 = _c_(37512, _a_(37511, _n_(37510, "df", lambda: df), "sort_index"), level=1)
_l_(37513)
_c_(37516, _n_(37514, "print", lambda: print), _n_(37515, "df2", lambda: df2))
_l_(37517)
_c_(37519, _n_(37518, "print", lambda: print), '\nPass a level name to sort the DataFrame:')
_l_(37520)
_c_(37523, _n_(37521, "print", lambda: print), _n_(37522, "df3", lambda: df3))
_l_(37524)