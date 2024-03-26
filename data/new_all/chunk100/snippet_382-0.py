# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import shuffle
    _l_(113783)

except ImportError:
    pass

def shuffle_word(text_list):
    _l_(113796)

    text_list = _c_(113786, _n_(113784, "list", lambda: list), _n_(113785, "text_list", lambda: text_list))
    _l_(113787)
    _c_(113790, _n_(113788, "shuffle", lambda: shuffle), _n_(113789, "text_list", lambda: text_list))
    _l_(113791)
    aux = _c_(113794, _a_(113792, '', "join"), _n_(113793, "text_list", lambda: text_list))
    _l_(113795)
    return aux
_c_(113798, _n_(113797, "print", lambda: print), 'Original list:')
_l_(113799)
_c_(113802, _n_(113800, "print", lambda: print), _n_(113801, "text_list", lambda: text_list))
_l_(113803)
_c_(113805, _n_(113804, "print", lambda: print), '\nAfter scrambling the letters of the strings of the said list:')
_l_(113806)
result = [_c_(113809, _n_(113807, "shuffle_word", lambda: shuffle_word), _n_(113808, "word", lambda: word)) for word in _n_(113810, "text_list", lambda: text_list)]
_l_(113811)
_c_(113814, _n_(113812, "print", lambda: print), _n_(113813, "result", lambda: result))
_l_(113815)