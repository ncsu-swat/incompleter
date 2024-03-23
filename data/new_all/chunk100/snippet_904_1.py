# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def weighted_average(nums, weights):
    _l_(88631)

    aux = _c_(88626, _n_(88619, "sum", lambda: sum), (_n_(88620, "x", lambda: x) * _n_(88621, "y", lambda: y) for (x, y) in _c_(88625, _n_(88622, "zip", lambda: zip), _n_(88623, "nums", lambda: nums), _n_(88624, "weights", lambda: weights)))) / _c_(88629, _n_(88627, "sum", lambda: sum), _n_(88628, "weights", lambda: weights))
    _l_(88630)
    return aux
nums1 = [10, 50, 40]
_l_(88632)
_c_(88634, _n_(88633, "print", lambda: print), 'Original list elements:')
_l_(88635)
_c_(88638, _n_(88636, "print", lambda: print), _n_(88637, "nums1", lambda: nums1))
_l_(88639)
_c_(88642, _n_(88640, "print", lambda: print), _n_(88641, "nums2", lambda: nums2))
_l_(88643)
_c_(88645, _n_(88644, "print", lambda: print), '\nWeighted average of the said two list of numbers:')
_l_(88646)
_c_(88652, _n_(88647, "print", lambda: print), _c_(88651, _n_(88648, "weighted_average", lambda: weighted_average), _n_(88649, "nums1", lambda: nums1), _n_(88650, "nums2", lambda: nums2)))
_l_(88653)
nums1 = [82, 90, 76, 83]
_l_(88654)
nums2 = [0.2, 0.35, 0.45, 32]
_l_(88655)
_c_(88657, _n_(88656, "print", lambda: print), '\nOriginal list elements:')
_l_(88658)
_c_(88661, _n_(88659, "print", lambda: print), _n_(88660, "nums1", lambda: nums1))
_l_(88662)
_c_(88665, _n_(88663, "print", lambda: print), _n_(88664, "nums2", lambda: nums2))
_l_(88666)
_c_(88668, _n_(88667, "print", lambda: print), '\nWeighted average of the said two list of numbers:')
_l_(88669)
_c_(88675, _n_(88670, "print", lambda: print), _c_(88674, _n_(88671, "weighted_average", lambda: weighted_average), _n_(88672, "nums1", lambda: nums1), _n_(88673, "nums2", lambda: nums2)))
_l_(88676)