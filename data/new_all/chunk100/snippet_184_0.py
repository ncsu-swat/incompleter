# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def first_repeated_word(str1):
    _l_(14606)

    for word in _c_(14593, _a_(14592, _n_(14591, "str1", lambda: str1), "split")):
        _l_(14604)

        if _n_(14594, "word", lambda: word) in _n_(14595, "temp", lambda: temp):
            _l_(14603)

            aux = _n_(14596, "word", lambda: word)
            _l_(14597)
            return aux
        else:
            _c_(14601, _a_(14599, _n_(14598, "temp", lambda: temp), "add"), _n_(14600, "word", lambda: word))
            _l_(14602)
    aux = 'None'
    _l_(14605)
    return aux
_c_(14610, _n_(14607, "print", lambda: print), _c_(14609, _n_(14608, "first_repeated_word", lambda: first_repeated_word), 'ab ca bc ab'))
_l_(14611)
_c_(14615, _n_(14612, "print", lambda: print), _c_(14614, _n_(14613, "first_repeated_word", lambda: first_repeated_word), 'ab ca bc ab ca ab bc'))
_l_(14616)
_c_(14620, _n_(14617, "print", lambda: print), _c_(14619, _n_(14618, "first_repeated_word", lambda: first_repeated_word), 'ab ca bc ca ab bc'))
_l_(14621)
_c_(14625, _n_(14622, "print", lambda: print), _c_(14624, _n_(14623, "first_repeated_word", lambda: first_repeated_word), 'ab ca bc'))
_l_(14626)