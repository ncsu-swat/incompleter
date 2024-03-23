# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(d):
    _l_(17497)

    aux = _c_(17495, _n_(17491, "list", lambda: list), _c_(17494, _a_(17493, _n_(17492, "d", lambda: d), "items")))
    _l_(17496)
    return aux
_c_(17499, _n_(17498, "print", lambda: print), 'Original Dictionary:')
_l_(17500)
_c_(17503, _n_(17501, "print", lambda: print), _n_(17502, "d", lambda: d))
_l_(17504)
_c_(17506, _n_(17505, "print", lambda: print), '\nConvert the said dictionary to a list of tuples:')
_l_(17507)
_c_(17512, _n_(17508, "print", lambda: print), _c_(17511, _n_(17509, "test", lambda: test), _n_(17510, "d", lambda: d)))
_l_(17513)