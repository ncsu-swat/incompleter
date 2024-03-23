# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def capitalize_first_last_letters(str1):
    _l_(98792)

    str1 = result = _c_(98779, _a_(98778, _n_(98777, "str1", lambda: str1), "title"))
    _l_(98780)
    for word in _c_(98783, _a_(98782, _n_(98781, "str1", lambda: str1), "split")):
        _l_(98789)

        result += _n_(98784, "word", lambda: word)[:-1] + _c_(98787, _a_(98786, _n_(98785, "word", lambda: word)[-1], "upper")) + ' '
        _l_(98788)
    aux = _n_(98790, "result", lambda: result)[:-1]
    _l_(98791)
    return aux
_c_(98796, _n_(98793, "print", lambda: print), _c_(98795, _n_(98794, "capitalize_first_last_letters", lambda: capitalize_first_last_letters), 'python exercises practice solution'))
_l_(98797)
_c_(98801, _n_(98798, "print", lambda: print), _c_(98800, _n_(98799, "capitalize_first_last_letters", lambda: capitalize_first_last_letters), 'w3resource'))
_l_(98802)