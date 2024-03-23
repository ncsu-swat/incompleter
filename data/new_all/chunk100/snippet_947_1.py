# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(95075)

except ImportError:
    pass
_c_(95077, _n_(95076, "print", lambda: print), 'Original list:')
_l_(95078)
_c_(95081, _n_(95079, "print", lambda: print), _n_(95080, "language", lambda: language))
_l_(95082)
cnt = _c_(95085, _n_(95083, "Counter", lambda: Counter), _n_(95084, "language", lambda: language))
_l_(95086)
_c_(95088, _n_(95087, "print", lambda: print), '\nMost common element of the said list:')
_l_(95089)
_c_(95094, _n_(95090, "print", lambda: print), _c_(95093, _a_(95092, _n_(95091, "cnt", lambda: cnt), "most_common"), 1)[0][0])
_l_(95095)