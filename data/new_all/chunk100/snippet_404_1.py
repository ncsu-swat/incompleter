# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def fibonacci_nums(n):
    _l_(39817)

    if _n_(39793, "n", lambda: n) <= 0:
        _l_(39795)

        aux = [0]
        _l_(39794)
        return aux
    while _c_(39798, _n_(39796, "len", lambda: len), _n_(39797, "sequence", lambda: sequence)) <= _n_(39799, "n", lambda: n):
        _l_(39814)

        next_value = _n_(39800, "sequence", lambda: sequence)[_c_(39803, _n_(39801, "len", lambda: len), _n_(39802, "sequence", lambda: sequence)) - 1] + _n_(39804, "sequence", lambda: sequence)[_c_(39807, _n_(39805, "len", lambda: len), _n_(39806, "sequence", lambda: sequence)) - 2]
        _l_(39808)
        _c_(39812, _a_(39810, _n_(39809, "sequence", lambda: sequence), "append"), _n_(39811, "next_value", lambda: next_value))
        _l_(39813)
    aux = _n_(39815, "sequence", lambda: sequence)
    _l_(39816)
    return aux
_c_(39819, _n_(39818, "print", lambda: print), 'First 7 Fibonacci numbers:')
_l_(39820)
_c_(39824, _n_(39821, "print", lambda: print), _c_(39823, _n_(39822, "fibonacci_nums", lambda: fibonacci_nums), 7))
_l_(39825)
_c_(39827, _n_(39826, "print", lambda: print), '\nFirst 15 Fibonacci numbers:')
_l_(39828)
_c_(39832, _n_(39829, "print", lambda: print), _c_(39831, _n_(39830, "fibonacci_nums", lambda: fibonacci_nums), 15))
_l_(39833)
_c_(39835, _n_(39834, "print", lambda: print), '\nFirst 50 Fibonacci numbers:')
_l_(39836)
_c_(39840, _n_(39837, "print", lambda: print), _c_(39839, _n_(39838, "fibonacci_nums", lambda: fibonacci_nums), 50))
_l_(39841)