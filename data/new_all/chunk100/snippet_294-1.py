# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(108896)

except ImportError:
    pass
n = _n_(108897, "x", lambda: x)[(_n_(108898, "x", lambda: x) % 3 == 0) | (_n_(108899, "x", lambda: x) % 5 == 0)]
_l_(108900)
_c_(108903, _n_(108901, "print", lambda: print), _n_(108902, "n", lambda: n)[:1000])
_l_(108904)
_c_(108909, _n_(108905, "print", lambda: print), _c_(108908, _a_(108907, _n_(108906, "n", lambda: n), "sum")))
_l_(108910)