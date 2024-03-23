# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def histogram(items):
    _l_(58440)

    for n in _n_(58428, "items", lambda: items):
        _l_(58439)

        output = ''
        _l_(58429)
        while _n_(58430, "times", lambda: times) > 0:
            _l_(58434)

            output += '*'
            _l_(58431)
            times = _n_(58432, "times", lambda: times) - 1
            _l_(58433)
        _c_(58437, _n_(58435, "print", lambda: print), _n_(58436, "output", lambda: output))
        _l_(58438)
_c_(58442, _n_(58441, "histogram", lambda: histogram), [2, 3, 6, 5])
_l_(58443)