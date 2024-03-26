# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def extract_index_ele(l1, l2, l3):
    _l_(108166)

    result = []
    _l_(108148)
    for m, n, o in _c_(108153, _n_(108149, "zip", lambda: zip), _n_(108150, "l1", lambda: l1), _n_(108151, "l2", lambda: l2), _n_(108152, "l3", lambda: l3)):
        _l_(108163)

        if _n_(108154, "m", lambda: m) == _n_(108155, "n", lambda: n) == _n_(108156, "o", lambda: o):
            _l_(108162)

            _c_(108160, _a_(108158, _n_(108157, "result", lambda: result), "append"), _n_(108159, "m", lambda: m))
            _l_(108161)
    aux = _n_(108164, "result", lambda: result)
    _l_(108165)
    return aux
nums1 = [1, 1, 3, 4, 5, 6, 7]
_l_(108167)
nums3 = [0, 1, 2, 3, 4, 5, 7]
_l_(108168)
_c_(108170, _n_(108169, "print", lambda: print), 'Original lists:')
_l_(108171)
_c_(108174, _n_(108172, "print", lambda: print), _n_(108173, "nums1", lambda: nums1))
_l_(108175)
_c_(108178, _n_(108176, "print", lambda: print), _n_(108177, "nums2", lambda: nums2))
_l_(108179)
_c_(108182, _n_(108180, "print", lambda: print), _n_(108181, "nums3", lambda: nums3))
_l_(108183)
_c_(108185, _n_(108184, "print", lambda: print), '\nCommon index elements of the said lists:')
_l_(108186)
_c_(108193, _n_(108187, "print", lambda: print), _c_(108192, _n_(108188, "extract_index_ele", lambda: extract_index_ele), _n_(108189, "nums1", lambda: nums1), _n_(108190, "nums2", lambda: nums2), _n_(108191, "nums3", lambda: nums3)))
_l_(108194)