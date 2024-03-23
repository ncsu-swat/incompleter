# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def add_val_to_list(lst, add_val):
    _l_(22559)

    result = _n_(22551, "lst", lambda: lst)
    _l_(22552)
    result = [_n_(22553, "x", lambda: x) + _n_(22554, "add_val", lambda: add_val) for x in _n_(22555, "result", lambda: result)]
    _l_(22556)
    aux = _n_(22557, "result", lambda: result)
    _l_(22558)
    return aux
nums = [3, 8, 9, 4, 5, 0, 5, 0, 3]
_l_(22560)
_c_(22562, _n_(22561, "print", lambda: print), 'Original lists:')
_l_(22563)
_c_(22566, _n_(22564, "print", lambda: print), _n_(22565, "nums", lambda: nums))
_l_(22567)
add_val = 3
_l_(22568)
_c_(22571, _n_(22569, "print", lambda: print), '\nAdd', _n_(22570, "add_val", lambda: add_val), 'to each element in the said list:')
_l_(22572)
_c_(22578, _n_(22573, "print", lambda: print), _c_(22577, _n_(22574, "add_val_to_list", lambda: add_val_to_list), _n_(22575, "nums", lambda: nums), _n_(22576, "add_val", lambda: add_val)))
_l_(22579)
nums = [3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
_l_(22580)
_c_(22582, _n_(22581, "print", lambda: print), '\nOriginal lists:')
_l_(22583)
_c_(22586, _n_(22584, "print", lambda: print), _n_(22585, "nums", lambda: nums))
_l_(22587)
_c_(22590, _n_(22588, "print", lambda: print), '\nAdd', _n_(22589, "add_val", lambda: add_val), 'to each element in the said list:')
_l_(22591)
_c_(22597, _n_(22592, "print", lambda: print), _c_(22596, _n_(22593, "add_val_to_list", lambda: add_val_to_list), _n_(22594, "nums", lambda: nums), _n_(22595, "add_val", lambda: add_val)))
_l_(22598)