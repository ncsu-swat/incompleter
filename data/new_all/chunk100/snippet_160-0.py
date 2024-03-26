# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_chars(str1, unwanted_chars):
    _l_(102846)

    for i in _n_(102837, "unwanted_chars", lambda: unwanted_chars):
        _l_(102843)

        str1 = _c_(102841, _a_(102839, _n_(102838, "str1", lambda: str1), "replace"), _n_(102840, "i", lambda: i), '')
        _l_(102842)
    aux = _n_(102844, "str1", lambda: str1)
    _l_(102845)
    return aux
str1 = 'Pyth*^on Exercis^es'
_l_(102847)
unwanted_chars = ['#', '*', '!', '^', '%']
_l_(102848)
_c_(102851, _n_(102849, "print", lambda: print), 'Original String : ' + _n_(102850, "str1", lambda: str1))
_l_(102852)
_c_(102854, _n_(102853, "print", lambda: print), 'After removing unwanted characters:')
_l_(102855)
_c_(102861, _n_(102856, "print", lambda: print), _c_(102860, _n_(102857, "remove_chars", lambda: remove_chars), _n_(102858, "str1", lambda: str1), _n_(102859, "unwanted_chars", lambda: unwanted_chars)))
_l_(102862)
_c_(102865, _n_(102863, "print", lambda: print), '\nOriginal String : ' + _n_(102864, "str2", lambda: str2))
_l_(102866)
_c_(102868, _n_(102867, "print", lambda: print), 'After removing unwanted characters:')
_l_(102869)
_c_(102875, _n_(102870, "print", lambda: print), _c_(102874, _n_(102871, "remove_chars", lambda: remove_chars), _n_(102872, "str2", lambda: str2), _n_(102873, "unwanted_chars", lambda: unwanted_chars)))
_l_(102876)