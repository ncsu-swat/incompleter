# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(104072)

except ImportError:
    pass
_c_(104074, _n_(104073, "print", lambda: print), 'Original array elements:')
_l_(104075)
_c_(104078, _n_(104076, "print", lambda: print), _n_(104077, "x", lambda: x))
_l_(104079)
_c_(104081, _n_(104080, "print", lambda: print), 'Print array values with precision 3:')
_l_(104082)
_c_(104085, _a_(104084, _n_(104083, "np", lambda: np), "set_printoptions"), suppress=True)
_l_(104086)
_c_(104089, _n_(104087, "print", lambda: print), _n_(104088, "x", lambda: x))
_l_(104090)