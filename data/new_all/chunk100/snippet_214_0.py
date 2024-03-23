# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(16850)

except ImportError:
    pass

def interleave_multiple_lists(list1, list2, list3):
    _l_(16864)

    result = _c_(16860, _n_(16851, "list", lambda: list), _c_(16859, _a_(16853, _n_(16852, "itertools", lambda: itertools), "chain"), *_c_(16858, _n_(16854, "zip", lambda: zip), _n_(16855, "list1", lambda: list1), _n_(16856, "list2", lambda: list2), _n_(16857, "list3", lambda: list3))))
    _l_(16861)
    aux = _n_(16862, "result", lambda: result)
    _l_(16863)
    return aux
list2 = [10, 20, 30, 40, 50, 60, 70]
_l_(16865)
list3 = [1, 2, 3, 4, 5, 6, 7]
_l_(16866)
_c_(16868, _n_(16867, "print", lambda: print), 'Original list:')
_l_(16869)
_c_(16872, _n_(16870, "print", lambda: print), 'list1:', _n_(16871, "list1", lambda: list1))
_l_(16873)
_c_(16876, _n_(16874, "print", lambda: print), 'list2:', _n_(16875, "list2", lambda: list2))
_l_(16877)
_c_(16880, _n_(16878, "print", lambda: print), 'list3:', _n_(16879, "list3", lambda: list3))
_l_(16881)
_c_(16883, _n_(16882, "print", lambda: print), '\nInterleave multiple lists:')
_l_(16884)
_c_(16891, _n_(16885, "print", lambda: print), _c_(16890, _n_(16886, "interleave_multiple_lists", lambda: interleave_multiple_lists), _n_(16887, "list1", lambda: list1), _n_(16888, "list2", lambda: list2), _n_(16889, "list3", lambda: list3)))
_l_(16892)