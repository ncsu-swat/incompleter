# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def concatenate_lists(l1, l2, l3):
    _l_(12330)

    aux = [_n_(12321, "i", lambda: i) + _n_(12322, "j", lambda: j) + _n_(12323, "k", lambda: k) for (i, j, k) in _c_(12328, _n_(12324, "zip", lambda: zip), _n_(12325, "l1", lambda: l1), _n_(12326, "l2", lambda: l2), _n_(12327, "l3", lambda: l3))]
    _l_(12329)
    return aux
l1 = ['0', '1', '2', '3', '4']
_l_(12331)
l2 = ['red', 'green', 'black', 'blue', 'white']
_l_(12332)
_c_(12334, _n_(12333, "print", lambda: print), 'Original lists:')
_l_(12335)
_c_(12338, _n_(12336, "print", lambda: print), _n_(12337, "l1", lambda: l1))
_l_(12339)
_c_(12342, _n_(12340, "print", lambda: print), _n_(12341, "l2", lambda: l2))
_l_(12343)
_c_(12346, _n_(12344, "print", lambda: print), _n_(12345, "l3", lambda: l3))
_l_(12347)
_c_(12349, _n_(12348, "print", lambda: print), '\nConcatenate element-wise three said lists:')
_l_(12350)
_c_(12357, _n_(12351, "print", lambda: print), _c_(12356, _n_(12352, "concatenate_lists", lambda: concatenate_lists), _n_(12353, "l1", lambda: l1), _n_(12354, "l2", lambda: l2), _n_(12355, "l3", lambda: l3)))
_l_(12358)