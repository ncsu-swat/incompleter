# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_same_pair(nums1, nums2, nums3):
    _l_(18421)

    result = _c_(18417, _n_(18408, "sum", lambda: sum), (_n_(18409, "m", lambda: m) == _n_(18410, "n", lambda: n) == _n_(18411, "o", lambda: o) for (m, n, o) in _c_(18416, _n_(18412, "zip", lambda: zip), _n_(18413, "nums1", lambda: nums1), _n_(18414, "nums2", lambda: nums2), _n_(18415, "nums3", lambda: nums3))))
    _l_(18418)
    aux = _n_(18419, "result", lambda: result)
    _l_(18420)
    return aux
nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(18422)
nums3 = [2, 1, 3, 1, 2, 6, 7, 9]
_l_(18423)
_c_(18425, _n_(18424, "print", lambda: print), 'Original lists:')
_l_(18426)
_c_(18429, _n_(18427, "print", lambda: print), _n_(18428, "nums1", lambda: nums1))
_l_(18430)
_c_(18433, _n_(18431, "print", lambda: print), _n_(18432, "nums2", lambda: nums2))
_l_(18434)
_c_(18437, _n_(18435, "print", lambda: print), _n_(18436, "nums3", lambda: nums3))
_l_(18438)
_c_(18440, _n_(18439, "print", lambda: print), '\nNumber of same pair of the said three given lists:')
_l_(18441)
_c_(18448, _n_(18442, "print", lambda: print), _c_(18447, _n_(18443, "count_same_pair", lambda: count_same_pair), _n_(18444, "nums1", lambda: nums1), _n_(18445, "nums2", lambda: nums2), _n_(18446, "nums3", lambda: nums3)))
_l_(18449)