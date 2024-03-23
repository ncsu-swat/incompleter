# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unique_product(list_data):
    _l_(72804)

    temp = _c_(72795, _n_(72791, "list", lambda: list), _c_(72794, _n_(72792, "set", lambda: set), _n_(72793, "list_data", lambda: list_data)))
    _l_(72796)
    p = 1
    _l_(72797)
    for i in _n_(72798, "temp", lambda: temp):
        _l_(72801)

        p *= _n_(72799, "i", lambda: i)
        _l_(72800)
    aux = _n_(72802, "p", lambda: p)
    _l_(72803)
    return aux
_c_(72807, _n_(72805, "print", lambda: print), 'Original List : ', _n_(72806, "nums", lambda: nums))
_l_(72808)
_c_(72813, _n_(72809, "print", lambda: print), 'Product of the unique numbers of the said list: ', _c_(72812, _n_(72810, "unique_product", lambda: unique_product), _n_(72811, "nums", lambda: nums)))
_l_(72814)