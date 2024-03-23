# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import product
    _l_(34290)

except ImportError:
    pass

def test(dictt):
    _l_(34305)

    result = [_c_(34296, _n_(34291, "dict", lambda: dict), _c_(34295, _n_(34292, "zip", lambda: zip), _n_(34293, "dictt", lambda: dictt), _n_(34294, "sub", lambda: sub))) for sub in _c_(34301, _n_(34297, "product", lambda: product), *_c_(34300, _a_(34299, _n_(34298, "dictt", lambda: dictt), "values")))]
    _l_(34302)
    aux = _n_(34303, "result", lambda: result)
    _l_(34304)
    return aux
_c_(34307, _n_(34306, "print", lambda: print), '\nOriginal dictionary:')
_l_(34308)
_c_(34311, _n_(34309, "print", lambda: print), _n_(34310, "students", lambda: students))
_l_(34312)
_c_(34314, _n_(34313, "print", lambda: print), '\nA key-value list pairings of the said dictionary:')
_l_(34315)
_c_(34320, _n_(34316, "print", lambda: print), _c_(34319, _n_(34317, "test", lambda: test), _n_(34318, "students", lambda: students)))
_l_(34321)