# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(73785, _n_(73784, "print", lambda: print), 'Original Dictionary:')
_l_(73786)
_c_(73789, _n_(73787, "print", lambda: print), _n_(73788, "dict1", lambda: dict1))
_l_(73790)
_c_(73792, _n_(73791, "print", lambda: print), 'New Dictionary after dropping empty items:')
_l_(73793)
dict1 = {_n_(73794, "key", lambda: key): _n_(73795, "value", lambda: value) for (key, value) in _c_(73798, _a_(73797, _n_(73796, "dict1", lambda: dict1), "items")) if _n_(73799, "value", lambda: value) is not None}
_l_(73800)
_c_(73803, _n_(73801, "print", lambda: print), _n_(73802, "dict1", lambda: dict1))
_l_(73804)