# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sum_digits_string(str1):
    _l_(93742)

    for x in _n_(93727, "str1", lambda: str1):
        _l_(93739)

        if _c_(93730, _a_(93729, _n_(93728, "x", lambda: x), "isdigit")) == True:
            _l_(93738)

            z = _c_(93733, _n_(93731, "int", lambda: int), _n_(93732, "x", lambda: x))
            _l_(93734)
            sum_digit = _n_(93735, "sum_digit", lambda: sum_digit) + _n_(93736, "z", lambda: z)
            _l_(93737)
    aux = _n_(93740, "sum_digit", lambda: sum_digit)
    _l_(93741)
    return aux
_c_(93746, _n_(93743, "print", lambda: print), _c_(93745, _n_(93744, "sum_digits_string", lambda: sum_digits_string), '123abcd45'))
_l_(93747)
_c_(93751, _n_(93748, "print", lambda: print), _c_(93750, _n_(93749, "sum_digits_string", lambda: sum_digits_string), 'abcd1234'))
_l_(93752)