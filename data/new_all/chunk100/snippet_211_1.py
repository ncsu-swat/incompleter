# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def pair_consecutive_elements(lst):
    _l_(16684)

    result = [[_n_(16672, "lst", lambda: lst)[_n_(16673, "i", lambda: i)], _n_(16674, "lst", lambda: lst)[_n_(16675, "i", lambda: i) + 1]] for i in _c_(16680, _n_(16676, "range", lambda: range), _c_(16679, _n_(16677, "len", lambda: len), _n_(16678, "lst", lambda: lst)) - 1)]
    _l_(16681)
    aux = _n_(16682, "result", lambda: result)
    _l_(16683)
    return aux
nums = [1, 2, 3, 4, 5, 6]
_l_(16685)
_c_(16687, _n_(16686, "print", lambda: print), 'Original lists:')
_l_(16688)
_c_(16691, _n_(16689, "print", lambda: print), _n_(16690, "nums", lambda: nums))
_l_(16692)
_c_(16694, _n_(16693, "print", lambda: print), 'Pair up the consecutive elements of the said list:')
_l_(16695)
_c_(16700, _n_(16696, "print", lambda: print), _c_(16699, _n_(16697, "pair_consecutive_elements", lambda: pair_consecutive_elements), _n_(16698, "nums", lambda: nums)))
_l_(16701)
_c_(16703, _n_(16702, "print", lambda: print), '\nOriginal lists:')
_l_(16704)
_c_(16707, _n_(16705, "print", lambda: print), _n_(16706, "nums", lambda: nums))
_l_(16708)
_c_(16710, _n_(16709, "print", lambda: print), 'Pair up the consecutive elements of the said list:')
_l_(16711)
_c_(16716, _n_(16712, "print", lambda: print), _c_(16715, _n_(16713, "pair_consecutive_elements", lambda: pair_consecutive_elements), _n_(16714, "nums", lambda: nums)))
_l_(16717)