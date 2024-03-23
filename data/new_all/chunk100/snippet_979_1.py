# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
my_dict = {'x': 500, 'y': 5874, 'z': 560}
_l_(98118)
key_min = _c_(98125, _n_(98119, "min", lambda: min), _c_(98122, _a_(98121, _n_(98120, "my_dict", lambda: my_dict), "keys")), key=lambda k: _n_(98123, "my_dict", lambda: my_dict)[_n_(98124, "k", lambda: k)])
_l_(98126)
_c_(98130, _n_(98127, "print", lambda: print), 'Maximum Value: ', _n_(98128, "my_dict", lambda: my_dict)[_n_(98129, "key_max", lambda: key_max)])
_l_(98131)
_c_(98135, _n_(98132, "print", lambda: print), 'Minimum Value: ', _n_(98133, "my_dict", lambda: my_dict)[_n_(98134, "key_min", lambda: key_min)])
_l_(98136)