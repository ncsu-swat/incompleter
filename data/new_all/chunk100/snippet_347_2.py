# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(34698)

except ImportError:
    pass
s2 = _c_(34701, _a_(34700, _n_(34699, "pd", lambda: pd), "Series"), [0, 1, 2, 3])
_l_(34702)
s3 = _c_(34705, _a_(34704, _n_(34703, "pd", lambda: pd), "Series"), [0, 1, 4, 5], name='col3')
_l_(34706)
df = _c_(34712, _a_(34708, _n_(34707, "pd", lambda: pd), "concat"), [_n_(34709, "s1", lambda: s1), _n_(34710, "s2", lambda: s2), _n_(34711, "s3", lambda: s3)], axis=1, keys=['column1', 'column2', 'column3'])
_l_(34713)
_c_(34716, _n_(34714, "print", lambda: print), _n_(34715, "df", lambda: df))
_l_(34717)