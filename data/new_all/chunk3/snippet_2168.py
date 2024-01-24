# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60293801/typeerror-float-argument-must-be-string-or-number-not-novaluetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import matplotlib.pyplot as plt
    _l_(562402)

except ImportError:
    pass

x = [1, 2, 3]
_l_(562403)

y = [2, 4, 1]
_l_(562404)

_c_(562409, _a_(562406, _n_(562405, "plt", lambda: plt), "plot"), _n_(562407, "x", lambda: x), _n_(562408, "y", lambda: y))
_l_(562410)

_c_(562413, _a_(562412, _n_(562411, "plt", lambda: plt), "xlabel"), 'X - axis')
_l_(562414)

_c_(562417, _a_(562416, _n_(562415, "plt", lambda: plt), "ylabel"), 'y - axis')
_l_(562418)

_c_(562421, _a_(562420, _n_(562419, "plt", lambda: plt), "title"), 'My first graph')
_l_(562422)

_c_(562425, _a_(562424, _n_(562423, "plt", lambda: plt), "show"))
_l_(562426)