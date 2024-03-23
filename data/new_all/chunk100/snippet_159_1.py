# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from functools import reduce
    _l_(10651)

except ImportError:
    pass

def mutiple_list(nums):
    _l_(10660)

    result = _c_(10656, _n_(10652, "reduce", lambda: reduce), lambda x, y: _n_(10653, "x", lambda: x) * _n_(10654, "y", lambda: y), _n_(10655, "nums", lambda: nums))
    _l_(10657)
    aux = _n_(10658, "result", lambda: result)
    _l_(10659)
    return aux
_c_(10662, _n_(10661, "print", lambda: print), 'Original list: ')
_l_(10663)
_c_(10666, _n_(10664, "print", lambda: print), _n_(10665, "nums", lambda: nums))
_l_(10667)
_c_(10672, _n_(10668, "print", lambda: print), 'Mmultiply all the numbers of the said list:', _c_(10671, _n_(10669, "mutiple_list", lambda: mutiple_list), _n_(10670, "nums", lambda: nums)))
_l_(10673)
nums = [2, 4, 8, 8, 3, 2, 9]
_l_(10674)
_c_(10676, _n_(10675, "print", lambda: print), '\nOriginal list: ')
_l_(10677)
_c_(10680, _n_(10678, "print", lambda: print), _n_(10679, "nums", lambda: nums))
_l_(10681)
_c_(10686, _n_(10682, "print", lambda: print), 'Mmultiply all the numbers of the said list:', _c_(10685, _n_(10683, "mutiple_list", lambda: mutiple_list), _n_(10684, "nums", lambda: nums)))
_l_(10687)