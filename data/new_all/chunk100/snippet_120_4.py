# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(8233)

except ImportError:
    pass
l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
_l_(8234)
l2 = [1, 1, 2, 4, 5, 6]
_l_(8235)
_c_(8237, _n_(8236, "print", lambda: print), 'Original lists:')
_l_(8238)
c1 = _c_(8241, _n_(8239, "Counter", lambda: Counter), _n_(8240, "l1", lambda: l1))
_l_(8242)
c2 = _c_(8245, _n_(8243, "Counter", lambda: Counter), _n_(8244, "l2", lambda: l2))
_l_(8246)
_c_(8253, _n_(8247, "print", lambda: print), _c_(8252, _n_(8248, "list", lambda: list), _c_(8251, _a_(8250, _n_(8249, "diff", lambda: diff), "elements"))))
_l_(8254)