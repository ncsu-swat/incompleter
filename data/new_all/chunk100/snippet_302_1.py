# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(25689)

except ImportError:
    pass

def randomly_interleave(nums1, nums2):
    _l_(25713)

    result = [_c_(25692, _a_(25691, _n_(25690, "x", lambda: x), "pop"), 0) for x in _c_(25709, _a_(25694, _n_(25693, "random", lambda: random), "sample"), [_n_(25695, "nums1", lambda: nums1)] * _c_(25698, _n_(25696, "len", lambda: len), _n_(25697, "nums1", lambda: nums1)) + [_n_(25699, "nums2", lambda: nums2)] * _c_(25702, _n_(25700, "len", lambda: len), _n_(25701, "nums2", lambda: nums2)), _c_(25705, _n_(25703, "len", lambda: len), _n_(25704, "nums1", lambda: nums1)) + _c_(25708, _n_(25706, "len", lambda: len), _n_(25707, "nums2", lambda: nums2)))]
    _l_(25710)
    aux = _n_(25711, "result", lambda: result)
    _l_(25712)
    return aux
nums1 = [1, 2, 7, 8, 3, 7]
_l_(25714)
_c_(25716, _n_(25715, "print", lambda: print), 'Original lists:')
_l_(25717)
_c_(25720, _n_(25718, "print", lambda: print), _n_(25719, "nums1", lambda: nums1))
_l_(25721)
_c_(25724, _n_(25722, "print", lambda: print), _n_(25723, "nums2", lambda: nums2))
_l_(25725)
_c_(25727, _n_(25726, "print", lambda: print), '\nInterleave two given list into another list randomly:')
_l_(25728)
_c_(25734, _n_(25729, "print", lambda: print), _c_(25733, _n_(25730, "randomly_interleave", lambda: randomly_interleave), _n_(25731, "nums1", lambda: nums1), _n_(25732, "nums2", lambda: nums2)))
_l_(25735)