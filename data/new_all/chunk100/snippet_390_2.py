# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def check_string(str1):
    _l_(38886)

    result = [_n_(38871, "x", lambda: x) for x in [_c_(38874, _n_(38872, "i", lambda: i), _n_(38873, "str1", lambda: str1)) for i in _n_(38875, "messg", lambda: messg)] if _n_(38876, "x", lambda: x) != True]
    _l_(38877)
    if not _n_(38878, "result", lambda: result):
        _l_(38883)

        _c_(38881, _a_(38880, _n_(38879, "result", lambda: result), "append"), 'Valid string.')
        _l_(38882)
    aux = _n_(38884, "result", lambda: result)
    _l_(38885)
    return aux
s = _c_(38888, _n_(38887, "input", lambda: input), 'Input the string: ')
_l_(38889)
_c_(38894, _n_(38890, "print", lambda: print), _c_(38893, _n_(38891, "check_string", lambda: check_string), _n_(38892, "s", lambda: s)))
_l_(38895)