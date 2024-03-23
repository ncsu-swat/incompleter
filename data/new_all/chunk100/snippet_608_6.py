# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_diff_len_lists(list1, list2, list3, list4):
    _l_(64224)

    result = []
    _l_(64164)
    l1 = _c_(64167, _n_(64165, "len", lambda: len), _n_(64166, "list1", lambda: list1))
    _l_(64168)
    l2 = _c_(64171, _n_(64169, "len", lambda: len), _n_(64170, "list2", lambda: list2))
    _l_(64172)
    l4 = _c_(64175, _n_(64173, "len", lambda: len), _n_(64174, "list4", lambda: list4))
    _l_(64176)
    for i in _c_(64184, _n_(64177, "range", lambda: range), _c_(64183, _n_(64178, "max", lambda: max), _n_(64179, "l1", lambda: l1), _n_(64180, "l2", lambda: l2), _n_(64181, "l3", lambda: l3), _n_(64182, "l4", lambda: l4))):
        _l_(64221)

        if _n_(64185, "i", lambda: i) < _n_(64186, "l1", lambda: l1):
            _l_(64193)

            _c_(64191, _a_(64188, _n_(64187, "result", lambda: result), "append"), _n_(64189, "list1", lambda: list1)[_n_(64190, "i", lambda: i)])
            _l_(64192)
        if _n_(64194, "i", lambda: i) < _n_(64195, "l2", lambda: l2):
            _l_(64202)

            _c_(64200, _a_(64197, _n_(64196, "result", lambda: result), "append"), _n_(64198, "list2", lambda: list2)[_n_(64199, "i", lambda: i)])
            _l_(64201)
        if _n_(64203, "i", lambda: i) < _n_(64204, "l3", lambda: l3):
            _l_(64211)

            _c_(64209, _a_(64206, _n_(64205, "result", lambda: result), "append"), _n_(64207, "list3", lambda: list3)[_n_(64208, "i", lambda: i)])
            _l_(64210)
        if _n_(64212, "i", lambda: i) < _n_(64213, "l4", lambda: l4):
            _l_(64220)

            _c_(64218, _a_(64215, _n_(64214, "result", lambda: result), "append"), _n_(64216, "list4", lambda: list4)[_n_(64217, "i", lambda: i)])
            _l_(64219)
    aux = _n_(64222, "result", lambda: result)
    _l_(64223)
    return aux
nums1 = [2, 4, 7, 0, 5, 8]
_l_(64225)
nums2 = [2, 5, 8]
_l_(64226)
nums3 = [0, 1]
_l_(64227)
nums4 = [3, 3, -1, 7]
_l_(64228)
_c_(64230, _n_(64229, "print", lambda: print), '\nOriginal lists:')
_l_(64231)
_c_(64234, _n_(64232, "print", lambda: print), _n_(64233, "nums1", lambda: nums1))
_l_(64235)
_c_(64238, _n_(64236, "print", lambda: print), _n_(64237, "nums2", lambda: nums2))
_l_(64239)
_c_(64242, _n_(64240, "print", lambda: print), _n_(64241, "nums3", lambda: nums3))
_l_(64243)
_c_(64246, _n_(64244, "print", lambda: print), _n_(64245, "nums4", lambda: nums4))
_l_(64247)
_c_(64249, _n_(64248, "print", lambda: print), '\nInterleave said lists of different lengths:')
_l_(64250)
_c_(64258, _n_(64251, "print", lambda: print), _c_(64257, _n_(64252, "interleave_diff_len_lists", lambda: interleave_diff_len_lists), _n_(64253, "nums1", lambda: nums1), _n_(64254, "nums2", lambda: nums2), _n_(64255, "nums3", lambda: nums3), _n_(64256, "nums4", lambda: nums4)))
_l_(64259)