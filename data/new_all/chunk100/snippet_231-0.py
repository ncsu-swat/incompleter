# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_same_pair(nums1, nums2, nums3):
    _l_(106027)

    result = _c_(106023, _n_(106014, "sum", lambda: sum), (_n_(106015, "m", lambda: m) == _n_(106016, "n", lambda: n) == _n_(106017, "o", lambda: o) for m, n, o in _c_(106022, _n_(106018, "zip", lambda: zip), _n_(106019, "nums1", lambda: nums1), _n_(106020, "nums2", lambda: nums2), _n_(106021, "nums3", lambda: nums3))))
    _l_(106024)
    aux = _n_(106025, "result", lambda: result)
    _l_(106026)
    return aux
nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(106028)
nums2 = [2, 2, 3, 1, 2, 6, 7, 9]
_l_(106029)
_c_(106031, _n_(106030, "print", lambda: print), 'Original lists:')
_l_(106032)
_c_(106035, _n_(106033, "print", lambda: print), _n_(106034, "nums1", lambda: nums1))
_l_(106036)
_c_(106039, _n_(106037, "print", lambda: print), _n_(106038, "nums2", lambda: nums2))
_l_(106040)
_c_(106043, _n_(106041, "print", lambda: print), _n_(106042, "nums3", lambda: nums3))
_l_(106044)
_c_(106046, _n_(106045, "print", lambda: print), '\nNumber of same pair of the said three given lists:')
_l_(106047)
_c_(106054, _n_(106048, "print", lambda: print), _c_(106053, _n_(106049, "count_same_pair", lambda: count_same_pair), _n_(106050, "nums1", lambda: nums1), _n_(106051, "nums2", lambda: nums2), _n_(106052, "nums3", lambda: nums3)))
_l_(106055)