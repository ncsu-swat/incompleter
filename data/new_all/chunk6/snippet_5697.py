# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52763000/numpy-code-works-in-repl-script-says-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
"""Softmax."""

scores = [3.0, 1.0, 0.2]
_l_(344076)
try:
    import numpy as np
    _l_(344078)

except ImportError:
    pass
try:
    from math import e
    _l_(344080)

except ImportError:
    pass

def softmax(x):
    _l_(344128)

    """Compute softmax values for each sets of scores in x."""
    results = []
    _l_(344081)
    x = _c_(344085, _a_(344083, _n_(344082, "np", lambda: np), "transpose"), _n_(344084, "x", lambda: x))
    _l_(344086)
    for j in _c_(344091, _n_(344087, "range", lambda: range), _c_(344090, _n_(344088, "len", lambda: len), _n_(344089, "x", lambda: x))):
        _l_(344117)

        exps = [_c_(344095, _a_(344093, _n_(344092, "np", lambda: np), "exp"), _n_(344094, "s", lambda: s)) for s in _n_(344096, "x", lambda: x)[_n_(344097, "j", lambda: j)]]
        _l_(344098)
        _sum = _c_(344106, _a_(344100, _n_(344099, "np", lambda: np), "sum"), _c_(344105, _a_(344102, _n_(344101, "np", lambda: np), "exp"), _n_(344103, "x", lambda: x)[_n_(344104, "j", lambda: j)]))
        _l_(344107)
        softmax = [_n_(344108, "i", lambda: i) / _n_(344109, "_sum", lambda: _sum) for i in _n_(344110, "exps", lambda: exps)]
        _l_(344111)
        _c_(344115, _a_(344113, _n_(344112, "results", lambda: results), "append"), _n_(344114, "softmax", lambda: softmax))
        _l_(344116)
    final = _c_(344121, _a_(344119, _n_(344118, "np", lambda: np), "vstack"), _n_(344120, "results", lambda: results))
    _l_(344122)
    aux = _c_(344126, _a_(344124, _n_(344123, "np", lambda: np), "transpose"), _n_(344125, "final", lambda: final))
    _l_(344127)
    return aux
#    pass  # TODO: Compute and return softmax(x)


_c_(344133, _n_(344129, "print", lambda: print), _c_(344132, _n_(344130, "softmax", lambda: softmax), _n_(344131, "scores", lambda: scores)))
_l_(344134)
try:
    import matplotlib.pyplot as plt
    _l_(344136)

except ImportError:
    pass
x = _c_(344139, _a_(344138, _n_(344137, "np", lambda: np), "arange"), -2.0, 6.0, 0.1)
_l_(344140)
scores = _c_(344152, _a_(344142, _n_(344141, "np", lambda: np), "vstack"), [_n_(344143, "x", lambda: x), _c_(344147, _a_(344145, _n_(344144, "np", lambda: np), "ones_like"), _n_(344146, "x", lambda: x)), 0.2 * _c_(344151, _a_(344149, _n_(344148, "np", lambda: np), "ones_like"), _n_(344150, "x", lambda: x))])
_l_(344153)

_c_(344161, _a_(344155, _n_(344154, "plt", lambda: plt), "plot"), _n_(344156, "x", lambda: x), _a_(344160, _c_(344159, _n_(344157, "softmax", lambda: softmax), _n_(344158, "scores", lambda: scores)), "T"), linewidth=2)
_l_(344162)
_c_(344165, _a_(344164, _n_(344163, "plt", lambda: plt), "show"))
_l_(344166)