# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import groupby
    _l_(113610)

except ImportError:
    pass

def extract_elements(nums, n):
    _l_(113624)

    result = [_n_(113611, "i", lambda: i) for i, j in _c_(113614, _n_(113612, "groupby", lambda: groupby), _n_(113613, "nums", lambda: nums)) if _c_(113619, _n_(113615, "len", lambda: len), _c_(113618, _n_(113616, "list", lambda: list), _n_(113617, "j", lambda: j))) == _n_(113620, "n", lambda: n)]
    _l_(113621)
    aux = _n_(113622, "result", lambda: result)
    _l_(113623)
    return aux
nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
_l_(113625)
n = 2
_l_(113626)
_c_(113628, _n_(113627, "print", lambda: print), 'Original list:')
_l_(113629)
_c_(113632, _n_(113630, "print", lambda: print), _n_(113631, "nums1", lambda: nums1))
_l_(113633)
_c_(113635, _n_(113634, "print", lambda: print), 'Extract 2 number of elements from the said list which follows each other continuously:')
_l_(113636)
_c_(113642, _n_(113637, "print", lambda: print), _c_(113641, _n_(113638, "extract_elements", lambda: extract_elements), _n_(113639, "nums1", lambda: nums1), _n_(113640, "n", lambda: n)))
_l_(113643)
n = 4
_l_(113644)
_c_(113646, _n_(113645, "print", lambda: print), 'Original lists:')
_l_(113647)
_c_(113650, _n_(113648, "print", lambda: print), _n_(113649, "nums2", lambda: nums2))
_l_(113651)
_c_(113653, _n_(113652, "print", lambda: print), 'Extract 4 number of elements from the said list which follows each other continuously:')
_l_(113654)
_c_(113660, _n_(113655, "print", lambda: print), _c_(113659, _n_(113656, "extract_elements", lambda: extract_elements), _n_(113657, "nums2", lambda: nums2), _n_(113658, "n", lambda: n)))
_l_(113661)