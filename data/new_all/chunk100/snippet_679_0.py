# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(70400)

except ImportError:
    pass

def list_max_min_pair(nums):
    _l_(70413)

    result_max = _c_(70408, _n_(70401, "max", lambda: max), _c_(70405, _a_(70403, _n_(70402, "it", lambda: it), "combinations"), _n_(70404, "nums", lambda: nums), 2), key=lambda sub: _n_(70406, "sub", lambda: sub)[0] * _n_(70407, "sub", lambda: sub)[1])
    _l_(70409)
    aux = (_n_(70410, "result_max", lambda: result_max), _n_(70411, "result_min", lambda: result_min))
    _l_(70412)
    return aux
nums = [2, 5, 8, 7, 4, 3, 1, 9, 10, 1]
_l_(70414)
_c_(70416, _n_(70415, "print", lambda: print), 'The original list: ')
_l_(70417)
_c_(70420, _n_(70418, "print", lambda: print), _n_(70419, "nums", lambda: nums))
_l_(70421)
_c_(70423, _n_(70422, "print", lambda: print), '\nPairs of maximum and minimum product from the said list:')
_l_(70424)
_c_(70429, _n_(70425, "print", lambda: print), _c_(70428, _n_(70426, "list_max_min_pair", lambda: list_max_min_pair), _n_(70427, "nums", lambda: nums)))
_l_(70430)