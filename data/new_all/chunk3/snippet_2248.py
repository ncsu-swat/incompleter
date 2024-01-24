# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56009288/typeerror-object-of-type-int-has-no-len-in-python-on-atom-editor
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def celsius_to_farhenheit(C):
    _l_(536885)

    if(_c_(536878, _n_(536876, "type", lambda: type), _n_(536877, "C", lambda: C))=='int'):
        _l_(536884)

        aux = ("Not possible to find out its length")
        _l_(536879)
        return aux
    else:
        aux = _c_(536882, _n_(536880, "len", lambda: len), _n_(536881, "C", lambda: C))
        _l_(536883)
        return aux


_c_(536889, _n_(536886, "print", lambda: print), _c_(536888, _n_(536887, "celsius_to_farhenheit", lambda: celsius_to_farhenheit), 10))
_l_(536890)