# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def extract_string(str_list1, l):
    _l_(119500)

    result = _c_(119496, _n_(119488, "list", lambda: list), _c_(119495, _n_(119489, "filter", lambda: filter), lambda e: _c_(119492, _n_(119490, "len", lambda: len), _n_(119491, "e", lambda: e)) == _n_(119493, "l", lambda: l), _n_(119494, "str_list1", lambda: str_list1)))
    _l_(119497)
    aux = _n_(119498, "result", lambda: result)
    _l_(119499)
    return aux
str_list1 = ['Python', 'list', 'exercises', 'practice', 'solution']
_l_(119501)
_c_(119503, _n_(119502, "print", lambda: print), 'Original list:')
_l_(119504)
_c_(119507, _n_(119505, "print", lambda: print), _n_(119506, "str_list1", lambda: str_list1))
_l_(119508)
_c_(119510, _n_(119509, "print", lambda: print), '\nlength of the string to extract:')
_l_(119511)
_c_(119514, _n_(119512, "print", lambda: print), _n_(119513, "l", lambda: l))
_l_(119515)
_c_(119517, _n_(119516, "print", lambda: print), '\nAfter extracting strings of specified length from the said list:')
_l_(119518)
_c_(119524, _n_(119519, "print", lambda: print), _c_(119523, _n_(119520, "extract_string", lambda: extract_string), _n_(119521, "str_list1", lambda: str_list1), _n_(119522, "l", lambda: l)))
_l_(119525)