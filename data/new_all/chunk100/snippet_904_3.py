# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def weighted_average(nums, weights):
    _l_(88747)

    aux = _c_(88742, _n_(88735, "sum", lambda: sum), (_n_(88736, "x", lambda: x) * _n_(88737, "y", lambda: y) for (x, y) in _c_(88741, _n_(88738, "zip", lambda: zip), _n_(88739, "nums", lambda: nums), _n_(88740, "weights", lambda: weights)))) / _c_(88745, _n_(88743, "sum", lambda: sum), _n_(88744, "weights", lambda: weights))
    _l_(88746)
    return aux
nums2 = [2, 5, 3]
_l_(88748)
_c_(88750, _n_(88749, "print", lambda: print), 'Original list elements:')
_l_(88751)
_c_(88754, _n_(88752, "print", lambda: print), _n_(88753, "nums1", lambda: nums1))
_l_(88755)
_c_(88758, _n_(88756, "print", lambda: print), _n_(88757, "nums2", lambda: nums2))
_l_(88759)
_c_(88761, _n_(88760, "print", lambda: print), '\nWeighted average of the said two list of numbers:')
_l_(88762)
_c_(88768, _n_(88763, "print", lambda: print), _c_(88767, _n_(88764, "weighted_average", lambda: weighted_average), _n_(88765, "nums1", lambda: nums1), _n_(88766, "nums2", lambda: nums2)))
_l_(88769)
nums1 = [82, 90, 76, 83]
_l_(88770)
nums2 = [0.2, 0.35, 0.45, 32]
_l_(88771)
_c_(88773, _n_(88772, "print", lambda: print), '\nOriginal list elements:')
_l_(88774)
_c_(88777, _n_(88775, "print", lambda: print), _n_(88776, "nums1", lambda: nums1))
_l_(88778)
_c_(88781, _n_(88779, "print", lambda: print), _n_(88780, "nums2", lambda: nums2))
_l_(88782)
_c_(88784, _n_(88783, "print", lambda: print), '\nWeighted average of the said two list of numbers:')
_l_(88785)
_c_(88791, _n_(88786, "print", lambda: print), _c_(88790, _n_(88787, "weighted_average", lambda: weighted_average), _n_(88788, "nums1", lambda: nums1), _n_(88789, "nums2", lambda: nums2)))
_l_(88792)