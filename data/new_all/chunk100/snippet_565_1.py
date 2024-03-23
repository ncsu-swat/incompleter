# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def histogram(items):
    _l_(58457)

    for n in _n_(58444, "items", lambda: items):
        _l_(58456)

        times = _n_(58445, "n", lambda: n)
        _l_(58446)
        while _n_(58447, "times", lambda: times) > 0:
            _l_(58451)

            output += '*'
            _l_(58448)
            times = _n_(58449, "times", lambda: times) - 1
            _l_(58450)
        _c_(58454, _n_(58452, "print", lambda: print), _n_(58453, "output", lambda: output))
        _l_(58455)
_c_(58459, _n_(58458, "histogram", lambda: histogram), [2, 3, 6, 5])
_l_(58460)