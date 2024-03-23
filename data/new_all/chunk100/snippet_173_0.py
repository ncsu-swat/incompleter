# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def concatenate_lists(l1, l2, l3):
    _l_(12292)

    aux = [_n_(12283, "i", lambda: i) + _n_(12284, "j", lambda: j) + _n_(12285, "k", lambda: k) for (i, j, k) in _c_(12290, _n_(12286, "zip", lambda: zip), _n_(12287, "l1", lambda: l1), _n_(12288, "l2", lambda: l2), _n_(12289, "l3", lambda: l3))]
    _l_(12291)
    return aux
l2 = ['red', 'green', 'black', 'blue', 'white']
_l_(12293)
l3 = ['100', '200', '300', '400', '500']
_l_(12294)
_c_(12296, _n_(12295, "print", lambda: print), 'Original lists:')
_l_(12297)
_c_(12300, _n_(12298, "print", lambda: print), _n_(12299, "l1", lambda: l1))
_l_(12301)
_c_(12304, _n_(12302, "print", lambda: print), _n_(12303, "l2", lambda: l2))
_l_(12305)
_c_(12308, _n_(12306, "print", lambda: print), _n_(12307, "l3", lambda: l3))
_l_(12309)
_c_(12311, _n_(12310, "print", lambda: print), '\nConcatenate element-wise three said lists:')
_l_(12312)
_c_(12319, _n_(12313, "print", lambda: print), _c_(12318, _n_(12314, "concatenate_lists", lambda: concatenate_lists), _n_(12315, "l1", lambda: l1), _n_(12316, "l2", lambda: l2), _n_(12317, "l3", lambda: l3)))
_l_(12320)