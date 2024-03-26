# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_same_pair(nums1, nums2, nums3):
    _l_(106069)

    result = _c_(106065, _n_(106056, "sum", lambda: sum), (_n_(106057, "m", lambda: m) == _n_(106058, "n", lambda: n) == _n_(106059, "o", lambda: o) for m, n, o in _c_(106064, _n_(106060, "zip", lambda: zip), _n_(106061, "nums1", lambda: nums1), _n_(106062, "nums2", lambda: nums2), _n_(106063, "nums3", lambda: nums3))))
    _l_(106066)
    aux = _n_(106067, "result", lambda: result)
    _l_(106068)
    return aux
nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(106070)
nums3 = [2, 1, 3, 1, 2, 6, 7, 9]
_l_(106071)
_c_(106073, _n_(106072, "print", lambda: print), 'Original lists:')
_l_(106074)
_c_(106077, _n_(106075, "print", lambda: print), _n_(106076, "nums1", lambda: nums1))
_l_(106078)
_c_(106081, _n_(106079, "print", lambda: print), _n_(106080, "nums2", lambda: nums2))
_l_(106082)
_c_(106085, _n_(106083, "print", lambda: print), _n_(106084, "nums3", lambda: nums3))
_l_(106086)
_c_(106088, _n_(106087, "print", lambda: print), '\nNumber of same pair of the said three given lists:')
_l_(106089)
_c_(106096, _n_(106090, "print", lambda: print), _c_(106095, _n_(106091, "count_same_pair", lambda: count_same_pair), _n_(106092, "nums1", lambda: nums1), _n_(106093, "nums2", lambda: nums2), _n_(106094, "nums3", lambda: nums3)))
_l_(106097)