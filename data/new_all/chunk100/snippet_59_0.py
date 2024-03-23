# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(63134)

except ImportError:
    pass
_c_(63136, _n_(63135, "print", lambda: print), 'Create an array of zeros')
_l_(63137)
_c_(63139, _n_(63138, "print", lambda: print), 'Default type is float')
_l_(63140)
_c_(63143, _n_(63141, "print", lambda: print), _n_(63142, "x", lambda: x))
_l_(63144)
_c_(63146, _n_(63145, "print", lambda: print), 'Type changes to int')
_l_(63147)
x = _c_(63152, _a_(63149, _n_(63148, "np", lambda: np), "zeros"), (1, 2), dtype=_a_(63151, _n_(63150, "np", lambda: np), "int"))
_l_(63153)
_c_(63156, _n_(63154, "print", lambda: print), _n_(63155, "x", lambda: x))
_l_(63157)
_c_(63159, _n_(63158, "print", lambda: print), 'Create an array of ones')
_l_(63160)
y = _c_(63163, _a_(63162, _n_(63161, "np", lambda: np), "ones"), (1, 2))
_l_(63164)
_c_(63166, _n_(63165, "print", lambda: print), 'Default type is float')
_l_(63167)
_c_(63170, _n_(63168, "print", lambda: print), _n_(63169, "y", lambda: y))
_l_(63171)
_c_(63173, _n_(63172, "print", lambda: print), 'Type changes to int')
_l_(63174)
y = _c_(63179, _a_(63176, _n_(63175, "np", lambda: np), "ones"), (1, 2), dtype=_a_(63178, _n_(63177, "np", lambda: np), "int"))
_l_(63180)
_c_(63183, _n_(63181, "print", lambda: print), _n_(63182, "y", lambda: y))
_l_(63184)