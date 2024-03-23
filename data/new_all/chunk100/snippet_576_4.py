# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(59354, "object", lambda: object)):
    _l_(59361)


    def __init__(self, x):
        _l_(59360)

        _n_(59355, "self", lambda: self).val = _n_(59356, "x", lambda: x)
        _l_(59357)
        _n_(59358, "self", lambda: self).right = None
        _l_(59359)

def array_to_bst(array_nums):
    _l_(59388)

    if not _n_(59362, "array_nums", lambda: array_nums):
        _l_(59364)

        aux = None
        _l_(59363)
        return aux
    mid_num = _c_(59367, _n_(59365, "len", lambda: len), _n_(59366, "array_nums", lambda: array_nums)) // 2
    _l_(59368)
    node = _c_(59372, _n_(59369, "TreeNode", lambda: TreeNode), _n_(59370, "array_nums", lambda: array_nums)[_n_(59371, "mid_num", lambda: mid_num)])
    _l_(59373)
    _n_(59374, "node", lambda: node).left = _c_(59378, _n_(59375, "array_to_bst", lambda: array_to_bst), _n_(59376, "array_nums", lambda: array_nums)[:_n_(59377, "mid_num", lambda: mid_num)])
    _l_(59379)
    _n_(59380, "node", lambda: node).right = _c_(59384, _n_(59381, "array_to_bst", lambda: array_to_bst), _n_(59382, "array_nums", lambda: array_nums)[_n_(59383, "mid_num", lambda: mid_num) + 1:])
    _l_(59385)
    aux = _n_(59386, "node", lambda: node)
    _l_(59387)
    return aux

def preOrder(node):
    _l_(59407)

    if not _n_(59389, "node", lambda: node):
        _l_(59391)

        aux = ""
        _l_(59390)
        return aux
    _c_(59395, _n_(59392, "print", lambda: print), _a_(59394, _n_(59393, "node", lambda: node), "val"))
    _l_(59396)
    _c_(59400, _n_(59397, "preOrder", lambda: preOrder), _a_(59399, _n_(59398, "node", lambda: node), "left"))
    _l_(59401)
    _c_(59405, _n_(59402, "preOrder", lambda: preOrder), _a_(59404, _n_(59403, "node", lambda: node), "right"))
    _l_(59406)
array_nums = [1, 2, 3, 4, 5, 6, 7]
_l_(59408)
_c_(59410, _n_(59409, "print", lambda: print), 'Original array:')
_l_(59411)
_c_(59414, _n_(59412, "print", lambda: print), _n_(59413, "array_nums", lambda: array_nums))
_l_(59415)
result = _c_(59418, _n_(59416, "array_to_bst", lambda: array_to_bst), _n_(59417, "array_nums", lambda: array_nums))
_l_(59419)
_c_(59421, _n_(59420, "print", lambda: print), '\nArray to a height balanced BST:')
_l_(59422)
_c_(59427, _n_(59423, "print", lambda: print), _c_(59426, _n_(59424, "preOrder", lambda: preOrder), _n_(59425, "result", lambda: result)))
_l_(59428)