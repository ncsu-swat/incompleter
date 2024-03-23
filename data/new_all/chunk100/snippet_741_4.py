# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst, char):
    _l_(74764)

    result = [_n_(74755, "i", lambda: i) for i in _n_(74756, "lst", lambda: lst) if _c_(74760, _a_(74758, _n_(74757, "i", lambda: i), "startswith"), _n_(74759, "char", lambda: char))]
    _l_(74761)
    aux = _n_(74762, "result", lambda: result)
    _l_(74763)
    return aux
_c_(74766, _n_(74765, "print", lambda: print), '\nOriginal list:')
_l_(74767)
_c_(74770, _n_(74768, "print", lambda: print), _n_(74769, "text", lambda: text))
_l_(74771)
char = 'a'
_l_(74772)
_c_(74775, _n_(74773, "print", lambda: print), '\nItems start with', _n_(74774, "char", lambda: char), 'from the said list:')
_l_(74776)
_c_(74782, _n_(74777, "print", lambda: print), _c_(74781, _n_(74778, "test", lambda: test), _n_(74779, "text", lambda: text), _n_(74780, "char", lambda: char)))
_l_(74783)
char = 'd'
_l_(74784)
_c_(74787, _n_(74785, "print", lambda: print), '\nItems start with', _n_(74786, "char", lambda: char), 'from the said list:')
_l_(74788)
_c_(74794, _n_(74789, "print", lambda: print), _c_(74793, _n_(74790, "test", lambda: test), _n_(74791, "text", lambda: text), _n_(74792, "char", lambda: char)))
_l_(74795)
char = 'w'
_l_(74796)
_c_(74799, _n_(74797, "print", lambda: print), '\nItems start with', _n_(74798, "char", lambda: char), 'from the said list:')
_l_(74800)
_c_(74806, _n_(74801, "print", lambda: print), _c_(74805, _n_(74802, "test", lambda: test), _n_(74803, "text", lambda: text), _n_(74804, "char", lambda: char)))
_l_(74807)