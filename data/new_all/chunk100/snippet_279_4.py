# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def add_val_to_list(lst, add_val):
    _l_(22607)

    result = _n_(22599, "lst", lambda: lst)
    _l_(22600)
    result = [_n_(22601, "x", lambda: x) + _n_(22602, "add_val", lambda: add_val) for x in _n_(22603, "result", lambda: result)]
    _l_(22604)
    aux = _n_(22605, "result", lambda: result)
    _l_(22606)
    return aux
nums = [3, 8, 9, 4, 5, 0, 5, 0, 3]
_l_(22608)
_c_(22610, _n_(22609, "print", lambda: print), 'Original lists:')
_l_(22611)
_c_(22614, _n_(22612, "print", lambda: print), _n_(22613, "nums", lambda: nums))
_l_(22615)
add_val = 3
_l_(22616)
_c_(22619, _n_(22617, "print", lambda: print), '\nAdd', _n_(22618, "add_val", lambda: add_val), 'to each element in the said list:')
_l_(22620)
_c_(22626, _n_(22621, "print", lambda: print), _c_(22625, _n_(22622, "add_val_to_list", lambda: add_val_to_list), _n_(22623, "nums", lambda: nums), _n_(22624, "add_val", lambda: add_val)))
_l_(22627)
_c_(22629, _n_(22628, "print", lambda: print), '\nOriginal lists:')
_l_(22630)
_c_(22633, _n_(22631, "print", lambda: print), _n_(22632, "nums", lambda: nums))
_l_(22634)
add_val = 0.51
_l_(22635)
_c_(22638, _n_(22636, "print", lambda: print), '\nAdd', _n_(22637, "add_val", lambda: add_val), 'to each element in the said list:')
_l_(22639)
_c_(22645, _n_(22640, "print", lambda: print), _c_(22644, _n_(22641, "add_val_to_list", lambda: add_val_to_list), _n_(22642, "nums", lambda: nums), _n_(22643, "add_val", lambda: add_val)))
_l_(22646)