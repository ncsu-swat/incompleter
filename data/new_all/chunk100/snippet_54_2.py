# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sieve_of_Eratosthenes(num):
    _l_(55766)

    limitn = _n_(55735, "num", lambda: num) + 1
    _l_(55736)
    not_prime_num = _c_(55738, _n_(55737, "set", lambda: set))
    _l_(55739)
    for i in _c_(55742, _n_(55740, "range", lambda: range), 2, _n_(55741, "limitn", lambda: limitn)):
        _l_(55763)

        if _n_(55743, "i", lambda: i) in _n_(55744, "not_prime_num", lambda: not_prime_num):
            _l_(55746)

            continue
            _l_(55745)
        for f in _c_(55751, _n_(55747, "range", lambda: range), _n_(55748, "i", lambda: i) * 2, _n_(55749, "limitn", lambda: limitn), _n_(55750, "i", lambda: i)):
            _l_(55757)

            _c_(55755, _a_(55753, _n_(55752, "not_prime_num", lambda: not_prime_num), "add"), _n_(55754, "f", lambda: f))
            _l_(55756)
        _c_(55761, _a_(55759, _n_(55758, "prime_nums", lambda: prime_nums), "append"), _n_(55760, "i", lambda: i))
        _l_(55762)
    aux = _n_(55764, "prime_nums", lambda: prime_nums)
    _l_(55765)
    return aux
_c_(55770, _n_(55767, "print", lambda: print), _c_(55769, _n_(55768, "sieve_of_Eratosthenes", lambda: sieve_of_Eratosthenes), 100))
_l_(55771)