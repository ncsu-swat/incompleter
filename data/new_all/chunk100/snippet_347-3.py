# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(111594)

except ImportError:
    pass
s1 = _c_(111597, _a_(111596, _n_(111595, "pd", lambda: pd), "Series"), [0, 1, 2, 3], name='col1')
_l_(111598)
s2 = _c_(111601, _a_(111600, _n_(111599, "pd", lambda: pd), "Series"), [0, 1, 2, 3])
_l_(111602)
df = _c_(111608, _a_(111604, _n_(111603, "pd", lambda: pd), "concat"), [_n_(111605, "s1", lambda: s1), _n_(111606, "s2", lambda: s2), _n_(111607, "s3", lambda: s3)], axis=1, keys=['column1', 'column2', 'column3'])
_l_(111609)
_c_(111612, _n_(111610, "print", lambda: print), _n_(111611, "df", lambda: df))
_l_(111613)