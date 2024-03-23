# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from timeit import default_timer
    _l_(12261)

except ImportError:
    pass

def timer(n):
    _l_(12276)

    for row in _c_(12264, _n_(12262, "range", lambda: range), 0, _n_(12263, "n", lambda: n)):
        _l_(12269)

        _c_(12267, _n_(12265, "print", lambda: print), _n_(12266, "row", lambda: row))
        _l_(12268)
    _c_(12274, _n_(12270, "print", lambda: print), _c_(12272, _n_(12271, "default_timer", lambda: default_timer)) - _n_(12273, "start", lambda: start))
    _l_(12275)
_c_(12278, _n_(12277, "timer", lambda: timer), 5)
_l_(12279)
_c_(12281, _n_(12280, "timer", lambda: timer), 15)
_l_(12282)