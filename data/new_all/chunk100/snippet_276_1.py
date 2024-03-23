# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def extract_index_ele(l1, l2, l3):
    _l_(22260)

    result = []
    _l_(22242)
    for (m, n, o) in _c_(22247, _n_(22243, "zip", lambda: zip), _n_(22244, "l1", lambda: l1), _n_(22245, "l2", lambda: l2), _n_(22246, "l3", lambda: l3)):
        _l_(22257)

        if _n_(22248, "m", lambda: m) == _n_(22249, "n", lambda: n) == _n_(22250, "o", lambda: o):
            _l_(22256)

            _c_(22254, _a_(22252, _n_(22251, "result", lambda: result), "append"), _n_(22253, "m", lambda: m))
            _l_(22255)
    aux = _n_(22258, "result", lambda: result)
    _l_(22259)
    return aux
nums1 = [1, 1, 3, 4, 5, 6, 7]
_l_(22261)
nums3 = [0, 1, 2, 3, 4, 5, 7]
_l_(22262)
_c_(22264, _n_(22263, "print", lambda: print), 'Original lists:')
_l_(22265)
_c_(22268, _n_(22266, "print", lambda: print), _n_(22267, "nums1", lambda: nums1))
_l_(22269)
_c_(22272, _n_(22270, "print", lambda: print), _n_(22271, "nums2", lambda: nums2))
_l_(22273)
_c_(22276, _n_(22274, "print", lambda: print), _n_(22275, "nums3", lambda: nums3))
_l_(22277)
_c_(22279, _n_(22278, "print", lambda: print), '\nCommon index elements of the said lists:')
_l_(22280)
_c_(22287, _n_(22281, "print", lambda: print), _c_(22286, _n_(22282, "extract_index_ele", lambda: extract_index_ele), _n_(22283, "nums1", lambda: nums1), _n_(22284, "nums2", lambda: nums2), _n_(22285, "nums3", lambda: nums3)))
_l_(22288)