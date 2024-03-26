# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(109847)

except ImportError:
    pass
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(109848)
_c_(109850, _n_(109849, "print", lambda: print), 'List to array: ')
_l_(109851)
_c_(109857, _n_(109852, "print", lambda: print), _c_(109856, _a_(109854, _n_(109853, "np", lambda: np), "asarray"), _n_(109855, "my_list", lambda: my_list)))
_l_(109858)
_c_(109860, _n_(109859, "print", lambda: print), 'Tuple to array: ')
_l_(109861)
_c_(109867, _n_(109862, "print", lambda: print), _c_(109866, _a_(109864, _n_(109863, "np", lambda: np), "asarray"), _n_(109865, "my_tuple", lambda: my_tuple)))
_l_(109868)