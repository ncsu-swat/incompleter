# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8220801/how-to-use-timeit-module
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import timeit
    _l_(64469)

except ImportError:
    pass

start_time = _c_(64472, _a_(64471, _n_(64470, "timeit", lambda: timeit), "default_timer"))
_l_(64473)
_c_(64475, _n_(64474, "func1", lambda: func1))
_l_(64476)
_c_(64482, _n_(64477, "print", lambda: print), _c_(64480, _a_(64479, _n_(64478, "timeit", lambda: timeit), "default_timer")) - _n_(64481, "start_time", lambda: start_time))
_l_(64483)

start_time = _c_(64486, _a_(64485, _n_(64484, "timeit", lambda: timeit), "default_timer"))
_l_(64487)
_c_(64489, _n_(64488, "func2", lambda: func2))
_l_(64490)
_c_(64496, _n_(64491, "print", lambda: print), _c_(64494, _a_(64493, _n_(64492, "timeit", lambda: timeit), "default_timer")) - _n_(64495, "start_time", lambda: start_time))
_l_(64497)

