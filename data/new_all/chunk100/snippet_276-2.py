# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def extract_index_ele(l1, l2, l3):
    _l_(108213)

    result = []
    _l_(108195)
    for m, n, o in _c_(108200, _n_(108196, "zip", lambda: zip), _n_(108197, "l1", lambda: l1), _n_(108198, "l2", lambda: l2), _n_(108199, "l3", lambda: l3)):
        _l_(108210)

        if _n_(108201, "m", lambda: m) == _n_(108202, "n", lambda: n) == _n_(108203, "o", lambda: o):
            _l_(108209)

            _c_(108207, _a_(108205, _n_(108204, "result", lambda: result), "append"), _n_(108206, "m", lambda: m))
            _l_(108208)
    aux = _n_(108211, "result", lambda: result)
    _l_(108212)
    return aux
nums1 = [1, 1, 3, 4, 5, 6, 7]
_l_(108214)
nums2 = [0, 1, 2, 3, 4, 5, 7]
_l_(108215)
_c_(108217, _n_(108216, "print", lambda: print), 'Original lists:')
_l_(108218)
_c_(108221, _n_(108219, "print", lambda: print), _n_(108220, "nums1", lambda: nums1))
_l_(108222)
_c_(108225, _n_(108223, "print", lambda: print), _n_(108224, "nums2", lambda: nums2))
_l_(108226)
_c_(108229, _n_(108227, "print", lambda: print), _n_(108228, "nums3", lambda: nums3))
_l_(108230)
_c_(108232, _n_(108231, "print", lambda: print), '\nCommon index elements of the said lists:')
_l_(108233)
_c_(108240, _n_(108234, "print", lambda: print), _c_(108239, _n_(108235, "extract_index_ele", lambda: extract_index_ele), _n_(108236, "nums1", lambda: nums1), _n_(108237, "nums2", lambda: nums2), _n_(108238, "nums3", lambda: nums3)))
_l_(108241)