# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(41776)

except ImportError:
    pass
s = _c_(41779, _a_(41778, _n_(41777, "pd", lambda: pd), "Series"), data=[1, 2, 3, 4, 5], index=['A', 'B', 'C', 'D', 'E'])
_l_(41780)
_c_(41782, _n_(41781, "print", lambda: print), 'Original Data Series:')
_l_(41783)
_c_(41786, _n_(41784, "print", lambda: print), _n_(41785, "s", lambda: s))
_l_(41787)
_c_(41789, _n_(41788, "print", lambda: print), 'Data Series after changing the order of index:')
_l_(41790)
_c_(41793, _n_(41791, "print", lambda: print), _n_(41792, "s", lambda: s))
_l_(41794)