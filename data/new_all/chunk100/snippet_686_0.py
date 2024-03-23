# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(70953)

except ImportError:
    pass
_c_(70955, _n_(70954, "print", lambda: print), 'Create a list of random integers:')
_l_(70956)
nums_list = _c_(70960, _a_(70958, _n_(70957, "random", lambda: random), "sample"), _n_(70959, "population", lambda: population), 10)
_l_(70961)
_c_(70964, _n_(70962, "print", lambda: print), _n_(70963, "nums_list", lambda: nums_list))
_l_(70965)
no_elements = 4
_l_(70966)
_c_(70969, _n_(70967, "print", lambda: print), '\nRandomly select', _n_(70968, "no_elements", lambda: no_elements), 'multiple items from the said list:')
_l_(70970)
result_elements = _c_(70975, _a_(70972, _n_(70971, "random", lambda: random), "sample"), _n_(70973, "nums_list", lambda: nums_list), _n_(70974, "no_elements", lambda: no_elements))
_l_(70976)
_c_(70979, _n_(70977, "print", lambda: print), _n_(70978, "result_elements", lambda: result_elements))
_l_(70980)
no_elements = 8
_l_(70981)
_c_(70984, _n_(70982, "print", lambda: print), '\nRandomly select', _n_(70983, "no_elements", lambda: no_elements), 'multiple items from the said list:')
_l_(70985)
result_elements = _c_(70990, _a_(70987, _n_(70986, "random", lambda: random), "sample"), _n_(70988, "nums_list", lambda: nums_list), _n_(70989, "no_elements", lambda: no_elements))
_l_(70991)
_c_(70994, _n_(70992, "print", lambda: print), _n_(70993, "result_elements", lambda: result_elements))
_l_(70995)