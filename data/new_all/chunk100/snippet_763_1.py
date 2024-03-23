# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(77467)

except ImportError:
    pass

def randomly_interleave(nums1, nums2):
    _l_(77497)

    result = _c_(77493, _n_(77468, "list", lambda: list), _c_(77492, _n_(77469, "map", lambda: map), _n_(77470, "next", lambda: next), _c_(77491, _a_(77472, _n_(77471, "random", lambda: random), "sample"), [_c_(77475, _n_(77473, "iter", lambda: iter), _n_(77474, "nums1", lambda: nums1))] * _c_(77478, _n_(77476, "len", lambda: len), _n_(77477, "nums1", lambda: nums1)) + [_c_(77481, _n_(77479, "iter", lambda: iter), _n_(77480, "nums2", lambda: nums2))] * _c_(77484, _n_(77482, "len", lambda: len), _n_(77483, "nums2", lambda: nums2)), _c_(77487, _n_(77485, "len", lambda: len), _n_(77486, "nums1", lambda: nums1)) + _c_(77490, _n_(77488, "len", lambda: len), _n_(77489, "nums2", lambda: nums2)))))
    _l_(77494)
    aux = _n_(77495, "result", lambda: result)
    _l_(77496)
    return aux
nums1 = [1, 2, 7, 8, 3, 7]
_l_(77498)
_c_(77500, _n_(77499, "print", lambda: print), 'Original lists:')
_l_(77501)
_c_(77504, _n_(77502, "print", lambda: print), _n_(77503, "nums1", lambda: nums1))
_l_(77505)
_c_(77508, _n_(77506, "print", lambda: print), _n_(77507, "nums2", lambda: nums2))
_l_(77509)
_c_(77511, _n_(77510, "print", lambda: print), '\nInterleave two given list into another list randomly:')
_l_(77512)
_c_(77518, _n_(77513, "print", lambda: print), _c_(77517, _n_(77514, "randomly_interleave", lambda: randomly_interleave), _n_(77515, "nums1", lambda: nums1), _n_(77516, "nums2", lambda: nums2)))
_l_(77519)