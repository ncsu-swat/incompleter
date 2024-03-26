# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def number_of_substrings(str):
    _l_(115735)

    str_len = _c_(115728, _n_(115726, "len", lambda: len), _n_(115727, "str", lambda: str))
    _l_(115729)
    aux = _c_(115733, _n_(115730, "int", lambda: int), _n_(115731, "str_len", lambda: str_len) * (_n_(115732, "str_len", lambda: str_len) + 1) / 2)
    _l_(115734)
    return aux
_c_(115737, _n_(115736, "print", lambda: print), 'Number of substrings:')
_l_(115738)
_c_(115743, _n_(115739, "print", lambda: print), _c_(115742, _n_(115740, "number_of_substrings", lambda: number_of_substrings), _n_(115741, "str1", lambda: str1)))
_l_(115744)