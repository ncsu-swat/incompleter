# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(25737)

except ImportError:
    pass

def randomly_interleave(nums1, nums2):
    _l_(25761)

    result = [_c_(25740, _a_(25739, _n_(25738, "x", lambda: x), "pop"), 0) for x in _c_(25757, _a_(25742, _n_(25741, "random", lambda: random), "sample"), [_n_(25743, "nums1", lambda: nums1)] * _c_(25746, _n_(25744, "len", lambda: len), _n_(25745, "nums1", lambda: nums1)) + [_n_(25747, "nums2", lambda: nums2)] * _c_(25750, _n_(25748, "len", lambda: len), _n_(25749, "nums2", lambda: nums2)), _c_(25753, _n_(25751, "len", lambda: len), _n_(25752, "nums1", lambda: nums1)) + _c_(25756, _n_(25754, "len", lambda: len), _n_(25755, "nums2", lambda: nums2)))]
    _l_(25758)
    aux = _n_(25759, "result", lambda: result)
    _l_(25760)
    return aux
nums2 = [4, 3, 8, 9, 4, 3, 8, 9]
_l_(25762)
_c_(25764, _n_(25763, "print", lambda: print), 'Original lists:')
_l_(25765)
_c_(25768, _n_(25766, "print", lambda: print), _n_(25767, "nums1", lambda: nums1))
_l_(25769)
_c_(25772, _n_(25770, "print", lambda: print), _n_(25771, "nums2", lambda: nums2))
_l_(25773)
_c_(25775, _n_(25774, "print", lambda: print), '\nInterleave two given list into another list randomly:')
_l_(25776)
_c_(25782, _n_(25777, "print", lambda: print), _c_(25781, _n_(25778, "randomly_interleave", lambda: randomly_interleave), _n_(25779, "nums1", lambda: nums1), _n_(25780, "nums2", lambda: nums2)))
_l_(25783)