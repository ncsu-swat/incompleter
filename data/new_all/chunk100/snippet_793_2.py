# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import chain, zip_longest
    _l_(80239)

except ImportError:
    pass

def interleave_diff_len_lists(list1, list2, list3, list4):
    _l_(80251)

    aux = [_n_(80240, "x", lambda: x) for x in _c_(80248, _n_(80241, "chain", lambda: chain), *_c_(80247, _n_(80242, "zip_longest", lambda: zip_longest), _n_(80243, "list1", lambda: list1), _n_(80244, "list2", lambda: list2), _n_(80245, "list3", lambda: list3), _n_(80246, "list4", lambda: list4))) if _n_(80249, "x", lambda: x) is not None]
    _l_(80250)
    return aux
nums2 = [2, 5, 8]
_l_(80252)
nums3 = [0, 1]
_l_(80253)
nums4 = [3, 3, -1, 7]
_l_(80254)
_c_(80256, _n_(80255, "print", lambda: print), '\nOriginal lists:')
_l_(80257)
_c_(80260, _n_(80258, "print", lambda: print), _n_(80259, "nums1", lambda: nums1))
_l_(80261)
_c_(80264, _n_(80262, "print", lambda: print), _n_(80263, "nums2", lambda: nums2))
_l_(80265)
_c_(80268, _n_(80266, "print", lambda: print), _n_(80267, "nums3", lambda: nums3))
_l_(80269)
_c_(80272, _n_(80270, "print", lambda: print), _n_(80271, "nums4", lambda: nums4))
_l_(80273)
_c_(80275, _n_(80274, "print", lambda: print), '\nInterleave said lists of different lengths:')
_l_(80276)
_c_(80284, _n_(80277, "print", lambda: print), _c_(80283, _n_(80278, "interleave_diff_len_lists", lambda: interleave_diff_len_lists), _n_(80279, "nums1", lambda: nums1), _n_(80280, "nums2", lambda: nums2), _n_(80281, "nums3", lambda: nums3), _n_(80282, "nums4", lambda: nums4)))
_l_(80285)