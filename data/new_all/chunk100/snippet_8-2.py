# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def inset_element_list(lst, x, n):
    _l_(120492)

    i = _n_(120475, "n", lambda: n)
    _l_(120476)
    while _n_(120477, "i", lambda: i) < _c_(120480, _n_(120478, "len", lambda: len), _n_(120479, "lst", lambda: lst)):
        _l_(120489)

        _c_(120485, _a_(120482, _n_(120481, "lst", lambda: lst), "insert"), _n_(120483, "i", lambda: i), _n_(120484, "x", lambda: x))
        _l_(120486)
        i += _n_(120487, "n", lambda: n) + 1
        _l_(120488)
    aux = _n_(120490, "lst", lambda: lst)
    _l_(120491)
    return aux
nums = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
_l_(120493)
_c_(120495, _n_(120494, "print", lambda: print), 'Original list:')
_l_(120496)
_c_(120499, _n_(120497, "print", lambda: print), _n_(120498, "nums", lambda: nums))
_l_(120500)
x = 20
_l_(120501)
_c_(120505, _n_(120502, "print", lambda: print), '\nInsert', _n_(120503, "x", lambda: x), 'in said list after every', _n_(120504, "n", lambda: n), 'th element:')
_l_(120506)
_c_(120513, _n_(120507, "print", lambda: print), _c_(120512, _n_(120508, "inset_element_list", lambda: inset_element_list), _n_(120509, "nums", lambda: nums), _n_(120510, "x", lambda: x), _n_(120511, "n", lambda: n)))
_l_(120514)
chars = ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']
_l_(120515)
_c_(120517, _n_(120516, "print", lambda: print), '\nOriginal list:')
_l_(120518)
_c_(120521, _n_(120519, "print", lambda: print), _n_(120520, "chars", lambda: chars))
_l_(120522)
x = 'Z'
_l_(120523)
n = 3
_l_(120524)
_c_(120528, _n_(120525, "print", lambda: print), '\nInsert', _n_(120526, "x", lambda: x), 'in said list after every', _n_(120527, "n", lambda: n), 'th element:')
_l_(120529)
_c_(120536, _n_(120530, "print", lambda: print), _c_(120535, _n_(120531, "inset_element_list", lambda: inset_element_list), _n_(120532, "chars", lambda: chars), _n_(120533, "x", lambda: x), _n_(120534, "n", lambda: n)))
_l_(120537)