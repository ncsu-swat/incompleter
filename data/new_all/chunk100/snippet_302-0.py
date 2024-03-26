# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(109273)

except ImportError:
    pass

def randomly_interleave(nums1, nums2):
    _l_(109297)

    result = [_c_(109276, _a_(109275, _n_(109274, "x", lambda: x), "pop"), 0) for x in _c_(109293, _a_(109278, _n_(109277, "random", lambda: random), "sample"), [_n_(109279, "nums1", lambda: nums1)] * _c_(109282, _n_(109280, "len", lambda: len), _n_(109281, "nums1", lambda: nums1)) + [_n_(109283, "nums2", lambda: nums2)] * _c_(109286, _n_(109284, "len", lambda: len), _n_(109285, "nums2", lambda: nums2)), _c_(109289, _n_(109287, "len", lambda: len), _n_(109288, "nums1", lambda: nums1)) + _c_(109292, _n_(109290, "len", lambda: len), _n_(109291, "nums2", lambda: nums2)))]
    _l_(109294)
    aux = _n_(109295, "result", lambda: result)
    _l_(109296)
    return aux
nums2 = [4, 3, 8, 9, 4, 3, 8, 9]
_l_(109298)
_c_(109300, _n_(109299, "print", lambda: print), 'Original lists:')
_l_(109301)
_c_(109304, _n_(109302, "print", lambda: print), _n_(109303, "nums1", lambda: nums1))
_l_(109305)
_c_(109308, _n_(109306, "print", lambda: print), _n_(109307, "nums2", lambda: nums2))
_l_(109309)
_c_(109311, _n_(109310, "print", lambda: print), '\nInterleave two given list into another list randomly:')
_l_(109312)
_c_(109318, _n_(109313, "print", lambda: print), _c_(109317, _n_(109314, "randomly_interleave", lambda: randomly_interleave), _n_(109315, "nums1", lambda: nums1), _n_(109316, "nums2", lambda: nums2)))
_l_(109319)