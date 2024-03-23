# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def pair_consecutive_elements(lst):
    _l_(16638)

    result = [[_n_(16626, "lst", lambda: lst)[_n_(16627, "i", lambda: i)], _n_(16628, "lst", lambda: lst)[_n_(16629, "i", lambda: i) + 1]] for i in _c_(16634, _n_(16630, "range", lambda: range), _c_(16633, _n_(16631, "len", lambda: len), _n_(16632, "lst", lambda: lst)) - 1)]
    _l_(16635)
    aux = _n_(16636, "result", lambda: result)
    _l_(16637)
    return aux
_c_(16640, _n_(16639, "print", lambda: print), 'Original lists:')
_l_(16641)
_c_(16644, _n_(16642, "print", lambda: print), _n_(16643, "nums", lambda: nums))
_l_(16645)
_c_(16647, _n_(16646, "print", lambda: print), 'Pair up the consecutive elements of the said list:')
_l_(16648)
_c_(16653, _n_(16649, "print", lambda: print), _c_(16652, _n_(16650, "pair_consecutive_elements", lambda: pair_consecutive_elements), _n_(16651, "nums", lambda: nums)))
_l_(16654)
nums = [1, 2, 3, 4, 5]
_l_(16655)
_c_(16657, _n_(16656, "print", lambda: print), '\nOriginal lists:')
_l_(16658)
_c_(16661, _n_(16659, "print", lambda: print), _n_(16660, "nums", lambda: nums))
_l_(16662)
_c_(16664, _n_(16663, "print", lambda: print), 'Pair up the consecutive elements of the said list:')
_l_(16665)
_c_(16670, _n_(16666, "print", lambda: print), _c_(16669, _n_(16667, "pair_consecutive_elements", lambda: pair_consecutive_elements), _n_(16668, "nums", lambda: nums)))
_l_(16671)