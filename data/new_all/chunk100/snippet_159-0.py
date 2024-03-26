# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from functools import reduce
    _l_(102748)

except ImportError:
    pass

def mutiple_list(nums):
    _l_(102757)

    result = _c_(102753, _n_(102749, "reduce", lambda: reduce), lambda x, y: _n_(102750, "x", lambda: x) * _n_(102751, "y", lambda: y), _n_(102752, "nums", lambda: nums))
    _l_(102754)
    aux = _n_(102755, "result", lambda: result)
    _l_(102756)
    return aux
_c_(102759, _n_(102758, "print", lambda: print), 'Original list: ')
_l_(102760)
_c_(102763, _n_(102761, "print", lambda: print), _n_(102762, "nums", lambda: nums))
_l_(102764)
_c_(102769, _n_(102765, "print", lambda: print), 'Mmultiply all the numbers of the said list:', _c_(102768, _n_(102766, "mutiple_list", lambda: mutiple_list), _n_(102767, "nums", lambda: nums)))
_l_(102770)
nums = [2, 4, 8, 8, 3, 2, 9]
_l_(102771)
_c_(102773, _n_(102772, "print", lambda: print), '\nOriginal list: ')
_l_(102774)
_c_(102777, _n_(102775, "print", lambda: print), _n_(102776, "nums", lambda: nums))
_l_(102778)
_c_(102783, _n_(102779, "print", lambda: print), 'Mmultiply all the numbers of the said list:', _c_(102782, _n_(102780, "mutiple_list", lambda: mutiple_list), _n_(102781, "nums", lambda: nums)))
_l_(102784)