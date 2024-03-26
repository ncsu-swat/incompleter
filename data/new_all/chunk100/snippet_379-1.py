# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import groupby
    _l_(113663)

except ImportError:
    pass

def extract_elements(nums, n):
    _l_(113677)

    result = [_n_(113664, "i", lambda: i) for i, j in _c_(113667, _n_(113665, "groupby", lambda: groupby), _n_(113666, "nums", lambda: nums)) if _c_(113672, _n_(113668, "len", lambda: len), _c_(113671, _n_(113669, "list", lambda: list), _n_(113670, "j", lambda: j))) == _n_(113673, "n", lambda: n)]
    _l_(113674)
    aux = _n_(113675, "result", lambda: result)
    _l_(113676)
    return aux
n = 2
_l_(113678)
_c_(113680, _n_(113679, "print", lambda: print), 'Original list:')
_l_(113681)
_c_(113684, _n_(113682, "print", lambda: print), _n_(113683, "nums1", lambda: nums1))
_l_(113685)
_c_(113687, _n_(113686, "print", lambda: print), 'Extract 2 number of elements from the said list which follows each other continuously:')
_l_(113688)
_c_(113694, _n_(113689, "print", lambda: print), _c_(113693, _n_(113690, "extract_elements", lambda: extract_elements), _n_(113691, "nums1", lambda: nums1), _n_(113692, "n", lambda: n)))
_l_(113695)
nums2 = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
_l_(113696)
n = 4
_l_(113697)
_c_(113699, _n_(113698, "print", lambda: print), 'Original lists:')
_l_(113700)
_c_(113703, _n_(113701, "print", lambda: print), _n_(113702, "nums2", lambda: nums2))
_l_(113704)
_c_(113706, _n_(113705, "print", lambda: print), 'Extract 4 number of elements from the said list which follows each other continuously:')
_l_(113707)
_c_(113713, _n_(113708, "print", lambda: print), _c_(113712, _n_(113709, "extract_elements", lambda: extract_elements), _n_(113710, "nums2", lambda: nums2), _n_(113711, "n", lambda: n)))
_l_(113714)