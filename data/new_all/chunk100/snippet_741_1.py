# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst, char):
    _l_(74611)

    result = [_n_(74602, "i", lambda: i) for i in _n_(74603, "lst", lambda: lst) if _c_(74607, _a_(74605, _n_(74604, "i", lambda: i), "startswith"), _n_(74606, "char", lambda: char))]
    _l_(74608)
    aux = _n_(74609, "result", lambda: result)
    _l_(74610)
    return aux
text = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
_l_(74612)
_c_(74614, _n_(74613, "print", lambda: print), '\nOriginal list:')
_l_(74615)
_c_(74618, _n_(74616, "print", lambda: print), _n_(74617, "text", lambda: text))
_l_(74619)
_c_(74622, _n_(74620, "print", lambda: print), '\nItems start with', _n_(74621, "char", lambda: char), 'from the said list:')
_l_(74623)
_c_(74629, _n_(74624, "print", lambda: print), _c_(74628, _n_(74625, "test", lambda: test), _n_(74626, "text", lambda: text), _n_(74627, "char", lambda: char)))
_l_(74630)
char = 'd'
_l_(74631)
_c_(74634, _n_(74632, "print", lambda: print), '\nItems start with', _n_(74633, "char", lambda: char), 'from the said list:')
_l_(74635)
_c_(74641, _n_(74636, "print", lambda: print), _c_(74640, _n_(74637, "test", lambda: test), _n_(74638, "text", lambda: text), _n_(74639, "char", lambda: char)))
_l_(74642)
char = 'w'
_l_(74643)
_c_(74646, _n_(74644, "print", lambda: print), '\nItems start with', _n_(74645, "char", lambda: char), 'from the said list:')
_l_(74647)
_c_(74653, _n_(74648, "print", lambda: print), _c_(74652, _n_(74649, "test", lambda: test), _n_(74650, "text", lambda: text), _n_(74651, "char", lambda: char)))
_l_(74654)