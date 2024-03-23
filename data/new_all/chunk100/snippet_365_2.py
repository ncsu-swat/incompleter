# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(35872)

except ImportError:
    pass
try:
    import numpy as np
    _l_(35874)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(35875)
sales_tuples = _c_(35880, _n_(35876, "list", lambda: list), _c_(35879, _n_(35877, "zip", lambda: zip), *_n_(35878, "sales_arrays", lambda: sales_arrays)))
_l_(35881)
_c_(35883, _n_(35882, "print", lambda: print), 'Create a MultiIndex:')
_l_(35884)
_c_(35887, _n_(35885, "print", lambda: print), _n_(35886, "sales_tuples", lambda: sales_tuples))
_l_(35888)
_c_(35890, _n_(35889, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(35891)
df = _c_(35899, _a_(35893, _n_(35892, "pd", lambda: pd), "DataFrame"), _c_(35897, _a_(35896, _a_(35895, _n_(35894, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(35898, "sales_index", lambda: sales_index))
_l_(35900)
_c_(35903, _n_(35901, "print", lambda: print), _n_(35902, "df", lambda: df))
_l_(35904)