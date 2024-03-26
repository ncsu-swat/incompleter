# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(115746)

except ImportError:
    pass
_c_(115748, _n_(115747, "print", lambda: print), 'Original Data Series:')
_l_(115749)
_c_(115752, _n_(115750, "print", lambda: print), _n_(115751, "s", lambda: s))
_l_(115753)
s = _c_(115756, _a_(115755, _n_(115754, "s", lambda: s), "reindex"), index=['B', 'A', 'C', 'D', 'E'])
_l_(115757)
_c_(115759, _n_(115758, "print", lambda: print), 'Data Series after changing the order of index:')
_l_(115760)
_c_(115763, _n_(115761, "print", lambda: print), _n_(115762, "s", lambda: s))
_l_(115764)