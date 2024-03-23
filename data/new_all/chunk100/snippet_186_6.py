# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import choice
    _l_(14990)

except ImportError:
    pass

def generate_random(start_range, end_range, nums):
    _l_(15003)

    result = _c_(14999, _n_(14991, "choice", lambda: choice), [_n_(14992, "i", lambda: i) for i in _c_(14996, _n_(14993, "range", lambda: range), _n_(14994, "start_range", lambda: start_range), _n_(14995, "end_range", lambda: end_range)) if _n_(14997, "i", lambda: i) not in _n_(14998, "nums", lambda: nums)])
    _l_(15000)
    aux = _n_(15001, "result", lambda: result)
    _l_(15002)
    return aux
start_range = 1
_l_(15004)
end_range = 10
_l_(15005)
_c_(15007, _n_(15006, "print", lambda: print), '\nGenerate a number in a specified range (1, 10) except [2, 9, 10]')
_l_(15008)
_c_(15015, _n_(15009, "print", lambda: print), _c_(15014, _n_(15010, "generate_random", lambda: generate_random), _n_(15011, "start_range", lambda: start_range), _n_(15012, "end_range", lambda: end_range), _n_(15013, "nums", lambda: nums)))
_l_(15016)
start_range = -5
_l_(15017)
end_range = 5
_l_(15018)
nums = [-5, 0, 4, 3, 2]
_l_(15019)
_c_(15021, _n_(15020, "print", lambda: print), '\nGenerate a number in a specified range (-5, 5) except [-5,0,4,3,2]')
_l_(15022)
_c_(15029, _n_(15023, "print", lambda: print), _c_(15028, _n_(15024, "generate_random", lambda: generate_random), _n_(15025, "start_range", lambda: start_range), _n_(15026, "end_range", lambda: end_range), _n_(15027, "nums", lambda: nums)))
_l_(15030)