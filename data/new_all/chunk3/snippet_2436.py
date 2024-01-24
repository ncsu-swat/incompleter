# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39141466/python-2-7-typeerror-float-object-has-no-attribute-getitem
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(546290)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(546292)

except ImportError:
    pass

a = 0.75 + (1.25 - 0.75)*_c_(546296, _a_(546295, _a_(546294, _n_(546293, "np", lambda: np), "random"), "lognormal"), 10000)
_l_(546297)

[n,bins,patches] = _c_(546301, _a_(546299, _n_(546298, "plt", lambda: plt), "hist"), _n_(546300, "a", lambda: a), bins=50, color = 'red',alpha = 0.5, normed = True)
_l_(546302)

_c_(546305, _a_(546304, _n_(546303, "plt", lambda: plt), "show"))
_l_(546306)