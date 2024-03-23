# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def average_two_lists(nums1, nums2):
    _l_(72544)

    result = _c_(72536, _n_(72533, "sum", lambda: sum), _n_(72534, "nums1", lambda: nums1) + _n_(72535, "nums2", lambda: nums2)) / _c_(72540, _n_(72537, "len", lambda: len), _n_(72538, "nums1", lambda: nums1) + _n_(72539, "nums2", lambda: nums2))
    _l_(72541)
    aux = _n_(72542, "result", lambda: result)
    _l_(72543)
    return aux
nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
_l_(72545)
_c_(72547, _n_(72546, "print", lambda: print), 'Original list:')
_l_(72548)
_c_(72551, _n_(72549, "print", lambda: print), _n_(72550, "nums1", lambda: nums1))
_l_(72552)
_c_(72555, _n_(72553, "print", lambda: print), _n_(72554, "nums2", lambda: nums2))
_l_(72556)
_c_(72558, _n_(72557, "print", lambda: print), '\nAverage of two lists:')
_l_(72559)
_c_(72565, _n_(72560, "print", lambda: print), _c_(72564, _n_(72561, "average_two_lists", lambda: average_two_lists), _n_(72562, "nums1", lambda: nums1), _n_(72563, "nums2", lambda: nums2)))
_l_(72566)