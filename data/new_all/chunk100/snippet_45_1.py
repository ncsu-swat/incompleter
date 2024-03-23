# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def extract_string(str_list1, l):
    _l_(48879)

    result = [_n_(48870, "e", lambda: e) for e in _n_(48871, "str_list1", lambda: str_list1) if _c_(48874, _n_(48872, "len", lambda: len), _n_(48873, "e", lambda: e)) == _n_(48875, "l", lambda: l)]
    _l_(48876)
    aux = _n_(48877, "result", lambda: result)
    _l_(48878)
    return aux
_c_(48881, _n_(48880, "print", lambda: print), 'Original list:')
_l_(48882)
_c_(48885, _n_(48883, "print", lambda: print), _n_(48884, "str_list1", lambda: str_list1))
_l_(48886)
l = 8
_l_(48887)
_c_(48889, _n_(48888, "print", lambda: print), '\nlength of the string to extract:')
_l_(48890)
_c_(48893, _n_(48891, "print", lambda: print), _n_(48892, "l", lambda: l))
_l_(48894)
_c_(48896, _n_(48895, "print", lambda: print), '\nAfter extracting strings of specified length from the said list:')
_l_(48897)
_c_(48903, _n_(48898, "print", lambda: print), _c_(48902, _n_(48899, "extract_string", lambda: extract_string), _n_(48900, "str_list1", lambda: str_list1), _n_(48901, "l", lambda: l)))
_l_(48904)