# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import product
    _l_(111403)

except ImportError:
    pass

def test(dictt):
    _l_(111418)

    result = [_c_(111409, _n_(111404, "dict", lambda: dict), _c_(111408, _n_(111405, "zip", lambda: zip), _n_(111406, "dictt", lambda: dictt), _n_(111407, "sub", lambda: sub))) for sub in _c_(111414, _n_(111410, "product", lambda: product), *_c_(111413, _a_(111412, _n_(111411, "dictt", lambda: dictt), "values")))]
    _l_(111415)
    aux = _n_(111416, "result", lambda: result)
    _l_(111417)
    return aux
_c_(111420, _n_(111419, "print", lambda: print), '\nOriginal dictionary:')
_l_(111421)
_c_(111424, _n_(111422, "print", lambda: print), _n_(111423, "students", lambda: students))
_l_(111425)
_c_(111427, _n_(111426, "print", lambda: print), '\nA key-value list pairings of the said dictionary:')
_l_(111428)
_c_(111433, _n_(111429, "print", lambda: print), _c_(111432, _n_(111430, "test", lambda: test), _n_(111431, "students", lambda: students)))
_l_(111434)