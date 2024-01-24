# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55564403/numba-indexing-error-typeerror-cant-index-at-0-in-i8
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numba import vectorize
    _l_(391959)

except ImportError:
    pass
try:
    import numpy as np
    _l_(391961)

except ImportError:
    pass
try:
    from timeit import timeit
    _l_(391963)

except ImportError:
    pass

@_n_(391964, "vectorize", lambda: vectorize)
def fib(n):
    _l_(391999)

    '''
    Adjusted from:
    https://lectures.quantecon.org/py/numba.html
    https://en.wikipedia.org/wiki/Fibonacci_number
    https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
    '''
    _l_(391965)

    if _n_(391966, "n", lambda: n) == 1:
        _l_(391998)

        aux = _c_(391969, _a_(391968, _n_(391967, "np", lambda: np), "ones"), 1)
        _l_(391970)
        return aux
    elif _n_(391971, "n", lambda: n) > 1:
        _l_(391997)

        x = _c_(391975, _a_(391973, _n_(391972, "np", lambda: np), "empty"), _n_(391974, "n", lambda: n))
        _l_(391976)
        _n_(391977, "x", lambda: x)[0] = 1
        _l_(391978)
        _n_(391979, "x", lambda: x)[1] = 1
        _l_(391980)
        for i in _c_(391983, _n_(391981, "range", lambda: range), 2,_n_(391982, "n", lambda: n)):
            _l_(391991)

            _n_(391984, "x", lambda: x)[_n_(391985, "i", lambda: i)] =  _n_(391986, "x", lambda: x)[_n_(391987, "i", lambda: i)-1] + _n_(391988, "x", lambda: x)[_n_(391989, "i", lambda: i)-2]
            _l_(391990)
        aux = _n_(391992, "x", lambda: x)
        _l_(391993)
        return aux
    else:
        _c_(391995, _n_(391994, "print", lambda: print), 'WARNING: Check validity of input.')
        _l_(391996)


_c_(392004, _n_(392000, "print", lambda: print), _c_(392003, _n_(392001, "timeit", lambda: timeit), 'fib(10)', globals={'fib':_n_(392002, "fib", lambda: fib)}))
_l_(392005)