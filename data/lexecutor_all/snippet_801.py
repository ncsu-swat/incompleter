# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/363944/python-idiom-to-return-first-item-or-none
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
first = lambda l, default=None: _c_(1539694, _n_(1539689, "next", lambda: next), _c_(1539692, _n_(1539690, "iter", lambda: iter), _n_(1539691, "l", lambda: l) or []), _n_(1539693, "default", lambda: default))
_l_(1539695)

