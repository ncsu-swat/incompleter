# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst):
    _l_(15066)

    result = [_n_(15057, "x", lambda: x) + _n_(15058, "y", lambda: y) for (x, y) in _c_(15062, _n_(15059, "zip", lambda: zip), _n_(15060, "lst", lambda: lst)[::2], _n_(15061, "lst", lambda: lst)[1::2])]
    _l_(15063)
    aux = _n_(15064, "result", lambda: result)
    _l_(15065)
    return aux
_c_(15068, _n_(15067, "print", lambda: print), 'Original list:')
_l_(15069)
_c_(15072, _n_(15070, "print", lambda: print), _n_(15071, "nums", lambda: nums))
_l_(15073)
_c_(15075, _n_(15074, "print", lambda: print), '\nJoin adjacent members of a given list:')
_l_(15076)
_c_(15081, _n_(15077, "print", lambda: print), _c_(15080, _n_(15078, "test", lambda: test), _n_(15079, "nums", lambda: nums)))
_l_(15082)
nums = ['1', '2', '3']
_l_(15083)
_c_(15085, _n_(15084, "print", lambda: print), '\nOriginal list:')
_l_(15086)
_c_(15089, _n_(15087, "print", lambda: print), _n_(15088, "nums", lambda: nums))
_l_(15090)
_c_(15092, _n_(15091, "print", lambda: print), '\nJoin adjacent members of a given list:')
_l_(15093)
_c_(15098, _n_(15094, "print", lambda: print), _c_(15097, _n_(15095, "test", lambda: test), _n_(15096, "nums", lambda: nums)))
_l_(15099)