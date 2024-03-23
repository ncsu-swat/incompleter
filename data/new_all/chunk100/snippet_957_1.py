# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import islice
    _l_(95887)

except ImportError:
    pass

def split_list(lst, n):
    _l_(95901)

    result = _c_(95895, _n_(95888, "iter", lambda: iter), lambda : _c_(95894, _n_(95889, "tuple", lambda: tuple), _c_(95893, _n_(95890, "islice", lambda: islice), _n_(95891, "lst", lambda: lst), _n_(95892, "n", lambda: n))), ())
    _l_(95896)
    aux = _c_(95899, _n_(95897, "list", lambda: list), _n_(95898, "result", lambda: result))
    _l_(95900)
    return aux
nums = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
_l_(95902)
_c_(95904, _n_(95903, "print", lambda: print), 'Original list:')
_l_(95905)
_c_(95908, _n_(95906, "print", lambda: print), _n_(95907, "nums", lambda: nums))
_l_(95909)
n = 3
_l_(95910)
_c_(95913, _n_(95911, "print", lambda: print), '\nSplit the said list into equal size', _n_(95912, "n", lambda: n))
_l_(95914)
_c_(95920, _n_(95915, "print", lambda: print), _c_(95919, _n_(95916, "split_list", lambda: split_list), _n_(95917, "nums", lambda: nums), _n_(95918, "n", lambda: n)))
_l_(95921)
n = 4
_l_(95922)
_c_(95925, _n_(95923, "print", lambda: print), '\nSplit the said list into equal size', _n_(95924, "n", lambda: n))
_l_(95926)
_c_(95932, _n_(95927, "print", lambda: print), _c_(95931, _n_(95928, "split_list", lambda: split_list), _n_(95929, "nums", lambda: nums), _n_(95930, "n", lambda: n)))
_l_(95933)
n = 5
_l_(95934)
_c_(95937, _n_(95935, "print", lambda: print), '\nSplit the said list into equal size', _n_(95936, "n", lambda: n))
_l_(95938)
_c_(95944, _n_(95939, "print", lambda: print), _c_(95943, _n_(95940, "split_list", lambda: split_list), _n_(95941, "nums", lambda: nums), _n_(95942, "n", lambda: n)))
_l_(95945)