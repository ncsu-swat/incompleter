# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import chain, zip_longest
    _l_(80287)

except ImportError:
    pass

def interleave_diff_len_lists(list1, list2, list3, list4):
    _l_(80299)

    aux = [_n_(80288, "x", lambda: x) for x in _c_(80296, _n_(80289, "chain", lambda: chain), *_c_(80295, _n_(80290, "zip_longest", lambda: zip_longest), _n_(80291, "list1", lambda: list1), _n_(80292, "list2", lambda: list2), _n_(80293, "list3", lambda: list3), _n_(80294, "list4", lambda: list4))) if _n_(80297, "x", lambda: x) is not None]
    _l_(80298)
    return aux
nums1 = [2, 4, 7, 0, 5, 8]
_l_(80300)
nums2 = [2, 5, 8]
_l_(80301)
nums4 = [3, 3, -1, 7]
_l_(80302)
_c_(80304, _n_(80303, "print", lambda: print), '\nOriginal lists:')
_l_(80305)
_c_(80308, _n_(80306, "print", lambda: print), _n_(80307, "nums1", lambda: nums1))
_l_(80309)
_c_(80312, _n_(80310, "print", lambda: print), _n_(80311, "nums2", lambda: nums2))
_l_(80313)
_c_(80316, _n_(80314, "print", lambda: print), _n_(80315, "nums3", lambda: nums3))
_l_(80317)
_c_(80320, _n_(80318, "print", lambda: print), _n_(80319, "nums4", lambda: nums4))
_l_(80321)
_c_(80323, _n_(80322, "print", lambda: print), '\nInterleave said lists of different lengths:')
_l_(80324)
_c_(80332, _n_(80325, "print", lambda: print), _c_(80331, _n_(80326, "interleave_diff_len_lists", lambda: interleave_diff_len_lists), _n_(80327, "nums1", lambda: nums1), _n_(80328, "nums2", lambda: nums2), _n_(80329, "nums3", lambda: nums3), _n_(80330, "nums4", lambda: nums4)))
_l_(80333)