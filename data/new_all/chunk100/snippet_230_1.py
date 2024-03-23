# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from copy import deepcopy
    _l_(18283)

except ImportError:
    pass
try:
    from random import randint
    _l_(18285)

except ImportError:
    pass

def shuffle_list(lst):
    _l_(18308)

    m = _c_(18288, _n_(18286, "len", lambda: len), _n_(18287, "temp_lst", lambda: temp_lst))
    _l_(18289)
    while _n_(18290, "m", lambda: m):
        _l_(18305)

        m -= 1
        _l_(18291)
        i = _c_(18294, _n_(18292, "randint", lambda: randint), 0, _n_(18293, "m", lambda: m))
        _l_(18295)
        (_n_(18296, "temp_lst", lambda: temp_lst)[_n_(18297, "m", lambda: m)], _n_(18298, "temp_lst", lambda: temp_lst)[_n_(18299, "i", lambda: i)]) = (_n_(18300, "temp_lst", lambda: temp_lst)[_n_(18301, "i", lambda: i)], _n_(18302, "temp_lst", lambda: temp_lst)[_n_(18303, "m", lambda: m)])
        _l_(18304)
    aux = _n_(18306, "temp_lst", lambda: temp_lst)
    _l_(18307)
    return aux
nums = [1, 2, 3, 4, 5, 6]
_l_(18309)
_c_(18312, _n_(18310, "print", lambda: print), 'Original list: ', _n_(18311, "nums", lambda: nums))
_l_(18313)
_c_(18315, _n_(18314, "print", lambda: print), '\nShuffle the elements of the said list:')
_l_(18316)
_c_(18321, _n_(18317, "print", lambda: print), _c_(18320, _n_(18318, "shuffle_list", lambda: shuffle_list), _n_(18319, "nums", lambda: nums)))
_l_(18322)