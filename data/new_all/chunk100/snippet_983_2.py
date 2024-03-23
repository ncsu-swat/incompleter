# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def change_char(str1):
    _l_(98329)

    char = _n_(98322, "str1", lambda: str1)[0]
    _l_(98323)
    str1 = _n_(98324, "char", lambda: char) + _n_(98325, "str1", lambda: str1)[1:]
    _l_(98326)
    aux = _n_(98327, "str1", lambda: str1)
    _l_(98328)
    return aux
_c_(98333, _n_(98330, "print", lambda: print), _c_(98332, _n_(98331, "change_char", lambda: change_char), 'restart'))
_l_(98334)