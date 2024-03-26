# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from copy import deepcopy
    _l_(105971)

except ImportError:
    pass
try:
    from random import randint
    _l_(105973)

except ImportError:
    pass

def shuffle_list(lst):
    _l_(106000)

    temp_lst = _c_(105976, _n_(105974, "deepcopy", lambda: deepcopy), _n_(105975, "lst", lambda: lst))
    _l_(105977)
    m = _c_(105980, _n_(105978, "len", lambda: len), _n_(105979, "temp_lst", lambda: temp_lst))
    _l_(105981)
    while _n_(105982, "m", lambda: m):
        _l_(105997)

        m -= 1
        _l_(105983)
        i = _c_(105986, _n_(105984, "randint", lambda: randint), 0, _n_(105985, "m", lambda: m))
        _l_(105987)
        _n_(105988, "temp_lst", lambda: temp_lst)[_n_(105989, "m", lambda: m)], _n_(105990, "temp_lst", lambda: temp_lst)[_n_(105991, "i", lambda: i)] = (_n_(105992, "temp_lst", lambda: temp_lst)[_n_(105993, "i", lambda: i)], _n_(105994, "temp_lst", lambda: temp_lst)[_n_(105995, "m", lambda: m)])
        _l_(105996)
    aux = _n_(105998, "temp_lst", lambda: temp_lst)
    _l_(105999)
    return aux
_c_(106003, _n_(106001, "print", lambda: print), 'Original list: ', _n_(106002, "nums", lambda: nums))
_l_(106004)
_c_(106006, _n_(106005, "print", lambda: print), '\nShuffle the elements of the said list:')
_l_(106007)
_c_(106012, _n_(106008, "print", lambda: print), _c_(106011, _n_(106009, "shuffle_list", lambda: shuffle_list), _n_(106010, "nums", lambda: nums)))
_l_(106013)