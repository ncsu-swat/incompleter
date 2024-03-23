# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def intersection_nested_lists(l1, l2):
    _l_(41139)

    result = [_c_(41134, _n_(41128, "list", lambda: list), _c_(41133, _n_(41129, "filter", lambda: filter), lambda x: _n_(41130, "x", lambda: x) in _n_(41131, "l1", lambda: l1), _n_(41132, "sublist", lambda: sublist))) for sublist in _n_(41135, "l2", lambda: l2)]
    _l_(41136)
    aux = _n_(41137, "result", lambda: result)
    _l_(41138)
    return aux
nums2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
_l_(41140)
_c_(41142, _n_(41141, "print", lambda: print), '\nOriginal lists:')
_l_(41143)
_c_(41146, _n_(41144, "print", lambda: print), _n_(41145, "nums1", lambda: nums1))
_l_(41147)
_c_(41150, _n_(41148, "print", lambda: print), _n_(41149, "nums2", lambda: nums2))
_l_(41151)
_c_(41153, _n_(41152, "print", lambda: print), '\nIntersection of said nested lists:')
_l_(41154)
_c_(41160, _n_(41155, "print", lambda: print), _c_(41159, _n_(41156, "intersection_nested_lists", lambda: intersection_nested_lists), _n_(41157, "nums1", lambda: nums1), _n_(41158, "nums2", lambda: nums2)))
_l_(41161)