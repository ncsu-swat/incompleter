# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def weighted_average(nums, weights):
    _l_(88573)

    aux = _c_(88568, _n_(88561, "sum", lambda: sum), (_n_(88562, "x", lambda: x) * _n_(88563, "y", lambda: y) for (x, y) in _c_(88567, _n_(88564, "zip", lambda: zip), _n_(88565, "nums", lambda: nums), _n_(88566, "weights", lambda: weights)))) / _c_(88571, _n_(88569, "sum", lambda: sum), _n_(88570, "weights", lambda: weights))
    _l_(88572)
    return aux
nums1 = [10, 50, 40]
_l_(88574)
nums2 = [2, 5, 3]
_l_(88575)
_c_(88577, _n_(88576, "print", lambda: print), 'Original list elements:')
_l_(88578)
_c_(88581, _n_(88579, "print", lambda: print), _n_(88580, "nums1", lambda: nums1))
_l_(88582)
_c_(88585, _n_(88583, "print", lambda: print), _n_(88584, "nums2", lambda: nums2))
_l_(88586)
_c_(88588, _n_(88587, "print", lambda: print), '\nWeighted average of the said two list of numbers:')
_l_(88589)
_c_(88595, _n_(88590, "print", lambda: print), _c_(88594, _n_(88591, "weighted_average", lambda: weighted_average), _n_(88592, "nums1", lambda: nums1), _n_(88593, "nums2", lambda: nums2)))
_l_(88596)
nums1 = [82, 90, 76, 83]
_l_(88597)
_c_(88599, _n_(88598, "print", lambda: print), '\nOriginal list elements:')
_l_(88600)
_c_(88603, _n_(88601, "print", lambda: print), _n_(88602, "nums1", lambda: nums1))
_l_(88604)
_c_(88607, _n_(88605, "print", lambda: print), _n_(88606, "nums2", lambda: nums2))
_l_(88608)
_c_(88610, _n_(88609, "print", lambda: print), '\nWeighted average of the said two list of numbers:')
_l_(88611)
_c_(88617, _n_(88612, "print", lambda: print), _c_(88616, _n_(88613, "weighted_average", lambda: weighted_average), _n_(88614, "nums1", lambda: nums1), _n_(88615, "nums2", lambda: nums2)))
_l_(88618)