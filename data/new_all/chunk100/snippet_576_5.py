# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(59429, "object", lambda: object)):
    _l_(59438)


    def __init__(self, x):
        _l_(59437)

        _n_(59430, "self", lambda: self).val = _n_(59431, "x", lambda: x)
        _l_(59432)
        _n_(59433, "self", lambda: self).left = None
        _l_(59434)
        _n_(59435, "self", lambda: self).right = None
        _l_(59436)

def array_to_bst(array_nums):
    _l_(59460)

    if not _n_(59439, "array_nums", lambda: array_nums):
        _l_(59441)

        aux = None
        _l_(59440)
        return aux
    mid_num = _c_(59444, _n_(59442, "len", lambda: len), _n_(59443, "array_nums", lambda: array_nums)) // 2
    _l_(59445)
    _n_(59446, "node", lambda: node).left = _c_(59450, _n_(59447, "array_to_bst", lambda: array_to_bst), _n_(59448, "array_nums", lambda: array_nums)[:_n_(59449, "mid_num", lambda: mid_num)])
    _l_(59451)
    _n_(59452, "node", lambda: node).right = _c_(59456, _n_(59453, "array_to_bst", lambda: array_to_bst), _n_(59454, "array_nums", lambda: array_nums)[_n_(59455, "mid_num", lambda: mid_num) + 1:])
    _l_(59457)
    aux = _n_(59458, "node", lambda: node)
    _l_(59459)
    return aux

def preOrder(node):
    _l_(59479)

    if not _n_(59461, "node", lambda: node):
        _l_(59463)

        aux = ""
        _l_(59462)
        return aux
    _c_(59467, _n_(59464, "print", lambda: print), _a_(59466, _n_(59465, "node", lambda: node), "val"))
    _l_(59468)
    _c_(59472, _n_(59469, "preOrder", lambda: preOrder), _a_(59471, _n_(59470, "node", lambda: node), "left"))
    _l_(59473)
    _c_(59477, _n_(59474, "preOrder", lambda: preOrder), _a_(59476, _n_(59475, "node", lambda: node), "right"))
    _l_(59478)
array_nums = [1, 2, 3, 4, 5, 6, 7]
_l_(59480)
_c_(59482, _n_(59481, "print", lambda: print), 'Original array:')
_l_(59483)
_c_(59486, _n_(59484, "print", lambda: print), _n_(59485, "array_nums", lambda: array_nums))
_l_(59487)
result = _c_(59490, _n_(59488, "array_to_bst", lambda: array_to_bst), _n_(59489, "array_nums", lambda: array_nums))
_l_(59491)
_c_(59493, _n_(59492, "print", lambda: print), '\nArray to a height balanced BST:')
_l_(59494)
_c_(59499, _n_(59495, "print", lambda: print), _c_(59498, _n_(59496, "preOrder", lambda: preOrder), _n_(59497, "result", lambda: result)))
_l_(59500)