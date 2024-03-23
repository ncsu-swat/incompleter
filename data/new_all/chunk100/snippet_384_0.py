# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def smallest_multiple(n):
    _l_(38438)

    if _n_(38412, "n", lambda: n) <= 2:
        _l_(38415)

        aux = _n_(38413, "n", lambda: n)
        _l_(38414)
        return aux
    i = _n_(38416, "n", lambda: n) * 2
    _l_(38417)
    _c_(38420, _n_(38418, "print", lambda: print), _n_(38419, "factors", lambda: factors))
    _l_(38421)
    while True:
        _l_(38437)

        for a in _n_(38422, "factors", lambda: factors):
            _l_(38436)

            if _n_(38423, "i", lambda: i) % _n_(38424, "a", lambda: a) != 0:
                _l_(38428)

                i += _n_(38425, "n", lambda: n)
                _l_(38426)
                break
                _l_(38427)
            if _n_(38429, "a", lambda: a) == _n_(38430, "factors", lambda: factors)[-1] and _n_(38431, "i", lambda: i) % _n_(38432, "a", lambda: a) == 0:
                _l_(38435)

                aux = _n_(38433, "i", lambda: i)
                _l_(38434)
                return aux
_c_(38442, _n_(38439, "print", lambda: print), _c_(38441, _n_(38440, "smallest_multiple", lambda: smallest_multiple), 13))
_l_(38443)
_c_(38447, _n_(38444, "print", lambda: print), _c_(38446, _n_(38445, "smallest_multiple", lambda: smallest_multiple), 11))
_l_(38448)
_c_(38452, _n_(38449, "print", lambda: print), _c_(38451, _n_(38450, "smallest_multiple", lambda: smallest_multiple), 2))
_l_(38453)
_c_(38457, _n_(38454, "print", lambda: print), _c_(38456, _n_(38455, "smallest_multiple", lambda: smallest_multiple), 1))
_l_(38458)