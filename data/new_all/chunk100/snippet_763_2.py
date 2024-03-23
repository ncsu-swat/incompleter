# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(77521)

except ImportError:
    pass

def randomly_interleave(nums1, nums2):
    _l_(77551)

    result = _c_(77547, _n_(77522, "list", lambda: list), _c_(77546, _n_(77523, "map", lambda: map), _n_(77524, "next", lambda: next), _c_(77545, _a_(77526, _n_(77525, "random", lambda: random), "sample"), [_c_(77529, _n_(77527, "iter", lambda: iter), _n_(77528, "nums1", lambda: nums1))] * _c_(77532, _n_(77530, "len", lambda: len), _n_(77531, "nums1", lambda: nums1)) + [_c_(77535, _n_(77533, "iter", lambda: iter), _n_(77534, "nums2", lambda: nums2))] * _c_(77538, _n_(77536, "len", lambda: len), _n_(77537, "nums2", lambda: nums2)), _c_(77541, _n_(77539, "len", lambda: len), _n_(77540, "nums1", lambda: nums1)) + _c_(77544, _n_(77542, "len", lambda: len), _n_(77543, "nums2", lambda: nums2)))))
    _l_(77548)
    aux = _n_(77549, "result", lambda: result)
    _l_(77550)
    return aux
nums2 = [4, 3, 8, 9, 4, 3, 8, 9]
_l_(77552)
_c_(77554, _n_(77553, "print", lambda: print), 'Original lists:')
_l_(77555)
_c_(77558, _n_(77556, "print", lambda: print), _n_(77557, "nums1", lambda: nums1))
_l_(77559)
_c_(77562, _n_(77560, "print", lambda: print), _n_(77561, "nums2", lambda: nums2))
_l_(77563)
_c_(77565, _n_(77564, "print", lambda: print), '\nInterleave two given list into another list randomly:')
_l_(77566)
_c_(77572, _n_(77567, "print", lambda: print), _c_(77571, _n_(77568, "randomly_interleave", lambda: randomly_interleave), _n_(77569, "nums1", lambda: nums1), _n_(77570, "nums2", lambda: nums2)))
_l_(77573)