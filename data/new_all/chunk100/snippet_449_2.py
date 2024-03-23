# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst, value):
    _l_(48018)

    result = [_n_(48009, "i", lambda: i) for (i, val) in _c_(48012, _n_(48010, "enumerate", lambda: enumerate), _n_(48011, "lst", lambda: lst)) if _n_(48013, "val", lambda: val) > _n_(48014, "value", lambda: value)]
    _l_(48015)
    aux = _n_(48016, "result", lambda: result)
    _l_(48017)
    return aux
nums = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
_l_(48019)
_c_(48021, _n_(48020, "print", lambda: print), '\nOriginal list:')
_l_(48022)
_c_(48025, _n_(48023, "print", lambda: print), _n_(48024, "nums", lambda: nums))
_l_(48026)
val = 3000
_l_(48027)
_c_(48030, _n_(48028, "print", lambda: print), 'Indices of elements of the said list, greater than', _n_(48029, "val", lambda: val))
_l_(48031)
_c_(48037, _n_(48032, "print", lambda: print), _c_(48036, _n_(48033, "test", lambda: test), _n_(48034, "nums", lambda: nums), _n_(48035, "val", lambda: val)))
_l_(48038)
_c_(48040, _n_(48039, "print", lambda: print), '\nOriginal list:')
_l_(48041)
_c_(48044, _n_(48042, "print", lambda: print), _n_(48043, "nums", lambda: nums))
_l_(48045)
val = 20000
_l_(48046)
_c_(48049, _n_(48047, "print", lambda: print), 'Indices of elements of the said list, greater than', _n_(48048, "val", lambda: val))
_l_(48050)
_c_(48056, _n_(48051, "print", lambda: print), _c_(48055, _n_(48052, "test", lambda: test), _n_(48053, "nums", lambda: nums), _n_(48054, "val", lambda: val)))
_l_(48057)