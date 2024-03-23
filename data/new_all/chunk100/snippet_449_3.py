# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst, value):
    _l_(48067)

    result = [_n_(48058, "i", lambda: i) for (i, val) in _c_(48061, _n_(48059, "enumerate", lambda: enumerate), _n_(48060, "lst", lambda: lst)) if _n_(48062, "val", lambda: val) > _n_(48063, "value", lambda: value)]
    _l_(48064)
    aux = _n_(48065, "result", lambda: result)
    _l_(48066)
    return aux
nums = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
_l_(48068)
_c_(48070, _n_(48069, "print", lambda: print), '\nOriginal list:')
_l_(48071)
_c_(48074, _n_(48072, "print", lambda: print), _n_(48073, "nums", lambda: nums))
_l_(48075)
_c_(48078, _n_(48076, "print", lambda: print), 'Indices of elements of the said list, greater than', _n_(48077, "val", lambda: val))
_l_(48079)
_c_(48085, _n_(48080, "print", lambda: print), _c_(48084, _n_(48081, "test", lambda: test), _n_(48082, "nums", lambda: nums), _n_(48083, "val", lambda: val)))
_l_(48086)
nums = [1234, 1522, 1984, 19372, 1000, 2342, 7626]
_l_(48087)
_c_(48089, _n_(48088, "print", lambda: print), '\nOriginal list:')
_l_(48090)
_c_(48093, _n_(48091, "print", lambda: print), _n_(48092, "nums", lambda: nums))
_l_(48094)
val = 20000
_l_(48095)
_c_(48098, _n_(48096, "print", lambda: print), 'Indices of elements of the said list, greater than', _n_(48097, "val", lambda: val))
_l_(48099)
_c_(48105, _n_(48100, "print", lambda: print), _c_(48104, _n_(48101, "test", lambda: test), _n_(48102, "nums", lambda: nums), _n_(48103, "val", lambda: val)))
_l_(48106)