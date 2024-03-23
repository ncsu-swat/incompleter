# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def capitalize_first_last_letters(str1):
    _l_(98766)

    result = ''
    _l_(98754)
    for word in _c_(98757, _a_(98756, _n_(98755, "str1", lambda: str1), "split")):
        _l_(98763)

        result += _n_(98758, "word", lambda: word)[:-1] + _c_(98761, _a_(98760, _n_(98759, "word", lambda: word)[-1], "upper")) + ' '
        _l_(98762)
    aux = _n_(98764, "result", lambda: result)[:-1]
    _l_(98765)
    return aux
_c_(98770, _n_(98767, "print", lambda: print), _c_(98769, _n_(98768, "capitalize_first_last_letters", lambda: capitalize_first_last_letters), 'python exercises practice solution'))
_l_(98771)
_c_(98775, _n_(98772, "print", lambda: print), _c_(98774, _n_(98773, "capitalize_first_last_letters", lambda: capitalize_first_last_letters), 'w3resource'))
_l_(98776)