# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def inset_element_list(lst, x, n):
    _l_(120366)

    i = _n_(120349, "n", lambda: n)
    _l_(120350)
    while _n_(120351, "i", lambda: i) < _c_(120354, _n_(120352, "len", lambda: len), _n_(120353, "lst", lambda: lst)):
        _l_(120363)

        _c_(120359, _a_(120356, _n_(120355, "lst", lambda: lst), "insert"), _n_(120357, "i", lambda: i), _n_(120358, "x", lambda: x))
        _l_(120360)
        i += _n_(120361, "n", lambda: n) + 1
        _l_(120362)
    aux = _n_(120364, "lst", lambda: lst)
    _l_(120365)
    return aux
nums = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
_l_(120367)
_c_(120369, _n_(120368, "print", lambda: print), 'Original list:')
_l_(120370)
_c_(120373, _n_(120371, "print", lambda: print), _n_(120372, "nums", lambda: nums))
_l_(120374)
n = 4
_l_(120375)
_c_(120379, _n_(120376, "print", lambda: print), '\nInsert', _n_(120377, "x", lambda: x), 'in said list after every', _n_(120378, "n", lambda: n), 'th element:')
_l_(120380)
_c_(120387, _n_(120381, "print", lambda: print), _c_(120386, _n_(120382, "inset_element_list", lambda: inset_element_list), _n_(120383, "nums", lambda: nums), _n_(120384, "x", lambda: x), _n_(120385, "n", lambda: n)))
_l_(120388)
chars = ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
_l_(120389)
_c_(120391, _n_(120390, "print", lambda: print), '\nOriginal list:')
_l_(120392)
_c_(120395, _n_(120393, "print", lambda: print), _n_(120394, "chars", lambda: chars))
_l_(120396)
x = 'Z'
_l_(120397)
n = 3
_l_(120398)
_c_(120402, _n_(120399, "print", lambda: print), '\nInsert', _n_(120400, "x", lambda: x), 'in said list after every', _n_(120401, "n", lambda: n), 'th element:')
_l_(120403)
_c_(120410, _n_(120404, "print", lambda: print), _c_(120409, _n_(120405, "inset_element_list", lambda: inset_element_list), _n_(120406, "chars", lambda: chars), _n_(120407, "x", lambda: x), _n_(120408, "n", lambda: n)))
_l_(120411)