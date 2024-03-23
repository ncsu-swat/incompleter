# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(71734)

except ImportError:
    pass

def test(dictt):
    _l_(71743)

    result = _c_(71739, _n_(71735, "Counter", lambda: Counter), _c_(71738, _a_(71737, _n_(71736, "dictt", lambda: dictt), "values")))
    _l_(71740)
    aux = _n_(71741, "result", lambda: result)
    _l_(71742)
    return aux
_c_(71745, _n_(71744, "print", lambda: print), '\nOriginal Dictionary:')
_l_(71746)
_c_(71749, _n_(71747, "print", lambda: print), _n_(71748, "dictt", lambda: dictt))
_l_(71750)
_c_(71752, _n_(71751, "print", lambda: print), '\nCount the frequency of the said dictionary:')
_l_(71753)
_c_(71758, _n_(71754, "print", lambda: print), _c_(71757, _n_(71755, "test", lambda: test), _n_(71756, "dictt", lambda: dictt)))
_l_(71759)