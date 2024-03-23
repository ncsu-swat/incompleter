# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(16894)

except ImportError:
    pass

def interleave_multiple_lists(list1, list2, list3):
    _l_(16908)

    result = _c_(16904, _n_(16895, "list", lambda: list), _c_(16903, _a_(16897, _n_(16896, "itertools", lambda: itertools), "chain"), *_c_(16902, _n_(16898, "zip", lambda: zip), _n_(16899, "list1", lambda: list1), _n_(16900, "list2", lambda: list2), _n_(16901, "list3", lambda: list3))))
    _l_(16905)
    aux = _n_(16906, "result", lambda: result)
    _l_(16907)
    return aux
list1 = [100, 200, 300, 400, 500, 600, 700]
_l_(16909)
list2 = [10, 20, 30, 40, 50, 60, 70]
_l_(16910)
_c_(16912, _n_(16911, "print", lambda: print), 'Original list:')
_l_(16913)
_c_(16916, _n_(16914, "print", lambda: print), 'list1:', _n_(16915, "list1", lambda: list1))
_l_(16917)
_c_(16920, _n_(16918, "print", lambda: print), 'list2:', _n_(16919, "list2", lambda: list2))
_l_(16921)
_c_(16924, _n_(16922, "print", lambda: print), 'list3:', _n_(16923, "list3", lambda: list3))
_l_(16925)
_c_(16927, _n_(16926, "print", lambda: print), '\nInterleave multiple lists:')
_l_(16928)
_c_(16935, _n_(16929, "print", lambda: print), _c_(16934, _n_(16930, "interleave_multiple_lists", lambda: interleave_multiple_lists), _n_(16931, "list1", lambda: list1), _n_(16932, "list2", lambda: list2), _n_(16933, "list3", lambda: list3)))
_l_(16936)