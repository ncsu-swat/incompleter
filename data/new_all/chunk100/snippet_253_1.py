# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def drop_left_right(a, n=1):
    _l_(19835)

    aux = (_n_(19830, "a", lambda: a)[_n_(19831, "n", lambda: n):], _n_(19832, "a", lambda: a)[:-_n_(19833, "n", lambda: n)])
    _l_(19834)
    return aux
nums = [1, 2, 3]
_l_(19836)
_c_(19838, _n_(19837, "print", lambda: print), 'Original list elements:')
_l_(19839)
_c_(19842, _n_(19840, "print", lambda: print), _n_(19841, "nums", lambda: nums))
_l_(19843)
result = _c_(19846, _n_(19844, "drop_left_right", lambda: drop_left_right), _n_(19845, "nums", lambda: nums))
_l_(19847)
_c_(19849, _n_(19848, "print", lambda: print), 'Remove 1 element from left of the said list:')
_l_(19850)
_c_(19853, _n_(19851, "print", lambda: print), _n_(19852, "result", lambda: result)[0])
_l_(19854)
_c_(19856, _n_(19855, "print", lambda: print), 'Remove 1 element from right of the said list:')
_l_(19857)
_c_(19860, _n_(19858, "print", lambda: print), _n_(19859, "result", lambda: result)[1])
_l_(19861)
nums = [1, 2, 3, 4]
_l_(19862)
_c_(19864, _n_(19863, "print", lambda: print), '\nOriginal list elements:')
_l_(19865)
_c_(19868, _n_(19866, "print", lambda: print), _n_(19867, "nums", lambda: nums))
_l_(19869)
result = _c_(19872, _n_(19870, "drop_left_right", lambda: drop_left_right), _n_(19871, "nums", lambda: nums), 2)
_l_(19873)
_c_(19875, _n_(19874, "print", lambda: print), 'Remove 2 elements from left of the said list:')
_l_(19876)
_c_(19879, _n_(19877, "print", lambda: print), _n_(19878, "result", lambda: result)[0])
_l_(19880)
_c_(19882, _n_(19881, "print", lambda: print), 'Remove 2 elements from right of the said list:')
_l_(19883)
_c_(19886, _n_(19884, "print", lambda: print), _n_(19885, "result", lambda: result)[1])
_l_(19887)
_c_(19889, _n_(19888, "print", lambda: print), '\nOriginal list elements:')
_l_(19890)
_c_(19893, _n_(19891, "print", lambda: print), _n_(19892, "nums", lambda: nums))
_l_(19894)
result = _c_(19897, _n_(19895, "drop_left_right", lambda: drop_left_right), _n_(19896, "nums", lambda: nums))
_l_(19898)
_c_(19900, _n_(19899, "print", lambda: print), 'Remove 7 elements from left of the said list:')
_l_(19901)
_c_(19904, _n_(19902, "print", lambda: print), _n_(19903, "result", lambda: result)[0])
_l_(19905)
_c_(19907, _n_(19906, "print", lambda: print), 'Remove 7 elements from right of the said list:')
_l_(19908)
_c_(19911, _n_(19909, "print", lambda: print), _n_(19910, "result", lambda: result)[1])
_l_(19912)