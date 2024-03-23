# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(59212, "object", lambda: object)):
    _l_(59221)


    def __init__(self, x):
        _l_(59220)

        _n_(59213, "self", lambda: self).val = _n_(59214, "x", lambda: x)
        _l_(59215)
        _n_(59216, "self", lambda: self).left = None
        _l_(59217)
        _n_(59218, "self", lambda: self).right = None
        _l_(59219)

def array_to_bst(array_nums):
    _l_(59242)

    if not _n_(59222, "array_nums", lambda: array_nums):
        _l_(59224)

        aux = None
        _l_(59223)
        return aux
    mid_num = _c_(59227, _n_(59225, "len", lambda: len), _n_(59226, "array_nums", lambda: array_nums)) // 2
    _l_(59228)
    node = _c_(59232, _n_(59229, "TreeNode", lambda: TreeNode), _n_(59230, "array_nums", lambda: array_nums)[_n_(59231, "mid_num", lambda: mid_num)])
    _l_(59233)
    _n_(59234, "node", lambda: node).right = _c_(59238, _n_(59235, "array_to_bst", lambda: array_to_bst), _n_(59236, "array_nums", lambda: array_nums)[_n_(59237, "mid_num", lambda: mid_num) + 1:])
    _l_(59239)
    aux = _n_(59240, "node", lambda: node)
    _l_(59241)
    return aux

def preOrder(node):
    _l_(59261)

    if not _n_(59243, "node", lambda: node):
        _l_(59245)

        aux = ""
        _l_(59244)
        return aux
    _c_(59249, _n_(59246, "print", lambda: print), _a_(59248, _n_(59247, "node", lambda: node), "val"))
    _l_(59250)
    _c_(59254, _n_(59251, "preOrder", lambda: preOrder), _a_(59253, _n_(59252, "node", lambda: node), "left"))
    _l_(59255)
    _c_(59259, _n_(59256, "preOrder", lambda: preOrder), _a_(59258, _n_(59257, "node", lambda: node), "right"))
    _l_(59260)
array_nums = [1, 2, 3, 4, 5, 6, 7]
_l_(59262)
_c_(59264, _n_(59263, "print", lambda: print), 'Original array:')
_l_(59265)
_c_(59268, _n_(59266, "print", lambda: print), _n_(59267, "array_nums", lambda: array_nums))
_l_(59269)
result = _c_(59272, _n_(59270, "array_to_bst", lambda: array_to_bst), _n_(59271, "array_nums", lambda: array_nums))
_l_(59273)
_c_(59275, _n_(59274, "print", lambda: print), '\nArray to a height balanced BST:')
_l_(59276)
_c_(59281, _n_(59277, "print", lambda: print), _c_(59280, _n_(59278, "preOrder", lambda: preOrder), _n_(59279, "result", lambda: result)))
_l_(59282)