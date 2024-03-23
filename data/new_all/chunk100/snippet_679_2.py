# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(70472)

except ImportError:
    pass

def list_max_min_pair(nums):
    _l_(70485)

    result_min = _c_(70480, _n_(70473, "min", lambda: min), _c_(70477, _a_(70475, _n_(70474, "it", lambda: it), "combinations"), _n_(70476, "nums", lambda: nums), 2), key=lambda sub: _n_(70478, "sub", lambda: sub)[0] * _n_(70479, "sub", lambda: sub)[1])
    _l_(70481)
    aux = (_n_(70482, "result_max", lambda: result_max), _n_(70483, "result_min", lambda: result_min))
    _l_(70484)
    return aux
nums = [2, 5, 8, 7, 4, 3, 1, 9, 10, 1]
_l_(70486)
_c_(70488, _n_(70487, "print", lambda: print), 'The original list: ')
_l_(70489)
_c_(70492, _n_(70490, "print", lambda: print), _n_(70491, "nums", lambda: nums))
_l_(70493)
_c_(70495, _n_(70494, "print", lambda: print), '\nPairs of maximum and minimum product from the said list:')
_l_(70496)
_c_(70501, _n_(70497, "print", lambda: print), _c_(70500, _n_(70498, "list_max_min_pair", lambda: list_max_min_pair), _n_(70499, "nums", lambda: nums)))
_l_(70502)