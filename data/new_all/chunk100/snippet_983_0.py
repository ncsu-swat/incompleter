# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def change_char(str1):
    _l_(98300)

    char = _n_(98291, "str1", lambda: str1)[0]
    _l_(98292)
    str1 = _c_(98296, _a_(98294, _n_(98293, "str1", lambda: str1), "replace"), _n_(98295, "char", lambda: char), '$')
    _l_(98297)
    aux = _n_(98298, "str1", lambda: str1)
    _l_(98299)
    return aux
_c_(98304, _n_(98301, "print", lambda: print), _c_(98303, _n_(98302, "change_char", lambda: change_char), 'restart'))
_l_(98305)