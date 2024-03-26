# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(107820)

except ImportError:
    pass
_c_(107822, _n_(107821, "print", lambda: print), 'Original Data Series:')
_l_(107823)
_c_(107826, _n_(107824, "print", lambda: print), _n_(107825, "s", lambda: s))
_l_(107827)
_c_(107829, _n_(107828, "print", lambda: print), '\nSubset of the above Data Series:')
_l_(107830)
n = 6
_l_(107831)
new_s = _n_(107832, "s", lambda: s)[_n_(107833, "s", lambda: s) < _n_(107834, "n", lambda: n)]
_l_(107835)
_c_(107838, _n_(107836, "print", lambda: print), _n_(107837, "new_s", lambda: new_s))
_l_(107839)