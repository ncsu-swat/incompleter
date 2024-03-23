# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(59137, "object", lambda: object)):
    _l_(59144)


    def __init__(self, x):
        _l_(59143)

        _n_(59138, "self", lambda: self).val = _n_(59139, "x", lambda: x)
        _l_(59140)
        _n_(59141, "self", lambda: self).left = None
        _l_(59142)

def array_to_bst(array_nums):
    _l_(59171)

    if not _n_(59145, "array_nums", lambda: array_nums):
        _l_(59147)

        aux = None
        _l_(59146)
        return aux
    mid_num = _c_(59150, _n_(59148, "len", lambda: len), _n_(59149, "array_nums", lambda: array_nums)) // 2
    _l_(59151)
    node = _c_(59155, _n_(59152, "TreeNode", lambda: TreeNode), _n_(59153, "array_nums", lambda: array_nums)[_n_(59154, "mid_num", lambda: mid_num)])
    _l_(59156)
    _n_(59157, "node", lambda: node).left = _c_(59161, _n_(59158, "array_to_bst", lambda: array_to_bst), _n_(59159, "array_nums", lambda: array_nums)[:_n_(59160, "mid_num", lambda: mid_num)])
    _l_(59162)
    _n_(59163, "node", lambda: node).right = _c_(59167, _n_(59164, "array_to_bst", lambda: array_to_bst), _n_(59165, "array_nums", lambda: array_nums)[_n_(59166, "mid_num", lambda: mid_num) + 1:])
    _l_(59168)
    aux = _n_(59169, "node", lambda: node)
    _l_(59170)
    return aux

def preOrder(node):
    _l_(59190)

    if not _n_(59172, "node", lambda: node):
        _l_(59174)

        aux = ""
        _l_(59173)
        return aux
    _c_(59178, _n_(59175, "print", lambda: print), _a_(59177, _n_(59176, "node", lambda: node), "val"))
    _l_(59179)
    _c_(59183, _n_(59180, "preOrder", lambda: preOrder), _a_(59182, _n_(59181, "node", lambda: node), "left"))
    _l_(59184)
    _c_(59188, _n_(59185, "preOrder", lambda: preOrder), _a_(59187, _n_(59186, "node", lambda: node), "right"))
    _l_(59189)
array_nums = [1, 2, 3, 4, 5, 6, 7]
_l_(59191)
_c_(59193, _n_(59192, "print", lambda: print), 'Original array:')
_l_(59194)
_c_(59197, _n_(59195, "print", lambda: print), _n_(59196, "array_nums", lambda: array_nums))
_l_(59198)
result = _c_(59201, _n_(59199, "array_to_bst", lambda: array_to_bst), _n_(59200, "array_nums", lambda: array_nums))
_l_(59202)
_c_(59204, _n_(59203, "print", lambda: print), '\nArray to a height balanced BST:')
_l_(59205)
_c_(59210, _n_(59206, "print", lambda: print), _c_(59209, _n_(59207, "preOrder", lambda: preOrder), _n_(59208, "result", lambda: result)))
_l_(59211)