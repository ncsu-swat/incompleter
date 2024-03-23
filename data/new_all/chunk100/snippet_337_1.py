# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def filter_data(students):
    _l_(33482)

    result = {_n_(33472, "k", lambda: k): _n_(33473, "s", lambda: s) for (k, s) in _c_(33476, _a_(33475, _n_(33474, "students", lambda: students), "items")) if _n_(33477, "s", lambda: s)[0] >= 6.0 and _n_(33478, "s", lambda: s)[1] >= 70}
    _l_(33479)
    aux = _n_(33480, "result", lambda: result)
    _l_(33481)
    return aux
_c_(33484, _n_(33483, "print", lambda: print), 'Original Dictionary:')
_l_(33485)
_c_(33488, _n_(33486, "print", lambda: print), _n_(33487, "students", lambda: students))
_l_(33489)
_c_(33491, _n_(33490, "print", lambda: print), '\nHeight > 6ft and Weight> 70kg:')
_l_(33492)
_c_(33497, _n_(33493, "print", lambda: print), _c_(33496, _n_(33494, "filter_data", lambda: filter_data), _n_(33495, "students", lambda: students)))
_l_(33498)