# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(118471)

except ImportError:
    pass
try:
    import os
    _l_(118473)

except ImportError:
    pass
x = _c_(118476, _a_(118475, _n_(118474, "np", lambda: np), "arange"), 10)
_l_(118477)
_c_(118479, _n_(118478, "print", lambda: print), 'Original arrays:')
_l_(118480)
_c_(118483, _n_(118481, "print", lambda: print), _n_(118482, "x", lambda: x))
_l_(118484)
_c_(118487, _n_(118485, "print", lambda: print), _n_(118486, "y", lambda: y))
_l_(118488)
_c_(118493, _a_(118490, _n_(118489, "np", lambda: np), "savez"), 'temp_arra.npz', x=_n_(118491, "x", lambda: x), y=_n_(118492, "y", lambda: y))
_l_(118494)
_c_(118496, _n_(118495, "print", lambda: print), "Load arrays from the 'temp_arra.npz' file:")
_l_(118497)
with _c_(118500, _a_(118499, _n_(118498, "np", lambda: np), "load"), 'temp_arra.npz') as data:
    _l_(118513)

    x2 = _n_(118501, "data", lambda: data)['x']
    _l_(118502)
    y2 = _n_(118503, "data", lambda: data)['y']
    _l_(118504)
    _c_(118507, _n_(118505, "print", lambda: print), _n_(118506, "x2", lambda: x2))
    _l_(118508)
    _c_(118511, _n_(118509, "print", lambda: print), _n_(118510, "y2", lambda: y2))
    _l_(118512)