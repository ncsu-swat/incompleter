# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def dividing_two_lists(l1, l2):
    _l_(67509)

    result = [_n_(67500, "x", lambda: x) / _n_(67501, "y", lambda: y) for (x, y) in _c_(67505, _n_(67502, "zip", lambda: zip), _n_(67503, "l1", lambda: l1), _n_(67504, "l2", lambda: l2))]
    _l_(67506)
    aux = _n_(67507, "result", lambda: result)
    _l_(67508)
    return aux
nums2 = [9, 8, 2, 3, 3, 1, 2]
_l_(67510)
_c_(67512, _n_(67511, "print", lambda: print), 'Original list:')
_l_(67513)
_c_(67516, _n_(67514, "print", lambda: print), _n_(67515, "nums1", lambda: nums1))
_l_(67517)
_c_(67520, _n_(67518, "print", lambda: print), _n_(67519, "nums1", lambda: nums1))
_l_(67521)
_c_(67527, _n_(67522, "print", lambda: print), _c_(67526, _n_(67523, "dividing_two_lists", lambda: dividing_two_lists), _n_(67524, "nums1", lambda: nums1), _n_(67525, "nums2", lambda: nums2)))
_l_(67528)