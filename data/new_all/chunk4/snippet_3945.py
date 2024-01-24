# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64998634/getting-an-error-typeerror-str-object-cannot-be-interpreted-as-an-integer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Name:
    _l_(634958)


    def __init__(self,first,last):
        _l_(634953)


        _n_(634947, "self", lambda: self).first = _n_(634948, "first", lambda: first)
        _l_(634949)
        _n_(634950, "self", lambda: self).last = _n_(634951, "last", lambda: last)
        _l_(634952)


    def __len__(self):
        _l_(634957)

        aux = _a_(634955, _n_(634954, "self", lambda: self), "first")
        _l_(634956)
        return aux

name_1 = _c_(634960, _n_(634959, "Name", lambda: Name), 'FIrst','last')
_l_(634961)

_c_(634966, _n_(634962, "print", lambda: print), _c_(634965, _n_(634963, "len", lambda: len), _n_(634964, "name_1", lambda: name_1)))
_l_(634967)