# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_min_list_tuples(nums):
    _l_(33263)

    _c_(33247, _n_(33245, "zip", lambda: zip), *_n_(33246, "nums", lambda: nums))
    _l_(33248)
    result1 = _c_(33254, _n_(33249, "map", lambda: map), _n_(33250, "max", lambda: max), _c_(33253, _n_(33251, "zip", lambda: zip), *_n_(33252, "nums", lambda: nums)))
    _l_(33255)
    aux = (_c_(33258, _n_(33256, "list", lambda: list), _n_(33257, "result1", lambda: result1)), _c_(33261, _n_(33259, "list", lambda: list), _n_(33260, "result2", lambda: result2)))
    _l_(33262)
    return aux
nums = [(2, 3), (2, 4), (0, 6), (7, 1)]
_l_(33264)
_c_(33266, _n_(33265, "print", lambda: print), 'Original list:')
_l_(33267)
_c_(33270, _n_(33268, "print", lambda: print), _n_(33269, "nums", lambda: nums))
_l_(33271)
result = _c_(33274, _n_(33272, "max_min_list_tuples", lambda: max_min_list_tuples), _n_(33273, "nums", lambda: nums))
_l_(33275)
_c_(33277, _n_(33276, "print", lambda: print), '\nMaximum value  for each tuple position in the said list of tuples:')
_l_(33278)
_c_(33281, _n_(33279, "print", lambda: print), _n_(33280, "result", lambda: result)[0])
_l_(33282)
_c_(33284, _n_(33283, "print", lambda: print), '\nMinimum value  for each tuple position in the said list of tuples:')
_l_(33285)
_c_(33288, _n_(33286, "print", lambda: print), _n_(33287, "result", lambda: result)[1])
_l_(33289)