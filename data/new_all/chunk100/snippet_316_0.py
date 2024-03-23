# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_multiple_lists(list1, list2, list3):
    _l_(30258)

    result = [_n_(30248, "el", lambda: el) for pair in _c_(30253, _n_(30249, "zip", lambda: zip), _n_(30250, "list1", lambda: list1), _n_(30251, "list2", lambda: list2), _n_(30252, "list3", lambda: list3)) for el in _n_(30254, "pair", lambda: pair)]
    _l_(30255)
    aux = _n_(30256, "result", lambda: result)
    _l_(30257)
    return aux
list1 = [1, 2, 3, 4, 5, 6, 7]
_l_(30259)
list3 = [100, 200, 300, 400, 500, 600, 700]
_l_(30260)
_c_(30262, _n_(30261, "print", lambda: print), 'Original list:')
_l_(30263)
_c_(30266, _n_(30264, "print", lambda: print), 'list1:', _n_(30265, "list1", lambda: list1))
_l_(30267)
_c_(30270, _n_(30268, "print", lambda: print), 'list2:', _n_(30269, "list2", lambda: list2))
_l_(30271)
_c_(30274, _n_(30272, "print", lambda: print), 'list3:', _n_(30273, "list3", lambda: list3))
_l_(30275)
_c_(30277, _n_(30276, "print", lambda: print), '\nInterleave multiple lists:')
_l_(30278)
_c_(30285, _n_(30279, "print", lambda: print), _c_(30284, _n_(30280, "interleave_multiple_lists", lambda: interleave_multiple_lists), _n_(30281, "list1", lambda: list1), _n_(30282, "list2", lambda: list2), _n_(30283, "list3", lambda: list3)))
_l_(30286)