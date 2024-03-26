# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(109321)

except ImportError:
    pass

def randomly_interleave(nums1, nums2):
    _l_(109345)

    result = [_c_(109324, _a_(109323, _n_(109322, "x", lambda: x), "pop"), 0) for x in _c_(109341, _a_(109326, _n_(109325, "random", lambda: random), "sample"), [_n_(109327, "nums1", lambda: nums1)] * _c_(109330, _n_(109328, "len", lambda: len), _n_(109329, "nums1", lambda: nums1)) + [_n_(109331, "nums2", lambda: nums2)] * _c_(109334, _n_(109332, "len", lambda: len), _n_(109333, "nums2", lambda: nums2)), _c_(109337, _n_(109335, "len", lambda: len), _n_(109336, "nums1", lambda: nums1)) + _c_(109340, _n_(109338, "len", lambda: len), _n_(109339, "nums2", lambda: nums2)))]
    _l_(109342)
    aux = _n_(109343, "result", lambda: result)
    _l_(109344)
    return aux
nums1 = [1, 2, 7, 8, 3, 7]
_l_(109346)
_c_(109348, _n_(109347, "print", lambda: print), 'Original lists:')
_l_(109349)
_c_(109352, _n_(109350, "print", lambda: print), _n_(109351, "nums1", lambda: nums1))
_l_(109353)
_c_(109356, _n_(109354, "print", lambda: print), _n_(109355, "nums2", lambda: nums2))
_l_(109357)
_c_(109359, _n_(109358, "print", lambda: print), '\nInterleave two given list into another list randomly:')
_l_(109360)
_c_(109366, _n_(109361, "print", lambda: print), _c_(109365, _n_(109362, "randomly_interleave", lambda: randomly_interleave), _n_(109363, "nums1", lambda: nums1), _n_(109364, "nums2", lambda: nums2)))
_l_(109367)