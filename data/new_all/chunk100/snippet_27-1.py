# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(107841)

except ImportError:
    pass
s = _c_(107844, _a_(107843, _n_(107842, "pd", lambda: pd), "Series"), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
_l_(107845)
_c_(107847, _n_(107846, "print", lambda: print), 'Original Data Series:')
_l_(107848)
_c_(107851, _n_(107849, "print", lambda: print), _n_(107850, "s", lambda: s))
_l_(107852)
_c_(107854, _n_(107853, "print", lambda: print), '\nSubset of the above Data Series:')
_l_(107855)
n = 6
_l_(107856)
_c_(107859, _n_(107857, "print", lambda: print), _n_(107858, "new_s", lambda: new_s))
_l_(107860)