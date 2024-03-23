# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_length_list(input_list):
    _l_(93085)

    max_length = _c_(93075, _n_(93070, "max", lambda: max), (_c_(93073, _n_(93071, "len", lambda: len), _n_(93072, "x", lambda: x)) for x in _n_(93074, "input_list", lambda: input_list)))
    _l_(93076)
    max_list = _c_(93080, _n_(93077, "max", lambda: max), _n_(93078, "input_list", lambda: input_list), key=_n_(93079, "len", lambda: len))
    _l_(93081)
    aux = (_n_(93082, "max_length", lambda: max_length), _n_(93083, "max_list", lambda: max_list))
    _l_(93084)
    return aux

def min_length_list(input_list):
    _l_(93101)

    min_length = _c_(93091, _n_(93086, "min", lambda: min), (_c_(93089, _n_(93087, "len", lambda: len), _n_(93088, "x", lambda: x)) for x in _n_(93090, "input_list", lambda: input_list)))
    _l_(93092)
    min_list = _c_(93096, _n_(93093, "min", lambda: min), _n_(93094, "input_list", lambda: input_list), key=_n_(93095, "len", lambda: len))
    _l_(93097)
    aux = (_n_(93098, "min_length", lambda: min_length), _n_(93099, "min_list", lambda: min_list))
    _l_(93100)
    return aux
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
_l_(93102)
_c_(93104, _n_(93103, "print", lambda: print), 'Original list:')
_l_(93105)
_c_(93108, _n_(93106, "print", lambda: print), _n_(93107, "list1", lambda: list1))
_l_(93109)
_c_(93111, _n_(93110, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93112)
_c_(93117, _n_(93113, "print", lambda: print), _c_(93116, _n_(93114, "max_length_list", lambda: max_length_list), _n_(93115, "list1", lambda: list1)))
_l_(93118)
_c_(93120, _n_(93119, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93121)
_c_(93126, _n_(93122, "print", lambda: print), _c_(93125, _n_(93123, "min_length_list", lambda: min_length_list), _n_(93124, "list1", lambda: list1)))
_l_(93127)
list1 = [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
_l_(93128)
_c_(93130, _n_(93129, "print", lambda: print), 'Original list:')
_l_(93131)
_c_(93134, _n_(93132, "print", lambda: print), _n_(93133, "list1", lambda: list1))
_l_(93135)
_c_(93137, _n_(93136, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93138)
_c_(93143, _n_(93139, "print", lambda: print), _c_(93142, _n_(93140, "max_length_list", lambda: max_length_list), _n_(93141, "list1", lambda: list1)))
_l_(93144)
_c_(93146, _n_(93145, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93147)
_c_(93152, _n_(93148, "print", lambda: print), _c_(93151, _n_(93149, "min_length_list", lambda: min_length_list), _n_(93150, "list1", lambda: list1)))
_l_(93153)
_c_(93155, _n_(93154, "print", lambda: print), 'Original list:')
_l_(93156)
_c_(93159, _n_(93157, "print", lambda: print), _n_(93158, "list1", lambda: list1))
_l_(93160)
_c_(93162, _n_(93161, "print", lambda: print), '\nList with maximum length of lists:')
_l_(93163)
_c_(93168, _n_(93164, "print", lambda: print), _c_(93167, _n_(93165, "max_length_list", lambda: max_length_list), _n_(93166, "list1", lambda: list1)))
_l_(93169)
_c_(93171, _n_(93170, "print", lambda: print), '\nList with minimum length of lists:')
_l_(93172)
_c_(93177, _n_(93173, "print", lambda: print), _c_(93176, _n_(93174, "min_length_list", lambda: min_length_list), _n_(93175, "list1", lambda: list1)))
_l_(93178)