# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_diff_len_lists(list1, list2, list3, list4):
    _l_(64324)

    result = []
    _l_(64260)
    l1 = _c_(64263, _n_(64261, "len", lambda: len), _n_(64262, "list1", lambda: list1))
    _l_(64264)
    l2 = _c_(64267, _n_(64265, "len", lambda: len), _n_(64266, "list2", lambda: list2))
    _l_(64268)
    l3 = _c_(64271, _n_(64269, "len", lambda: len), _n_(64270, "list3", lambda: list3))
    _l_(64272)
    l4 = _c_(64275, _n_(64273, "len", lambda: len), _n_(64274, "list4", lambda: list4))
    _l_(64276)
    for i in _c_(64284, _n_(64277, "range", lambda: range), _c_(64283, _n_(64278, "max", lambda: max), _n_(64279, "l1", lambda: l1), _n_(64280, "l2", lambda: l2), _n_(64281, "l3", lambda: l3), _n_(64282, "l4", lambda: l4))):
        _l_(64321)

        if _n_(64285, "i", lambda: i) < _n_(64286, "l1", lambda: l1):
            _l_(64293)

            _c_(64291, _a_(64288, _n_(64287, "result", lambda: result), "append"), _n_(64289, "list1", lambda: list1)[_n_(64290, "i", lambda: i)])
            _l_(64292)
        if _n_(64294, "i", lambda: i) < _n_(64295, "l2", lambda: l2):
            _l_(64302)

            _c_(64300, _a_(64297, _n_(64296, "result", lambda: result), "append"), _n_(64298, "list2", lambda: list2)[_n_(64299, "i", lambda: i)])
            _l_(64301)
        if _n_(64303, "i", lambda: i) < _n_(64304, "l3", lambda: l3):
            _l_(64311)

            _c_(64309, _a_(64306, _n_(64305, "result", lambda: result), "append"), _n_(64307, "list3", lambda: list3)[_n_(64308, "i", lambda: i)])
            _l_(64310)
        if _n_(64312, "i", lambda: i) < _n_(64313, "l4", lambda: l4):
            _l_(64320)

            _c_(64318, _a_(64315, _n_(64314, "result", lambda: result), "append"), _n_(64316, "list4", lambda: list4)[_n_(64317, "i", lambda: i)])
            _l_(64319)
    aux = _n_(64322, "result", lambda: result)
    _l_(64323)
    return aux
nums1 = [2, 4, 7, 0, 5, 8]
_l_(64325)
nums2 = [2, 5, 8]
_l_(64326)
nums4 = [3, 3, -1, 7]
_l_(64327)
_c_(64329, _n_(64328, "print", lambda: print), '\nOriginal lists:')
_l_(64330)
_c_(64333, _n_(64331, "print", lambda: print), _n_(64332, "nums1", lambda: nums1))
_l_(64334)
_c_(64337, _n_(64335, "print", lambda: print), _n_(64336, "nums2", lambda: nums2))
_l_(64338)
_c_(64341, _n_(64339, "print", lambda: print), _n_(64340, "nums3", lambda: nums3))
_l_(64342)
_c_(64345, _n_(64343, "print", lambda: print), _n_(64344, "nums4", lambda: nums4))
_l_(64346)
_c_(64348, _n_(64347, "print", lambda: print), '\nInterleave said lists of different lengths:')
_l_(64349)
_c_(64357, _n_(64350, "print", lambda: print), _c_(64356, _n_(64351, "interleave_diff_len_lists", lambda: interleave_diff_len_lists), _n_(64352, "nums1", lambda: nums1), _n_(64353, "nums2", lambda: nums2), _n_(64354, "nums3", lambda: nums3), _n_(64355, "nums4", lambda: nums4)))
_l_(64358)