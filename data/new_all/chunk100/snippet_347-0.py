# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(111534)

except ImportError:
    pass
s2 = _c_(111537, _a_(111536, _n_(111535, "pd", lambda: pd), "Series"), [0, 1, 2, 3])
_l_(111538)
s3 = _c_(111541, _a_(111540, _n_(111539, "pd", lambda: pd), "Series"), [0, 1, 4, 5], name='col3')
_l_(111542)
df = _c_(111548, _a_(111544, _n_(111543, "pd", lambda: pd), "concat"), [_n_(111545, "s1", lambda: s1), _n_(111546, "s2", lambda: s2), _n_(111547, "s3", lambda: s3)], axis=1, keys=['column1', 'column2', 'column3'])
_l_(111549)
_c_(111552, _n_(111550, "print", lambda: print), _n_(111551, "df", lambda: df))
_l_(111553)