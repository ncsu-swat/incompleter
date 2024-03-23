# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(88359)

except ImportError:
    pass
_c_(88361, _n_(88360, "print", lambda: print), 'First array:')
_l_(88362)
_c_(88365, _n_(88363, "print", lambda: print), _n_(88364, "x", lambda: x))
_l_(88366)
y = _c_(88370, _a_(88369, _a_(88368, _n_(88367, "np", lambda: np), "random"), "random"), (3, 2))
_l_(88371)
_c_(88373, _n_(88372, "print", lambda: print), 'Second array:')
_l_(88374)
_c_(88377, _n_(88375, "print", lambda: print), _n_(88376, "y", lambda: y))
_l_(88378)
z = _c_(88383, _a_(88380, _n_(88379, "np", lambda: np), "dot"), _n_(88381, "x", lambda: x), _n_(88382, "y", lambda: y))
_l_(88384)
_c_(88386, _n_(88385, "print", lambda: print), 'Dot product of two arrays:')
_l_(88387)
_c_(88390, _n_(88388, "print", lambda: print), _n_(88389, "z", lambda: z))
_l_(88391)