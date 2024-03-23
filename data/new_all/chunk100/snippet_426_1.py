# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def number_of_substrings(str):
    _l_(41765)

    str_len = _c_(41758, _n_(41756, "len", lambda: len), _n_(41757, "str", lambda: str))
    _l_(41759)
    aux = _c_(41763, _n_(41760, "int", lambda: int), _n_(41761, "str_len", lambda: str_len) * (_n_(41762, "str_len", lambda: str_len) + 1) / 2)
    _l_(41764)
    return aux
_c_(41767, _n_(41766, "print", lambda: print), 'Number of substrings:')
_l_(41768)
_c_(41773, _n_(41769, "print", lambda: print), _c_(41772, _n_(41770, "number_of_substrings", lambda: number_of_substrings), _n_(41771, "str1", lambda: str1)))
_l_(41774)