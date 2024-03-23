# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_diff_len_lists(list1, list2, list3, list4):
    _l_(64129)

    result = []
    _l_(64065)
    l1 = _c_(64068, _n_(64066, "len", lambda: len), _n_(64067, "list1", lambda: list1))
    _l_(64069)
    l2 = _c_(64072, _n_(64070, "len", lambda: len), _n_(64071, "list2", lambda: list2))
    _l_(64073)
    l3 = _c_(64076, _n_(64074, "len", lambda: len), _n_(64075, "list3", lambda: list3))
    _l_(64077)
    l4 = _c_(64080, _n_(64078, "len", lambda: len), _n_(64079, "list4", lambda: list4))
    _l_(64081)
    for i in _c_(64089, _n_(64082, "range", lambda: range), _c_(64088, _n_(64083, "max", lambda: max), _n_(64084, "l1", lambda: l1), _n_(64085, "l2", lambda: l2), _n_(64086, "l3", lambda: l3), _n_(64087, "l4", lambda: l4))):
        _l_(64126)

        if _n_(64090, "i", lambda: i) < _n_(64091, "l1", lambda: l1):
            _l_(64098)

            _c_(64096, _a_(64093, _n_(64092, "result", lambda: result), "append"), _n_(64094, "list1", lambda: list1)[_n_(64095, "i", lambda: i)])
            _l_(64097)
        if _n_(64099, "i", lambda: i) < _n_(64100, "l2", lambda: l2):
            _l_(64107)

            _c_(64105, _a_(64102, _n_(64101, "result", lambda: result), "append"), _n_(64103, "list2", lambda: list2)[_n_(64104, "i", lambda: i)])
            _l_(64106)
        if _n_(64108, "i", lambda: i) < _n_(64109, "l3", lambda: l3):
            _l_(64116)

            _c_(64114, _a_(64111, _n_(64110, "result", lambda: result), "append"), _n_(64112, "list3", lambda: list3)[_n_(64113, "i", lambda: i)])
            _l_(64115)
        if _n_(64117, "i", lambda: i) < _n_(64118, "l4", lambda: l4):
            _l_(64125)

            _c_(64123, _a_(64120, _n_(64119, "result", lambda: result), "append"), _n_(64121, "list4", lambda: list4)[_n_(64122, "i", lambda: i)])
            _l_(64124)
    aux = _n_(64127, "result", lambda: result)
    _l_(64128)
    return aux
nums2 = [2, 5, 8]
_l_(64130)
nums3 = [0, 1]
_l_(64131)
nums4 = [3, 3, -1, 7]
_l_(64132)
_c_(64134, _n_(64133, "print", lambda: print), '\nOriginal lists:')
_l_(64135)
_c_(64138, _n_(64136, "print", lambda: print), _n_(64137, "nums1", lambda: nums1))
_l_(64139)
_c_(64142, _n_(64140, "print", lambda: print), _n_(64141, "nums2", lambda: nums2))
_l_(64143)
_c_(64146, _n_(64144, "print", lambda: print), _n_(64145, "nums3", lambda: nums3))
_l_(64147)
_c_(64150, _n_(64148, "print", lambda: print), _n_(64149, "nums4", lambda: nums4))
_l_(64151)
_c_(64153, _n_(64152, "print", lambda: print), '\nInterleave said lists of different lengths:')
_l_(64154)
_c_(64162, _n_(64155, "print", lambda: print), _c_(64161, _n_(64156, "interleave_diff_len_lists", lambda: interleave_diff_len_lists), _n_(64157, "nums1", lambda: nums1), _n_(64158, "nums2", lambda: nums2), _n_(64159, "nums3", lambda: nums3), _n_(64160, "nums4", lambda: nums4)))
_l_(64163)