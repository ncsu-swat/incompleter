# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sum_of_cubes(n):
    _l_(8265)

    n -= 1
    _l_(8255)
    while _n_(8256, "n", lambda: n) > 0:
        _l_(8262)

        total += _n_(8257, "n", lambda: n) * _n_(8258, "n", lambda: n) * _n_(8259, "n", lambda: n)
        _l_(8260)
        n -= 1
        _l_(8261)
    aux = _n_(8263, "total", lambda: total)
    _l_(8264)
    return aux
_c_(8269, _n_(8266, "print", lambda: print), 'Sum of cubes smaller than the specified number: ', _c_(8268, _n_(8267, "sum_of_cubes", lambda: sum_of_cubes), 3))
_l_(8270)