# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_diff_len_lists(list1, list2, list3, list4):
    _l_(63735)

    result = []
    _l_(63675)
    l2 = _c_(63678, _n_(63676, "len", lambda: len), _n_(63677, "list2", lambda: list2))
    _l_(63679)
    l3 = _c_(63682, _n_(63680, "len", lambda: len), _n_(63681, "list3", lambda: list3))
    _l_(63683)
    l4 = _c_(63686, _n_(63684, "len", lambda: len), _n_(63685, "list4", lambda: list4))
    _l_(63687)
    for i in _c_(63695, _n_(63688, "range", lambda: range), _c_(63694, _n_(63689, "max", lambda: max), _n_(63690, "l1", lambda: l1), _n_(63691, "l2", lambda: l2), _n_(63692, "l3", lambda: l3), _n_(63693, "l4", lambda: l4))):
        _l_(63732)

        if _n_(63696, "i", lambda: i) < _n_(63697, "l1", lambda: l1):
            _l_(63704)

            _c_(63702, _a_(63699, _n_(63698, "result", lambda: result), "append"), _n_(63700, "list1", lambda: list1)[_n_(63701, "i", lambda: i)])
            _l_(63703)
        if _n_(63705, "i", lambda: i) < _n_(63706, "l2", lambda: l2):
            _l_(63713)

            _c_(63711, _a_(63708, _n_(63707, "result", lambda: result), "append"), _n_(63709, "list2", lambda: list2)[_n_(63710, "i", lambda: i)])
            _l_(63712)
        if _n_(63714, "i", lambda: i) < _n_(63715, "l3", lambda: l3):
            _l_(63722)

            _c_(63720, _a_(63717, _n_(63716, "result", lambda: result), "append"), _n_(63718, "list3", lambda: list3)[_n_(63719, "i", lambda: i)])
            _l_(63721)
        if _n_(63723, "i", lambda: i) < _n_(63724, "l4", lambda: l4):
            _l_(63731)

            _c_(63729, _a_(63726, _n_(63725, "result", lambda: result), "append"), _n_(63727, "list4", lambda: list4)[_n_(63728, "i", lambda: i)])
            _l_(63730)
    aux = _n_(63733, "result", lambda: result)
    _l_(63734)
    return aux
nums1 = [2, 4, 7, 0, 5, 8]
_l_(63736)
nums2 = [2, 5, 8]
_l_(63737)
nums3 = [0, 1]
_l_(63738)
nums4 = [3, 3, -1, 7]
_l_(63739)
_c_(63741, _n_(63740, "print", lambda: print), '\nOriginal lists:')
_l_(63742)
_c_(63745, _n_(63743, "print", lambda: print), _n_(63744, "nums1", lambda: nums1))
_l_(63746)
_c_(63749, _n_(63747, "print", lambda: print), _n_(63748, "nums2", lambda: nums2))
_l_(63750)
_c_(63753, _n_(63751, "print", lambda: print), _n_(63752, "nums3", lambda: nums3))
_l_(63754)
_c_(63757, _n_(63755, "print", lambda: print), _n_(63756, "nums4", lambda: nums4))
_l_(63758)
_c_(63760, _n_(63759, "print", lambda: print), '\nInterleave said lists of different lengths:')
_l_(63761)
_c_(63769, _n_(63762, "print", lambda: print), _c_(63768, _n_(63763, "interleave_diff_len_lists", lambda: interleave_diff_len_lists), _n_(63764, "nums1", lambda: nums1), _n_(63765, "nums2", lambda: nums2), _n_(63766, "nums3", lambda: nums3), _n_(63767, "nums4", lambda: nums4)))
_l_(63770)