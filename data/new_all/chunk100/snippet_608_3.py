# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_diff_len_lists(list1, list2, list3, list4):
    _l_(63934)

    result = []
    _l_(63870)
    l1 = _c_(63873, _n_(63871, "len", lambda: len), _n_(63872, "list1", lambda: list1))
    _l_(63874)
    l2 = _c_(63877, _n_(63875, "len", lambda: len), _n_(63876, "list2", lambda: list2))
    _l_(63878)
    l3 = _c_(63881, _n_(63879, "len", lambda: len), _n_(63880, "list3", lambda: list3))
    _l_(63882)
    l4 = _c_(63885, _n_(63883, "len", lambda: len), _n_(63884, "list4", lambda: list4))
    _l_(63886)
    for i in _c_(63894, _n_(63887, "range", lambda: range), _c_(63893, _n_(63888, "max", lambda: max), _n_(63889, "l1", lambda: l1), _n_(63890, "l2", lambda: l2), _n_(63891, "l3", lambda: l3), _n_(63892, "l4", lambda: l4))):
        _l_(63931)

        if _n_(63895, "i", lambda: i) < _n_(63896, "l1", lambda: l1):
            _l_(63903)

            _c_(63901, _a_(63898, _n_(63897, "result", lambda: result), "append"), _n_(63899, "list1", lambda: list1)[_n_(63900, "i", lambda: i)])
            _l_(63902)
        if _n_(63904, "i", lambda: i) < _n_(63905, "l2", lambda: l2):
            _l_(63912)

            _c_(63910, _a_(63907, _n_(63906, "result", lambda: result), "append"), _n_(63908, "list2", lambda: list2)[_n_(63909, "i", lambda: i)])
            _l_(63911)
        if _n_(63913, "i", lambda: i) < _n_(63914, "l3", lambda: l3):
            _l_(63921)

            _c_(63919, _a_(63916, _n_(63915, "result", lambda: result), "append"), _n_(63917, "list3", lambda: list3)[_n_(63918, "i", lambda: i)])
            _l_(63920)
        if _n_(63922, "i", lambda: i) < _n_(63923, "l4", lambda: l4):
            _l_(63930)

            _c_(63928, _a_(63925, _n_(63924, "result", lambda: result), "append"), _n_(63926, "list4", lambda: list4)[_n_(63927, "i", lambda: i)])
            _l_(63929)
    aux = _n_(63932, "result", lambda: result)
    _l_(63933)
    return aux
nums1 = [2, 4, 7, 0, 5, 8]
_l_(63935)
nums2 = [2, 5, 8]
_l_(63936)
nums3 = [0, 1]
_l_(63937)
_c_(63939, _n_(63938, "print", lambda: print), '\nOriginal lists:')
_l_(63940)
_c_(63943, _n_(63941, "print", lambda: print), _n_(63942, "nums1", lambda: nums1))
_l_(63944)
_c_(63947, _n_(63945, "print", lambda: print), _n_(63946, "nums2", lambda: nums2))
_l_(63948)
_c_(63951, _n_(63949, "print", lambda: print), _n_(63950, "nums3", lambda: nums3))
_l_(63952)
_c_(63955, _n_(63953, "print", lambda: print), _n_(63954, "nums4", lambda: nums4))
_l_(63956)
_c_(63958, _n_(63957, "print", lambda: print), '\nInterleave said lists of different lengths:')
_l_(63959)
_c_(63967, _n_(63960, "print", lambda: print), _c_(63966, _n_(63961, "interleave_diff_len_lists", lambda: interleave_diff_len_lists), _n_(63962, "nums1", lambda: nums1), _n_(63963, "nums2", lambda: nums2), _n_(63964, "nums3", lambda: nums3), _n_(63965, "nums4", lambda: nums4)))
_l_(63968)