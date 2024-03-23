# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from functools import reduce
    _l_(10689)

except ImportError:
    pass

def mutiple_list(nums):
    _l_(10698)

    result = _c_(10694, _n_(10690, "reduce", lambda: reduce), lambda x, y: _n_(10691, "x", lambda: x) * _n_(10692, "y", lambda: y), _n_(10693, "nums", lambda: nums))
    _l_(10695)
    aux = _n_(10696, "result", lambda: result)
    _l_(10697)
    return aux
nums = [4, 3, 2, 2, -1, 18]
_l_(10699)
_c_(10701, _n_(10700, "print", lambda: print), 'Original list: ')
_l_(10702)
_c_(10705, _n_(10703, "print", lambda: print), _n_(10704, "nums", lambda: nums))
_l_(10706)
_c_(10711, _n_(10707, "print", lambda: print), 'Mmultiply all the numbers of the said list:', _c_(10710, _n_(10708, "mutiple_list", lambda: mutiple_list), _n_(10709, "nums", lambda: nums)))
_l_(10712)
_c_(10714, _n_(10713, "print", lambda: print), '\nOriginal list: ')
_l_(10715)
_c_(10718, _n_(10716, "print", lambda: print), _n_(10717, "nums", lambda: nums))
_l_(10719)
_c_(10724, _n_(10720, "print", lambda: print), 'Mmultiply all the numbers of the said list:', _c_(10723, _n_(10721, "mutiple_list", lambda: mutiple_list), _n_(10722, "nums", lambda: nums)))
_l_(10725)