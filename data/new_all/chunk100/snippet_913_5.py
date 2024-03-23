# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(92377)

except ImportError:
    pass
try:
    import numpy as np
    _l_(92379)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(92380)
sales_tuples = _c_(92385, _n_(92381, "list", lambda: list), _c_(92384, _n_(92382, "zip", lambda: zip), *_n_(92383, "sales_arrays", lambda: sales_arrays)))
_l_(92386)
sales_index = _c_(92391, _a_(92389, _a_(92388, _n_(92387, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(92390, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(92392)
_c_(92395, _n_(92393, "print", lambda: print), _n_(92394, "sales_tuples", lambda: sales_tuples))
_l_(92396)
_c_(92398, _n_(92397, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(92399)
df = _c_(92407, _a_(92401, _n_(92400, "pd", lambda: pd), "DataFrame"), _c_(92405, _a_(92404, _a_(92403, _n_(92402, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(92406, "sales_index", lambda: sales_index))
_l_(92408)
_c_(92411, _n_(92409, "print", lambda: print), _n_(92410, "df", lambda: df))
_l_(92412)
_c_(92414, _n_(92413, "print", lambda: print), '\nRename the columns name of the said dataframe')
_l_(92415)
_c_(92418, _n_(92416, "print", lambda: print), _n_(92417, "df1", lambda: df1))
_l_(92419)
_c_(92421, _n_(92420, "print", lambda: print), '\nRename specific labels of the main index of the DataFrame')
_l_(92422)
df2 = _c_(92425, _a_(92424, _n_(92423, "df1", lambda: df1), "rename"), index={'sale2': 'S2', 'city2': 'C2'})
_l_(92426)
_c_(92429, _n_(92427, "print", lambda: print), _n_(92428, "df2", lambda: df2))
_l_(92430)