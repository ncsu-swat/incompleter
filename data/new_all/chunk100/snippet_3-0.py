# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(109236)

except ImportError:
    pass
_c_(109239, _n_(109237, "print", lambda: print), 'Original List', _n_(109238, "num", lambda: num))
_l_(109240)
_c_(109243, _a_(109242, _n_(109241, "num", lambda: num), "sort"))
_l_(109244)
new_num = _c_(109251, _n_(109245, "list", lambda: list), (_n_(109246, "num", lambda: num) for num, _ in _c_(109250, _a_(109248, _n_(109247, "itertools", lambda: itertools), "groupby"), _n_(109249, "num", lambda: num))))
_l_(109252)
_c_(109255, _n_(109253, "print", lambda: print), 'New List', _n_(109254, "new_num", lambda: new_num))
_l_(109256)