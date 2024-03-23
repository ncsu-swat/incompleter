# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def histogram(items):
    _l_(58473)

    for n in _n_(58461, "items", lambda: items):
        _l_(58472)

        output = ''
        _l_(58462)
        times = _n_(58463, "n", lambda: n)
        _l_(58464)
        while _n_(58465, "times", lambda: times) > 0:
            _l_(58467)

            output += '*'
            _l_(58466)
        _c_(58470, _n_(58468, "print", lambda: print), _n_(58469, "output", lambda: output))
        _l_(58471)
_c_(58475, _n_(58474, "histogram", lambda: histogram), [2, 3, 6, 5])
_l_(58476)