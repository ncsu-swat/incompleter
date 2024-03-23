# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(31003, _n_(31002, "print", lambda: print), 'Original list:')
_l_(31004)
_c_(31007, _n_(31005, "print", lambda: print), _n_(31006, "list1", lambda: list1))
_l_(31008)
_c_(31010, _n_(31009, "print", lambda: print), '\nAfter deleting the empty lists from the said lists of lists')
_l_(31011)
list2 = [_n_(31012, "x", lambda: x) for x in _n_(31013, "list1", lambda: list1) if _n_(31014, "x", lambda: x)]
_l_(31015)
_c_(31018, _n_(31016, "print", lambda: print), _n_(31017, "list2", lambda: list2))
_l_(31019)