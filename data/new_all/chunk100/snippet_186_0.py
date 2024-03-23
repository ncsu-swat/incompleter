# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import choice
    _l_(14747)

except ImportError:
    pass

def generate_random(start_range, end_range, nums):
    _l_(14760)

    result = _c_(14756, _n_(14748, "choice", lambda: choice), [_n_(14749, "i", lambda: i) for i in _c_(14753, _n_(14750, "range", lambda: range), _n_(14751, "start_range", lambda: start_range), _n_(14752, "end_range", lambda: end_range)) if _n_(14754, "i", lambda: i) not in _n_(14755, "nums", lambda: nums)])
    _l_(14757)
    aux = _n_(14758, "result", lambda: result)
    _l_(14759)
    return aux
start_range = 1
_l_(14761)
end_range = 10
_l_(14762)
nums = [2, 9, 10]
_l_(14763)
_c_(14765, _n_(14764, "print", lambda: print), '\nGenerate a number in a specified range (1, 10) except [2, 9, 10]')
_l_(14766)
_c_(14773, _n_(14767, "print", lambda: print), _c_(14772, _n_(14768, "generate_random", lambda: generate_random), _n_(14769, "start_range", lambda: start_range), _n_(14770, "end_range", lambda: end_range), _n_(14771, "nums", lambda: nums)))
_l_(14774)
start_range = -5
_l_(14775)
nums = [-5, 0, 4, 3, 2]
_l_(14776)
_c_(14778, _n_(14777, "print", lambda: print), '\nGenerate a number in a specified range (-5, 5) except [-5,0,4,3,2]')
_l_(14779)
_c_(14786, _n_(14780, "print", lambda: print), _c_(14785, _n_(14781, "generate_random", lambda: generate_random), _n_(14782, "start_range", lambda: start_range), _n_(14783, "end_range", lambda: end_range), _n_(14784, "nums", lambda: nums)))
_l_(14787)