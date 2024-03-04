# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8213522/when-to-use-cla-clf-or-close-for-clearing-a-plot-in-matplotlib
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for i in _c_(62680, _n_(62679, "range", lambda: range), 5):
    _l_(62689)

    fig = _c_(62682, _n_(62681, "plot_figure", lambda: plot_figure))
    _l_(62683)
    _c_(62687, _a_(62685, _n_(62684, "plt", lambda: plt), "close"), _n_(62686, "fig", lambda: fig))
    _l_(62688)
# This returns a list with all figure numbers available
_c_(62694, _n_(62690, "print", lambda: print), _c_(62693, _a_(62692, _n_(62691, "plt", lambda: plt), "get_fignums")))
_l_(62695)

for i in _c_(62697, _n_(62696, "range", lambda: range), 5):
    _l_(62705)

    fig = _c_(62699, _n_(62698, "plot_figure", lambda: plot_figure))
    _l_(62700)
    _c_(62703, _a_(62702, _n_(62701, "fig", lambda: fig), "clf"))
    _l_(62704)
# This returns a list with all figure numbers available
_c_(62710, _n_(62706, "print", lambda: print), _c_(62709, _a_(62708, _n_(62707, "plt", lambda: plt), "get_fignums")))
_l_(62711)
try:
    import numpy as np
    _l_(62713)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(62715)

except ImportError:
    pass
x = _c_(62718, _a_(62717, _n_(62716, "np", lambda: np), "arange"), 1000)
_l_(62719)
y = _c_(62723, _a_(62721, _n_(62720, "np", lambda: np), "sin"), _n_(62722, "x", lambda: x))
_l_(62724)

for i in _c_(62726, _n_(62725, "range", lambda: range), 5):
    _l_(62746)

    fig = _c_(62729, _a_(62728, _n_(62727, "plt", lambda: plt), "figure"))
    _l_(62730)
    ax = _c_(62733, _a_(62732, _n_(62731, "fig", lambda: fig), "add_subplot"), 1, 1, 1)
    _l_(62734)
    _c_(62739, _a_(62736, _n_(62735, "ax", lambda: ax), "plot"), _n_(62737, "x", lambda: x), _n_(62738, "y", lambda: y))
    _l_(62740)
    _c_(62744, _a_(62742, _n_(62741, "plt", lambda: plt), "close"), _n_(62743, "fig", lambda: fig))
    _l_(62745)

_c_(62751, _n_(62747, "print", lambda: print), _c_(62750, _a_(62749, _n_(62748, "plt", lambda: plt), "get_fignums")))
_l_(62752)

for i in _c_(62754, _n_(62753, "range", lambda: range), 5):
    _l_(62773)

    fig = _c_(62757, _a_(62756, _n_(62755, "plt", lambda: plt), "figure"))
    _l_(62758)
    ax = _c_(62761, _a_(62760, _n_(62759, "fig", lambda: fig), "add_subplot"), 1, 1, 1)
    _l_(62762)
    _c_(62767, _a_(62764, _n_(62763, "ax", lambda: ax), "plot"), _n_(62765, "x", lambda: x), _n_(62766, "y", lambda: y))
    _l_(62768)
    _c_(62771, _a_(62770, _n_(62769, "fig", lambda: fig), "clf"))
    _l_(62772)

_c_(62778, _n_(62774, "print", lambda: print), _c_(62777, _a_(62776, _n_(62775, "plt", lambda: plt), "get_fignums")))
_l_(62779)

