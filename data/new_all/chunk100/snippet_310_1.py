# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(29449)

except ImportError:
    pass
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
_l_(29450)
_c_(29452, _n_(29451, "print", lambda: print), 'List to array: ')
_l_(29453)
_c_(29459, _n_(29454, "print", lambda: print), _c_(29458, _a_(29456, _n_(29455, "np", lambda: np), "asarray"), _n_(29457, "my_list", lambda: my_list)))
_l_(29460)
_c_(29462, _n_(29461, "print", lambda: print), 'Tuple to array: ')
_l_(29463)
_c_(29469, _n_(29464, "print", lambda: print), _c_(29468, _a_(29466, _n_(29465, "np", lambda: np), "asarray"), _n_(29467, "my_tuple", lambda: my_tuple)))
_l_(29470)