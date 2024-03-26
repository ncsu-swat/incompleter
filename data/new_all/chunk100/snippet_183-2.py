# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(103965)

except ImportError:
    pass
_c_(103967, _n_(103966, "print", lambda: print), '\nOriginal arrays:')
_l_(103968)
x = _c_(103973, _a_(103972, _c_(103971, _a_(103970, _n_(103969, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(103974)
_c_(103976, _n_(103975, "print", lambda: print), 'Array-1')
_l_(103977)
_c_(103980, _n_(103978, "print", lambda: print), _n_(103979, "x", lambda: x))
_l_(103981)
_c_(103983, _n_(103982, "print", lambda: print), 'Array-2')
_l_(103984)
_c_(103987, _n_(103985, "print", lambda: print), _n_(103986, "y", lambda: y))
_l_(103988)
new_array = _c_(103993, _a_(103990, _n_(103989, "np", lambda: np), "hstack"), (_n_(103991, "x", lambda: x), _n_(103992, "y", lambda: y)))
_l_(103994)
_c_(103996, _n_(103995, "print", lambda: print), '\nStack arrays in sequence horizontally:')
_l_(103997)
_c_(104000, _n_(103998, "print", lambda: print), _n_(103999, "new_array", lambda: new_array))
_l_(104001)