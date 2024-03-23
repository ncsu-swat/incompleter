# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import groupby
    _l_(37764)

except ImportError:
    pass

def extract_elements(nums, n):
    _l_(37778)

    result = [_n_(37765, "i", lambda: i) for (i, j) in _c_(37768, _n_(37766, "groupby", lambda: groupby), _n_(37767, "nums", lambda: nums)) if _c_(37773, _n_(37769, "len", lambda: len), _c_(37772, _n_(37770, "list", lambda: list), _n_(37771, "j", lambda: j))) == _n_(37774, "n", lambda: n)]
    _l_(37775)
    aux = _n_(37776, "result", lambda: result)
    _l_(37777)
    return aux
n = 2
_l_(37779)
_c_(37781, _n_(37780, "print", lambda: print), 'Original list:')
_l_(37782)
_c_(37785, _n_(37783, "print", lambda: print), _n_(37784, "nums1", lambda: nums1))
_l_(37786)
_c_(37788, _n_(37787, "print", lambda: print), 'Extract 2 number of elements from the said list which follows each other continuously:')
_l_(37789)
_c_(37795, _n_(37790, "print", lambda: print), _c_(37794, _n_(37791, "extract_elements", lambda: extract_elements), _n_(37792, "nums1", lambda: nums1), _n_(37793, "n", lambda: n)))
_l_(37796)
nums2 = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
_l_(37797)
n = 4
_l_(37798)
_c_(37800, _n_(37799, "print", lambda: print), 'Original lists:')
_l_(37801)
_c_(37804, _n_(37802, "print", lambda: print), _n_(37803, "nums2", lambda: nums2))
_l_(37805)
_c_(37807, _n_(37806, "print", lambda: print), 'Extract 4 number of elements from the said list which follows each other continuously:')
_l_(37808)
_c_(37814, _n_(37809, "print", lambda: print), _c_(37813, _n_(37810, "extract_elements", lambda: extract_elements), _n_(37811, "nums2", lambda: nums2), _n_(37812, "n", lambda: n)))
_l_(37815)