# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(80464)

except ImportError:
    pass
_c_(80466, _n_(80465, "print", lambda: print), '\nOriginal arrays:')
_l_(80467)
x = _c_(80472, _a_(80471, _c_(80470, _a_(80469, _n_(80468, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(80473)
y = _n_(80474, "x", lambda: x) * 3
_l_(80475)
_c_(80477, _n_(80476, "print", lambda: print), 'Array-1')
_l_(80478)
_c_(80481, _n_(80479, "print", lambda: print), _n_(80480, "x", lambda: x))
_l_(80482)
_c_(80484, _n_(80483, "print", lambda: print), 'Array-2')
_l_(80485)
_c_(80488, _n_(80486, "print", lambda: print), _n_(80487, "y", lambda: y))
_l_(80489)
_c_(80491, _n_(80490, "print", lambda: print), '\nStack arrays in sequence vertically:')
_l_(80492)
_c_(80495, _n_(80493, "print", lambda: print), _n_(80494, "new_array", lambda: new_array))
_l_(80496)