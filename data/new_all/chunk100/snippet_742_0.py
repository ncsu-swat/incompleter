# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def split_two_parts(n_list, L):
    _l_(74813)

    aux = (_n_(74808, "n_list", lambda: n_list)[:_n_(74809, "L", lambda: L)], _n_(74810, "n_list", lambda: n_list)[_n_(74811, "L", lambda: L):])
    _l_(74812)
    return aux
n_list = [1, 1, 2, 3, 4, 4, 5, 1]
_l_(74814)
_c_(74816, _n_(74815, "print", lambda: print), 'Original list:')
_l_(74817)
_c_(74820, _n_(74818, "print", lambda: print), _n_(74819, "n_list", lambda: n_list))
_l_(74821)
_c_(74824, _n_(74822, "print", lambda: print), '\nLength of the first part of the list:', _n_(74823, "first_list_length", lambda: first_list_length))
_l_(74825)
_c_(74827, _n_(74826, "print", lambda: print), '\nSplited the said list into two parts:')
_l_(74828)
_c_(74834, _n_(74829, "print", lambda: print), _c_(74833, _n_(74830, "split_two_parts", lambda: split_two_parts), _n_(74831, "n_list", lambda: n_list), _n_(74832, "first_list_length", lambda: first_list_length)))
_l_(74835)