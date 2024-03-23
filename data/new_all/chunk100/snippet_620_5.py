# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(65183)

except ImportError:
    pass
a = _c_(65186, _a_(65185, _n_(65184, "np", lambda: np), "array"), [1, 2, 3])
_l_(65187)
_c_(65189, _n_(65188, "print", lambda: print), 'Original 1-d arrays:')
_l_(65190)
_c_(65193, _n_(65191, "print", lambda: print), _n_(65192, "a", lambda: a))
_l_(65194)
_c_(65197, _n_(65195, "print", lambda: print), _n_(65196, "b", lambda: b))
_l_(65198)
result = _c_(65203, _a_(65200, _n_(65199, "np", lambda: np), "einsum"), 'n,n', _n_(65201, "a", lambda: a), _n_(65202, "b", lambda: b))
_l_(65204)
_c_(65206, _n_(65205, "print", lambda: print), 'Einstein’s summation convention of the said arrays:')
_l_(65207)
_c_(65210, _n_(65208, "print", lambda: print), _n_(65209, "result", lambda: result))
_l_(65211)
x = _c_(65216, _a_(65215, _c_(65214, _a_(65213, _n_(65212, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(65217)
y = _c_(65222, _a_(65221, _c_(65220, _a_(65219, _n_(65218, "np", lambda: np), "arange"), 3, 12), "reshape"), 3, 3)
_l_(65223)
_c_(65225, _n_(65224, "print", lambda: print), 'Original Higher dimension:')
_l_(65226)
_c_(65229, _n_(65227, "print", lambda: print), _n_(65228, "x", lambda: x))
_l_(65230)
_c_(65233, _n_(65231, "print", lambda: print), _n_(65232, "y", lambda: y))
_l_(65234)
result = _c_(65239, _a_(65236, _n_(65235, "np", lambda: np), "einsum"), 'mk,kn', _n_(65237, "x", lambda: x), _n_(65238, "y", lambda: y))
_l_(65240)
_c_(65242, _n_(65241, "print", lambda: print), 'Einstein’s summation convention of the said arrays:')
_l_(65243)
_c_(65246, _n_(65244, "print", lambda: print), _n_(65245, "result", lambda: result))
_l_(65247)