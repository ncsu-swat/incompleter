# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64998634/getting-an-error-typeerror-str-object-cannot-be-interpreted-as-an-integer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Name:
    _l_(605077)


    def __init__(self,first,last):
        _l_(605072)


        _n_(605066, "self", lambda: self).first = _n_(605067, "first", lambda: first)
        _l_(605068)
        _n_(605069, "self", lambda: self).last = _n_(605070, "last", lambda: last)
        _l_(605071)


    def __len__(self):
        _l_(605076)

        aux = _a_(605074, _n_(605073, "self", lambda: self), "first")
        _l_(605075)
        return aux

name_1 = _c_(605079, _n_(605078, "Name", lambda: Name), 'FIrst','last')
_l_(605080)

_c_(605085, _n_(605081, "print", lambda: print), _c_(605084, _n_(605082, "len", lambda: len), _n_(605083, "name_1", lambda: name_1)))
_l_(605086)