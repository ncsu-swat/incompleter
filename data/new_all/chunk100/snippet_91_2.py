# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sum_digits_string(str1):
    _l_(93766)

    sum_digit = 0
    _l_(93753)
    for x in _n_(93754, "str1", lambda: str1):
        _l_(93763)

        if _c_(93757, _a_(93756, _n_(93755, "x", lambda: x), "isdigit")) == True:
            _l_(93762)

            z = _c_(93760, _n_(93758, "int", lambda: int), _n_(93759, "x", lambda: x))
            _l_(93761)
    aux = _n_(93764, "sum_digit", lambda: sum_digit)
    _l_(93765)
    return aux
_c_(93770, _n_(93767, "print", lambda: print), _c_(93769, _n_(93768, "sum_digits_string", lambda: sum_digits_string), '123abcd45'))
_l_(93771)
_c_(93775, _n_(93772, "print", lambda: print), _c_(93774, _n_(93773, "sum_digits_string", lambda: sum_digits_string), 'abcd1234'))
_l_(93776)