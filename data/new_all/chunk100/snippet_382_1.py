# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import shuffle
    _l_(38255)

except ImportError:
    pass

def shuffle_word(text_list):
    _l_(38268)

    text_list = _c_(38258, _n_(38256, "list", lambda: list), _n_(38257, "text_list", lambda: text_list))
    _l_(38259)
    _c_(38262, _n_(38260, "shuffle", lambda: shuffle), _n_(38261, "text_list", lambda: text_list))
    _l_(38263)
    aux = _c_(38266, _a_(38264, '', "join"), _n_(38265, "text_list", lambda: text_list))
    _l_(38267)
    return aux
text_list = ['Python', 'list', 'exercises', 'practice', 'solution']
_l_(38269)
_c_(38271, _n_(38270, "print", lambda: print), 'Original list:')
_l_(38272)
_c_(38275, _n_(38273, "print", lambda: print), _n_(38274, "text_list", lambda: text_list))
_l_(38276)
_c_(38278, _n_(38277, "print", lambda: print), '\nAfter scrambling the letters of the strings of the said list:')
_l_(38279)
_c_(38282, _n_(38280, "print", lambda: print), _n_(38281, "result", lambda: result))
_l_(38283)