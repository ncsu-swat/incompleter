# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def inset_element_list(lst, x, n):
    _l_(120429)

    i = _n_(120412, "n", lambda: n)
    _l_(120413)
    while _n_(120414, "i", lambda: i) < _c_(120417, _n_(120415, "len", lambda: len), _n_(120416, "lst", lambda: lst)):
        _l_(120426)

        _c_(120422, _a_(120419, _n_(120418, "lst", lambda: lst), "insert"), _n_(120420, "i", lambda: i), _n_(120421, "x", lambda: x))
        _l_(120423)
        i += _n_(120424, "n", lambda: n) + 1
        _l_(120425)
    aux = _n_(120427, "lst", lambda: lst)
    _l_(120428)
    return aux
nums = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
_l_(120430)
_c_(120432, _n_(120431, "print", lambda: print), 'Original list:')
_l_(120433)
_c_(120436, _n_(120434, "print", lambda: print), _n_(120435, "nums", lambda: nums))
_l_(120437)
x = 20
_l_(120438)
n = 4
_l_(120439)
_c_(120443, _n_(120440, "print", lambda: print), '\nInsert', _n_(120441, "x", lambda: x), 'in said list after every', _n_(120442, "n", lambda: n), 'th element:')
_l_(120444)
_c_(120451, _n_(120445, "print", lambda: print), _c_(120450, _n_(120446, "inset_element_list", lambda: inset_element_list), _n_(120447, "nums", lambda: nums), _n_(120448, "x", lambda: x), _n_(120449, "n", lambda: n)))
_l_(120452)
_c_(120454, _n_(120453, "print", lambda: print), '\nOriginal list:')
_l_(120455)
_c_(120458, _n_(120456, "print", lambda: print), _n_(120457, "chars", lambda: chars))
_l_(120459)
x = 'Z'
_l_(120460)
n = 3
_l_(120461)
_c_(120465, _n_(120462, "print", lambda: print), '\nInsert', _n_(120463, "x", lambda: x), 'in said list after every', _n_(120464, "n", lambda: n), 'th element:')
_l_(120466)
_c_(120473, _n_(120467, "print", lambda: print), _c_(120472, _n_(120468, "inset_element_list", lambda: inset_element_list), _n_(120469, "chars", lambda: chars), _n_(120470, "x", lambda: x), _n_(120471, "n", lambda: n)))
_l_(120474)