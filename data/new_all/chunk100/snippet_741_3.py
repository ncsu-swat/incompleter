# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(lst, char):
    _l_(74711)

    result = [_n_(74702, "i", lambda: i) for i in _n_(74703, "lst", lambda: lst) if _c_(74707, _a_(74705, _n_(74704, "i", lambda: i), "startswith"), _n_(74706, "char", lambda: char))]
    _l_(74708)
    aux = _n_(74709, "result", lambda: result)
    _l_(74710)
    return aux
text = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
_l_(74712)
_c_(74714, _n_(74713, "print", lambda: print), '\nOriginal list:')
_l_(74715)
_c_(74718, _n_(74716, "print", lambda: print), _n_(74717, "text", lambda: text))
_l_(74719)
char = 'a'
_l_(74720)
_c_(74723, _n_(74721, "print", lambda: print), '\nItems start with', _n_(74722, "char", lambda: char), 'from the said list:')
_l_(74724)
_c_(74730, _n_(74725, "print", lambda: print), _c_(74729, _n_(74726, "test", lambda: test), _n_(74727, "text", lambda: text), _n_(74728, "char", lambda: char)))
_l_(74731)
char = 'd'
_l_(74732)
_c_(74735, _n_(74733, "print", lambda: print), '\nItems start with', _n_(74734, "char", lambda: char), 'from the said list:')
_l_(74736)
_c_(74742, _n_(74737, "print", lambda: print), _c_(74741, _n_(74738, "test", lambda: test), _n_(74739, "text", lambda: text), _n_(74740, "char", lambda: char)))
_l_(74743)
_c_(74746, _n_(74744, "print", lambda: print), '\nItems start with', _n_(74745, "char", lambda: char), 'from the said list:')
_l_(74747)
_c_(74753, _n_(74748, "print", lambda: print), _c_(74752, _n_(74749, "test", lambda: test), _n_(74750, "text", lambda: text), _n_(74751, "char", lambda: char)))
_l_(74754)