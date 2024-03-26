# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(105382)

except ImportError:
    pass

def interleave_multiple_lists(list1, list2, list3):
    _l_(105396)

    result = _c_(105392, _n_(105383, "list", lambda: list), _c_(105391, _a_(105385, _n_(105384, "itertools", lambda: itertools), "chain"), *_c_(105390, _n_(105386, "zip", lambda: zip), _n_(105387, "list1", lambda: list1), _n_(105388, "list2", lambda: list2), _n_(105389, "list3", lambda: list3))))
    _l_(105393)
    aux = _n_(105394, "result", lambda: result)
    _l_(105395)
    return aux
list1 = [100, 200, 300, 400, 500, 600, 700]
_l_(105397)
list3 = [1, 2, 3, 4, 5, 6, 7]
_l_(105398)
_c_(105400, _n_(105399, "print", lambda: print), 'Original list:')
_l_(105401)
_c_(105404, _n_(105402, "print", lambda: print), 'list1:', _n_(105403, "list1", lambda: list1))
_l_(105405)
_c_(105408, _n_(105406, "print", lambda: print), 'list2:', _n_(105407, "list2", lambda: list2))
_l_(105409)
_c_(105412, _n_(105410, "print", lambda: print), 'list3:', _n_(105411, "list3", lambda: list3))
_l_(105413)
_c_(105415, _n_(105414, "print", lambda: print), '\nInterleave multiple lists:')
_l_(105416)
_c_(105423, _n_(105417, "print", lambda: print), _c_(105422, _n_(105418, "interleave_multiple_lists", lambda: interleave_multiple_lists), _n_(105419, "list1", lambda: list1), _n_(105420, "list2", lambda: list2), _n_(105421, "list3", lambda: list3)))
_l_(105424)