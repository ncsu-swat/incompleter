# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def extract_index_ele(l1, l2, l3):
    _l_(108119)

    result = []
    _l_(108101)
    for m, n, o in _c_(108106, _n_(108102, "zip", lambda: zip), _n_(108103, "l1", lambda: l1), _n_(108104, "l2", lambda: l2), _n_(108105, "l3", lambda: l3)):
        _l_(108116)

        if _n_(108107, "m", lambda: m) == _n_(108108, "n", lambda: n) == _n_(108109, "o", lambda: o):
            _l_(108115)

            _c_(108113, _a_(108111, _n_(108110, "result", lambda: result), "append"), _n_(108112, "m", lambda: m))
            _l_(108114)
    aux = _n_(108117, "result", lambda: result)
    _l_(108118)
    return aux
nums2 = [0, 1, 2, 3, 4, 5, 7]
_l_(108120)
nums3 = [0, 1, 2, 3, 4, 5, 7]
_l_(108121)
_c_(108123, _n_(108122, "print", lambda: print), 'Original lists:')
_l_(108124)
_c_(108127, _n_(108125, "print", lambda: print), _n_(108126, "nums1", lambda: nums1))
_l_(108128)
_c_(108131, _n_(108129, "print", lambda: print), _n_(108130, "nums2", lambda: nums2))
_l_(108132)
_c_(108135, _n_(108133, "print", lambda: print), _n_(108134, "nums3", lambda: nums3))
_l_(108136)
_c_(108138, _n_(108137, "print", lambda: print), '\nCommon index elements of the said lists:')
_l_(108139)
_c_(108146, _n_(108140, "print", lambda: print), _c_(108145, _n_(108141, "extract_index_ele", lambda: extract_index_ele), _n_(108142, "nums1", lambda: nums1), _n_(108143, "nums2", lambda: nums2), _n_(108144, "nums3", lambda: nums3)))
_l_(108147)