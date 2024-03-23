# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def add_val_to_list(lst, add_val):
    _l_(22415)

    result = _n_(22411, "lst", lambda: lst)
    _l_(22412)
    aux = _n_(22413, "result", lambda: result)
    _l_(22414)
    return aux
nums = [3, 8, 9, 4, 5, 0, 5, 0, 3]
_l_(22416)
_c_(22418, _n_(22417, "print", lambda: print), 'Original lists:')
_l_(22419)
_c_(22422, _n_(22420, "print", lambda: print), _n_(22421, "nums", lambda: nums))
_l_(22423)
add_val = 3
_l_(22424)
_c_(22427, _n_(22425, "print", lambda: print), '\nAdd', _n_(22426, "add_val", lambda: add_val), 'to each element in the said list:')
_l_(22428)
_c_(22434, _n_(22429, "print", lambda: print), _c_(22433, _n_(22430, "add_val_to_list", lambda: add_val_to_list), _n_(22431, "nums", lambda: nums), _n_(22432, "add_val", lambda: add_val)))
_l_(22435)
nums = [3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
_l_(22436)
_c_(22438, _n_(22437, "print", lambda: print), '\nOriginal lists:')
_l_(22439)
_c_(22442, _n_(22440, "print", lambda: print), _n_(22441, "nums", lambda: nums))
_l_(22443)
add_val = 0.51
_l_(22444)
_c_(22447, _n_(22445, "print", lambda: print), '\nAdd', _n_(22446, "add_val", lambda: add_val), 'to each element in the said list:')
_l_(22448)
_c_(22454, _n_(22449, "print", lambda: print), _c_(22453, _n_(22450, "add_val_to_list", lambda: add_val_to_list), _n_(22451, "nums", lambda: nums), _n_(22452, "add_val", lambda: add_val)))
_l_(22455)