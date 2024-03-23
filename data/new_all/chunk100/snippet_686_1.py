# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(70997)

except ImportError:
    pass
_c_(70999, _n_(70998, "print", lambda: print), 'Create a list of random integers:')
_l_(71000)
population = _c_(71002, _n_(71001, "range", lambda: range), 0, 100)
_l_(71003)
nums_list = _c_(71007, _a_(71005, _n_(71004, "random", lambda: random), "sample"), _n_(71006, "population", lambda: population), 10)
_l_(71008)
_c_(71011, _n_(71009, "print", lambda: print), _n_(71010, "nums_list", lambda: nums_list))
_l_(71012)
no_elements = 4
_l_(71013)
_c_(71016, _n_(71014, "print", lambda: print), '\nRandomly select', _n_(71015, "no_elements", lambda: no_elements), 'multiple items from the said list:')
_l_(71017)
_c_(71020, _n_(71018, "print", lambda: print), _n_(71019, "result_elements", lambda: result_elements))
_l_(71021)
no_elements = 8
_l_(71022)
_c_(71025, _n_(71023, "print", lambda: print), '\nRandomly select', _n_(71024, "no_elements", lambda: no_elements), 'multiple items from the said list:')
_l_(71026)
result_elements = _c_(71031, _a_(71028, _n_(71027, "random", lambda: random), "sample"), _n_(71029, "nums_list", lambda: nums_list), _n_(71030, "no_elements", lambda: no_elements))
_l_(71032)
_c_(71035, _n_(71033, "print", lambda: print), _n_(71034, "result_elements", lambda: result_elements))
_l_(71036)