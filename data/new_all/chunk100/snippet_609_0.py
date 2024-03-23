# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(64459)

except ImportError:
    pass
x = _c_(64462, _a_(64461, _n_(64460, "np", lambda: np), "arange"), 4)
_l_(64463)
_c_(64465, _n_(64464, "print", lambda: print), 'One dimensional array:')
_l_(64466)
_c_(64469, _n_(64467, "print", lambda: print), _n_(64468, "x", lambda: x))
_l_(64470)
_c_(64472, _n_(64471, "print", lambda: print), 'Two dimensional array:')
_l_(64473)
_c_(64476, _n_(64474, "print", lambda: print), _n_(64475, "y", lambda: y))
_l_(64477)
for (a, b) in _c_(64482, _a_(64479, _n_(64478, "np", lambda: np), "nditer"), [_n_(64480, "x", lambda: x), _n_(64481, "y", lambda: y)]):
    _l_(64488)

    _c_(64486, _n_(64483, "print", lambda: print), '%d:%d' % (_n_(64484, "a", lambda: a), _n_(64485, "b", lambda: b)))
    _l_(64487)