# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import groupby
    _l_(37711)

except ImportError:
    pass

def extract_elements(nums, n):
    _l_(37725)

    result = [_n_(37712, "i", lambda: i) for (i, j) in _c_(37715, _n_(37713, "groupby", lambda: groupby), _n_(37714, "nums", lambda: nums)) if _c_(37720, _n_(37716, "len", lambda: len), _c_(37719, _n_(37717, "list", lambda: list), _n_(37718, "j", lambda: j))) == _n_(37721, "n", lambda: n)]
    _l_(37722)
    aux = _n_(37723, "result", lambda: result)
    _l_(37724)
    return aux
nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
_l_(37726)
n = 2
_l_(37727)
_c_(37729, _n_(37728, "print", lambda: print), 'Original list:')
_l_(37730)
_c_(37733, _n_(37731, "print", lambda: print), _n_(37732, "nums1", lambda: nums1))
_l_(37734)
_c_(37736, _n_(37735, "print", lambda: print), 'Extract 2 number of elements from the said list which follows each other continuously:')
_l_(37737)
_c_(37743, _n_(37738, "print", lambda: print), _c_(37742, _n_(37739, "extract_elements", lambda: extract_elements), _n_(37740, "nums1", lambda: nums1), _n_(37741, "n", lambda: n)))
_l_(37744)
nums2 = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
_l_(37745)
_c_(37747, _n_(37746, "print", lambda: print), 'Original lists:')
_l_(37748)
_c_(37751, _n_(37749, "print", lambda: print), _n_(37750, "nums2", lambda: nums2))
_l_(37752)
_c_(37754, _n_(37753, "print", lambda: print), 'Extract 4 number of elements from the said list which follows each other continuously:')
_l_(37755)
_c_(37761, _n_(37756, "print", lambda: print), _c_(37760, _n_(37757, "extract_elements", lambda: extract_elements), _n_(37758, "nums2", lambda: nums2), _n_(37759, "n", lambda: n)))
_l_(37762)