# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def reverse_strings_list(string_list):
    _l_(85547)

    result = [_n_(85542, "x", lambda: x)[::-1] for x in _n_(85543, "string_list", lambda: string_list)]
    _l_(85544)
    aux = _n_(85545, "result", lambda: result)
    _l_(85546)
    return aux
_c_(85549, _n_(85548, "print", lambda: print), '\nOriginal lists:')
_l_(85550)
_c_(85553, _n_(85551, "print", lambda: print), _n_(85552, "colors_list", lambda: colors_list))
_l_(85554)
_c_(85556, _n_(85555, "print", lambda: print), '\nReverse strings of the said given list:')
_l_(85557)
_c_(85562, _n_(85558, "print", lambda: print), _c_(85561, _n_(85559, "reverse_strings_list", lambda: reverse_strings_list), _n_(85560, "colors_list", lambda: colors_list)))
_l_(85563)