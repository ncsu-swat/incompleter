# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_multiple_lists(list1, list2, list3):
    _l_(110222)

    result = [_n_(110212, "el", lambda: el) for pair in _c_(110217, _n_(110213, "zip", lambda: zip), _n_(110214, "list1", lambda: list1), _n_(110215, "list2", lambda: list2), _n_(110216, "list3", lambda: list3)) for el in _n_(110218, "pair", lambda: pair)]
    _l_(110219)
    aux = _n_(110220, "result", lambda: result)
    _l_(110221)
    return aux
list1 = [1, 2, 3, 4, 5, 6, 7]
_l_(110223)
list2 = [10, 20, 30, 40, 50, 60, 70]
_l_(110224)
_c_(110226, _n_(110225, "print", lambda: print), 'Original list:')
_l_(110227)
_c_(110230, _n_(110228, "print", lambda: print), 'list1:', _n_(110229, "list1", lambda: list1))
_l_(110231)
_c_(110234, _n_(110232, "print", lambda: print), 'list2:', _n_(110233, "list2", lambda: list2))
_l_(110235)
_c_(110238, _n_(110236, "print", lambda: print), 'list3:', _n_(110237, "list3", lambda: list3))
_l_(110239)
_c_(110241, _n_(110240, "print", lambda: print), '\nInterleave multiple lists:')
_l_(110242)
_c_(110249, _n_(110243, "print", lambda: print), _c_(110248, _n_(110244, "interleave_multiple_lists", lambda: interleave_multiple_lists), _n_(110245, "list1", lambda: list1), _n_(110246, "list2", lambda: list2), _n_(110247, "list3", lambda: list3)))
_l_(110250)