# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import choice
    _l_(14873)

except ImportError:
    pass

def generate_random(start_range, end_range, nums):
    _l_(14886)

    result = _c_(14882, _n_(14874, "choice", lambda: choice), [_n_(14875, "i", lambda: i) for i in _c_(14879, _n_(14876, "range", lambda: range), _n_(14877, "start_range", lambda: start_range), _n_(14878, "end_range", lambda: end_range)) if _n_(14880, "i", lambda: i) not in _n_(14881, "nums", lambda: nums)])
    _l_(14883)
    aux = _n_(14884, "result", lambda: result)
    _l_(14885)
    return aux
start_range = 1
_l_(14887)
end_range = 10
_l_(14888)
nums = [2, 9, 10]
_l_(14889)
_c_(14891, _n_(14890, "print", lambda: print), '\nGenerate a number in a specified range (1, 10) except [2, 9, 10]')
_l_(14892)
_c_(14899, _n_(14893, "print", lambda: print), _c_(14898, _n_(14894, "generate_random", lambda: generate_random), _n_(14895, "start_range", lambda: start_range), _n_(14896, "end_range", lambda: end_range), _n_(14897, "nums", lambda: nums)))
_l_(14900)
end_range = 5
_l_(14901)
nums = [-5, 0, 4, 3, 2]
_l_(14902)
_c_(14904, _n_(14903, "print", lambda: print), '\nGenerate a number in a specified range (-5, 5) except [-5,0,4,3,2]')
_l_(14905)
_c_(14912, _n_(14906, "print", lambda: print), _c_(14911, _n_(14907, "generate_random", lambda: generate_random), _n_(14908, "start_range", lambda: start_range), _n_(14909, "end_range", lambda: end_range), _n_(14910, "nums", lambda: nums)))
_l_(14913)