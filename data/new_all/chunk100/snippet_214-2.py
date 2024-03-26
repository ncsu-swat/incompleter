# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(105426)

except ImportError:
    pass

def interleave_multiple_lists(list1, list2, list3):
    _l_(105440)

    result = _c_(105436, _n_(105427, "list", lambda: list), _c_(105435, _a_(105429, _n_(105428, "itertools", lambda: itertools), "chain"), *_c_(105434, _n_(105430, "zip", lambda: zip), _n_(105431, "list1", lambda: list1), _n_(105432, "list2", lambda: list2), _n_(105433, "list3", lambda: list3))))
    _l_(105437)
    aux = _n_(105438, "result", lambda: result)
    _l_(105439)
    return aux
list2 = [10, 20, 30, 40, 50, 60, 70]
_l_(105441)
list3 = [1, 2, 3, 4, 5, 6, 7]
_l_(105442)
_c_(105444, _n_(105443, "print", lambda: print), 'Original list:')
_l_(105445)
_c_(105448, _n_(105446, "print", lambda: print), 'list1:', _n_(105447, "list1", lambda: list1))
_l_(105449)
_c_(105452, _n_(105450, "print", lambda: print), 'list2:', _n_(105451, "list2", lambda: list2))
_l_(105453)
_c_(105456, _n_(105454, "print", lambda: print), 'list3:', _n_(105455, "list3", lambda: list3))
_l_(105457)
_c_(105459, _n_(105458, "print", lambda: print), '\nInterleave multiple lists:')
_l_(105460)
_c_(105467, _n_(105461, "print", lambda: print), _c_(105466, _n_(105462, "interleave_multiple_lists", lambda: interleave_multiple_lists), _n_(105463, "list1", lambda: list1), _n_(105464, "list2", lambda: list2), _n_(105465, "list3", lambda: list3)))
_l_(105468)