# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(103931)

except ImportError:
    pass
_c_(103933, _n_(103932, "print", lambda: print), '\nOriginal arrays:')
_l_(103934)
y = _n_(103935, "x", lambda: x) * 3
_l_(103936)
_c_(103938, _n_(103937, "print", lambda: print), 'Array-1')
_l_(103939)
_c_(103942, _n_(103940, "print", lambda: print), _n_(103941, "x", lambda: x))
_l_(103943)
_c_(103945, _n_(103944, "print", lambda: print), 'Array-2')
_l_(103946)
_c_(103949, _n_(103947, "print", lambda: print), _n_(103948, "y", lambda: y))
_l_(103950)
new_array = _c_(103955, _a_(103952, _n_(103951, "np", lambda: np), "hstack"), (_n_(103953, "x", lambda: x), _n_(103954, "y", lambda: y)))
_l_(103956)
_c_(103958, _n_(103957, "print", lambda: print), '\nStack arrays in sequence horizontally:')
_l_(103959)
_c_(103962, _n_(103960, "print", lambda: print), _n_(103961, "new_array", lambda: new_array))
_l_(103963)