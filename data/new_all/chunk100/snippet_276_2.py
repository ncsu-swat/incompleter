# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def extract_index_ele(l1, l2, l3):
    _l_(22307)

    result = []
    _l_(22289)
    for (m, n, o) in _c_(22294, _n_(22290, "zip", lambda: zip), _n_(22291, "l1", lambda: l1), _n_(22292, "l2", lambda: l2), _n_(22293, "l3", lambda: l3)):
        _l_(22304)

        if _n_(22295, "m", lambda: m) == _n_(22296, "n", lambda: n) == _n_(22297, "o", lambda: o):
            _l_(22303)

            _c_(22301, _a_(22299, _n_(22298, "result", lambda: result), "append"), _n_(22300, "m", lambda: m))
            _l_(22302)
    aux = _n_(22305, "result", lambda: result)
    _l_(22306)
    return aux
nums1 = [1, 1, 3, 4, 5, 6, 7]
_l_(22308)
nums2 = [0, 1, 2, 3, 4, 5, 7]
_l_(22309)
_c_(22311, _n_(22310, "print", lambda: print), 'Original lists:')
_l_(22312)
_c_(22315, _n_(22313, "print", lambda: print), _n_(22314, "nums1", lambda: nums1))
_l_(22316)
_c_(22319, _n_(22317, "print", lambda: print), _n_(22318, "nums2", lambda: nums2))
_l_(22320)
_c_(22323, _n_(22321, "print", lambda: print), _n_(22322, "nums3", lambda: nums3))
_l_(22324)
_c_(22326, _n_(22325, "print", lambda: print), '\nCommon index elements of the said lists:')
_l_(22327)
_c_(22334, _n_(22328, "print", lambda: print), _c_(22333, _n_(22329, "extract_index_ele", lambda: extract_index_ele), _n_(22330, "nums1", lambda: nums1), _n_(22331, "nums2", lambda: nums2), _n_(22332, "nums3", lambda: nums3)))
_l_(22335)