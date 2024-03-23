# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_diff_len_lists(list1, list2, list3, list4):
    _l_(63639)

    result = []
    _l_(63579)
    l1 = _c_(63582, _n_(63580, "len", lambda: len), _n_(63581, "list1", lambda: list1))
    _l_(63583)
    l2 = _c_(63586, _n_(63584, "len", lambda: len), _n_(63585, "list2", lambda: list2))
    _l_(63587)
    l3 = _c_(63590, _n_(63588, "len", lambda: len), _n_(63589, "list3", lambda: list3))
    _l_(63591)
    for i in _c_(63599, _n_(63592, "range", lambda: range), _c_(63598, _n_(63593, "max", lambda: max), _n_(63594, "l1", lambda: l1), _n_(63595, "l2", lambda: l2), _n_(63596, "l3", lambda: l3), _n_(63597, "l4", lambda: l4))):
        _l_(63636)

        if _n_(63600, "i", lambda: i) < _n_(63601, "l1", lambda: l1):
            _l_(63608)

            _c_(63606, _a_(63603, _n_(63602, "result", lambda: result), "append"), _n_(63604, "list1", lambda: list1)[_n_(63605, "i", lambda: i)])
            _l_(63607)
        if _n_(63609, "i", lambda: i) < _n_(63610, "l2", lambda: l2):
            _l_(63617)

            _c_(63615, _a_(63612, _n_(63611, "result", lambda: result), "append"), _n_(63613, "list2", lambda: list2)[_n_(63614, "i", lambda: i)])
            _l_(63616)
        if _n_(63618, "i", lambda: i) < _n_(63619, "l3", lambda: l3):
            _l_(63626)

            _c_(63624, _a_(63621, _n_(63620, "result", lambda: result), "append"), _n_(63622, "list3", lambda: list3)[_n_(63623, "i", lambda: i)])
            _l_(63625)
        if _n_(63627, "i", lambda: i) < _n_(63628, "l4", lambda: l4):
            _l_(63635)

            _c_(63633, _a_(63630, _n_(63629, "result", lambda: result), "append"), _n_(63631, "list4", lambda: list4)[_n_(63632, "i", lambda: i)])
            _l_(63634)
    aux = _n_(63637, "result", lambda: result)
    _l_(63638)
    return aux
nums1 = [2, 4, 7, 0, 5, 8]
_l_(63640)
nums2 = [2, 5, 8]
_l_(63641)
nums3 = [0, 1]
_l_(63642)
nums4 = [3, 3, -1, 7]
_l_(63643)
_c_(63645, _n_(63644, "print", lambda: print), '\nOriginal lists:')
_l_(63646)
_c_(63649, _n_(63647, "print", lambda: print), _n_(63648, "nums1", lambda: nums1))
_l_(63650)
_c_(63653, _n_(63651, "print", lambda: print), _n_(63652, "nums2", lambda: nums2))
_l_(63654)
_c_(63657, _n_(63655, "print", lambda: print), _n_(63656, "nums3", lambda: nums3))
_l_(63658)
_c_(63661, _n_(63659, "print", lambda: print), _n_(63660, "nums4", lambda: nums4))
_l_(63662)
_c_(63664, _n_(63663, "print", lambda: print), '\nInterleave said lists of different lengths:')
_l_(63665)
_c_(63673, _n_(63666, "print", lambda: print), _c_(63672, _n_(63667, "interleave_diff_len_lists", lambda: interleave_diff_len_lists), _n_(63668, "nums1", lambda: nums1), _n_(63669, "nums2", lambda: nums2), _n_(63670, "nums3", lambda: nums3), _n_(63671, "nums4", lambda: nums4)))
_l_(63674)