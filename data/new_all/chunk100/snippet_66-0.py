# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(119612)

except ImportError:
    pass

def max_time(nums):
    _l_(119648)

    for i in _c_(119617, _n_(119613, "range", lambda: range), _c_(119616, _n_(119614, "len", lambda: len), _n_(119615, "nums", lambda: nums))):
        _l_(119621)

        _n_(119618, "nums", lambda: nums)[_n_(119619, "i", lambda: i)] *= -1
        _l_(119620)
    _c_(119624, _a_(119623, _n_(119622, "nums", lambda: nums), "sort"))
    _l_(119625)
    for hr1, hr2, m1, m2 in _c_(119629, _a_(119627, _n_(119626, "itertools", lambda: itertools), "permutations"), _n_(119628, "nums", lambda: nums)):
        _l_(119645)

        hrs = -(10 * _n_(119630, "hr1", lambda: hr1) + _n_(119631, "hr2", lambda: hr2))
        _l_(119632)
        mins = -(10 * _n_(119633, "m1", lambda: m1) + _n_(119634, "m2", lambda: m2))
        _l_(119635)
        if 60 > _n_(119636, "mins", lambda: mins) >= 0 and 24 > _n_(119637, "hrs", lambda: hrs) >= 0:
            _l_(119644)

            result = _c_(119641, _a_(119638, '{:02}:{:02}', "format"), _n_(119639, "hrs", lambda: hrs), _n_(119640, "mins", lambda: mins))
            _l_(119642)
            break
            _l_(119643)
    aux = _n_(119646, "result", lambda: result)
    _l_(119647)
    return aux
_c_(119651, _n_(119649, "print", lambda: print), 'Original array:', _n_(119650, "nums", lambda: nums))
_l_(119652)
_c_(119657, _n_(119653, "print", lambda: print), 'Latest time: ', _c_(119656, _n_(119654, "max_time", lambda: max_time), _n_(119655, "nums", lambda: nums)))
_l_(119658)
nums = [1, 2, 4, 5]
_l_(119659)
_c_(119662, _n_(119660, "print", lambda: print), '\nOriginal array:', _n_(119661, "nums", lambda: nums))
_l_(119663)
_c_(119668, _n_(119664, "print", lambda: print), 'Latest time: ', _c_(119667, _n_(119665, "max_time", lambda: max_time), _n_(119666, "nums", lambda: nums)))
_l_(119669)
nums = [2, 2, 4, 5]
_l_(119670)
_c_(119673, _n_(119671, "print", lambda: print), '\nOriginal array:', _n_(119672, "nums", lambda: nums))
_l_(119674)
_c_(119679, _n_(119675, "print", lambda: print), 'Latest time: ', _c_(119678, _n_(119676, "max_time", lambda: max_time), _n_(119677, "nums", lambda: nums)))
_l_(119680)
nums = [2, 2, 4, 3]
_l_(119681)
_c_(119684, _n_(119682, "print", lambda: print), '\nOriginal array:', _n_(119683, "nums", lambda: nums))
_l_(119685)
_c_(119690, _n_(119686, "print", lambda: print), 'Latest time: ', _c_(119689, _n_(119687, "max_time", lambda: max_time), _n_(119688, "nums", lambda: nums)))
_l_(119691)
nums = [0, 2, 4, 3]
_l_(119692)
_c_(119695, _n_(119693, "print", lambda: print), '\nOriginal array:', _n_(119694, "nums", lambda: nums))
_l_(119696)
_c_(119701, _n_(119697, "print", lambda: print), 'Latest time: ', _c_(119700, _n_(119698, "max_time", lambda: max_time), _n_(119699, "nums", lambda: nums)))
_l_(119702)