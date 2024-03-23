# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(70432)

except ImportError:
    pass

def list_max_min_pair(nums):
    _l_(70454)

    result_max = _c_(70440, _n_(70433, "max", lambda: max), _c_(70437, _a_(70435, _n_(70434, "it", lambda: it), "combinations"), _n_(70436, "nums", lambda: nums), 2), key=lambda sub: _n_(70438, "sub", lambda: sub)[0] * _n_(70439, "sub", lambda: sub)[1])
    _l_(70441)
    result_min = _c_(70449, _n_(70442, "min", lambda: min), _c_(70446, _a_(70444, _n_(70443, "it", lambda: it), "combinations"), _n_(70445, "nums", lambda: nums), 2), key=lambda sub: _n_(70447, "sub", lambda: sub)[0] * _n_(70448, "sub", lambda: sub)[1])
    _l_(70450)
    aux = (_n_(70451, "result_max", lambda: result_max), _n_(70452, "result_min", lambda: result_min))
    _l_(70453)
    return aux
_c_(70456, _n_(70455, "print", lambda: print), 'The original list: ')
_l_(70457)
_c_(70460, _n_(70458, "print", lambda: print), _n_(70459, "nums", lambda: nums))
_l_(70461)
_c_(70463, _n_(70462, "print", lambda: print), '\nPairs of maximum and minimum product from the said list:')
_l_(70464)
_c_(70469, _n_(70465, "print", lambda: print), _c_(70468, _n_(70466, "list_max_min_pair", lambda: list_max_min_pair), _n_(70467, "nums", lambda: nums)))
_l_(70470)