# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(104186)

except ImportError:
    pass

def compare_lists(x, y):
    _l_(104194)

    aux = _c_(104189, _n_(104187, "Counter", lambda: Counter), _n_(104188, "x", lambda: x)) == _c_(104192, _n_(104190, "Counter", lambda: Counter), _n_(104191, "y", lambda: y))
    _l_(104193)
    return aux
n2 = [30, 20, 10, 30, 20, 50]
_l_(104195)
_c_(104201, _n_(104196, "print", lambda: print), _c_(104200, _n_(104197, "compare_lists", lambda: compare_lists), _n_(104198, "n1", lambda: n1), _n_(104199, "n2", lambda: n2)))
_l_(104202)