# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from copy import deepcopy
    _l_(18324)

except ImportError:
    pass
try:
    from random import randint
    _l_(18326)

except ImportError:
    pass

def shuffle_list(lst):
    _l_(18349)

    temp_lst = _c_(18329, _n_(18327, "deepcopy", lambda: deepcopy), _n_(18328, "lst", lambda: lst))
    _l_(18330)
    while _n_(18331, "m", lambda: m):
        _l_(18346)

        m -= 1
        _l_(18332)
        i = _c_(18335, _n_(18333, "randint", lambda: randint), 0, _n_(18334, "m", lambda: m))
        _l_(18336)
        (_n_(18337, "temp_lst", lambda: temp_lst)[_n_(18338, "m", lambda: m)], _n_(18339, "temp_lst", lambda: temp_lst)[_n_(18340, "i", lambda: i)]) = (_n_(18341, "temp_lst", lambda: temp_lst)[_n_(18342, "i", lambda: i)], _n_(18343, "temp_lst", lambda: temp_lst)[_n_(18344, "m", lambda: m)])
        _l_(18345)
    aux = _n_(18347, "temp_lst", lambda: temp_lst)
    _l_(18348)
    return aux
nums = [1, 2, 3, 4, 5, 6]
_l_(18350)
_c_(18353, _n_(18351, "print", lambda: print), 'Original list: ', _n_(18352, "nums", lambda: nums))
_l_(18354)
_c_(18356, _n_(18355, "print", lambda: print), '\nShuffle the elements of the said list:')
_l_(18357)
_c_(18362, _n_(18358, "print", lambda: print), _c_(18361, _n_(18359, "shuffle_list", lambda: shuffle_list), _n_(18360, "nums", lambda: nums)))
_l_(18363)