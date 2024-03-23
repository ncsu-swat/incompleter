# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from random import shuffle
    _l_(38285)

except ImportError:
    pass

def shuffle_word(text_list):
    _l_(38298)

    text_list = _c_(38288, _n_(38286, "list", lambda: list), _n_(38287, "text_list", lambda: text_list))
    _l_(38289)
    _c_(38292, _n_(38290, "shuffle", lambda: shuffle), _n_(38291, "text_list", lambda: text_list))
    _l_(38293)
    aux = _c_(38296, _a_(38294, '', "join"), _n_(38295, "text_list", lambda: text_list))
    _l_(38297)
    return aux
_c_(38300, _n_(38299, "print", lambda: print), 'Original list:')
_l_(38301)
_c_(38304, _n_(38302, "print", lambda: print), _n_(38303, "text_list", lambda: text_list))
_l_(38305)
_c_(38307, _n_(38306, "print", lambda: print), '\nAfter scrambling the letters of the strings of the said list:')
_l_(38308)
result = [_c_(38311, _n_(38309, "shuffle_word", lambda: shuffle_word), _n_(38310, "word", lambda: word)) for word in _n_(38312, "text_list", lambda: text_list)]
_l_(38313)
_c_(38316, _n_(38314, "print", lambda: print), _n_(38315, "result", lambda: result))
_l_(38317)