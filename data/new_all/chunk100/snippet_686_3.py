# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(71084)

except ImportError:
    pass
_c_(71086, _n_(71085, "print", lambda: print), 'Create a list of random integers:')
_l_(71087)
population = _c_(71089, _n_(71088, "range", lambda: range), 0, 100)
_l_(71090)
nums_list = _c_(71094, _a_(71092, _n_(71091, "random", lambda: random), "sample"), _n_(71093, "population", lambda: population), 10)
_l_(71095)
_c_(71098, _n_(71096, "print", lambda: print), _n_(71097, "nums_list", lambda: nums_list))
_l_(71099)
no_elements = 4
_l_(71100)
_c_(71103, _n_(71101, "print", lambda: print), '\nRandomly select', _n_(71102, "no_elements", lambda: no_elements), 'multiple items from the said list:')
_l_(71104)
result_elements = _c_(71109, _a_(71106, _n_(71105, "random", lambda: random), "sample"), _n_(71107, "nums_list", lambda: nums_list), _n_(71108, "no_elements", lambda: no_elements))
_l_(71110)
_c_(71113, _n_(71111, "print", lambda: print), _n_(71112, "result_elements", lambda: result_elements))
_l_(71114)
no_elements = 8
_l_(71115)
_c_(71118, _n_(71116, "print", lambda: print), '\nRandomly select', _n_(71117, "no_elements", lambda: no_elements), 'multiple items from the said list:')
_l_(71119)
_c_(71122, _n_(71120, "print", lambda: print), _n_(71121, "result_elements", lambda: result_elements))
_l_(71123)