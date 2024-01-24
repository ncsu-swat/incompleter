# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47587547/sympy-plot-piecewise-typeerror-not-supported-between-instances-of-complex
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sympy
    _l_(524230)

except ImportError:
    pass
try:
    from sympy.abc import x
    _l_(524232)

except ImportError:
    pass
try:
    from sympy.plotting import plot
    _l_(524234)

except ImportError:
    pass