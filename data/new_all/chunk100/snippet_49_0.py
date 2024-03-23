# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def diff_consecutive_nums(nums):
    _l_(52017)

    result = [_n_(52008, "b", lambda: b) - _n_(52009, "a", lambda: a) for (a, b) in _c_(52013, _n_(52010, "zip", lambda: zip), _n_(52011, "nums", lambda: nums)[:-1], _n_(52012, "nums", lambda: nums)[1:])]
    _l_(52014)
    aux = _n_(52015, "result", lambda: result)
    _l_(52016)
    return aux
nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
_l_(52018)
_c_(52020, _n_(52019, "print", lambda: print), 'Original list:')
_l_(52021)
_c_(52024, _n_(52022, "print", lambda: print), _n_(52023, "nums1", lambda: nums1))
_l_(52025)
_c_(52027, _n_(52026, "print", lambda: print), 'Difference between consecutive numbers of the said list:')
_l_(52028)
_c_(52033, _n_(52029, "print", lambda: print), _c_(52032, _n_(52030, "diff_consecutive_nums", lambda: diff_consecutive_nums), _n_(52031, "nums1", lambda: nums1)))
_l_(52034)
_c_(52036, _n_(52035, "print", lambda: print), '\nOriginal list:')
_l_(52037)
_c_(52040, _n_(52038, "print", lambda: print), _n_(52039, "nums2", lambda: nums2))
_l_(52041)
_c_(52043, _n_(52042, "print", lambda: print), 'Difference between consecutive numbers of the said list:')
_l_(52044)
_c_(52049, _n_(52045, "print", lambda: print), _c_(52048, _n_(52046, "diff_consecutive_nums", lambda: diff_consecutive_nums), _n_(52047, "nums2", lambda: nums2)))
_l_(52050)