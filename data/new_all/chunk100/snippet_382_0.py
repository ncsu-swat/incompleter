# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import shuffle
    _l_(38224)

except ImportError:
    pass

def shuffle_word(text_list):
    _l_(38233)

    _c_(38227, _n_(38225, "shuffle", lambda: shuffle), _n_(38226, "text_list", lambda: text_list))
    _l_(38228)
    aux = _c_(38231, _a_(38229, '', "join"), _n_(38230, "text_list", lambda: text_list))
    _l_(38232)
    return aux
text_list = ['Python', 'list', 'exercises', 'practice', 'solution']
_l_(38234)
_c_(38236, _n_(38235, "print", lambda: print), 'Original list:')
_l_(38237)
_c_(38240, _n_(38238, "print", lambda: print), _n_(38239, "text_list", lambda: text_list))
_l_(38241)
_c_(38243, _n_(38242, "print", lambda: print), '\nAfter scrambling the letters of the strings of the said list:')
_l_(38244)
result = [_c_(38247, _n_(38245, "shuffle_word", lambda: shuffle_word), _n_(38246, "word", lambda: word)) for word in _n_(38248, "text_list", lambda: text_list)]
_l_(38249)
_c_(38252, _n_(38250, "print", lambda: print), _n_(38251, "result", lambda: result))
_l_(38253)