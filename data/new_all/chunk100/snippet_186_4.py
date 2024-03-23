# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import choice
    _l_(14915)

except ImportError:
    pass

def generate_random(start_range, end_range, nums):
    _l_(14918)

    aux = _n_(14916, "result", lambda: result)
    _l_(14917)
    return aux
start_range = 1
_l_(14919)
end_range = 10
_l_(14920)
nums = [2, 9, 10]
_l_(14921)
_c_(14923, _n_(14922, "print", lambda: print), '\nGenerate a number in a specified range (1, 10) except [2, 9, 10]')
_l_(14924)
_c_(14931, _n_(14925, "print", lambda: print), _c_(14930, _n_(14926, "generate_random", lambda: generate_random), _n_(14927, "start_range", lambda: start_range), _n_(14928, "end_range", lambda: end_range), _n_(14929, "nums", lambda: nums)))
_l_(14932)
start_range = -5
_l_(14933)
end_range = 5
_l_(14934)
nums = [-5, 0, 4, 3, 2]
_l_(14935)
_c_(14937, _n_(14936, "print", lambda: print), '\nGenerate a number in a specified range (-5, 5) except [-5,0,4,3,2]')
_l_(14938)
_c_(14945, _n_(14939, "print", lambda: print), _c_(14944, _n_(14940, "generate_random", lambda: generate_random), _n_(14941, "start_range", lambda: start_range), _n_(14942, "end_range", lambda: end_range), _n_(14943, "nums", lambda: nums)))
_l_(14946)