# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def add_val_to_list(lst, add_val):
    _l_(22462)

    result = [_n_(22456, "x", lambda: x) + _n_(22457, "add_val", lambda: add_val) for x in _n_(22458, "result", lambda: result)]
    _l_(22459)
    aux = _n_(22460, "result", lambda: result)
    _l_(22461)
    return aux
nums = [3, 8, 9, 4, 5, 0, 5, 0, 3]
_l_(22463)
_c_(22465, _n_(22464, "print", lambda: print), 'Original lists:')
_l_(22466)
_c_(22469, _n_(22467, "print", lambda: print), _n_(22468, "nums", lambda: nums))
_l_(22470)
add_val = 3
_l_(22471)
_c_(22474, _n_(22472, "print", lambda: print), '\nAdd', _n_(22473, "add_val", lambda: add_val), 'to each element in the said list:')
_l_(22475)
_c_(22481, _n_(22476, "print", lambda: print), _c_(22480, _n_(22477, "add_val_to_list", lambda: add_val_to_list), _n_(22478, "nums", lambda: nums), _n_(22479, "add_val", lambda: add_val)))
_l_(22482)
nums = [3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
_l_(22483)
_c_(22485, _n_(22484, "print", lambda: print), '\nOriginal lists:')
_l_(22486)
_c_(22489, _n_(22487, "print", lambda: print), _n_(22488, "nums", lambda: nums))
_l_(22490)
add_val = 0.51
_l_(22491)
_c_(22494, _n_(22492, "print", lambda: print), '\nAdd', _n_(22493, "add_val", lambda: add_val), 'to each element in the said list:')
_l_(22495)
_c_(22501, _n_(22496, "print", lambda: print), _c_(22500, _n_(22497, "add_val_to_list", lambda: add_val_to_list), _n_(22498, "nums", lambda: nums), _n_(22499, "add_val", lambda: add_val)))
_l_(22502)