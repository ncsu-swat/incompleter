# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(59645, "object", lambda: object)):
    _l_(59654)


    def __init__(self, x):
        _l_(59653)

        _n_(59646, "self", lambda: self).val = _n_(59647, "x", lambda: x)
        _l_(59648)
        _n_(59649, "self", lambda: self).left = None
        _l_(59650)
        _n_(59651, "self", lambda: self).right = None
        _l_(59652)

def array_to_bst(array_nums):
    _l_(59675)

    if not _n_(59655, "array_nums", lambda: array_nums):
        _l_(59657)

        aux = None
        _l_(59656)
        return aux
    mid_num = _c_(59660, _n_(59658, "len", lambda: len), _n_(59659, "array_nums", lambda: array_nums)) // 2
    _l_(59661)
    node = _c_(59665, _n_(59662, "TreeNode", lambda: TreeNode), _n_(59663, "array_nums", lambda: array_nums)[_n_(59664, "mid_num", lambda: mid_num)])
    _l_(59666)
    _n_(59667, "node", lambda: node).left = _c_(59671, _n_(59668, "array_to_bst", lambda: array_to_bst), _n_(59669, "array_nums", lambda: array_nums)[:_n_(59670, "mid_num", lambda: mid_num)])
    _l_(59672)
    aux = _n_(59673, "node", lambda: node)
    _l_(59674)
    return aux

def preOrder(node):
    _l_(59694)

    if not _n_(59676, "node", lambda: node):
        _l_(59678)

        aux = ""
        _l_(59677)
        return aux
    _c_(59682, _n_(59679, "print", lambda: print), _a_(59681, _n_(59680, "node", lambda: node), "val"))
    _l_(59683)
    _c_(59687, _n_(59684, "preOrder", lambda: preOrder), _a_(59686, _n_(59685, "node", lambda: node), "left"))
    _l_(59688)
    _c_(59692, _n_(59689, "preOrder", lambda: preOrder), _a_(59691, _n_(59690, "node", lambda: node), "right"))
    _l_(59693)
array_nums = [1, 2, 3, 4, 5, 6, 7]
_l_(59695)
_c_(59697, _n_(59696, "print", lambda: print), 'Original array:')
_l_(59698)
_c_(59701, _n_(59699, "print", lambda: print), _n_(59700, "array_nums", lambda: array_nums))
_l_(59702)
result = _c_(59705, _n_(59703, "array_to_bst", lambda: array_to_bst), _n_(59704, "array_nums", lambda: array_nums))
_l_(59706)
_c_(59708, _n_(59707, "print", lambda: print), '\nArray to a height balanced BST:')
_l_(59709)
_c_(59714, _n_(59710, "print", lambda: print), _c_(59713, _n_(59711, "preOrder", lambda: preOrder), _n_(59712, "result", lambda: result)))
_l_(59715)