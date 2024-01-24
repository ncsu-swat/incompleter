# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64510938/keep-getting-this-typeerror-str-object-is-not-callable-for-trying-to-plot-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numpy import *
    _l_(568699)

except ImportError:
    pass
try:
    from matplotlib import *
    _l_(568701)

except ImportError:
    pass

a = [1, 2, 3, 4, 5]
_l_(568702)
b = [2, 3, 2, 3, 2]
_l_(568703)
_c_(568708, _a_(568705, _n_(568704, "pyplot", lambda: pyplot), "plot"), _n_(568706, "a", lambda: a), _n_(568707, "b", lambda: b))
_l_(568709)
_c_(568712, _a_(568711, _n_(568710, "pylab", lambda: pylab), "xlabel"), "Time")
_l_(568713)
_c_(568716, _a_(568715, _n_(568714, "pylab", lambda: pylab), "ylabel"), "Speed")
_l_(568717)