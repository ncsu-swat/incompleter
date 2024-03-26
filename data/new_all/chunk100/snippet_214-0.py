# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import itertools
    _l_(105338)

except ImportError:
    pass

def interleave_multiple_lists(list1, list2, list3):
    _l_(105352)

    result = _c_(105348, _n_(105339, "list", lambda: list), _c_(105347, _a_(105341, _n_(105340, "itertools", lambda: itertools), "chain"), *_c_(105346, _n_(105342, "zip", lambda: zip), _n_(105343, "list1", lambda: list1), _n_(105344, "list2", lambda: list2), _n_(105345, "list3", lambda: list3))))
    _l_(105349)
    aux = _n_(105350, "result", lambda: result)
    _l_(105351)
    return aux
list1 = [100, 200, 300, 400, 500, 600, 700]
_l_(105353)
list2 = [10, 20, 30, 40, 50, 60, 70]
_l_(105354)
_c_(105356, _n_(105355, "print", lambda: print), 'Original list:')
_l_(105357)
_c_(105360, _n_(105358, "print", lambda: print), 'list1:', _n_(105359, "list1", lambda: list1))
_l_(105361)
_c_(105364, _n_(105362, "print", lambda: print), 'list2:', _n_(105363, "list2", lambda: list2))
_l_(105365)
_c_(105368, _n_(105366, "print", lambda: print), 'list3:', _n_(105367, "list3", lambda: list3))
_l_(105369)
_c_(105371, _n_(105370, "print", lambda: print), '\nInterleave multiple lists:')
_l_(105372)
_c_(105379, _n_(105373, "print", lambda: print), _c_(105378, _n_(105374, "interleave_multiple_lists", lambda: interleave_multiple_lists), _n_(105375, "list1", lambda: list1), _n_(105376, "list2", lambda: list2), _n_(105377, "list3", lambda: list3)))
_l_(105380)