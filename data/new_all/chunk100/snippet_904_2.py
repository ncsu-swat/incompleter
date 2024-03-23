# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def weighted_average(nums, weights):
    _l_(88689)

    aux = _c_(88684, _n_(88677, "sum", lambda: sum), (_n_(88678, "x", lambda: x) * _n_(88679, "y", lambda: y) for (x, y) in _c_(88683, _n_(88680, "zip", lambda: zip), _n_(88681, "nums", lambda: nums), _n_(88682, "weights", lambda: weights)))) / _c_(88687, _n_(88685, "sum", lambda: sum), _n_(88686, "weights", lambda: weights))
    _l_(88688)
    return aux
nums1 = [10, 50, 40]
_l_(88690)
nums2 = [2, 5, 3]
_l_(88691)
_c_(88693, _n_(88692, "print", lambda: print), 'Original list elements:')
_l_(88694)
_c_(88697, _n_(88695, "print", lambda: print), _n_(88696, "nums1", lambda: nums1))
_l_(88698)
_c_(88701, _n_(88699, "print", lambda: print), _n_(88700, "nums2", lambda: nums2))
_l_(88702)
_c_(88704, _n_(88703, "print", lambda: print), '\nWeighted average of the said two list of numbers:')
_l_(88705)
_c_(88711, _n_(88706, "print", lambda: print), _c_(88710, _n_(88707, "weighted_average", lambda: weighted_average), _n_(88708, "nums1", lambda: nums1), _n_(88709, "nums2", lambda: nums2)))
_l_(88712)
nums2 = [0.2, 0.35, 0.45, 32]
_l_(88713)
_c_(88715, _n_(88714, "print", lambda: print), '\nOriginal list elements:')
_l_(88716)
_c_(88719, _n_(88717, "print", lambda: print), _n_(88718, "nums1", lambda: nums1))
_l_(88720)
_c_(88723, _n_(88721, "print", lambda: print), _n_(88722, "nums2", lambda: nums2))
_l_(88724)
_c_(88726, _n_(88725, "print", lambda: print), '\nWeighted average of the said two list of numbers:')
_l_(88727)
_c_(88733, _n_(88728, "print", lambda: print), _c_(88732, _n_(88729, "weighted_average", lambda: weighted_average), _n_(88730, "nums1", lambda: nums1), _n_(88731, "nums2", lambda: nums2)))
_l_(88734)