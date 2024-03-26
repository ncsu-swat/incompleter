# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def extract_string(str_list1, l):
    _l_(116700)

    result = [_n_(116691, "e", lambda: e) for e in _n_(116692, "str_list1", lambda: str_list1) if _c_(116695, _n_(116693, "len", lambda: len), _n_(116694, "e", lambda: e)) == _n_(116696, "l", lambda: l)]
    _l_(116697)
    aux = _n_(116698, "result", lambda: result)
    _l_(116699)
    return aux
_c_(116702, _n_(116701, "print", lambda: print), 'Original list:')
_l_(116703)
_c_(116706, _n_(116704, "print", lambda: print), _n_(116705, "str_list1", lambda: str_list1))
_l_(116707)
l = 8
_l_(116708)
_c_(116710, _n_(116709, "print", lambda: print), '\nlength of the string to extract:')
_l_(116711)
_c_(116714, _n_(116712, "print", lambda: print), _n_(116713, "l", lambda: l))
_l_(116715)
_c_(116717, _n_(116716, "print", lambda: print), '\nAfter extracting strings of specified length from the said list:')
_l_(116718)
_c_(116724, _n_(116719, "print", lambda: print), _c_(116723, _n_(116720, "extract_string", lambda: extract_string), _n_(116721, "str_list1", lambda: str_list1), _n_(116722, "l", lambda: l)))
_l_(116725)