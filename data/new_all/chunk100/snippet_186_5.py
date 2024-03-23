# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import choice
    _l_(14948)

except ImportError:
    pass

def generate_random(start_range, end_range, nums):
    _l_(14961)

    result = _c_(14957, _n_(14949, "choice", lambda: choice), [_n_(14950, "i", lambda: i) for i in _c_(14954, _n_(14951, "range", lambda: range), _n_(14952, "start_range", lambda: start_range), _n_(14953, "end_range", lambda: end_range)) if _n_(14955, "i", lambda: i) not in _n_(14956, "nums", lambda: nums)])
    _l_(14958)
    aux = _n_(14959, "result", lambda: result)
    _l_(14960)
    return aux
start_range = 1
_l_(14962)
nums = [2, 9, 10]
_l_(14963)
_c_(14965, _n_(14964, "print", lambda: print), '\nGenerate a number in a specified range (1, 10) except [2, 9, 10]')
_l_(14966)
_c_(14973, _n_(14967, "print", lambda: print), _c_(14972, _n_(14968, "generate_random", lambda: generate_random), _n_(14969, "start_range", lambda: start_range), _n_(14970, "end_range", lambda: end_range), _n_(14971, "nums", lambda: nums)))
_l_(14974)
start_range = -5
_l_(14975)
end_range = 5
_l_(14976)
nums = [-5, 0, 4, 3, 2]
_l_(14977)
_c_(14979, _n_(14978, "print", lambda: print), '\nGenerate a number in a specified range (-5, 5) except [-5,0,4,3,2]')
_l_(14980)
_c_(14987, _n_(14981, "print", lambda: print), _c_(14986, _n_(14982, "generate_random", lambda: generate_random), _n_(14983, "start_range", lambda: start_range), _n_(14984, "end_range", lambda: end_range), _n_(14985, "nums", lambda: nums)))
_l_(14988)