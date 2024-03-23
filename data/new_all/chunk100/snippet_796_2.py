# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(80498)

except ImportError:
    pass
_c_(80500, _n_(80499, "print", lambda: print), '\nOriginal arrays:')
_l_(80501)
x = _c_(80506, _a_(80505, _c_(80504, _a_(80503, _n_(80502, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(80507)
_c_(80509, _n_(80508, "print", lambda: print), 'Array-1')
_l_(80510)
_c_(80513, _n_(80511, "print", lambda: print), _n_(80512, "x", lambda: x))
_l_(80514)
_c_(80516, _n_(80515, "print", lambda: print), 'Array-2')
_l_(80517)
_c_(80520, _n_(80518, "print", lambda: print), _n_(80519, "y", lambda: y))
_l_(80521)
new_array = _c_(80526, _a_(80523, _n_(80522, "np", lambda: np), "vstack"), (_n_(80524, "x", lambda: x), _n_(80525, "y", lambda: y)))
_l_(80527)
_c_(80529, _n_(80528, "print", lambda: print), '\nStack arrays in sequence vertically:')
_l_(80530)
_c_(80533, _n_(80531, "print", lambda: print), _n_(80532, "new_array", lambda: new_array))
_l_(80534)