# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(59572, "object", lambda: object)):
    _l_(59581)


    def __init__(self, x):
        _l_(59580)

        _n_(59573, "self", lambda: self).val = _n_(59574, "x", lambda: x)
        _l_(59575)
        _n_(59576, "self", lambda: self).left = None
        _l_(59577)
        _n_(59578, "self", lambda: self).right = None
        _l_(59579)

def array_to_bst(array_nums):
    _l_(59604)

    if not _n_(59582, "array_nums", lambda: array_nums):
        _l_(59584)

        aux = None
        _l_(59583)
        return aux
    node = _c_(59588, _n_(59585, "TreeNode", lambda: TreeNode), _n_(59586, "array_nums", lambda: array_nums)[_n_(59587, "mid_num", lambda: mid_num)])
    _l_(59589)
    _n_(59590, "node", lambda: node).left = _c_(59594, _n_(59591, "array_to_bst", lambda: array_to_bst), _n_(59592, "array_nums", lambda: array_nums)[:_n_(59593, "mid_num", lambda: mid_num)])
    _l_(59595)
    _n_(59596, "node", lambda: node).right = _c_(59600, _n_(59597, "array_to_bst", lambda: array_to_bst), _n_(59598, "array_nums", lambda: array_nums)[_n_(59599, "mid_num", lambda: mid_num) + 1:])
    _l_(59601)
    aux = _n_(59602, "node", lambda: node)
    _l_(59603)
    return aux

def preOrder(node):
    _l_(59623)

    if not _n_(59605, "node", lambda: node):
        _l_(59607)

        aux = ""
        _l_(59606)
        return aux
    _c_(59611, _n_(59608, "print", lambda: print), _a_(59610, _n_(59609, "node", lambda: node), "val"))
    _l_(59612)
    _c_(59616, _n_(59613, "preOrder", lambda: preOrder), _a_(59615, _n_(59614, "node", lambda: node), "left"))
    _l_(59617)
    _c_(59621, _n_(59618, "preOrder", lambda: preOrder), _a_(59620, _n_(59619, "node", lambda: node), "right"))
    _l_(59622)
array_nums = [1, 2, 3, 4, 5, 6, 7]
_l_(59624)
_c_(59626, _n_(59625, "print", lambda: print), 'Original array:')
_l_(59627)
_c_(59630, _n_(59628, "print", lambda: print), _n_(59629, "array_nums", lambda: array_nums))
_l_(59631)
result = _c_(59634, _n_(59632, "array_to_bst", lambda: array_to_bst), _n_(59633, "array_nums", lambda: array_nums))
_l_(59635)
_c_(59637, _n_(59636, "print", lambda: print), '\nArray to a height balanced BST:')
_l_(59638)
_c_(59643, _n_(59639, "print", lambda: print), _c_(59642, _n_(59640, "preOrder", lambda: preOrder), _n_(59641, "result", lambda: result)))
_l_(59644)