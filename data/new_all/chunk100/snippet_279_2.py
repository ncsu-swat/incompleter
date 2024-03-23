# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def add_val_to_list(lst, add_val):
    _l_(22511)

    result = _n_(22503, "lst", lambda: lst)
    _l_(22504)
    result = [_n_(22505, "x", lambda: x) + _n_(22506, "add_val", lambda: add_val) for x in _n_(22507, "result", lambda: result)]
    _l_(22508)
    aux = _n_(22509, "result", lambda: result)
    _l_(22510)
    return aux
_c_(22513, _n_(22512, "print", lambda: print), 'Original lists:')
_l_(22514)
_c_(22517, _n_(22515, "print", lambda: print), _n_(22516, "nums", lambda: nums))
_l_(22518)
add_val = 3
_l_(22519)
_c_(22522, _n_(22520, "print", lambda: print), '\nAdd', _n_(22521, "add_val", lambda: add_val), 'to each element in the said list:')
_l_(22523)
_c_(22529, _n_(22524, "print", lambda: print), _c_(22528, _n_(22525, "add_val_to_list", lambda: add_val_to_list), _n_(22526, "nums", lambda: nums), _n_(22527, "add_val", lambda: add_val)))
_l_(22530)
nums = [3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
_l_(22531)
_c_(22533, _n_(22532, "print", lambda: print), '\nOriginal lists:')
_l_(22534)
_c_(22537, _n_(22535, "print", lambda: print), _n_(22536, "nums", lambda: nums))
_l_(22538)
add_val = 0.51
_l_(22539)
_c_(22542, _n_(22540, "print", lambda: print), '\nAdd', _n_(22541, "add_val", lambda: add_val), 'to each element in the said list:')
_l_(22543)
_c_(22549, _n_(22544, "print", lambda: print), _c_(22548, _n_(22545, "add_val_to_list", lambda: add_val_to_list), _n_(22546, "nums", lambda: nums), _n_(22547, "add_val", lambda: add_val)))
_l_(22550)