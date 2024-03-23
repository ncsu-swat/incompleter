# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(83160)

except ImportError:
    pass
try:
    import numpy as np
    _l_(83162)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(83163)
sales_tuples = _c_(83168, _n_(83164, "list", lambda: list), _c_(83167, _n_(83165, "zip", lambda: zip), *_n_(83166, "sales_arrays", lambda: sales_arrays)))
_l_(83169)
_c_(83171, _n_(83170, "print", lambda: print), 'Create a MultiIndex:')
_l_(83172)
sales_index = _c_(83177, _a_(83175, _a_(83174, _n_(83173, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(83176, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(83178)
_c_(83181, _n_(83179, "print", lambda: print), _n_(83180, "sales_tuples", lambda: sales_tuples))
_l_(83182)
_c_(83184, _n_(83183, "print", lambda: print), '\nConstruct a series using the said MultiIndex levels: ')
_l_(83185)
_c_(83188, _n_(83186, "print", lambda: print), _n_(83187, "s", lambda: s))
_l_(83189)