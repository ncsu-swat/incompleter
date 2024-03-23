# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(15275)

except ImportError:
    pass

def compare_lists(x, y):
    _l_(15283)

    aux = _c_(15278, _n_(15276, "Counter", lambda: Counter), _n_(15277, "x", lambda: x)) == _c_(15281, _n_(15279, "Counter", lambda: Counter), _n_(15280, "y", lambda: y))
    _l_(15282)
    return aux
n2 = [30, 20, 10, 30, 20, 50]
_l_(15284)
_c_(15290, _n_(15285, "print", lambda: print), _c_(15289, _n_(15286, "compare_lists", lambda: compare_lists), _n_(15287, "n1", lambda: n1), _n_(15288, "n2", lambda: n2)))
_l_(15291)