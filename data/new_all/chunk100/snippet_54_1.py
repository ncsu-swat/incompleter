# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sieve_of_Eratosthenes(num):
    _l_(55729)

    not_prime_num = _c_(55700, _n_(55699, "set", lambda: set))
    _l_(55701)
    prime_nums = []
    _l_(55702)
    for i in _c_(55705, _n_(55703, "range", lambda: range), 2, _n_(55704, "limitn", lambda: limitn)):
        _l_(55726)

        if _n_(55706, "i", lambda: i) in _n_(55707, "not_prime_num", lambda: not_prime_num):
            _l_(55709)

            continue
            _l_(55708)
        for f in _c_(55714, _n_(55710, "range", lambda: range), _n_(55711, "i", lambda: i) * 2, _n_(55712, "limitn", lambda: limitn), _n_(55713, "i", lambda: i)):
            _l_(55720)

            _c_(55718, _a_(55716, _n_(55715, "not_prime_num", lambda: not_prime_num), "add"), _n_(55717, "f", lambda: f))
            _l_(55719)
        _c_(55724, _a_(55722, _n_(55721, "prime_nums", lambda: prime_nums), "append"), _n_(55723, "i", lambda: i))
        _l_(55725)
    aux = _n_(55727, "prime_nums", lambda: prime_nums)
    _l_(55728)
    return aux
_c_(55733, _n_(55730, "print", lambda: print), _c_(55732, _n_(55731, "sieve_of_Eratosthenes", lambda: sieve_of_Eratosthenes), 100))
_l_(55734)