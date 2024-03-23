# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unique_product(list_data):
    _l_(72827)

    temp = _c_(72819, _n_(72815, "list", lambda: list), _c_(72818, _n_(72816, "set", lambda: set), _n_(72817, "list_data", lambda: list_data)))
    _l_(72820)
    for i in _n_(72821, "temp", lambda: temp):
        _l_(72824)

        p *= _n_(72822, "i", lambda: i)
        _l_(72823)
    aux = _n_(72825, "p", lambda: p)
    _l_(72826)
    return aux
nums = [10, 20, 30, 40, 20, 50, 60, 40]
_l_(72828)
_c_(72831, _n_(72829, "print", lambda: print), 'Original List : ', _n_(72830, "nums", lambda: nums))
_l_(72832)
_c_(72837, _n_(72833, "print", lambda: print), 'Product of the unique numbers of the said list: ', _c_(72836, _n_(72834, "unique_product", lambda: unique_product), _n_(72835, "nums", lambda: nums)))
_l_(72838)