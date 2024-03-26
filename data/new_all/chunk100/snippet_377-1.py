# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(113212)

except ImportError:
    pass
try:
    import numpy as np
    _l_(113214)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale3', 'sale3', 'sale2', 'sale2', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(113215)
sales_tuples = _c_(113220, _n_(113216, "list", lambda: list), _c_(113219, _n_(113217, "zip", lambda: zip), *_n_(113218, "sales_arrays", lambda: sales_arrays)))
_l_(113221)
sales_index = _c_(113226, _a_(113224, _a_(113223, _n_(113222, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(113225, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(113227)
_c_(113230, _n_(113228, "print", lambda: print), _n_(113229, "sales_tuples", lambda: sales_tuples))
_l_(113231)
_c_(113233, _n_(113232, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(113234)
df = _c_(113242, _a_(113236, _n_(113235, "pd", lambda: pd), "DataFrame"), _c_(113240, _a_(113239, _a_(113238, _n_(113237, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(113241, "sales_index", lambda: sales_index))
_l_(113243)
_c_(113246, _n_(113244, "print", lambda: print), _n_(113245, "df", lambda: df))
_l_(113247)
_c_(113249, _n_(113248, "print", lambda: print), '\nSort on MultiIndex DataFrame:')
_l_(113250)
df1 = _c_(113253, _a_(113252, _n_(113251, "df", lambda: df), "sort_index"))
_l_(113254)
_c_(113256, _n_(113255, "print", lambda: print), '\nSort on Index level=0 of the DataFrame:')
_l_(113257)
df2 = _c_(113260, _a_(113259, _n_(113258, "df", lambda: df), "sort_index"), level=0)
_l_(113261)
_c_(113264, _n_(113262, "print", lambda: print), _n_(113263, "df2", lambda: df2))
_l_(113265)
_c_(113267, _n_(113266, "print", lambda: print), '\nSort on Index level=1 of the DataFrame:')
_l_(113268)
df2 = _c_(113271, _a_(113270, _n_(113269, "df", lambda: df), "sort_index"), level=1)
_l_(113272)
_c_(113275, _n_(113273, "print", lambda: print), _n_(113274, "df2", lambda: df2))
_l_(113276)
_c_(113278, _n_(113277, "print", lambda: print), '\nPass a level name to sort the DataFrame:')
_l_(113279)
_c_(113282, _n_(113280, "print", lambda: print), _n_(113281, "df3", lambda: df3))
_l_(113283)