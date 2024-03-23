# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_last_n(nums, N):
    _l_(11824)

    result = _n_(11816, "nums", lambda: nums)[:_c_(11819, _n_(11817, "len", lambda: len), _n_(11818, "nums", lambda: nums)) - _n_(11820, "N", lambda: N)]
    _l_(11821)
    aux = _n_(11822, "result", lambda: result)
    _l_(11823)
    return aux
nums = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]
_l_(11825)
_c_(11827, _n_(11826, "print", lambda: print), 'Original lists:')
_l_(11828)
_c_(11831, _n_(11829, "print", lambda: print), _n_(11830, "nums", lambda: nums))
_l_(11832)
_c_(11835, _n_(11833, "print", lambda: print), '\nRemove the last', _n_(11834, "N", lambda: N), 'elements from the said list:')
_l_(11836)
_c_(11842, _n_(11837, "print", lambda: print), _c_(11841, _n_(11838, "remove_last_n", lambda: remove_last_n), _n_(11839, "nums", lambda: nums), _n_(11840, "N", lambda: N)))
_l_(11843)
N = 5
_l_(11844)
_c_(11847, _n_(11845, "print", lambda: print), '\nRemove the last', _n_(11846, "N", lambda: N), 'elements from the said list:')
_l_(11848)
_c_(11854, _n_(11849, "print", lambda: print), _c_(11853, _n_(11850, "remove_last_n", lambda: remove_last_n), _n_(11851, "nums", lambda: nums), _n_(11852, "N", lambda: N)))
_l_(11855)
N = 1
_l_(11856)
_c_(11859, _n_(11857, "print", lambda: print), '\nRemove the last', _n_(11858, "N", lambda: N), 'element from the said list:')
_l_(11860)
_c_(11866, _n_(11861, "print", lambda: print), _c_(11865, _n_(11862, "remove_last_n", lambda: remove_last_n), _n_(11863, "nums", lambda: nums), _n_(11864, "N", lambda: N)))
_l_(11867)