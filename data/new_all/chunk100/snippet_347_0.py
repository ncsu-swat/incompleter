# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(34659)

except ImportError:
    pass
s1 = _c_(34662, _a_(34661, _n_(34660, "pd", lambda: pd), "Series"), [0, 1, 2, 3], name='col1')
_l_(34663)
s2 = _c_(34666, _a_(34665, _n_(34664, "pd", lambda: pd), "Series"), [0, 1, 2, 3])
_l_(34667)
df = _c_(34673, _a_(34669, _n_(34668, "pd", lambda: pd), "concat"), [_n_(34670, "s1", lambda: s1), _n_(34671, "s2", lambda: s2), _n_(34672, "s3", lambda: s3)], axis=1, keys=['column1', 'column2', 'column3'])
_l_(34674)
_c_(34677, _n_(34675, "print", lambda: print), _n_(34676, "df", lambda: df))
_l_(34678)