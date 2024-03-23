# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def intersection_nested_lists(l1, l2):
    _l_(41105)

    result = [_c_(41100, _n_(41094, "list", lambda: list), _c_(41099, _n_(41095, "filter", lambda: filter), lambda x: _n_(41096, "x", lambda: x) in _n_(41097, "l1", lambda: l1), _n_(41098, "sublist", lambda: sublist))) for sublist in _n_(41101, "l2", lambda: l2)]
    _l_(41102)
    aux = _n_(41103, "result", lambda: result)
    _l_(41104)
    return aux
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
_l_(41106)
_c_(41108, _n_(41107, "print", lambda: print), '\nOriginal lists:')
_l_(41109)
_c_(41112, _n_(41110, "print", lambda: print), _n_(41111, "nums1", lambda: nums1))
_l_(41113)
_c_(41116, _n_(41114, "print", lambda: print), _n_(41115, "nums2", lambda: nums2))
_l_(41117)
_c_(41119, _n_(41118, "print", lambda: print), '\nIntersection of said nested lists:')
_l_(41120)
_c_(41126, _n_(41121, "print", lambda: print), _c_(41125, _n_(41122, "intersection_nested_lists", lambda: intersection_nested_lists), _n_(41123, "nums1", lambda: nums1), _n_(41124, "nums2", lambda: nums2)))
_l_(41127)