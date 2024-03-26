# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(113427)

except ImportError:
    pass
try:
    import numpy as np
    _l_(113429)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(113430)
sales_tuples = _c_(113435, _n_(113431, "list", lambda: list), _c_(113434, _n_(113432, "zip", lambda: zip), *_n_(113433, "sales_arrays", lambda: sales_arrays)))
_l_(113436)
sales_index = _c_(113441, _a_(113439, _a_(113438, _n_(113437, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(113440, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(113442)
_c_(113445, _n_(113443, "print", lambda: print), _n_(113444, "sales_tuples", lambda: sales_tuples))
_l_(113446)
_c_(113448, _n_(113447, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(113449)
_c_(113452, _n_(113450, "print", lambda: print), _n_(113451, "df", lambda: df))
_l_(113453)
_c_(113455, _n_(113454, "print", lambda: print), '\nSort on MultiIndex DataFrame:')
_l_(113456)
df1 = _c_(113459, _a_(113458, _n_(113457, "df", lambda: df), "sort_index"))
_l_(113460)
_c_(113462, _n_(113461, "print", lambda: print), '\nSort on Index level=0 of the DataFrame:')
_l_(113463)
df2 = _c_(113466, _a_(113465, _n_(113464, "df", lambda: df), "sort_index"), level=0)
_l_(113467)
_c_(113470, _n_(113468, "print", lambda: print), _n_(113469, "df2", lambda: df2))
_l_(113471)
_c_(113473, _n_(113472, "print", lambda: print), '\nSort on Index level=1 of the DataFrame:')
_l_(113474)
df2 = _c_(113477, _a_(113476, _n_(113475, "df", lambda: df), "sort_index"), level=1)
_l_(113478)
_c_(113481, _n_(113479, "print", lambda: print), _n_(113480, "df2", lambda: df2))
_l_(113482)
_c_(113484, _n_(113483, "print", lambda: print), '\nPass a level name to sort the DataFrame:')
_l_(113485)
df3 = _c_(113488, _a_(113487, _n_(113486, "df", lambda: df), "sort_index"), level='city')
_l_(113489)
_c_(113492, _n_(113490, "print", lambda: print), _n_(113491, "df3", lambda: df3))
_l_(113493)