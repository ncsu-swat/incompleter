# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(37526)

except ImportError:
    pass
try:
    import numpy as np
    _l_(37528)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(37529)
sales_tuples = _c_(37534, _n_(37530, "list", lambda: list), _c_(37533, _n_(37531, "zip", lambda: zip), *_n_(37532, "sales_arrays", lambda: sales_arrays)))
_l_(37535)
sales_index = _c_(37540, _a_(37538, _a_(37537, _n_(37536, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(37539, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(37541)
_c_(37544, _n_(37542, "print", lambda: print), _n_(37543, "sales_tuples", lambda: sales_tuples))
_l_(37545)
_c_(37547, _n_(37546, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(37548)
df = _c_(37556, _a_(37550, _n_(37549, "pd", lambda: pd), "DataFrame"), _c_(37554, _a_(37553, _a_(37552, _n_(37551, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(37555, "sales_index", lambda: sales_index))
_l_(37557)
_c_(37560, _n_(37558, "print", lambda: print), _n_(37559, "df", lambda: df))
_l_(37561)
_c_(37563, _n_(37562, "print", lambda: print), '\nSort on MultiIndex DataFrame:')
_l_(37564)
df1 = _c_(37567, _a_(37566, _n_(37565, "df", lambda: df), "sort_index"))
_l_(37568)
_c_(37570, _n_(37569, "print", lambda: print), '\nSort on Index level=0 of the DataFrame:')
_l_(37571)
df2 = _c_(37574, _a_(37573, _n_(37572, "df", lambda: df), "sort_index"), level=0)
_l_(37575)
_c_(37578, _n_(37576, "print", lambda: print), _n_(37577, "df2", lambda: df2))
_l_(37579)
_c_(37581, _n_(37580, "print", lambda: print), '\nSort on Index level=1 of the DataFrame:')
_l_(37582)
_c_(37585, _n_(37583, "print", lambda: print), _n_(37584, "df2", lambda: df2))
_l_(37586)
_c_(37588, _n_(37587, "print", lambda: print), '\nPass a level name to sort the DataFrame:')
_l_(37589)
df3 = _c_(37592, _a_(37591, _n_(37590, "df", lambda: df), "sort_index"), level='city')
_l_(37593)
_c_(37596, _n_(37594, "print", lambda: print), _n_(37595, "df3", lambda: df3))
_l_(37597)