# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(14486)

except ImportError:
    pass
_c_(14488, _n_(14487, "print", lambda: print), '\nOriginal arrays:')
_l_(14489)
y = _n_(14490, "x", lambda: x) * 3
_l_(14491)
_c_(14493, _n_(14492, "print", lambda: print), 'Array-1')
_l_(14494)
_c_(14497, _n_(14495, "print", lambda: print), _n_(14496, "x", lambda: x))
_l_(14498)
_c_(14500, _n_(14499, "print", lambda: print), 'Array-2')
_l_(14501)
_c_(14504, _n_(14502, "print", lambda: print), _n_(14503, "y", lambda: y))
_l_(14505)
new_array = _c_(14510, _a_(14507, _n_(14506, "np", lambda: np), "hstack"), (_n_(14508, "x", lambda: x), _n_(14509, "y", lambda: y)))
_l_(14511)
_c_(14513, _n_(14512, "print", lambda: print), '\nStack arrays in sequence horizontally:')
_l_(14514)
_c_(14517, _n_(14515, "print", lambda: print), _n_(14516, "new_array", lambda: new_array))
_l_(14518)