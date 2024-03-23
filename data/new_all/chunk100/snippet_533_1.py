# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import combinations
    _l_(54114)

except ImportError:
    pass
try:
    from heapq import nlargest
    _l_(54116)

except ImportError:
    pass

def test(lst):
    _l_(54129)

    result = _c_(54125, _n_(54117, "nlargest", lambda: nlargest), 1, _c_(54120, _n_(54118, "combinations", lambda: combinations), _n_(54119, "lst", lambda: lst), 2), key=lambda sub: _c_(54124, _n_(54121, "abs", lambda: abs), _n_(54122, "sub", lambda: sub)[0] - _n_(54123, "sub", lambda: sub)[1]))
    _l_(54126)
    aux = _n_(54127, "result", lambda: result)
    _l_(54128)
    return aux
_c_(54131, _n_(54130, "print", lambda: print), '\nOriginal list:')
_l_(54132)
_c_(54135, _n_(54133, "print", lambda: print), _n_(54134, "marks", lambda: marks))
_l_(54136)
_c_(54138, _n_(54137, "print", lambda: print), '\nFind maximum difference pair of the said list:')
_l_(54139)
_c_(54144, _n_(54140, "print", lambda: print), _c_(54143, _n_(54141, "test", lambda: test), _n_(54142, "marks", lambda: marks)))
_l_(54145)