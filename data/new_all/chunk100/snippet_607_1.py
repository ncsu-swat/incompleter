# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_kth_element(n_list, L):
    _l_(63532)

    aux = _n_(63527, "n_list", lambda: n_list)[:_n_(63528, "L", lambda: L) - 1] + _n_(63529, "n_list", lambda: n_list)[_n_(63530, "L", lambda: L):]
    _l_(63531)
    return aux
n_list = [1, 1, 2, 3, 4, 4, 5, 1]
_l_(63533)
_c_(63535, _n_(63534, "print", lambda: print), 'Original list:')
_l_(63536)
_c_(63539, _n_(63537, "print", lambda: print), _n_(63538, "n_list", lambda: n_list))
_l_(63540)
result = _c_(63544, _n_(63541, "remove_kth_element", lambda: remove_kth_element), _n_(63542, "n_list", lambda: n_list), _n_(63543, "kth_position", lambda: kth_position))
_l_(63545)
_c_(63547, _n_(63546, "print", lambda: print), '\nAfter removing an element at the kth position of the said list:')
_l_(63548)
_c_(63551, _n_(63549, "print", lambda: print), _n_(63550, "result", lambda: result))
_l_(63552)