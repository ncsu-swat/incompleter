# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(115523)

except ImportError:
    pass
p = _c_(115526, _a_(115525, _n_(115524, "np", lambda: np), "array"), [[0, 0, 0], [1, 2, 3], [4, 5, 6]])
_l_(115527)
_c_(115529, _n_(115528, "print", lambda: print), 'Original arrays:')
_l_(115530)
_c_(115532, _n_(115531, "print", lambda: print), 'Array-1')
_l_(115533)
_c_(115536, _n_(115534, "print", lambda: print), _n_(115535, "p", lambda: p))
_l_(115537)
_c_(115539, _n_(115538, "print", lambda: print), 'Array-2')
_l_(115540)
_c_(115543, _n_(115541, "print", lambda: print), _n_(115542, "q", lambda: q))
_l_(115544)
_c_(115546, _n_(115545, "print", lambda: print), '\nNew Array:')
_l_(115547)
new_array1 = _n_(115548, "p", lambda: p) + _n_(115549, "q", lambda: q)
_l_(115550)
_c_(115553, _n_(115551, "print", lambda: print), _n_(115552, "new_array1", lambda: new_array1))
_l_(115554)