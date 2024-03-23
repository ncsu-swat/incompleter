# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from copy import deepcopy
    _l_(18365)

except ImportError:
    pass
try:
    from random import randint
    _l_(18367)

except ImportError:
    pass

def shuffle_list(lst):
    _l_(18394)

    temp_lst = _c_(18370, _n_(18368, "deepcopy", lambda: deepcopy), _n_(18369, "lst", lambda: lst))
    _l_(18371)
    m = _c_(18374, _n_(18372, "len", lambda: len), _n_(18373, "temp_lst", lambda: temp_lst))
    _l_(18375)
    while _n_(18376, "m", lambda: m):
        _l_(18391)

        m -= 1
        _l_(18377)
        i = _c_(18380, _n_(18378, "randint", lambda: randint), 0, _n_(18379, "m", lambda: m))
        _l_(18381)
        (_n_(18382, "temp_lst", lambda: temp_lst)[_n_(18383, "m", lambda: m)], _n_(18384, "temp_lst", lambda: temp_lst)[_n_(18385, "i", lambda: i)]) = (_n_(18386, "temp_lst", lambda: temp_lst)[_n_(18387, "i", lambda: i)], _n_(18388, "temp_lst", lambda: temp_lst)[_n_(18389, "m", lambda: m)])
        _l_(18390)
    aux = _n_(18392, "temp_lst", lambda: temp_lst)
    _l_(18393)
    return aux
_c_(18397, _n_(18395, "print", lambda: print), 'Original list: ', _n_(18396, "nums", lambda: nums))
_l_(18398)
_c_(18400, _n_(18399, "print", lambda: print), '\nShuffle the elements of the said list:')
_l_(18401)
_c_(18406, _n_(18402, "print", lambda: print), _c_(18405, _n_(18403, "shuffle_list", lambda: shuffle_list), _n_(18404, "nums", lambda: nums)))
_l_(18407)