# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import groupby
    _l_(37913)

except ImportError:
    pass

def extract_elements(nums, n):
    _l_(37927)

    result = [_n_(37914, "i", lambda: i) for (i, j) in _c_(37917, _n_(37915, "groupby", lambda: groupby), _n_(37916, "nums", lambda: nums)) if _c_(37922, _n_(37918, "len", lambda: len), _c_(37921, _n_(37919, "list", lambda: list), _n_(37920, "j", lambda: j))) == _n_(37923, "n", lambda: n)]
    _l_(37924)
    aux = _n_(37925, "result", lambda: result)
    _l_(37926)
    return aux
nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
_l_(37928)
_c_(37930, _n_(37929, "print", lambda: print), 'Original list:')
_l_(37931)
_c_(37934, _n_(37932, "print", lambda: print), _n_(37933, "nums1", lambda: nums1))
_l_(37935)
_c_(37937, _n_(37936, "print", lambda: print), 'Extract 2 number of elements from the said list which follows each other continuously:')
_l_(37938)
_c_(37944, _n_(37939, "print", lambda: print), _c_(37943, _n_(37940, "extract_elements", lambda: extract_elements), _n_(37941, "nums1", lambda: nums1), _n_(37942, "n", lambda: n)))
_l_(37945)
nums2 = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
_l_(37946)
n = 4
_l_(37947)
_c_(37949, _n_(37948, "print", lambda: print), 'Original lists:')
_l_(37950)
_c_(37953, _n_(37951, "print", lambda: print), _n_(37952, "nums2", lambda: nums2))
_l_(37954)
_c_(37956, _n_(37955, "print", lambda: print), 'Extract 4 number of elements from the said list which follows each other continuously:')
_l_(37957)
_c_(37963, _n_(37958, "print", lambda: print), _c_(37962, _n_(37959, "extract_elements", lambda: extract_elements), _n_(37960, "nums2", lambda: nums2), _n_(37961, "n", lambda: n)))
_l_(37964)