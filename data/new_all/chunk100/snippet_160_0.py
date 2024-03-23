# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_chars(str1, unwanted_chars):
    _l_(10813)

    for i in _n_(10804, "unwanted_chars", lambda: unwanted_chars):
        _l_(10810)

        str1 = _c_(10808, _a_(10806, _n_(10805, "str1", lambda: str1), "replace"), _n_(10807, "i", lambda: i), '')
        _l_(10809)
    aux = _n_(10811, "str1", lambda: str1)
    _l_(10812)
    return aux
str2 = 'A%^!B#*CD'
_l_(10814)
unwanted_chars = ['#', '*', '!', '^', '%']
_l_(10815)
_c_(10818, _n_(10816, "print", lambda: print), 'Original String : ' + _n_(10817, "str1", lambda: str1))
_l_(10819)
_c_(10821, _n_(10820, "print", lambda: print), 'After removing unwanted characters:')
_l_(10822)
_c_(10828, _n_(10823, "print", lambda: print), _c_(10827, _n_(10824, "remove_chars", lambda: remove_chars), _n_(10825, "str1", lambda: str1), _n_(10826, "unwanted_chars", lambda: unwanted_chars)))
_l_(10829)
_c_(10832, _n_(10830, "print", lambda: print), '\nOriginal String : ' + _n_(10831, "str2", lambda: str2))
_l_(10833)
_c_(10835, _n_(10834, "print", lambda: print), 'After removing unwanted characters:')
_l_(10836)
_c_(10842, _n_(10837, "print", lambda: print), _c_(10841, _n_(10838, "remove_chars", lambda: remove_chars), _n_(10839, "str2", lambda: str2), _n_(10840, "unwanted_chars", lambda: unwanted_chars)))
_l_(10843)