# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(15257)

except ImportError:
    pass

def compare_lists(x, y):
    _l_(15265)

    aux = _c_(15260, _n_(15258, "Counter", lambda: Counter), _n_(15259, "x", lambda: x)) == _c_(15263, _n_(15261, "Counter", lambda: Counter), _n_(15262, "y", lambda: y))
    _l_(15264)
    return aux
n1 = [20, 10, 30, 10, 20, 30]
_l_(15266)
_c_(15272, _n_(15267, "print", lambda: print), _c_(15271, _n_(15268, "compare_lists", lambda: compare_lists), _n_(15269, "n1", lambda: n1), _n_(15270, "n2", lambda: n2)))
_l_(15273)