# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def string_reverse(str1):
    _l_(16087)

    rstr1 = ''
    _l_(16077)
    while _n_(16078, "index", lambda: index) > 0:
        _l_(16084)

        rstr1 += _n_(16079, "str1", lambda: str1)[_n_(16080, "index", lambda: index) - 1]
        _l_(16081)
        index = _n_(16082, "index", lambda: index) - 1
        _l_(16083)
    aux = _n_(16085, "rstr1", lambda: rstr1)
    _l_(16086)
    return aux
_c_(16091, _n_(16088, "print", lambda: print), _c_(16090, _n_(16089, "string_reverse", lambda: string_reverse), '1234abcd'))
_l_(16092)