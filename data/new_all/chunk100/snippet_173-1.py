# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def concatenate_lists(l1, l2, l3):
    _l_(103469)

    aux = [_n_(103460, "i", lambda: i) + _n_(103461, "j", lambda: j) + _n_(103462, "k", lambda: k) for i, j, k in _c_(103467, _n_(103463, "zip", lambda: zip), _n_(103464, "l1", lambda: l1), _n_(103465, "l2", lambda: l2), _n_(103466, "l3", lambda: l3))]
    _l_(103468)
    return aux
l1 = ['0', '1', '2', '3', '4']
_l_(103470)
l2 = ['red', 'green', 'black', 'blue', 'white']
_l_(103471)
_c_(103473, _n_(103472, "print", lambda: print), 'Original lists:')
_l_(103474)
_c_(103477, _n_(103475, "print", lambda: print), _n_(103476, "l1", lambda: l1))
_l_(103478)
_c_(103481, _n_(103479, "print", lambda: print), _n_(103480, "l2", lambda: l2))
_l_(103482)
_c_(103485, _n_(103483, "print", lambda: print), _n_(103484, "l3", lambda: l3))
_l_(103486)
_c_(103488, _n_(103487, "print", lambda: print), '\nConcatenate element-wise three said lists:')
_l_(103489)
_c_(103496, _n_(103490, "print", lambda: print), _c_(103495, _n_(103491, "concatenate_lists", lambda: concatenate_lists), _n_(103492, "l1", lambda: l1), _n_(103493, "l2", lambda: l2), _n_(103494, "l3", lambda: l3)))
_l_(103497)