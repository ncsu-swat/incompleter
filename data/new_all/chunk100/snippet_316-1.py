# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_multiple_lists(list1, list2, list3):
    _l_(110261)

    result = [_n_(110251, "el", lambda: el) for pair in _c_(110256, _n_(110252, "zip", lambda: zip), _n_(110253, "list1", lambda: list1), _n_(110254, "list2", lambda: list2), _n_(110255, "list3", lambda: list3)) for el in _n_(110257, "pair", lambda: pair)]
    _l_(110258)
    aux = _n_(110259, "result", lambda: result)
    _l_(110260)
    return aux
list1 = [1, 2, 3, 4, 5, 6, 7]
_l_(110262)
list3 = [100, 200, 300, 400, 500, 600, 700]
_l_(110263)
_c_(110265, _n_(110264, "print", lambda: print), 'Original list:')
_l_(110266)
_c_(110269, _n_(110267, "print", lambda: print), 'list1:', _n_(110268, "list1", lambda: list1))
_l_(110270)
_c_(110273, _n_(110271, "print", lambda: print), 'list2:', _n_(110272, "list2", lambda: list2))
_l_(110274)
_c_(110277, _n_(110275, "print", lambda: print), 'list3:', _n_(110276, "list3", lambda: list3))
_l_(110278)
_c_(110280, _n_(110279, "print", lambda: print), '\nInterleave multiple lists:')
_l_(110281)
_c_(110288, _n_(110282, "print", lambda: print), _c_(110287, _n_(110283, "interleave_multiple_lists", lambda: interleave_multiple_lists), _n_(110284, "list1", lambda: list1), _n_(110285, "list2", lambda: list2), _n_(110286, "list3", lambda: list3)))
_l_(110289)