# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(80430)

except ImportError:
    pass
_c_(80432, _n_(80431, "print", lambda: print), '\nOriginal arrays:')
_l_(80433)
y = _n_(80434, "x", lambda: x) * 3
_l_(80435)
_c_(80437, _n_(80436, "print", lambda: print), 'Array-1')
_l_(80438)
_c_(80441, _n_(80439, "print", lambda: print), _n_(80440, "x", lambda: x))
_l_(80442)
_c_(80444, _n_(80443, "print", lambda: print), 'Array-2')
_l_(80445)
_c_(80448, _n_(80446, "print", lambda: print), _n_(80447, "y", lambda: y))
_l_(80449)
new_array = _c_(80454, _a_(80451, _n_(80450, "np", lambda: np), "vstack"), (_n_(80452, "x", lambda: x), _n_(80453, "y", lambda: y)))
_l_(80455)
_c_(80457, _n_(80456, "print", lambda: print), '\nStack arrays in sequence vertically:')
_l_(80458)
_c_(80461, _n_(80459, "print", lambda: print), _n_(80460, "new_array", lambda: new_array))
_l_(80462)