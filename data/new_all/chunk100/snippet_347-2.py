# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(111573)

except ImportError:
    pass
s1 = _c_(111576, _a_(111575, _n_(111574, "pd", lambda: pd), "Series"), [0, 1, 2, 3], name='col1')
_l_(111577)
s3 = _c_(111580, _a_(111579, _n_(111578, "pd", lambda: pd), "Series"), [0, 1, 4, 5], name='col3')
_l_(111581)
df = _c_(111587, _a_(111583, _n_(111582, "pd", lambda: pd), "concat"), [_n_(111584, "s1", lambda: s1), _n_(111585, "s2", lambda: s2), _n_(111586, "s3", lambda: s3)], axis=1, keys=['column1', 'column2', 'column3'])
_l_(111588)
_c_(111591, _n_(111589, "print", lambda: print), _n_(111590, "df", lambda: df))
_l_(111592)