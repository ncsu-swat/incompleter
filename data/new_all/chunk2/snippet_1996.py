# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71321991/accessing-c-sharp-dll-through-python-3-8-using-python-net-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import clr
    _l_(466904)

except ImportError:
    pass

_c_(466907, _a_(466906, _n_(466905, "clr", lambda: clr), "AddReference"), r"calcsDLL")
_l_(466908)
try:
    from myDLL import calcs
    _l_(466910)

except ImportError:
    pass

_c_(466913, _a_(466912, _n_(466911, "calcs", lambda: calcs), "Pipe_Area"), 0.2)
_l_(466914)