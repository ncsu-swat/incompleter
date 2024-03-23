# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sum_digits_string(str1):
    _l_(93716)

    sum_digit = 0
    _l_(93704)
    for x in _n_(93705, "str1", lambda: str1):
        _l_(93713)

        if _c_(93708, _a_(93707, _n_(93706, "x", lambda: x), "isdigit")) == True:
            _l_(93712)

            sum_digit = _n_(93709, "sum_digit", lambda: sum_digit) + _n_(93710, "z", lambda: z)
            _l_(93711)
    aux = _n_(93714, "sum_digit", lambda: sum_digit)
    _l_(93715)
    return aux
_c_(93720, _n_(93717, "print", lambda: print), _c_(93719, _n_(93718, "sum_digits_string", lambda: sum_digits_string), '123abcd45'))
_l_(93721)
_c_(93725, _n_(93722, "print", lambda: print), _c_(93724, _n_(93723, "sum_digits_string", lambda: sum_digits_string), 'abcd1234'))
_l_(93726)