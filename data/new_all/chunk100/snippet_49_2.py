# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def diff_consecutive_nums(nums):
    _l_(52097)

    result = [_n_(52088, "b", lambda: b) - _n_(52089, "a", lambda: a) for (a, b) in _c_(52093, _n_(52090, "zip", lambda: zip), _n_(52091, "nums", lambda: nums)[:-1], _n_(52092, "nums", lambda: nums)[1:])]
    _l_(52094)
    aux = _n_(52095, "result", lambda: result)
    _l_(52096)
    return aux
_c_(52099, _n_(52098, "print", lambda: print), 'Original list:')
_l_(52100)
_c_(52103, _n_(52101, "print", lambda: print), _n_(52102, "nums1", lambda: nums1))
_l_(52104)
_c_(52106, _n_(52105, "print", lambda: print), 'Difference between consecutive numbers of the said list:')
_l_(52107)
_c_(52112, _n_(52108, "print", lambda: print), _c_(52111, _n_(52109, "diff_consecutive_nums", lambda: diff_consecutive_nums), _n_(52110, "nums1", lambda: nums1)))
_l_(52113)
nums2 = [4, 5, 8, 9, 6, 10]
_l_(52114)
_c_(52116, _n_(52115, "print", lambda: print), '\nOriginal list:')
_l_(52117)
_c_(52120, _n_(52118, "print", lambda: print), _n_(52119, "nums2", lambda: nums2))
_l_(52121)
_c_(52123, _n_(52122, "print", lambda: print), 'Difference between consecutive numbers of the said list:')
_l_(52124)
_c_(52129, _n_(52125, "print", lambda: print), _c_(52128, _n_(52126, "diff_consecutive_nums", lambda: diff_consecutive_nums), _n_(52127, "nums2", lambda: nums2)))
_l_(52130)