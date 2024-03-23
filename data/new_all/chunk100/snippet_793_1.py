# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import chain, zip_longest
    _l_(80191)

except ImportError:
    pass

def interleave_diff_len_lists(list1, list2, list3, list4):
    _l_(80203)

    aux = [_n_(80192, "x", lambda: x) for x in _c_(80200, _n_(80193, "chain", lambda: chain), *_c_(80199, _n_(80194, "zip_longest", lambda: zip_longest), _n_(80195, "list1", lambda: list1), _n_(80196, "list2", lambda: list2), _n_(80197, "list3", lambda: list3), _n_(80198, "list4", lambda: list4))) if _n_(80201, "x", lambda: x) is not None]
    _l_(80202)
    return aux
nums1 = [2, 4, 7, 0, 5, 8]
_l_(80204)
nums3 = [0, 1]
_l_(80205)
nums4 = [3, 3, -1, 7]
_l_(80206)
_c_(80208, _n_(80207, "print", lambda: print), '\nOriginal lists:')
_l_(80209)
_c_(80212, _n_(80210, "print", lambda: print), _n_(80211, "nums1", lambda: nums1))
_l_(80213)
_c_(80216, _n_(80214, "print", lambda: print), _n_(80215, "nums2", lambda: nums2))
_l_(80217)
_c_(80220, _n_(80218, "print", lambda: print), _n_(80219, "nums3", lambda: nums3))
_l_(80221)
_c_(80224, _n_(80222, "print", lambda: print), _n_(80223, "nums4", lambda: nums4))
_l_(80225)
_c_(80227, _n_(80226, "print", lambda: print), '\nInterleave said lists of different lengths:')
_l_(80228)
_c_(80236, _n_(80229, "print", lambda: print), _c_(80235, _n_(80230, "interleave_diff_len_lists", lambda: interleave_diff_len_lists), _n_(80231, "nums1", lambda: nums1), _n_(80232, "nums2", lambda: nums2), _n_(80233, "nums3", lambda: nums3), _n_(80234, "nums4", lambda: nums4)))
_l_(80237)