# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst, char):
    _l_(74558)

    result = [_n_(74549, "i", lambda: i) for i in _n_(74550, "lst", lambda: lst) if _c_(74554, _a_(74552, _n_(74551, "i", lambda: i), "startswith"), _n_(74553, "char", lambda: char))]
    _l_(74555)
    aux = _n_(74556, "result", lambda: result)
    _l_(74557)
    return aux
text = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
_l_(74559)
_c_(74561, _n_(74560, "print", lambda: print), '\nOriginal list:')
_l_(74562)
_c_(74565, _n_(74563, "print", lambda: print), _n_(74564, "text", lambda: text))
_l_(74566)
char = 'a'
_l_(74567)
_c_(74570, _n_(74568, "print", lambda: print), '\nItems start with', _n_(74569, "char", lambda: char), 'from the said list:')
_l_(74571)
_c_(74577, _n_(74572, "print", lambda: print), _c_(74576, _n_(74573, "test", lambda: test), _n_(74574, "text", lambda: text), _n_(74575, "char", lambda: char)))
_l_(74578)
_c_(74581, _n_(74579, "print", lambda: print), '\nItems start with', _n_(74580, "char", lambda: char), 'from the said list:')
_l_(74582)
_c_(74588, _n_(74583, "print", lambda: print), _c_(74587, _n_(74584, "test", lambda: test), _n_(74585, "text", lambda: text), _n_(74586, "char", lambda: char)))
_l_(74589)
char = 'w'
_l_(74590)
_c_(74593, _n_(74591, "print", lambda: print), '\nItems start with', _n_(74592, "char", lambda: char), 'from the said list:')
_l_(74594)
_c_(74600, _n_(74595, "print", lambda: print), _c_(74599, _n_(74596, "test", lambda: test), _n_(74597, "text", lambda: text), _n_(74598, "char", lambda: char)))
_l_(74601)