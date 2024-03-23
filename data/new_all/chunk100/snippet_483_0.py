# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_integer(list1):
    _l_(50488)

    ert = _c_(50484, _n_(50476, "list", lambda: list), _c_(50483, _n_(50477, "map", lambda: map), lambda i: _c_(50481, _n_(50478, "isinstance", lambda: isinstance), _n_(50479, "i", lambda: i), _n_(50480, "float", lambda: float)), _n_(50482, "list1", lambda: list1)))
    _l_(50485)
    aux = _n_(50486, "result", lambda: result)
    _l_(50487)
    return aux
list1 = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
_l_(50489)
_c_(50491, _n_(50490, "print", lambda: print), 'Original list:')
_l_(50492)
_c_(50495, _n_(50493, "print", lambda: print), _n_(50494, "list1", lambda: list1))
_l_(50496)
_c_(50498, _n_(50497, "print", lambda: print), '\nNumber of floats in the said mixed list:')
_l_(50499)
_c_(50504, _n_(50500, "print", lambda: print), _c_(50503, _n_(50501, "count_integer", lambda: count_integer), _n_(50502, "list1", lambda: list1)))
_l_(50505)