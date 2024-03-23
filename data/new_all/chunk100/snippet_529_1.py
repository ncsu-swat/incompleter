# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(53440)

except ImportError:
    pass
s = _c_(53443, _a_(53442, _n_(53441, "pd", lambda: pd), "Series"), ['100', '200', 'python', '300.12', '400'])
_l_(53444)
_c_(53446, _n_(53445, "print", lambda: print), 'Original Data Series:')
_l_(53447)
_c_(53450, _n_(53448, "print", lambda: print), _n_(53449, "s", lambda: s))
_l_(53451)
_c_(53454, _n_(53452, "print", lambda: print), _n_(53453, "new_s", lambda: new_s))
_l_(53455)