# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def fibonacci_nums(n):
    _l_(39768)

    if _n_(39752, "n", lambda: n) <= 0:
        _l_(39754)

        aux = [0]
        _l_(39753)
        return aux
    sequence = [0, 1]
    _l_(39755)
    while _c_(39758, _n_(39756, "len", lambda: len), _n_(39757, "sequence", lambda: sequence)) <= _n_(39759, "n", lambda: n):
        _l_(39765)

        _c_(39763, _a_(39761, _n_(39760, "sequence", lambda: sequence), "append"), _n_(39762, "next_value", lambda: next_value))
        _l_(39764)
    aux = _n_(39766, "sequence", lambda: sequence)
    _l_(39767)
    return aux
_c_(39770, _n_(39769, "print", lambda: print), 'First 7 Fibonacci numbers:')
_l_(39771)
_c_(39775, _n_(39772, "print", lambda: print), _c_(39774, _n_(39773, "fibonacci_nums", lambda: fibonacci_nums), 7))
_l_(39776)
_c_(39778, _n_(39777, "print", lambda: print), '\nFirst 15 Fibonacci numbers:')
_l_(39779)
_c_(39783, _n_(39780, "print", lambda: print), _c_(39782, _n_(39781, "fibonacci_nums", lambda: fibonacci_nums), 15))
_l_(39784)
_c_(39786, _n_(39785, "print", lambda: print), '\nFirst 50 Fibonacci numbers:')
_l_(39787)
_c_(39791, _n_(39788, "print", lambda: print), _c_(39790, _n_(39789, "fibonacci_nums", lambda: fibonacci_nums), 50))
_l_(39792)