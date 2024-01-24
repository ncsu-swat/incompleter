# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47251752/matplotlib-pyplot-hist-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(528101)

except ImportError:
    pass
try:
    import numpy as np
    _l_(528103)

except ImportError:
    pass


test = [_c_(528107, _a_(528106, _a_(528105, _n_(528104, "np", lambda: np), "random"), "randn")) for i in _c_(528109, _n_(528108, "range", lambda: range), 100)]
_l_(528110)

_c_(528114, _a_(528112, _n_(528111, "plt", lambda: plt), "hist"), _n_(528113, "test", lambda: test))
_l_(528115)
_c_(528118, _a_(528117, _n_(528116, "plt", lambda: plt), "show"))
_l_(528119)