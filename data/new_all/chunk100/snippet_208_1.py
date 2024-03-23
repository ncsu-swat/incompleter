# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def string_reverse(str1):
    _l_(16105)

    rstr1 = ''
    _l_(16093)
    index = _c_(16096, _n_(16094, "len", lambda: len), _n_(16095, "str1", lambda: str1))
    _l_(16097)
    while _n_(16098, "index", lambda: index) > 0:
        _l_(16102)

        rstr1 += _n_(16099, "str1", lambda: str1)[_n_(16100, "index", lambda: index) - 1]
        _l_(16101)
    aux = _n_(16103, "rstr1", lambda: rstr1)
    _l_(16104)
    return aux
_c_(16109, _n_(16106, "print", lambda: print), _c_(16108, _n_(16107, "string_reverse", lambda: string_reverse), '1234abcd'))
_l_(16110)