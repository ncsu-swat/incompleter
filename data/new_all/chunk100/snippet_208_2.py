# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def string_reverse(str1):
    _l_(16124)

    index = _c_(16113, _n_(16111, "len", lambda: len), _n_(16112, "str1", lambda: str1))
    _l_(16114)
    while _n_(16115, "index", lambda: index) > 0:
        _l_(16121)

        rstr1 += _n_(16116, "str1", lambda: str1)[_n_(16117, "index", lambda: index) - 1]
        _l_(16118)
        index = _n_(16119, "index", lambda: index) - 1
        _l_(16120)
    aux = _n_(16122, "rstr1", lambda: rstr1)
    _l_(16123)
    return aux
_c_(16128, _n_(16125, "print", lambda: print), _c_(16127, _n_(16126, "string_reverse", lambda: string_reverse), '1234abcd'))
_l_(16129)