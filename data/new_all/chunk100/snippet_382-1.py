# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import shuffle
    _l_(113817)

except ImportError:
    pass

def shuffle_word(text_list):
    _l_(113830)

    text_list = _c_(113820, _n_(113818, "list", lambda: list), _n_(113819, "text_list", lambda: text_list))
    _l_(113821)
    _c_(113824, _n_(113822, "shuffle", lambda: shuffle), _n_(113823, "text_list", lambda: text_list))
    _l_(113825)
    aux = _c_(113828, _a_(113826, '', "join"), _n_(113827, "text_list", lambda: text_list))
    _l_(113829)
    return aux
text_list = ['Python', 'list', 'exercises', 'practice', 'solution']
_l_(113831)
_c_(113833, _n_(113832, "print", lambda: print), 'Original list:')
_l_(113834)
_c_(113837, _n_(113835, "print", lambda: print), _n_(113836, "text_list", lambda: text_list))
_l_(113838)
_c_(113840, _n_(113839, "print", lambda: print), '\nAfter scrambling the letters of the strings of the said list:')
_l_(113841)
_c_(113844, _n_(113842, "print", lambda: print), _n_(113843, "result", lambda: result))
_l_(113845)