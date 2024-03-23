# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(35906)

except ImportError:
    pass
try:
    import numpy as np
    _l_(35908)

except ImportError:
    pass
sales_tuples = _c_(35913, _n_(35909, "list", lambda: list), _c_(35912, _n_(35910, "zip", lambda: zip), *_n_(35911, "sales_arrays", lambda: sales_arrays)))
_l_(35914)
_c_(35916, _n_(35915, "print", lambda: print), 'Create a MultiIndex:')
_l_(35917)
sales_index = _c_(35922, _a_(35920, _a_(35919, _n_(35918, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(35921, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(35923)
_c_(35926, _n_(35924, "print", lambda: print), _n_(35925, "sales_tuples", lambda: sales_tuples))
_l_(35927)
_c_(35929, _n_(35928, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(35930)
df = _c_(35938, _a_(35932, _n_(35931, "pd", lambda: pd), "DataFrame"), _c_(35936, _a_(35935, _a_(35934, _n_(35933, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(35937, "sales_index", lambda: sales_index))
_l_(35939)
_c_(35942, _n_(35940, "print", lambda: print), _n_(35941, "df", lambda: df))
_l_(35943)