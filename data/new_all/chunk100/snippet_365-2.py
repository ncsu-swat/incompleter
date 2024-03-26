# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(112363)

except ImportError:
    pass
try:
    import numpy as np
    _l_(112365)

except ImportError:
    pass
sales_tuples = _c_(112370, _n_(112366, "list", lambda: list), _c_(112369, _n_(112367, "zip", lambda: zip), *_n_(112368, "sales_arrays", lambda: sales_arrays)))
_l_(112371)
_c_(112373, _n_(112372, "print", lambda: print), 'Create a MultiIndex:')
_l_(112374)
sales_index = _c_(112379, _a_(112377, _a_(112376, _n_(112375, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(112378, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(112380)
_c_(112383, _n_(112381, "print", lambda: print), _n_(112382, "sales_tuples", lambda: sales_tuples))
_l_(112384)
_c_(112386, _n_(112385, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(112387)
df = _c_(112395, _a_(112389, _n_(112388, "pd", lambda: pd), "DataFrame"), _c_(112393, _a_(112392, _a_(112391, _n_(112390, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(112394, "sales_index", lambda: sales_index))
_l_(112396)
_c_(112399, _n_(112397, "print", lambda: print), _n_(112398, "df", lambda: df))
_l_(112400)