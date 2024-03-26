# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def concatenate_lists(l1, l2, l3):
    _l_(103507)

    aux = [_n_(103498, "i", lambda: i) + _n_(103499, "j", lambda: j) + _n_(103500, "k", lambda: k) for i, j, k in _c_(103505, _n_(103501, "zip", lambda: zip), _n_(103502, "l1", lambda: l1), _n_(103503, "l2", lambda: l2), _n_(103504, "l3", lambda: l3))]
    _l_(103506)
    return aux
l1 = ['0', '1', '2', '3', '4']
_l_(103508)
l3 = ['100', '200', '300', '400', '500']
_l_(103509)
_c_(103511, _n_(103510, "print", lambda: print), 'Original lists:')
_l_(103512)
_c_(103515, _n_(103513, "print", lambda: print), _n_(103514, "l1", lambda: l1))
_l_(103516)
_c_(103519, _n_(103517, "print", lambda: print), _n_(103518, "l2", lambda: l2))
_l_(103520)
_c_(103523, _n_(103521, "print", lambda: print), _n_(103522, "l3", lambda: l3))
_l_(103524)
_c_(103526, _n_(103525, "print", lambda: print), '\nConcatenate element-wise three said lists:')
_l_(103527)
_c_(103534, _n_(103528, "print", lambda: print), _c_(103533, _n_(103529, "concatenate_lists", lambda: concatenate_lists), _n_(103530, "l1", lambda: l1), _n_(103531, "l2", lambda: l2), _n_(103532, "l3", lambda: l3)))
_l_(103535)