# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_same_pair(nums1, nums2, nums3):
    _l_(18537)

    result = _c_(18533, _n_(18524, "sum", lambda: sum), (_n_(18525, "m", lambda: m) == _n_(18526, "n", lambda: n) == _n_(18527, "o", lambda: o) for (m, n, o) in _c_(18532, _n_(18528, "zip", lambda: zip), _n_(18529, "nums1", lambda: nums1), _n_(18530, "nums2", lambda: nums2), _n_(18531, "nums3", lambda: nums3))))
    _l_(18534)
    aux = _n_(18535, "result", lambda: result)
    _l_(18536)
    return aux
nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(18538)
nums2 = [2, 2, 3, 1, 2, 6, 7, 9]
_l_(18539)
_c_(18541, _n_(18540, "print", lambda: print), 'Original lists:')
_l_(18542)
_c_(18545, _n_(18543, "print", lambda: print), _n_(18544, "nums1", lambda: nums1))
_l_(18546)
_c_(18549, _n_(18547, "print", lambda: print), _n_(18548, "nums2", lambda: nums2))
_l_(18550)
_c_(18553, _n_(18551, "print", lambda: print), _n_(18552, "nums3", lambda: nums3))
_l_(18554)
_c_(18556, _n_(18555, "print", lambda: print), '\nNumber of same pair of the said three given lists:')
_l_(18557)
_c_(18564, _n_(18558, "print", lambda: print), _c_(18563, _n_(18559, "count_same_pair", lambda: count_same_pair), _n_(18560, "nums1", lambda: nums1), _n_(18561, "nums2", lambda: nums2), _n_(18562, "nums3", lambda: nums3)))
_l_(18565)