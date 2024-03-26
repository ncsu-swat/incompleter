# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def intersection_nested_lists(l1, l2):
    _l_(115483)

    result = [_c_(115478, _n_(115472, "list", lambda: list), _c_(115477, _n_(115473, "filter", lambda: filter), lambda x: _n_(115474, "x", lambda: x) in _n_(115475, "l1", lambda: l1), _n_(115476, "sublist", lambda: sublist))) for sublist in _n_(115479, "l2", lambda: l2)]
    _l_(115480)
    aux = _n_(115481, "result", lambda: result)
    _l_(115482)
    return aux
nums2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
_l_(115484)
_c_(115486, _n_(115485, "print", lambda: print), '\nOriginal lists:')
_l_(115487)
_c_(115490, _n_(115488, "print", lambda: print), _n_(115489, "nums1", lambda: nums1))
_l_(115491)
_c_(115494, _n_(115492, "print", lambda: print), _n_(115493, "nums2", lambda: nums2))
_l_(115495)
_c_(115497, _n_(115496, "print", lambda: print), '\nIntersection of said nested lists:')
_l_(115498)
_c_(115504, _n_(115499, "print", lambda: print), _c_(115503, _n_(115500, "intersection_nested_lists", lambda: intersection_nested_lists), _n_(115501, "nums1", lambda: nums1), _n_(115502, "nums2", lambda: nums2)))
_l_(115505)