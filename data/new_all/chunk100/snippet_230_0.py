# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from copy import deepcopy
    _l_(18242)

except ImportError:
    pass
try:
    from random import randint
    _l_(18244)

except ImportError:
    pass

def shuffle_list(lst):
    _l_(18267)

    temp_lst = _c_(18247, _n_(18245, "deepcopy", lambda: deepcopy), _n_(18246, "lst", lambda: lst))
    _l_(18248)
    m = _c_(18251, _n_(18249, "len", lambda: len), _n_(18250, "temp_lst", lambda: temp_lst))
    _l_(18252)
    while _n_(18253, "m", lambda: m):
        _l_(18264)

        m -= 1
        _l_(18254)
        (_n_(18255, "temp_lst", lambda: temp_lst)[_n_(18256, "m", lambda: m)], _n_(18257, "temp_lst", lambda: temp_lst)[_n_(18258, "i", lambda: i)]) = (_n_(18259, "temp_lst", lambda: temp_lst)[_n_(18260, "i", lambda: i)], _n_(18261, "temp_lst", lambda: temp_lst)[_n_(18262, "m", lambda: m)])
        _l_(18263)
    aux = _n_(18265, "temp_lst", lambda: temp_lst)
    _l_(18266)
    return aux
nums = [1, 2, 3, 4, 5, 6]
_l_(18268)
_c_(18271, _n_(18269, "print", lambda: print), 'Original list: ', _n_(18270, "nums", lambda: nums))
_l_(18272)
_c_(18274, _n_(18273, "print", lambda: print), '\nShuffle the elements of the said list:')
_l_(18275)
_c_(18280, _n_(18276, "print", lambda: print), _c_(18279, _n_(18277, "shuffle_list", lambda: shuffle_list), _n_(18278, "nums", lambda: nums)))
_l_(18281)