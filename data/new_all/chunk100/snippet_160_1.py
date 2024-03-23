# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_chars(str1, unwanted_chars):
    _l_(10853)

    for i in _n_(10844, "unwanted_chars", lambda: unwanted_chars):
        _l_(10850)

        str1 = _c_(10848, _a_(10846, _n_(10845, "str1", lambda: str1), "replace"), _n_(10847, "i", lambda: i), '')
        _l_(10849)
    aux = _n_(10851, "str1", lambda: str1)
    _l_(10852)
    return aux
str1 = 'Pyth*^on Exercis^es'
_l_(10854)
unwanted_chars = ['#', '*', '!', '^', '%']
_l_(10855)
_c_(10858, _n_(10856, "print", lambda: print), 'Original String : ' + _n_(10857, "str1", lambda: str1))
_l_(10859)
_c_(10861, _n_(10860, "print", lambda: print), 'After removing unwanted characters:')
_l_(10862)
_c_(10868, _n_(10863, "print", lambda: print), _c_(10867, _n_(10864, "remove_chars", lambda: remove_chars), _n_(10865, "str1", lambda: str1), _n_(10866, "unwanted_chars", lambda: unwanted_chars)))
_l_(10869)
_c_(10872, _n_(10870, "print", lambda: print), '\nOriginal String : ' + _n_(10871, "str2", lambda: str2))
_l_(10873)
_c_(10875, _n_(10874, "print", lambda: print), 'After removing unwanted characters:')
_l_(10876)
_c_(10882, _n_(10877, "print", lambda: print), _c_(10881, _n_(10878, "remove_chars", lambda: remove_chars), _n_(10879, "str2", lambda: str2), _n_(10880, "unwanted_chars", lambda: unwanted_chars)))
_l_(10883)