# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_kth_element(n_list, L):
    _l_(63510)

    aux = _n_(63505, "n_list", lambda: n_list)[:_n_(63506, "L", lambda: L) - 1] + _n_(63507, "n_list", lambda: n_list)[_n_(63508, "L", lambda: L):]
    _l_(63509)
    return aux
n_list = [1, 1, 2, 3, 4, 4, 5, 1]
_l_(63511)
_c_(63513, _n_(63512, "print", lambda: print), 'Original list:')
_l_(63514)
_c_(63517, _n_(63515, "print", lambda: print), _n_(63516, "n_list", lambda: n_list))
_l_(63518)
kth_position = 3
_l_(63519)
_c_(63521, _n_(63520, "print", lambda: print), '\nAfter removing an element at the kth position of the said list:')
_l_(63522)
_c_(63525, _n_(63523, "print", lambda: print), _n_(63524, "result", lambda: result))
_l_(63526)