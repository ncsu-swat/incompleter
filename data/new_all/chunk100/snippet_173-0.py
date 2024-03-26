# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def concatenate_lists(l1, l2, l3):
    _l_(103431)

    aux = [_n_(103422, "i", lambda: i) + _n_(103423, "j", lambda: j) + _n_(103424, "k", lambda: k) for i, j, k in _c_(103429, _n_(103425, "zip", lambda: zip), _n_(103426, "l1", lambda: l1), _n_(103427, "l2", lambda: l2), _n_(103428, "l3", lambda: l3))]
    _l_(103430)
    return aux
l2 = ['red', 'green', 'black', 'blue', 'white']
_l_(103432)
l3 = ['100', '200', '300', '400', '500']
_l_(103433)
_c_(103435, _n_(103434, "print", lambda: print), 'Original lists:')
_l_(103436)
_c_(103439, _n_(103437, "print", lambda: print), _n_(103438, "l1", lambda: l1))
_l_(103440)
_c_(103443, _n_(103441, "print", lambda: print), _n_(103442, "l2", lambda: l2))
_l_(103444)
_c_(103447, _n_(103445, "print", lambda: print), _n_(103446, "l3", lambda: l3))
_l_(103448)
_c_(103450, _n_(103449, "print", lambda: print), '\nConcatenate element-wise three said lists:')
_l_(103451)
_c_(103458, _n_(103452, "print", lambda: print), _c_(103457, _n_(103453, "concatenate_lists", lambda: concatenate_lists), _n_(103454, "l1", lambda: l1), _n_(103455, "l2", lambda: l2), _n_(103456, "l3", lambda: l3)))
_l_(103459)