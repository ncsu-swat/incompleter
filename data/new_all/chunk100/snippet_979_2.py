# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
key_max = _c_(98143, _n_(98137, "max", lambda: max), _c_(98140, _a_(98139, _n_(98138, "my_dict", lambda: my_dict), "keys")), key=lambda k: _n_(98141, "my_dict", lambda: my_dict)[_n_(98142, "k", lambda: k)])
_l_(98144)
key_min = _c_(98151, _n_(98145, "min", lambda: min), _c_(98148, _a_(98147, _n_(98146, "my_dict", lambda: my_dict), "keys")), key=lambda k: _n_(98149, "my_dict", lambda: my_dict)[_n_(98150, "k", lambda: k)])
_l_(98152)
_c_(98156, _n_(98153, "print", lambda: print), 'Maximum Value: ', _n_(98154, "my_dict", lambda: my_dict)[_n_(98155, "key_max", lambda: key_max)])
_l_(98157)
_c_(98161, _n_(98158, "print", lambda: print), 'Minimum Value: ', _n_(98159, "my_dict", lambda: my_dict)[_n_(98160, "key_min", lambda: key_min)])
_l_(98162)