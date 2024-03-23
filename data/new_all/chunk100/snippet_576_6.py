# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(59501, "object", lambda: object)):
    _l_(59510)


    def __init__(self, x):
        _l_(59509)

        _n_(59502, "self", lambda: self).val = _n_(59503, "x", lambda: x)
        _l_(59504)
        _n_(59505, "self", lambda: self).left = None
        _l_(59506)
        _n_(59507, "self", lambda: self).right = None
        _l_(59508)

def array_to_bst(array_nums):
    _l_(59531)

    if not _n_(59511, "array_nums", lambda: array_nums):
        _l_(59513)

        aux = None
        _l_(59512)
        return aux
    mid_num = _c_(59516, _n_(59514, "len", lambda: len), _n_(59515, "array_nums", lambda: array_nums)) // 2
    _l_(59517)
    node = _c_(59521, _n_(59518, "TreeNode", lambda: TreeNode), _n_(59519, "array_nums", lambda: array_nums)[_n_(59520, "mid_num", lambda: mid_num)])
    _l_(59522)
    _n_(59523, "node", lambda: node).right = _c_(59527, _n_(59524, "array_to_bst", lambda: array_to_bst), _n_(59525, "array_nums", lambda: array_nums)[_n_(59526, "mid_num", lambda: mid_num) + 1:])
    _l_(59528)
    aux = _n_(59529, "node", lambda: node)
    _l_(59530)
    return aux

def preOrder(node):
    _l_(59550)

    if not _n_(59532, "node", lambda: node):
        _l_(59534)

        aux = ""
        _l_(59533)
        return aux
    _c_(59538, _n_(59535, "print", lambda: print), _a_(59537, _n_(59536, "node", lambda: node), "val"))
    _l_(59539)
    _c_(59543, _n_(59540, "preOrder", lambda: preOrder), _a_(59542, _n_(59541, "node", lambda: node), "left"))
    _l_(59544)
    _c_(59548, _n_(59545, "preOrder", lambda: preOrder), _a_(59547, _n_(59546, "node", lambda: node), "right"))
    _l_(59549)
array_nums = [1, 2, 3, 4, 5, 6, 7]
_l_(59551)
_c_(59553, _n_(59552, "print", lambda: print), 'Original array:')
_l_(59554)
_c_(59557, _n_(59555, "print", lambda: print), _n_(59556, "array_nums", lambda: array_nums))
_l_(59558)
result = _c_(59561, _n_(59559, "array_to_bst", lambda: array_to_bst), _n_(59560, "array_nums", lambda: array_nums))
_l_(59562)
_c_(59564, _n_(59563, "print", lambda: print), '\nArray to a height balanced BST:')
_l_(59565)
_c_(59570, _n_(59566, "print", lambda: print), _c_(59569, _n_(59567, "preOrder", lambda: preOrder), _n_(59568, "result", lambda: result)))
_l_(59571)