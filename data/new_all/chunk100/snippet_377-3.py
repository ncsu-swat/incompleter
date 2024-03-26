# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(113356)

except ImportError:
    pass
try:
    import numpy as np
    _l_(113358)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(113359)
sales_index = _c_(113364, _a_(113362, _a_(113361, _n_(113360, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(113363, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(113365)
_c_(113368, _n_(113366, "print", lambda: print), _n_(113367, "sales_tuples", lambda: sales_tuples))
_l_(113369)
_c_(113371, _n_(113370, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(113372)
df = _c_(113380, _a_(113374, _n_(113373, "pd", lambda: pd), "DataFrame"), _c_(113378, _a_(113377, _a_(113376, _n_(113375, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(113379, "sales_index", lambda: sales_index))
_l_(113381)
_c_(113384, _n_(113382, "print", lambda: print), _n_(113383, "df", lambda: df))
_l_(113385)
_c_(113387, _n_(113386, "print", lambda: print), '\nSort on MultiIndex DataFrame:')
_l_(113388)
df1 = _c_(113391, _a_(113390, _n_(113389, "df", lambda: df), "sort_index"))
_l_(113392)
_c_(113394, _n_(113393, "print", lambda: print), '\nSort on Index level=0 of the DataFrame:')
_l_(113395)
df2 = _c_(113398, _a_(113397, _n_(113396, "df", lambda: df), "sort_index"), level=0)
_l_(113399)
_c_(113402, _n_(113400, "print", lambda: print), _n_(113401, "df2", lambda: df2))
_l_(113403)
_c_(113405, _n_(113404, "print", lambda: print), '\nSort on Index level=1 of the DataFrame:')
_l_(113406)
df2 = _c_(113409, _a_(113408, _n_(113407, "df", lambda: df), "sort_index"), level=1)
_l_(113410)
_c_(113413, _n_(113411, "print", lambda: print), _n_(113412, "df2", lambda: df2))
_l_(113414)
_c_(113416, _n_(113415, "print", lambda: print), '\nPass a level name to sort the DataFrame:')
_l_(113417)
df3 = _c_(113420, _a_(113419, _n_(113418, "df", lambda: df), "sort_index"), level='city')
_l_(113421)
_c_(113424, _n_(113422, "print", lambda: print), _n_(113423, "df3", lambda: df3))
_l_(113425)