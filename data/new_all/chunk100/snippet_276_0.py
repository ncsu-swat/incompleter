# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def extract_index_ele(l1, l2, l3):
    _l_(22213)

    result = []
    _l_(22195)
    for (m, n, o) in _c_(22200, _n_(22196, "zip", lambda: zip), _n_(22197, "l1", lambda: l1), _n_(22198, "l2", lambda: l2), _n_(22199, "l3", lambda: l3)):
        _l_(22210)

        if _n_(22201, "m", lambda: m) == _n_(22202, "n", lambda: n) == _n_(22203, "o", lambda: o):
            _l_(22209)

            _c_(22207, _a_(22205, _n_(22204, "result", lambda: result), "append"), _n_(22206, "m", lambda: m))
            _l_(22208)
    aux = _n_(22211, "result", lambda: result)
    _l_(22212)
    return aux
nums2 = [0, 1, 2, 3, 4, 5, 7]
_l_(22214)
nums3 = [0, 1, 2, 3, 4, 5, 7]
_l_(22215)
_c_(22217, _n_(22216, "print", lambda: print), 'Original lists:')
_l_(22218)
_c_(22221, _n_(22219, "print", lambda: print), _n_(22220, "nums1", lambda: nums1))
_l_(22222)
_c_(22225, _n_(22223, "print", lambda: print), _n_(22224, "nums2", lambda: nums2))
_l_(22226)
_c_(22229, _n_(22227, "print", lambda: print), _n_(22228, "nums3", lambda: nums3))
_l_(22230)
_c_(22232, _n_(22231, "print", lambda: print), '\nCommon index elements of the said lists:')
_l_(22233)
_c_(22240, _n_(22234, "print", lambda: print), _c_(22239, _n_(22235, "extract_index_ele", lambda: extract_index_ele), _n_(22236, "nums1", lambda: nums1), _n_(22237, "nums2", lambda: nums2), _n_(22238, "nums3", lambda: nums3)))
_l_(22241)