# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import choice
    _l_(14831)

except ImportError:
    pass

def generate_random(start_range, end_range, nums):
    _l_(14844)

    result = _c_(14840, _n_(14832, "choice", lambda: choice), [_n_(14833, "i", lambda: i) for i in _c_(14837, _n_(14834, "range", lambda: range), _n_(14835, "start_range", lambda: start_range), _n_(14836, "end_range", lambda: end_range)) if _n_(14838, "i", lambda: i) not in _n_(14839, "nums", lambda: nums)])
    _l_(14841)
    aux = _n_(14842, "result", lambda: result)
    _l_(14843)
    return aux
start_range = 1
_l_(14845)
end_range = 10
_l_(14846)
nums = [2, 9, 10]
_l_(14847)
_c_(14849, _n_(14848, "print", lambda: print), '\nGenerate a number in a specified range (1, 10) except [2, 9, 10]')
_l_(14850)
_c_(14857, _n_(14851, "print", lambda: print), _c_(14856, _n_(14852, "generate_random", lambda: generate_random), _n_(14853, "start_range", lambda: start_range), _n_(14854, "end_range", lambda: end_range), _n_(14855, "nums", lambda: nums)))
_l_(14858)
start_range = -5
_l_(14859)
end_range = 5
_l_(14860)
_c_(14862, _n_(14861, "print", lambda: print), '\nGenerate a number in a specified range (-5, 5) except [-5,0,4,3,2]')
_l_(14863)
_c_(14870, _n_(14864, "print", lambda: print), _c_(14869, _n_(14865, "generate_random", lambda: generate_random), _n_(14866, "start_range", lambda: start_range), _n_(14867, "end_range", lambda: end_range), _n_(14868, "nums", lambda: nums)))
_l_(14871)