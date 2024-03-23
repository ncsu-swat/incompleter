# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_diff_len_lists(list1, list2, list3, list4):
    _l_(64029)

    result = []
    _l_(63969)
    l1 = _c_(63972, _n_(63970, "len", lambda: len), _n_(63971, "list1", lambda: list1))
    _l_(63973)
    l3 = _c_(63976, _n_(63974, "len", lambda: len), _n_(63975, "list3", lambda: list3))
    _l_(63977)
    l4 = _c_(63980, _n_(63978, "len", lambda: len), _n_(63979, "list4", lambda: list4))
    _l_(63981)
    for i in _c_(63989, _n_(63982, "range", lambda: range), _c_(63988, _n_(63983, "max", lambda: max), _n_(63984, "l1", lambda: l1), _n_(63985, "l2", lambda: l2), _n_(63986, "l3", lambda: l3), _n_(63987, "l4", lambda: l4))):
        _l_(64026)

        if _n_(63990, "i", lambda: i) < _n_(63991, "l1", lambda: l1):
            _l_(63998)

            _c_(63996, _a_(63993, _n_(63992, "result", lambda: result), "append"), _n_(63994, "list1", lambda: list1)[_n_(63995, "i", lambda: i)])
            _l_(63997)
        if _n_(63999, "i", lambda: i) < _n_(64000, "l2", lambda: l2):
            _l_(64007)

            _c_(64005, _a_(64002, _n_(64001, "result", lambda: result), "append"), _n_(64003, "list2", lambda: list2)[_n_(64004, "i", lambda: i)])
            _l_(64006)
        if _n_(64008, "i", lambda: i) < _n_(64009, "l3", lambda: l3):
            _l_(64016)

            _c_(64014, _a_(64011, _n_(64010, "result", lambda: result), "append"), _n_(64012, "list3", lambda: list3)[_n_(64013, "i", lambda: i)])
            _l_(64015)
        if _n_(64017, "i", lambda: i) < _n_(64018, "l4", lambda: l4):
            _l_(64025)

            _c_(64023, _a_(64020, _n_(64019, "result", lambda: result), "append"), _n_(64021, "list4", lambda: list4)[_n_(64022, "i", lambda: i)])
            _l_(64024)
    aux = _n_(64027, "result", lambda: result)
    _l_(64028)
    return aux
nums1 = [2, 4, 7, 0, 5, 8]
_l_(64030)
nums2 = [2, 5, 8]
_l_(64031)
nums3 = [0, 1]
_l_(64032)
nums4 = [3, 3, -1, 7]
_l_(64033)
_c_(64035, _n_(64034, "print", lambda: print), '\nOriginal lists:')
_l_(64036)
_c_(64039, _n_(64037, "print", lambda: print), _n_(64038, "nums1", lambda: nums1))
_l_(64040)
_c_(64043, _n_(64041, "print", lambda: print), _n_(64042, "nums2", lambda: nums2))
_l_(64044)
_c_(64047, _n_(64045, "print", lambda: print), _n_(64046, "nums3", lambda: nums3))
_l_(64048)
_c_(64051, _n_(64049, "print", lambda: print), _n_(64050, "nums4", lambda: nums4))
_l_(64052)
_c_(64054, _n_(64053, "print", lambda: print), '\nInterleave said lists of different lengths:')
_l_(64055)
_c_(64063, _n_(64056, "print", lambda: print), _c_(64062, _n_(64057, "interleave_diff_len_lists", lambda: interleave_diff_len_lists), _n_(64058, "nums1", lambda: nums1), _n_(64059, "nums2", lambda: nums2), _n_(64060, "nums3", lambda: nums3), _n_(64061, "nums4", lambda: nums4)))
_l_(64064)