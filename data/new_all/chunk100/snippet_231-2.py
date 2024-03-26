# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_same_pair(nums1, nums2, nums3):
    _l_(106111)

    result = _c_(106107, _n_(106098, "sum", lambda: sum), (_n_(106099, "m", lambda: m) == _n_(106100, "n", lambda: n) == _n_(106101, "o", lambda: o) for m, n, o in _c_(106106, _n_(106102, "zip", lambda: zip), _n_(106103, "nums1", lambda: nums1), _n_(106104, "nums2", lambda: nums2), _n_(106105, "nums3", lambda: nums3))))
    _l_(106108)
    aux = _n_(106109, "result", lambda: result)
    _l_(106110)
    return aux
nums2 = [2, 2, 3, 1, 2, 6, 7, 9]
_l_(106112)
nums3 = [2, 1, 3, 1, 2, 6, 7, 9]
_l_(106113)
_c_(106115, _n_(106114, "print", lambda: print), 'Original lists:')
_l_(106116)
_c_(106119, _n_(106117, "print", lambda: print), _n_(106118, "nums1", lambda: nums1))
_l_(106120)
_c_(106123, _n_(106121, "print", lambda: print), _n_(106122, "nums2", lambda: nums2))
_l_(106124)
_c_(106127, _n_(106125, "print", lambda: print), _n_(106126, "nums3", lambda: nums3))
_l_(106128)
_c_(106130, _n_(106129, "print", lambda: print), '\nNumber of same pair of the said three given lists:')
_l_(106131)
_c_(106138, _n_(106132, "print", lambda: print), _c_(106137, _n_(106133, "count_same_pair", lambda: count_same_pair), _n_(106134, "nums1", lambda: nums1), _n_(106135, "nums2", lambda: nums2), _n_(106136, "nums3", lambda: nums3)))
_l_(106139)