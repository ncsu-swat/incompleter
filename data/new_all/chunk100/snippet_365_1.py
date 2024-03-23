# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(35838)

except ImportError:
    pass
try:
    import numpy as np
    _l_(35840)

except ImportError:
    pass
sales_arrays = [['sale1', 'sale1', 'sale2', 'sale2', 'sale3', 'sale3', 'sale4', 'sale4'], ['city1', 'city2', 'city1', 'city2', 'city1', 'city2', 'city1', 'city2']]
_l_(35841)
_c_(35843, _n_(35842, "print", lambda: print), 'Create a MultiIndex:')
_l_(35844)
sales_index = _c_(35849, _a_(35847, _a_(35846, _n_(35845, "pd", lambda: pd), "MultiIndex"), "from_tuples"), _n_(35848, "sales_tuples", lambda: sales_tuples), names=['sale', 'city'])
_l_(35850)
_c_(35853, _n_(35851, "print", lambda: print), _n_(35852, "sales_tuples", lambda: sales_tuples))
_l_(35854)
_c_(35856, _n_(35855, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(35857)
df = _c_(35865, _a_(35859, _n_(35858, "pd", lambda: pd), "DataFrame"), _c_(35863, _a_(35862, _a_(35861, _n_(35860, "np", lambda: np), "random"), "randn"), 8, 5), index=_n_(35864, "sales_index", lambda: sales_index))
_l_(35866)
_c_(35869, _n_(35867, "print", lambda: print), _n_(35868, "df", lambda: df))
_l_(35870)