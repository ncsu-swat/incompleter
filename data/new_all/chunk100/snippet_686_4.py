# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(71125)

except ImportError:
    pass
_c_(71127, _n_(71126, "print", lambda: print), 'Create a list of random integers:')
_l_(71128)
population = _c_(71130, _n_(71129, "range", lambda: range), 0, 100)
_l_(71131)
nums_list = _c_(71135, _a_(71133, _n_(71132, "random", lambda: random), "sample"), _n_(71134, "population", lambda: population), 10)
_l_(71136)
_c_(71139, _n_(71137, "print", lambda: print), _n_(71138, "nums_list", lambda: nums_list))
_l_(71140)
_c_(71143, _n_(71141, "print", lambda: print), '\nRandomly select', _n_(71142, "no_elements", lambda: no_elements), 'multiple items from the said list:')
_l_(71144)
result_elements = _c_(71149, _a_(71146, _n_(71145, "random", lambda: random), "sample"), _n_(71147, "nums_list", lambda: nums_list), _n_(71148, "no_elements", lambda: no_elements))
_l_(71150)
_c_(71153, _n_(71151, "print", lambda: print), _n_(71152, "result_elements", lambda: result_elements))
_l_(71154)
no_elements = 8
_l_(71155)
_c_(71158, _n_(71156, "print", lambda: print), '\nRandomly select', _n_(71157, "no_elements", lambda: no_elements), 'multiple items from the said list:')
_l_(71159)
result_elements = _c_(71164, _a_(71161, _n_(71160, "random", lambda: random), "sample"), _n_(71162, "nums_list", lambda: nums_list), _n_(71163, "no_elements", lambda: no_elements))
_l_(71165)
_c_(71168, _n_(71166, "print", lambda: print), _n_(71167, "result_elements", lambda: result_elements))
_l_(71169)