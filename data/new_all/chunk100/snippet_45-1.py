# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def extract_string(str_list1, l):
    _l_(116735)

    result = [_n_(116726, "e", lambda: e) for e in _n_(116727, "str_list1", lambda: str_list1) if _c_(116730, _n_(116728, "len", lambda: len), _n_(116729, "e", lambda: e)) == _n_(116731, "l", lambda: l)]
    _l_(116732)
    aux = _n_(116733, "result", lambda: result)
    _l_(116734)
    return aux
str_list1 = ['Python', 'list', 'exercises', 'practice', 'solution']
_l_(116736)
_c_(116738, _n_(116737, "print", lambda: print), 'Original list:')
_l_(116739)
_c_(116742, _n_(116740, "print", lambda: print), _n_(116741, "str_list1", lambda: str_list1))
_l_(116743)
_c_(116745, _n_(116744, "print", lambda: print), '\nlength of the string to extract:')
_l_(116746)
_c_(116749, _n_(116747, "print", lambda: print), _n_(116748, "l", lambda: l))
_l_(116750)
_c_(116752, _n_(116751, "print", lambda: print), '\nAfter extracting strings of specified length from the said list:')
_l_(116753)
_c_(116759, _n_(116754, "print", lambda: print), _c_(116758, _n_(116755, "extract_string", lambda: extract_string), _n_(116756, "str_list1", lambda: str_list1), _n_(116757, "l", lambda: l)))
_l_(116760)