# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50845106/matplotlib-ylabel-typeerror-str-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numpy import *
    _l_(409007)

except ImportError:
    pass
try:
    from matplotlib import *
    _l_(409009)

except ImportError:
    pass

a = [1, 2, 3, 4, 5]
_l_(409010)
b = [2, 3, 2, 3, 2]
_l_(409011)
_c_(409016, _a_(409013, _n_(409012, "pyplot", lambda: pyplot), "plot"), _n_(409014, "a", lambda: a), _n_(409015, "b", lambda: b))
_l_(409017)
_c_(409020, _a_(409019, _n_(409018, "pylab", lambda: pylab), "xlabel"), "Time")
_l_(409021)
_c_(409024, _a_(409023, _n_(409022, "pylab", lambda: pylab), "ylabel"), "Speed")
_l_(409025)