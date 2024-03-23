# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_diff_len_lists(list1, list2, list3, list4):
    _l_(64423)

    result = []
    _l_(64359)
    l1 = _c_(64362, _n_(64360, "len", lambda: len), _n_(64361, "list1", lambda: list1))
    _l_(64363)
    l2 = _c_(64366, _n_(64364, "len", lambda: len), _n_(64365, "list2", lambda: list2))
    _l_(64367)
    l3 = _c_(64370, _n_(64368, "len", lambda: len), _n_(64369, "list3", lambda: list3))
    _l_(64371)
    l4 = _c_(64374, _n_(64372, "len", lambda: len), _n_(64373, "list4", lambda: list4))
    _l_(64375)
    for i in _c_(64383, _n_(64376, "range", lambda: range), _c_(64382, _n_(64377, "max", lambda: max), _n_(64378, "l1", lambda: l1), _n_(64379, "l2", lambda: l2), _n_(64380, "l3", lambda: l3), _n_(64381, "l4", lambda: l4))):
        _l_(64420)

        if _n_(64384, "i", lambda: i) < _n_(64385, "l1", lambda: l1):
            _l_(64392)

            _c_(64390, _a_(64387, _n_(64386, "result", lambda: result), "append"), _n_(64388, "list1", lambda: list1)[_n_(64389, "i", lambda: i)])
            _l_(64391)
        if _n_(64393, "i", lambda: i) < _n_(64394, "l2", lambda: l2):
            _l_(64401)

            _c_(64399, _a_(64396, _n_(64395, "result", lambda: result), "append"), _n_(64397, "list2", lambda: list2)[_n_(64398, "i", lambda: i)])
            _l_(64400)
        if _n_(64402, "i", lambda: i) < _n_(64403, "l3", lambda: l3):
            _l_(64410)

            _c_(64408, _a_(64405, _n_(64404, "result", lambda: result), "append"), _n_(64406, "list3", lambda: list3)[_n_(64407, "i", lambda: i)])
            _l_(64409)
        if _n_(64411, "i", lambda: i) < _n_(64412, "l4", lambda: l4):
            _l_(64419)

            _c_(64417, _a_(64414, _n_(64413, "result", lambda: result), "append"), _n_(64415, "list4", lambda: list4)[_n_(64416, "i", lambda: i)])
            _l_(64418)
    aux = _n_(64421, "result", lambda: result)
    _l_(64422)
    return aux
nums1 = [2, 4, 7, 0, 5, 8]
_l_(64424)
nums3 = [0, 1]
_l_(64425)
nums4 = [3, 3, -1, 7]
_l_(64426)
_c_(64428, _n_(64427, "print", lambda: print), '\nOriginal lists:')
_l_(64429)
_c_(64432, _n_(64430, "print", lambda: print), _n_(64431, "nums1", lambda: nums1))
_l_(64433)
_c_(64436, _n_(64434, "print", lambda: print), _n_(64435, "nums2", lambda: nums2))
_l_(64437)
_c_(64440, _n_(64438, "print", lambda: print), _n_(64439, "nums3", lambda: nums3))
_l_(64441)
_c_(64444, _n_(64442, "print", lambda: print), _n_(64443, "nums4", lambda: nums4))
_l_(64445)
_c_(64447, _n_(64446, "print", lambda: print), '\nInterleave said lists of different lengths:')
_l_(64448)
_c_(64456, _n_(64449, "print", lambda: print), _c_(64455, _n_(64450, "interleave_diff_len_lists", lambda: interleave_diff_len_lists), _n_(64451, "nums1", lambda: nums1), _n_(64452, "nums2", lambda: nums2), _n_(64453, "nums3", lambda: nums3), _n_(64454, "nums4", lambda: nums4)))
_l_(64457)