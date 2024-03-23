# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(16938)

except ImportError:
    pass

def interleave_multiple_lists(list1, list2, list3):
    _l_(16952)

    result = _c_(16948, _n_(16939, "list", lambda: list), _c_(16947, _a_(16941, _n_(16940, "itertools", lambda: itertools), "chain"), *_c_(16946, _n_(16942, "zip", lambda: zip), _n_(16943, "list1", lambda: list1), _n_(16944, "list2", lambda: list2), _n_(16945, "list3", lambda: list3))))
    _l_(16949)
    aux = _n_(16950, "result", lambda: result)
    _l_(16951)
    return aux
list1 = [100, 200, 300, 400, 500, 600, 700]
_l_(16953)
list3 = [1, 2, 3, 4, 5, 6, 7]
_l_(16954)
_c_(16956, _n_(16955, "print", lambda: print), 'Original list:')
_l_(16957)
_c_(16960, _n_(16958, "print", lambda: print), 'list1:', _n_(16959, "list1", lambda: list1))
_l_(16961)
_c_(16964, _n_(16962, "print", lambda: print), 'list2:', _n_(16963, "list2", lambda: list2))
_l_(16965)
_c_(16968, _n_(16966, "print", lambda: print), 'list3:', _n_(16967, "list3", lambda: list3))
_l_(16969)
_c_(16971, _n_(16970, "print", lambda: print), '\nInterleave multiple lists:')
_l_(16972)
_c_(16979, _n_(16973, "print", lambda: print), _c_(16978, _n_(16974, "interleave_multiple_lists", lambda: interleave_multiple_lists), _n_(16975, "list1", lambda: list1), _n_(16976, "list2", lambda: list2), _n_(16977, "list3", lambda: list3)))
_l_(16980)