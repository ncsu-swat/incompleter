# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sieve_of_Eratosthenes(num):
    _l_(55693)

    limitn = _n_(55664, "num", lambda: num) + 1
    _l_(55665)
    prime_nums = []
    _l_(55666)
    for i in _c_(55669, _n_(55667, "range", lambda: range), 2, _n_(55668, "limitn", lambda: limitn)):
        _l_(55690)

        if _n_(55670, "i", lambda: i) in _n_(55671, "not_prime_num", lambda: not_prime_num):
            _l_(55673)

            continue
            _l_(55672)
        for f in _c_(55678, _n_(55674, "range", lambda: range), _n_(55675, "i", lambda: i) * 2, _n_(55676, "limitn", lambda: limitn), _n_(55677, "i", lambda: i)):
            _l_(55684)

            _c_(55682, _a_(55680, _n_(55679, "not_prime_num", lambda: not_prime_num), "add"), _n_(55681, "f", lambda: f))
            _l_(55683)
        _c_(55688, _a_(55686, _n_(55685, "prime_nums", lambda: prime_nums), "append"), _n_(55687, "i", lambda: i))
        _l_(55689)
    aux = _n_(55691, "prime_nums", lambda: prime_nums)
    _l_(55692)
    return aux
_c_(55697, _n_(55694, "print", lambda: print), _c_(55696, _n_(55695, "sieve_of_Eratosthenes", lambda: sieve_of_Eratosthenes), 100))
_l_(55698)