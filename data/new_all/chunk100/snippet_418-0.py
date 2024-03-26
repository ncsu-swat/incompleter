# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def intersection_nested_lists(l1, l2):
    _l_(115449)

    result = [_c_(115444, _n_(115438, "list", lambda: list), _c_(115443, _n_(115439, "filter", lambda: filter), lambda x: _n_(115440, "x", lambda: x) in _n_(115441, "l1", lambda: l1), _n_(115442, "sublist", lambda: sublist))) for sublist in _n_(115445, "l2", lambda: l2)]
    _l_(115446)
    aux = _n_(115447, "result", lambda: result)
    _l_(115448)
    return aux
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
_l_(115450)
_c_(115452, _n_(115451, "print", lambda: print), '\nOriginal lists:')
_l_(115453)
_c_(115456, _n_(115454, "print", lambda: print), _n_(115455, "nums1", lambda: nums1))
_l_(115457)
_c_(115460, _n_(115458, "print", lambda: print), _n_(115459, "nums2", lambda: nums2))
_l_(115461)
_c_(115463, _n_(115462, "print", lambda: print), '\nIntersection of said nested lists:')
_l_(115464)
_c_(115470, _n_(115465, "print", lambda: print), _c_(115469, _n_(115466, "intersection_nested_lists", lambda: intersection_nested_lists), _n_(115467, "nums1", lambda: nums1), _n_(115468, "nums2", lambda: nums2)))
_l_(115471)