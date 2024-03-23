# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def concatenate_lists(l1, l2, l3):
    _l_(12368)

    aux = [_n_(12359, "i", lambda: i) + _n_(12360, "j", lambda: j) + _n_(12361, "k", lambda: k) for (i, j, k) in _c_(12366, _n_(12362, "zip", lambda: zip), _n_(12363, "l1", lambda: l1), _n_(12364, "l2", lambda: l2), _n_(12365, "l3", lambda: l3))]
    _l_(12367)
    return aux
l1 = ['0', '1', '2', '3', '4']
_l_(12369)
l3 = ['100', '200', '300', '400', '500']
_l_(12370)
_c_(12372, _n_(12371, "print", lambda: print), 'Original lists:')
_l_(12373)
_c_(12376, _n_(12374, "print", lambda: print), _n_(12375, "l1", lambda: l1))
_l_(12377)
_c_(12380, _n_(12378, "print", lambda: print), _n_(12379, "l2", lambda: l2))
_l_(12381)
_c_(12384, _n_(12382, "print", lambda: print), _n_(12383, "l3", lambda: l3))
_l_(12385)
_c_(12387, _n_(12386, "print", lambda: print), '\nConcatenate element-wise three said lists:')
_l_(12388)
_c_(12395, _n_(12389, "print", lambda: print), _c_(12394, _n_(12390, "concatenate_lists", lambda: concatenate_lists), _n_(12391, "l1", lambda: l1), _n_(12392, "l2", lambda: l2), _n_(12393, "l3", lambda: l3)))
_l_(12396)