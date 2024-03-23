# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(71038)

except ImportError:
    pass
_c_(71040, _n_(71039, "print", lambda: print), 'Create a list of random integers:')
_l_(71041)
population = _c_(71043, _n_(71042, "range", lambda: range), 0, 100)
_l_(71044)
nums_list = _c_(71048, _a_(71046, _n_(71045, "random", lambda: random), "sample"), _n_(71047, "population", lambda: population), 10)
_l_(71049)
_c_(71052, _n_(71050, "print", lambda: print), _n_(71051, "nums_list", lambda: nums_list))
_l_(71053)
no_elements = 4
_l_(71054)
_c_(71057, _n_(71055, "print", lambda: print), '\nRandomly select', _n_(71056, "no_elements", lambda: no_elements), 'multiple items from the said list:')
_l_(71058)
result_elements = _c_(71063, _a_(71060, _n_(71059, "random", lambda: random), "sample"), _n_(71061, "nums_list", lambda: nums_list), _n_(71062, "no_elements", lambda: no_elements))
_l_(71064)
_c_(71067, _n_(71065, "print", lambda: print), _n_(71066, "result_elements", lambda: result_elements))
_l_(71068)
_c_(71071, _n_(71069, "print", lambda: print), '\nRandomly select', _n_(71070, "no_elements", lambda: no_elements), 'multiple items from the said list:')
_l_(71072)
result_elements = _c_(71077, _a_(71074, _n_(71073, "random", lambda: random), "sample"), _n_(71075, "nums_list", lambda: nums_list), _n_(71076, "no_elements", lambda: no_elements))
_l_(71078)
_c_(71081, _n_(71079, "print", lambda: print), _n_(71080, "result_elements", lambda: result_elements))
_l_(71082)