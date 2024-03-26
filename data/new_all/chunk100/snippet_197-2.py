# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(104587)

except ImportError:
    pass
y = _c_(104590, _a_(104589, _n_(104588, "np", lambda: np), "array"), [[1, 2], [1, 2]])
_l_(104591)
_c_(104593, _n_(104592, "print", lambda: print), 'Array1: ')
_l_(104594)
_c_(104597, _n_(104595, "print", lambda: print), _n_(104596, "x", lambda: x))
_l_(104598)
_c_(104600, _n_(104599, "print", lambda: print), 'Array1: ')
_l_(104601)
_c_(104604, _n_(104602, "print", lambda: print), _n_(104603, "y", lambda: y))
_l_(104605)
_c_(104607, _n_(104606, "print", lambda: print), 'Result- x^y:')
_l_(104608)
r1 = _c_(104613, _a_(104610, _n_(104609, "np", lambda: np), "power"), _n_(104611, "x", lambda: x), _n_(104612, "y", lambda: y))
_l_(104614)
_c_(104617, _n_(104615, "print", lambda: print), _n_(104616, "r1", lambda: r1))
_l_(104618)