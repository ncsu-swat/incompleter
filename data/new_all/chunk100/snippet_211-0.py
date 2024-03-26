# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def pair_consecutive_elements(lst):
    _l_(105267)

    result = [[_n_(105255, "lst", lambda: lst)[_n_(105256, "i", lambda: i)], _n_(105257, "lst", lambda: lst)[_n_(105258, "i", lambda: i) + 1]] for i in _c_(105263, _n_(105259, "range", lambda: range), _c_(105262, _n_(105260, "len", lambda: len), _n_(105261, "lst", lambda: lst)) - 1)]
    _l_(105264)
    aux = _n_(105265, "result", lambda: result)
    _l_(105266)
    return aux
_c_(105269, _n_(105268, "print", lambda: print), 'Original lists:')
_l_(105270)
_c_(105273, _n_(105271, "print", lambda: print), _n_(105272, "nums", lambda: nums))
_l_(105274)
_c_(105276, _n_(105275, "print", lambda: print), 'Pair up the consecutive elements of the said list:')
_l_(105277)
_c_(105282, _n_(105278, "print", lambda: print), _c_(105281, _n_(105279, "pair_consecutive_elements", lambda: pair_consecutive_elements), _n_(105280, "nums", lambda: nums)))
_l_(105283)
nums = [1, 2, 3, 4, 5]
_l_(105284)
_c_(105286, _n_(105285, "print", lambda: print), '\nOriginal lists:')
_l_(105287)
_c_(105290, _n_(105288, "print", lambda: print), _n_(105289, "nums", lambda: nums))
_l_(105291)
_c_(105293, _n_(105292, "print", lambda: print), 'Pair up the consecutive elements of the said list:')
_l_(105294)
_c_(105299, _n_(105295, "print", lambda: print), _c_(105298, _n_(105296, "pair_consecutive_elements", lambda: pair_consecutive_elements), _n_(105297, "nums", lambda: nums)))
_l_(105300)