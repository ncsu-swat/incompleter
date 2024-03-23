# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_multiple_lists(list1, list2, list3):
    _l_(30336)

    result = [_n_(30326, "el", lambda: el) for pair in _c_(30331, _n_(30327, "zip", lambda: zip), _n_(30328, "list1", lambda: list1), _n_(30329, "list2", lambda: list2), _n_(30330, "list3", lambda: list3)) for el in _n_(30332, "pair", lambda: pair)]
    _l_(30333)
    aux = _n_(30334, "result", lambda: result)
    _l_(30335)
    return aux
list1 = [1, 2, 3, 4, 5, 6, 7]
_l_(30337)
list2 = [10, 20, 30, 40, 50, 60, 70]
_l_(30338)
_c_(30340, _n_(30339, "print", lambda: print), 'Original list:')
_l_(30341)
_c_(30344, _n_(30342, "print", lambda: print), 'list1:', _n_(30343, "list1", lambda: list1))
_l_(30345)
_c_(30348, _n_(30346, "print", lambda: print), 'list2:', _n_(30347, "list2", lambda: list2))
_l_(30349)
_c_(30352, _n_(30350, "print", lambda: print), 'list3:', _n_(30351, "list3", lambda: list3))
_l_(30353)
_c_(30355, _n_(30354, "print", lambda: print), '\nInterleave multiple lists:')
_l_(30356)
_c_(30363, _n_(30357, "print", lambda: print), _c_(30362, _n_(30358, "interleave_multiple_lists", lambda: interleave_multiple_lists), _n_(30359, "list1", lambda: list1), _n_(30360, "list2", lambda: list2), _n_(30361, "list3", lambda: list3)))
_l_(30364)