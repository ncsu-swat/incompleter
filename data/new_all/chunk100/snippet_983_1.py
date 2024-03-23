# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def change_char(str1):
    _l_(98316)

    str1 = _c_(98309, _a_(98307, _n_(98306, "str1", lambda: str1), "replace"), _n_(98308, "char", lambda: char), '$')
    _l_(98310)
    str1 = _n_(98311, "char", lambda: char) + _n_(98312, "str1", lambda: str1)[1:]
    _l_(98313)
    aux = _n_(98314, "str1", lambda: str1)
    _l_(98315)
    return aux
_c_(98320, _n_(98317, "print", lambda: print), _c_(98319, _n_(98318, "change_char", lambda: change_char), 'restart'))
_l_(98321)