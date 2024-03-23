# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(dictt):
    _l_(66081)

    result = [_n_(66070, "k", lambda: k) for (k, v) in _c_(66073, _a_(66072, _n_(66071, "dictt", lambda: dictt), "items")) if _c_(66076, _n_(66074, "len", lambda: len), _n_(66075, "v", lambda: v)) == _n_(66077, "min_value", lambda: min_value)]
    _l_(66078)
    aux = _n_(66079, "result", lambda: result)
    _l_(66080)
    return aux
dictt = {'V': [10, 12], 'VI': [10], 'VII': [10, 20, 30, 40], 'VIII': [20], 'IX': [10, 30, 50, 70], 'X': [80]}
_l_(66082)
_c_(66084, _n_(66083, "print", lambda: print), '\nOriginal Dictionary:')
_l_(66085)
_c_(66088, _n_(66086, "print", lambda: print), _n_(66087, "dictt", lambda: dictt))
_l_(66089)
_c_(66091, _n_(66090, "print", lambda: print), '\nShortest list of values with the keys of the said dictionary:')
_l_(66092)
_c_(66097, _n_(66093, "print", lambda: print), _c_(66096, _n_(66094, "test", lambda: test), _n_(66095, "dictt", lambda: dictt)))
_l_(66098)