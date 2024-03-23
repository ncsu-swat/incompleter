# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools as it
    _l_(10925)

except ImportError:
    pass
nums = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
_l_(10926)
_c_(10928, _n_(10927, "print", lambda: print), 'Original list:')
_l_(10929)
_c_(10932, _n_(10930, "print", lambda: print), _n_(10931, "nums", lambda: nums))
_l_(10933)

def get_avg(x):
    _l_(10945)

    x = [_n_(10934, "i", lambda: i) for i in _n_(10935, "x", lambda: x) if _n_(10936, "i", lambda: i) is not None]
    _l_(10937)
    aux = _c_(10940, _n_(10938, "sum", lambda: sum), _n_(10939, "x", lambda: x), 0.0) / _c_(10943, _n_(10941, "len", lambda: len), _n_(10942, "x", lambda: x))
    _l_(10944)
    return aux
_c_(10947, _n_(10946, "print", lambda: print), '\nAverage of n-th elements in the said list of lists with different lengths:')
_l_(10948)
_c_(10953, _n_(10949, "print", lambda: print), _c_(10952, _n_(10950, "list", lambda: list), _n_(10951, "result", lambda: result)))
_l_(10954)