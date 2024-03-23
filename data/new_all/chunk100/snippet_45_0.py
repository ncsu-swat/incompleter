# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def extract_string(str_list1, l):
    _l_(48844)

    result = [_n_(48835, "e", lambda: e) for e in _n_(48836, "str_list1", lambda: str_list1) if _c_(48839, _n_(48837, "len", lambda: len), _n_(48838, "e", lambda: e)) == _n_(48840, "l", lambda: l)]
    _l_(48841)
    aux = _n_(48842, "result", lambda: result)
    _l_(48843)
    return aux
str_list1 = ['Python', 'list', 'exercises', 'practice', 'solution']
_l_(48845)
_c_(48847, _n_(48846, "print", lambda: print), 'Original list:')
_l_(48848)
_c_(48851, _n_(48849, "print", lambda: print), _n_(48850, "str_list1", lambda: str_list1))
_l_(48852)
_c_(48854, _n_(48853, "print", lambda: print), '\nlength of the string to extract:')
_l_(48855)
_c_(48858, _n_(48856, "print", lambda: print), _n_(48857, "l", lambda: l))
_l_(48859)
_c_(48861, _n_(48860, "print", lambda: print), '\nAfter extracting strings of specified length from the said list:')
_l_(48862)
_c_(48868, _n_(48863, "print", lambda: print), _c_(48867, _n_(48864, "extract_string", lambda: extract_string), _n_(48865, "str_list1", lambda: str_list1), _n_(48866, "l", lambda: l)))
_l_(48869)