# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def average_two_lists(nums1, nums2):
    _l_(72578)

    result = _c_(72570, _n_(72567, "sum", lambda: sum), _n_(72568, "nums1", lambda: nums1) + _n_(72569, "nums2", lambda: nums2)) / _c_(72574, _n_(72571, "len", lambda: len), _n_(72572, "nums1", lambda: nums1) + _n_(72573, "nums2", lambda: nums2))
    _l_(72575)
    aux = _n_(72576, "result", lambda: result)
    _l_(72577)
    return aux
nums2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]
_l_(72579)
_c_(72581, _n_(72580, "print", lambda: print), 'Original list:')
_l_(72582)
_c_(72585, _n_(72583, "print", lambda: print), _n_(72584, "nums1", lambda: nums1))
_l_(72586)
_c_(72589, _n_(72587, "print", lambda: print), _n_(72588, "nums2", lambda: nums2))
_l_(72590)
_c_(72592, _n_(72591, "print", lambda: print), '\nAverage of two lists:')
_l_(72593)
_c_(72599, _n_(72594, "print", lambda: print), _c_(72598, _n_(72595, "average_two_lists", lambda: average_two_lists), _n_(72596, "nums1", lambda: nums1), _n_(72597, "nums2", lambda: nums2)))
_l_(72600)