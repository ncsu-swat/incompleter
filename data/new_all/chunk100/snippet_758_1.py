# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(77130, _n_(77129, "print", lambda: print), 'Original List: ')
_l_(77131)
_c_(77134, _n_(77132, "print", lambda: print), _n_(77133, "original_list", lambda: original_list))
_l_(77135)
new_list = [{_n_(77136, "k", lambda: k): _n_(77137, "v", lambda: v) for (k, v) in _c_(77140, _a_(77139, _n_(77138, "d", lambda: d), "items")) if _n_(77141, "k", lambda: k) != 'key1'} for d in _n_(77142, "original_list", lambda: original_list)]
_l_(77143)
_c_(77145, _n_(77144, "print", lambda: print), 'New List: ')
_l_(77146)
_c_(77149, _n_(77147, "print", lambda: print), _n_(77148, "new_list", lambda: new_list))
_l_(77150)