# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(dictionary):
    _l_(94894)

    _n_(94884, "dictionary", lambda: dictionary)['Math'] = [_n_(94885, "x", lambda: x) + 1 for x in _n_(94886, "dictionary", lambda: dictionary)['Math']]
    _l_(94887)
    _n_(94888, "dictionary", lambda: dictionary)['Physics'] = [_n_(94889, "x", lambda: x) - 2 for x in _n_(94890, "dictionary", lambda: dictionary)['Physics']]
    _l_(94891)
    aux = _n_(94892, "dictionary", lambda: dictionary)
    _l_(94893)
    return aux
_c_(94896, _n_(94895, "print", lambda: print), '\nOriginal Dictionary:')
_l_(94897)
_c_(94900, _n_(94898, "print", lambda: print), _n_(94899, "dictionary", lambda: dictionary))
_l_(94901)
_c_(94903, _n_(94902, "print", lambda: print), '\nUpdate the list values of the said dictionary:')
_l_(94904)
_c_(94909, _n_(94905, "print", lambda: print), _c_(94908, _n_(94906, "test", lambda: test), _n_(94907, "dictionary", lambda: dictionary)))
_l_(94910)