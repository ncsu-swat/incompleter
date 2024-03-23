# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def smallest_multiple(n):
    _l_(38490)

    if _n_(38459, "n", lambda: n) <= 2:
        _l_(38462)

        aux = _n_(38460, "n", lambda: n)
        _l_(38461)
        return aux
    factors = [_n_(38463, "number", lambda: number) for number in _c_(38466, _n_(38464, "range", lambda: range), _n_(38465, "n", lambda: n), 1, -1) if _n_(38467, "number", lambda: number) * 2 > _n_(38468, "n", lambda: n)]
    _l_(38469)
    _c_(38472, _n_(38470, "print", lambda: print), _n_(38471, "factors", lambda: factors))
    _l_(38473)
    while True:
        _l_(38489)

        for a in _n_(38474, "factors", lambda: factors):
            _l_(38488)

            if _n_(38475, "i", lambda: i) % _n_(38476, "a", lambda: a) != 0:
                _l_(38480)

                i += _n_(38477, "n", lambda: n)
                _l_(38478)
                break
                _l_(38479)
            if _n_(38481, "a", lambda: a) == _n_(38482, "factors", lambda: factors)[-1] and _n_(38483, "i", lambda: i) % _n_(38484, "a", lambda: a) == 0:
                _l_(38487)

                aux = _n_(38485, "i", lambda: i)
                _l_(38486)
                return aux
_c_(38494, _n_(38491, "print", lambda: print), _c_(38493, _n_(38492, "smallest_multiple", lambda: smallest_multiple), 13))
_l_(38495)
_c_(38499, _n_(38496, "print", lambda: print), _c_(38498, _n_(38497, "smallest_multiple", lambda: smallest_multiple), 11))
_l_(38500)
_c_(38504, _n_(38501, "print", lambda: print), _c_(38503, _n_(38502, "smallest_multiple", lambda: smallest_multiple), 2))
_l_(38505)
_c_(38509, _n_(38506, "print", lambda: print), _c_(38508, _n_(38507, "smallest_multiple", lambda: smallest_multiple), 1))
_l_(38510)