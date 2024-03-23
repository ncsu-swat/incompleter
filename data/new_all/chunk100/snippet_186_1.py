# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import choice
    _l_(14789)

except ImportError:
    pass

def generate_random(start_range, end_range, nums):
    _l_(14802)

    result = _c_(14798, _n_(14790, "choice", lambda: choice), [_n_(14791, "i", lambda: i) for i in _c_(14795, _n_(14792, "range", lambda: range), _n_(14793, "start_range", lambda: start_range), _n_(14794, "end_range", lambda: end_range)) if _n_(14796, "i", lambda: i) not in _n_(14797, "nums", lambda: nums)])
    _l_(14799)
    aux = _n_(14800, "result", lambda: result)
    _l_(14801)
    return aux
end_range = 10
_l_(14803)
nums = [2, 9, 10]
_l_(14804)
_c_(14806, _n_(14805, "print", lambda: print), '\nGenerate a number in a specified range (1, 10) except [2, 9, 10]')
_l_(14807)
_c_(14814, _n_(14808, "print", lambda: print), _c_(14813, _n_(14809, "generate_random", lambda: generate_random), _n_(14810, "start_range", lambda: start_range), _n_(14811, "end_range", lambda: end_range), _n_(14812, "nums", lambda: nums)))
_l_(14815)
start_range = -5
_l_(14816)
end_range = 5
_l_(14817)
nums = [-5, 0, 4, 3, 2]
_l_(14818)
_c_(14820, _n_(14819, "print", lambda: print), '\nGenerate a number in a specified range (-5, 5) except [-5,0,4,3,2]')
_l_(14821)
_c_(14828, _n_(14822, "print", lambda: print), _c_(14827, _n_(14823, "generate_random", lambda: generate_random), _n_(14824, "start_range", lambda: start_range), _n_(14825, "end_range", lambda: end_range), _n_(14826, "nums", lambda: nums)))
_l_(14829)