# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_integer(list1):
    _l_(66284)

    for i in _n_(66273, "list1", lambda: list1):
        _l_(66281)

        if _c_(66277, _n_(66274, "isinstance", lambda: isinstance), _n_(66275, "i", lambda: i), _n_(66276, "int", lambda: int)):
            _l_(66280)

            ctr = _n_(66278, "ctr", lambda: ctr) + 1
            _l_(66279)
    aux = _n_(66282, "ctr", lambda: ctr)
    _l_(66283)
    return aux
list1 = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
_l_(66285)
_c_(66287, _n_(66286, "print", lambda: print), 'Original list:')
_l_(66288)
_c_(66291, _n_(66289, "print", lambda: print), _n_(66290, "list1", lambda: list1))
_l_(66292)
_c_(66294, _n_(66293, "print", lambda: print), '\nNumber of integers in the said mixed list:')
_l_(66295)
_c_(66300, _n_(66296, "print", lambda: print), _c_(66299, _n_(66297, "count_integer", lambda: count_integer), _n_(66298, "list1", lambda: list1)))
_l_(66301)