# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def dividing_two_lists(l1, l2):
    _l_(67480)

    result = [_n_(67471, "x", lambda: x) / _n_(67472, "y", lambda: y) for (x, y) in _c_(67476, _n_(67473, "zip", lambda: zip), _n_(67474, "l1", lambda: l1), _n_(67475, "l2", lambda: l2))]
    _l_(67477)
    aux = _n_(67478, "result", lambda: result)
    _l_(67479)
    return aux
nums1 = [7, 2, 3, 4, 9, 2, 3]
_l_(67481)
_c_(67483, _n_(67482, "print", lambda: print), 'Original list:')
_l_(67484)
_c_(67487, _n_(67485, "print", lambda: print), _n_(67486, "nums1", lambda: nums1))
_l_(67488)
_c_(67491, _n_(67489, "print", lambda: print), _n_(67490, "nums1", lambda: nums1))
_l_(67492)
_c_(67498, _n_(67493, "print", lambda: print), _c_(67497, _n_(67494, "dividing_two_lists", lambda: dividing_two_lists), _n_(67495, "nums1", lambda: nums1), _n_(67496, "nums2", lambda: nums2)))
_l_(67499)