# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import chain, zip_longest
    _l_(80143)

except ImportError:
    pass

def interleave_diff_len_lists(list1, list2, list3, list4):
    _l_(80155)

    aux = [_n_(80144, "x", lambda: x) for x in _c_(80152, _n_(80145, "chain", lambda: chain), *_c_(80151, _n_(80146, "zip_longest", lambda: zip_longest), _n_(80147, "list1", lambda: list1), _n_(80148, "list2", lambda: list2), _n_(80149, "list3", lambda: list3), _n_(80150, "list4", lambda: list4))) if _n_(80153, "x", lambda: x) is not None]
    _l_(80154)
    return aux
nums1 = [2, 4, 7, 0, 5, 8]
_l_(80156)
nums2 = [2, 5, 8]
_l_(80157)
nums3 = [0, 1]
_l_(80158)
_c_(80160, _n_(80159, "print", lambda: print), '\nOriginal lists:')
_l_(80161)
_c_(80164, _n_(80162, "print", lambda: print), _n_(80163, "nums1", lambda: nums1))
_l_(80165)
_c_(80168, _n_(80166, "print", lambda: print), _n_(80167, "nums2", lambda: nums2))
_l_(80169)
_c_(80172, _n_(80170, "print", lambda: print), _n_(80171, "nums3", lambda: nums3))
_l_(80173)
_c_(80176, _n_(80174, "print", lambda: print), _n_(80175, "nums4", lambda: nums4))
_l_(80177)
_c_(80179, _n_(80178, "print", lambda: print), '\nInterleave said lists of different lengths:')
_l_(80180)
_c_(80188, _n_(80181, "print", lambda: print), _c_(80187, _n_(80182, "interleave_diff_len_lists", lambda: interleave_diff_len_lists), _n_(80183, "nums1", lambda: nums1), _n_(80184, "nums2", lambda: nums2), _n_(80185, "nums3", lambda: nums3), _n_(80186, "nums4", lambda: nums4)))
_l_(80189)