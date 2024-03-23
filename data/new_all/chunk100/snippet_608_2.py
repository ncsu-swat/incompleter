# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_diff_len_lists(list1, list2, list3, list4):
    _l_(63834)

    l1 = _c_(63773, _n_(63771, "len", lambda: len), _n_(63772, "list1", lambda: list1))
    _l_(63774)
    l2 = _c_(63777, _n_(63775, "len", lambda: len), _n_(63776, "list2", lambda: list2))
    _l_(63778)
    l3 = _c_(63781, _n_(63779, "len", lambda: len), _n_(63780, "list3", lambda: list3))
    _l_(63782)
    l4 = _c_(63785, _n_(63783, "len", lambda: len), _n_(63784, "list4", lambda: list4))
    _l_(63786)
    for i in _c_(63794, _n_(63787, "range", lambda: range), _c_(63793, _n_(63788, "max", lambda: max), _n_(63789, "l1", lambda: l1), _n_(63790, "l2", lambda: l2), _n_(63791, "l3", lambda: l3), _n_(63792, "l4", lambda: l4))):
        _l_(63831)

        if _n_(63795, "i", lambda: i) < _n_(63796, "l1", lambda: l1):
            _l_(63803)

            _c_(63801, _a_(63798, _n_(63797, "result", lambda: result), "append"), _n_(63799, "list1", lambda: list1)[_n_(63800, "i", lambda: i)])
            _l_(63802)
        if _n_(63804, "i", lambda: i) < _n_(63805, "l2", lambda: l2):
            _l_(63812)

            _c_(63810, _a_(63807, _n_(63806, "result", lambda: result), "append"), _n_(63808, "list2", lambda: list2)[_n_(63809, "i", lambda: i)])
            _l_(63811)
        if _n_(63813, "i", lambda: i) < _n_(63814, "l3", lambda: l3):
            _l_(63821)

            _c_(63819, _a_(63816, _n_(63815, "result", lambda: result), "append"), _n_(63817, "list3", lambda: list3)[_n_(63818, "i", lambda: i)])
            _l_(63820)
        if _n_(63822, "i", lambda: i) < _n_(63823, "l4", lambda: l4):
            _l_(63830)

            _c_(63828, _a_(63825, _n_(63824, "result", lambda: result), "append"), _n_(63826, "list4", lambda: list4)[_n_(63827, "i", lambda: i)])
            _l_(63829)
    aux = _n_(63832, "result", lambda: result)
    _l_(63833)
    return aux
nums1 = [2, 4, 7, 0, 5, 8]
_l_(63835)
nums2 = [2, 5, 8]
_l_(63836)
nums3 = [0, 1]
_l_(63837)
nums4 = [3, 3, -1, 7]
_l_(63838)
_c_(63840, _n_(63839, "print", lambda: print), '\nOriginal lists:')
_l_(63841)
_c_(63844, _n_(63842, "print", lambda: print), _n_(63843, "nums1", lambda: nums1))
_l_(63845)
_c_(63848, _n_(63846, "print", lambda: print), _n_(63847, "nums2", lambda: nums2))
_l_(63849)
_c_(63852, _n_(63850, "print", lambda: print), _n_(63851, "nums3", lambda: nums3))
_l_(63853)
_c_(63856, _n_(63854, "print", lambda: print), _n_(63855, "nums4", lambda: nums4))
_l_(63857)
_c_(63859, _n_(63858, "print", lambda: print), '\nInterleave said lists of different lengths:')
_l_(63860)
_c_(63868, _n_(63861, "print", lambda: print), _c_(63867, _n_(63862, "interleave_diff_len_lists", lambda: interleave_diff_len_lists), _n_(63863, "nums1", lambda: nums1), _n_(63864, "nums2", lambda: nums2), _n_(63865, "nums3", lambda: nums3), _n_(63866, "nums4", lambda: nums4)))
_l_(63869)