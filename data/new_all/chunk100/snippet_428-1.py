# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(115801)

except ImportError:
    pass
p = [[1, 0], [0, 1]]
_l_(115802)
_c_(115804, _n_(115803, "print", lambda: print), 'original matrix:')
_l_(115805)
_c_(115808, _n_(115806, "print", lambda: print), _n_(115807, "p", lambda: p))
_l_(115809)
_c_(115812, _n_(115810, "print", lambda: print), _n_(115811, "q", lambda: q))
_l_(115813)
result1 = _c_(115818, _a_(115815, _n_(115814, "np", lambda: np), "cross"), _n_(115816, "p", lambda: p), _n_(115817, "q", lambda: q))
_l_(115819)
result2 = _c_(115824, _a_(115821, _n_(115820, "np", lambda: np), "cross"), _n_(115822, "q", lambda: q), _n_(115823, "p", lambda: p))
_l_(115825)
_c_(115827, _n_(115826, "print", lambda: print), 'cross product of the said two vectors(p, q):')
_l_(115828)
_c_(115831, _n_(115829, "print", lambda: print), _n_(115830, "result1", lambda: result1))
_l_(115832)
_c_(115834, _n_(115833, "print", lambda: print), 'cross product of the said two vectors(q, p):')
_l_(115835)
_c_(115838, _n_(115836, "print", lambda: print), _n_(115837, "result2", lambda: result2))
_l_(115839)