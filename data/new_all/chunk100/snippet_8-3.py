# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def inset_element_list(lst, x, n):
    _l_(120555)

    i = _n_(120538, "n", lambda: n)
    _l_(120539)
    while _n_(120540, "i", lambda: i) < _c_(120543, _n_(120541, "len", lambda: len), _n_(120542, "lst", lambda: lst)):
        _l_(120552)

        _c_(120548, _a_(120545, _n_(120544, "lst", lambda: lst), "insert"), _n_(120546, "i", lambda: i), _n_(120547, "x", lambda: x))
        _l_(120549)
        i += _n_(120550, "n", lambda: n) + 1
        _l_(120551)
    aux = _n_(120553, "lst", lambda: lst)
    _l_(120554)
    return aux
_c_(120557, _n_(120556, "print", lambda: print), 'Original list:')
_l_(120558)
_c_(120561, _n_(120559, "print", lambda: print), _n_(120560, "nums", lambda: nums))
_l_(120562)
x = 20
_l_(120563)
n = 4
_l_(120564)
_c_(120568, _n_(120565, "print", lambda: print), '\nInsert', _n_(120566, "x", lambda: x), 'in said list after every', _n_(120567, "n", lambda: n), 'th element:')
_l_(120569)
_c_(120576, _n_(120570, "print", lambda: print), _c_(120575, _n_(120571, "inset_element_list", lambda: inset_element_list), _n_(120572, "nums", lambda: nums), _n_(120573, "x", lambda: x), _n_(120574, "n", lambda: n)))
_l_(120577)
chars = ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
_l_(120578)
_c_(120580, _n_(120579, "print", lambda: print), '\nOriginal list:')
_l_(120581)
_c_(120584, _n_(120582, "print", lambda: print), _n_(120583, "chars", lambda: chars))
_l_(120585)
x = 'Z'
_l_(120586)
n = 3
_l_(120587)
_c_(120591, _n_(120588, "print", lambda: print), '\nInsert', _n_(120589, "x", lambda: x), 'in said list after every', _n_(120590, "n", lambda: n), 'th element:')
_l_(120592)
_c_(120599, _n_(120593, "print", lambda: print), _c_(120598, _n_(120594, "inset_element_list", lambda: inset_element_list), _n_(120595, "chars", lambda: chars), _n_(120596, "x", lambda: x), _n_(120597, "n", lambda: n)))
_l_(120600)