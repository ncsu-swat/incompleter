# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(41816)

except ImportError:
    pass
p = [[1, 0], [0, 1]]
_l_(41817)
q = [[1, 2], [3, 4]]
_l_(41818)
_c_(41820, _n_(41819, "print", lambda: print), 'original matrix:')
_l_(41821)
_c_(41824, _n_(41822, "print", lambda: print), _n_(41823, "p", lambda: p))
_l_(41825)
_c_(41828, _n_(41826, "print", lambda: print), _n_(41827, "q", lambda: q))
_l_(41829)
result2 = _c_(41834, _a_(41831, _n_(41830, "np", lambda: np), "cross"), _n_(41832, "q", lambda: q), _n_(41833, "p", lambda: p))
_l_(41835)
_c_(41837, _n_(41836, "print", lambda: print), 'cross product of the said two vectors(p, q):')
_l_(41838)
_c_(41841, _n_(41839, "print", lambda: print), _n_(41840, "result1", lambda: result1))
_l_(41842)
_c_(41844, _n_(41843, "print", lambda: print), 'cross product of the said two vectors(q, p):')
_l_(41845)
_c_(41848, _n_(41846, "print", lambda: print), _n_(41847, "result2", lambda: result2))
_l_(41849)