# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(d):
    _l_(105846)

    aux = _c_(105844, _n_(105840, "list", lambda: list), _c_(105843, _a_(105842, _n_(105841, "d", lambda: d), "items")))
    _l_(105845)
    return aux
_c_(105848, _n_(105847, "print", lambda: print), 'Original Dictionary:')
_l_(105849)
_c_(105852, _n_(105850, "print", lambda: print), _n_(105851, "d", lambda: d))
_l_(105853)
_c_(105855, _n_(105854, "print", lambda: print), '\nConvert the said dictionary to a list of tuples:')
_l_(105856)
_c_(105861, _n_(105857, "print", lambda: print), _c_(105860, _n_(105858, "test", lambda: test), _n_(105859, "d", lambda: d)))
_l_(105862)