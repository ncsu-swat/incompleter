# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_kth_element(n_list, L):
    _l_(63558)

    aux = _n_(63553, "n_list", lambda: n_list)[:_n_(63554, "L", lambda: L) - 1] + _n_(63555, "n_list", lambda: n_list)[_n_(63556, "L", lambda: L):]
    _l_(63557)
    return aux
_c_(63560, _n_(63559, "print", lambda: print), 'Original list:')
_l_(63561)
_c_(63564, _n_(63562, "print", lambda: print), _n_(63563, "n_list", lambda: n_list))
_l_(63565)
kth_position = 3
_l_(63566)
result = _c_(63570, _n_(63567, "remove_kth_element", lambda: remove_kth_element), _n_(63568, "n_list", lambda: n_list), _n_(63569, "kth_position", lambda: kth_position))
_l_(63571)
_c_(63573, _n_(63572, "print", lambda: print), '\nAfter removing an element at the kth position of the said list:')
_l_(63574)
_c_(63577, _n_(63575, "print", lambda: print), _n_(63576, "result", lambda: result))
_l_(63578)