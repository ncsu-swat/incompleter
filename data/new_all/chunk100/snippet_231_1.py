# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_same_pair(nums1, nums2, nums3):
    _l_(18463)

    result = _c_(18459, _n_(18450, "sum", lambda: sum), (_n_(18451, "m", lambda: m) == _n_(18452, "n", lambda: n) == _n_(18453, "o", lambda: o) for (m, n, o) in _c_(18458, _n_(18454, "zip", lambda: zip), _n_(18455, "nums1", lambda: nums1), _n_(18456, "nums2", lambda: nums2), _n_(18457, "nums3", lambda: nums3))))
    _l_(18460)
    aux = _n_(18461, "result", lambda: result)
    _l_(18462)
    return aux
nums2 = [2, 2, 3, 1, 2, 6, 7, 9]
_l_(18464)
nums3 = [2, 1, 3, 1, 2, 6, 7, 9]
_l_(18465)
_c_(18467, _n_(18466, "print", lambda: print), 'Original lists:')
_l_(18468)
_c_(18471, _n_(18469, "print", lambda: print), _n_(18470, "nums1", lambda: nums1))
_l_(18472)
_c_(18475, _n_(18473, "print", lambda: print), _n_(18474, "nums2", lambda: nums2))
_l_(18476)
_c_(18479, _n_(18477, "print", lambda: print), _n_(18478, "nums3", lambda: nums3))
_l_(18480)
_c_(18482, _n_(18481, "print", lambda: print), '\nNumber of same pair of the said three given lists:')
_l_(18483)
_c_(18490, _n_(18484, "print", lambda: print), _c_(18489, _n_(18485, "count_same_pair", lambda: count_same_pair), _n_(18486, "nums1", lambda: nums1), _n_(18487, "nums2", lambda: nums2), _n_(18488, "nums3", lambda: nums3)))
_l_(18491)