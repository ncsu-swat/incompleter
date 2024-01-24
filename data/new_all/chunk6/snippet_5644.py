# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49543553/name-error-when-calculating-the-average-error-between-two-data-sets
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy
    _l_(343588)

except ImportError:
    pass
try:
    from numpy import *
    _l_(343590)

except ImportError:
    pass
try:
    import scipy
    _l_(343592)

except ImportError:
    pass
try:
    import scipy.stats
    _l_(343594)

except ImportError:
    pass
try:
    import matplotlib. pyplot as plt
    _l_(343596)

except ImportError:
    pass
try:
    import matplotlib.patches as patches
    _l_(343598)

except ImportError:
    pass
try:
    from pylab import *
    _l_(343600)

except ImportError:
    pass
try:
    import scipy.integrate
    _l_(343602)

except ImportError:
    pass
try:
    from operator import itemgetter, attrgetter
    _l_(343604)

except ImportError:
    pass
try:
    import sys
    _l_(343606)

except ImportError:
    pass

def main(argv):
    _l_(343627)

    t = _c_(343610, _n_(343607, "open", lambda: open), _a_(343609, _n_(343608, "sys", lambda: sys), "argv")[1])
    _l_(343611)
    first1 = _c_(343614, _a_(343613, _n_(343612, "t", lambda: t), "readline"))
    _l_(343615)

    tt = _c_(343618, _n_(343616, "open", lambda: open), _n_(343617, "argv", lambda: argv)[2])
    _l_(343619)
    second2 = _c_(343622, _a_(343621, _n_(343620, "tt", lambda: tt), "readline"))
    _l_(343623)
    aux = [_n_(343624, "first1", lambda: first1)], [_n_(343625, "second2", lambda: second2)]
    _l_(343626)
    return aux

def analysis(first1, second2):
    _l_(343649)


    first = _c_(343633, _a_(343629, _n_(343628, "np", lambda: np), "array"), _n_(343630, "first1", lambda: first1), dtype = _a_(343632, _n_(343631, "np", lambda: np), "float64"))
    _l_(343634)
    second = _c_(343640, _a_(343636, _n_(343635, "np", lambda: np), "array"), _n_(343637, "second2", lambda: second2), dtype = _a_(343639, _n_(343638, "np", lambda: np), "float64"))
    _l_(343641)

    #Average error
    avgerr = _c_(343645, _a_(343644, (_n_(343642, "first", lambda: first) - _n_(343643, "second", lambda: second)), "mean"))
    _l_(343646)
    aux = [_n_(343647, "avgerr", lambda: avgerr)]
    _l_(343648)

    return aux

_c_(343653, _n_(343650, "analysis", lambda: analysis), _n_(343651, "first1", lambda: first1), _n_(343652, "second2", lambda: second2))
_l_(343654)

if _n_(343655, "__name__", lambda: __name__) == '__main__':
    _l_(343664)

    _c_(343662, _a_(343657, _n_(343656, "sys", lambda: sys), "exit"), _c_(343661, _n_(343658, "main", lambda: main), _a_(343660, _n_(343659, "sys", lambda: sys), "argv")))
    _l_(343663)