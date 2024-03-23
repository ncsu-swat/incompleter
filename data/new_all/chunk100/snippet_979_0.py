# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
my_dict = {'x': 500, 'y': 5874, 'z': 560}
_l_(98099)
key_max = _c_(98106, _n_(98100, "max", lambda: max), _c_(98103, _a_(98102, _n_(98101, "my_dict", lambda: my_dict), "keys")), key=lambda k: _n_(98104, "my_dict", lambda: my_dict)[_n_(98105, "k", lambda: k)])
_l_(98107)
_c_(98111, _n_(98108, "print", lambda: print), 'Maximum Value: ', _n_(98109, "my_dict", lambda: my_dict)[_n_(98110, "key_max", lambda: key_max)])
_l_(98112)
_c_(98116, _n_(98113, "print", lambda: print), 'Minimum Value: ', _n_(98114, "my_dict", lambda: my_dict)[_n_(98115, "key_min", lambda: key_min)])
_l_(98117)