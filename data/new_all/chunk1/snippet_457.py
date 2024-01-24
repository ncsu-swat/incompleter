# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54287042/why-this-case-pandas-dataframe-assign-raise-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from math import sqrt
    _l_(401054)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(401056)

except ImportError:
    pass
df = _c_(401059, _a_(401058, _n_(401057, "pd", lambda: pd), "DataFrame"), {'x':[1,2,3], 'y':[4,5,6]})
_l_(401060)

df = _c_(401069, _a_(401062, _n_(401061, "df", lambda: df), "assign"), d = lambda z: _c_(401068, _n_(401063, "sqrt", lambda: sqrt), _a_(401065, _n_(401064, "z", lambda: z), "x")**2 + _a_(401067, _n_(401066, "z", lambda: z), "y")**2))
_l_(401070)