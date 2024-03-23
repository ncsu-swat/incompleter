# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def add_val_to_list(lst, add_val):
    _l_(22655)

    result = _n_(22647, "lst", lambda: lst)
    _l_(22648)
    result = [_n_(22649, "x", lambda: x) + _n_(22650, "add_val", lambda: add_val) for x in _n_(22651, "result", lambda: result)]
    _l_(22652)
    aux = _n_(22653, "result", lambda: result)
    _l_(22654)
    return aux
nums = [3, 8, 9, 4, 5, 0, 5, 0, 3]
_l_(22656)
_c_(22658, _n_(22657, "print", lambda: print), 'Original lists:')
_l_(22659)
_c_(22662, _n_(22660, "print", lambda: print), _n_(22661, "nums", lambda: nums))
_l_(22663)
_c_(22666, _n_(22664, "print", lambda: print), '\nAdd', _n_(22665, "add_val", lambda: add_val), 'to each element in the said list:')
_l_(22667)
_c_(22673, _n_(22668, "print", lambda: print), _c_(22672, _n_(22669, "add_val_to_list", lambda: add_val_to_list), _n_(22670, "nums", lambda: nums), _n_(22671, "add_val", lambda: add_val)))
_l_(22674)
nums = [3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
_l_(22675)
_c_(22677, _n_(22676, "print", lambda: print), '\nOriginal lists:')
_l_(22678)
_c_(22681, _n_(22679, "print", lambda: print), _n_(22680, "nums", lambda: nums))
_l_(22682)
add_val = 0.51
_l_(22683)
_c_(22686, _n_(22684, "print", lambda: print), '\nAdd', _n_(22685, "add_val", lambda: add_val), 'to each element in the said list:')
_l_(22687)
_c_(22693, _n_(22688, "print", lambda: print), _c_(22692, _n_(22689, "add_val_to_list", lambda: add_val_to_list), _n_(22690, "nums", lambda: nums), _n_(22691, "add_val", lambda: add_val)))
_l_(22694)