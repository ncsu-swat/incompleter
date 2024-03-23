# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def extract_index_ele(l1, l2, l3):
    _l_(22353)

    for (m, n, o) in _c_(22340, _n_(22336, "zip", lambda: zip), _n_(22337, "l1", lambda: l1), _n_(22338, "l2", lambda: l2), _n_(22339, "l3", lambda: l3)):
        _l_(22350)

        if _n_(22341, "m", lambda: m) == _n_(22342, "n", lambda: n) == _n_(22343, "o", lambda: o):
            _l_(22349)

            _c_(22347, _a_(22345, _n_(22344, "result", lambda: result), "append"), _n_(22346, "m", lambda: m))
            _l_(22348)
    aux = _n_(22351, "result", lambda: result)
    _l_(22352)
    return aux
nums1 = [1, 1, 3, 4, 5, 6, 7]
_l_(22354)
nums2 = [0, 1, 2, 3, 4, 5, 7]
_l_(22355)
nums3 = [0, 1, 2, 3, 4, 5, 7]
_l_(22356)
_c_(22358, _n_(22357, "print", lambda: print), 'Original lists:')
_l_(22359)
_c_(22362, _n_(22360, "print", lambda: print), _n_(22361, "nums1", lambda: nums1))
_l_(22363)
_c_(22366, _n_(22364, "print", lambda: print), _n_(22365, "nums2", lambda: nums2))
_l_(22367)
_c_(22370, _n_(22368, "print", lambda: print), _n_(22369, "nums3", lambda: nums3))
_l_(22371)
_c_(22373, _n_(22372, "print", lambda: print), '\nCommon index elements of the said lists:')
_l_(22374)
_c_(22381, _n_(22375, "print", lambda: print), _c_(22380, _n_(22376, "extract_index_ele", lambda: extract_index_ele), _n_(22377, "nums1", lambda: nums1), _n_(22378, "nums2", lambda: nums2), _n_(22379, "nums3", lambda: nums3)))
_l_(22382)