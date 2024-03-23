# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import groupby
    _l_(37860)

except ImportError:
    pass

def extract_elements(nums, n):
    _l_(37874)

    result = [_n_(37861, "i", lambda: i) for (i, j) in _c_(37864, _n_(37862, "groupby", lambda: groupby), _n_(37863, "nums", lambda: nums)) if _c_(37869, _n_(37865, "len", lambda: len), _c_(37868, _n_(37866, "list", lambda: list), _n_(37867, "j", lambda: j))) == _n_(37870, "n", lambda: n)]
    _l_(37871)
    aux = _n_(37872, "result", lambda: result)
    _l_(37873)
    return aux
nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
_l_(37875)
n = 2
_l_(37876)
_c_(37878, _n_(37877, "print", lambda: print), 'Original list:')
_l_(37879)
_c_(37882, _n_(37880, "print", lambda: print), _n_(37881, "nums1", lambda: nums1))
_l_(37883)
_c_(37885, _n_(37884, "print", lambda: print), 'Extract 2 number of elements from the said list which follows each other continuously:')
_l_(37886)
_c_(37892, _n_(37887, "print", lambda: print), _c_(37891, _n_(37888, "extract_elements", lambda: extract_elements), _n_(37889, "nums1", lambda: nums1), _n_(37890, "n", lambda: n)))
_l_(37893)
n = 4
_l_(37894)
_c_(37896, _n_(37895, "print", lambda: print), 'Original lists:')
_l_(37897)
_c_(37900, _n_(37898, "print", lambda: print), _n_(37899, "nums2", lambda: nums2))
_l_(37901)
_c_(37903, _n_(37902, "print", lambda: print), 'Extract 4 number of elements from the said list which follows each other continuously:')
_l_(37904)
_c_(37910, _n_(37905, "print", lambda: print), _c_(37909, _n_(37906, "extract_elements", lambda: extract_elements), _n_(37907, "nums2", lambda: nums2), _n_(37908, "n", lambda: n)))
_l_(37911)