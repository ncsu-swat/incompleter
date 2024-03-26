# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(104204)

except ImportError:
    pass

def compare_lists(x, y):
    _l_(104212)

    aux = _c_(104207, _n_(104205, "Counter", lambda: Counter), _n_(104206, "x", lambda: x)) == _c_(104210, _n_(104208, "Counter", lambda: Counter), _n_(104209, "y", lambda: y))
    _l_(104211)
    return aux
n1 = [20, 10, 30, 10, 20, 30]
_l_(104213)
_c_(104219, _n_(104214, "print", lambda: print), _c_(104218, _n_(104215, "compare_lists", lambda: compare_lists), _n_(104216, "n1", lambda: n1), _n_(104217, "n2", lambda: n2)))
_l_(104220)