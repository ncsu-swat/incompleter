# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst, value):
    _l_(47969)

    result = [_n_(47960, "i", lambda: i) for (i, val) in _c_(47963, _n_(47961, "enumerate", lambda: enumerate), _n_(47962, "lst", lambda: lst)) if _n_(47964, "val", lambda: val) > _n_(47965, "value", lambda: value)]
    _l_(47966)
    aux = _n_(47967, "result", lambda: result)
    _l_(47968)
    return aux
_c_(47971, _n_(47970, "print", lambda: print), '\nOriginal list:')
_l_(47972)
_c_(47975, _n_(47973, "print", lambda: print), _n_(47974, "nums", lambda: nums))
_l_(47976)
val = 3000
_l_(47977)
_c_(47980, _n_(47978, "print", lambda: print), 'Indices of elements of the said list, greater than', _n_(47979, "val", lambda: val))
_l_(47981)
_c_(47987, _n_(47982, "print", lambda: print), _c_(47986, _n_(47983, "test", lambda: test), _n_(47984, "nums", lambda: nums), _n_(47985, "val", lambda: val)))
_l_(47988)
nums = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
_l_(47989)
_c_(47991, _n_(47990, "print", lambda: print), '\nOriginal list:')
_l_(47992)
_c_(47995, _n_(47993, "print", lambda: print), _n_(47994, "nums", lambda: nums))
_l_(47996)
val = 20000
_l_(47997)
_c_(48000, _n_(47998, "print", lambda: print), 'Indices of elements of the said list, greater than', _n_(47999, "val", lambda: val))
_l_(48001)
_c_(48007, _n_(48002, "print", lambda: print), _c_(48006, _n_(48003, "test", lambda: test), _n_(48004, "nums", lambda: nums), _n_(48005, "val", lambda: val)))
_l_(48008)