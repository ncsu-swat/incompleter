# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(34719)

except ImportError:
    pass
s1 = _c_(34722, _a_(34721, _n_(34720, "pd", lambda: pd), "Series"), [0, 1, 2, 3], name='col1')
_l_(34723)
s3 = _c_(34726, _a_(34725, _n_(34724, "pd", lambda: pd), "Series"), [0, 1, 4, 5], name='col3')
_l_(34727)
df = _c_(34733, _a_(34729, _n_(34728, "pd", lambda: pd), "concat"), [_n_(34730, "s1", lambda: s1), _n_(34731, "s2", lambda: s2), _n_(34732, "s3", lambda: s3)], axis=1, keys=['column1', 'column2', 'column3'])
_l_(34734)
_c_(34737, _n_(34735, "print", lambda: print), _n_(34736, "df", lambda: df))
_l_(34738)