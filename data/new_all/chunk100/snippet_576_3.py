# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(59283, "object", lambda: object)):
    _l_(59292)


    def __init__(self, x):
        _l_(59291)

        _n_(59284, "self", lambda: self).val = _n_(59285, "x", lambda: x)
        _l_(59286)
        _n_(59287, "self", lambda: self).left = None
        _l_(59288)
        _n_(59289, "self", lambda: self).right = None
        _l_(59290)

def array_to_bst(array_nums):
    _l_(59313)

    if not _n_(59293, "array_nums", lambda: array_nums):
        _l_(59295)

        aux = None
        _l_(59294)
        return aux
    mid_num = _c_(59298, _n_(59296, "len", lambda: len), _n_(59297, "array_nums", lambda: array_nums)) // 2
    _l_(59299)
    node = _c_(59303, _n_(59300, "TreeNode", lambda: TreeNode), _n_(59301, "array_nums", lambda: array_nums)[_n_(59302, "mid_num", lambda: mid_num)])
    _l_(59304)
    _n_(59305, "node", lambda: node).left = _c_(59309, _n_(59306, "array_to_bst", lambda: array_to_bst), _n_(59307, "array_nums", lambda: array_nums)[:_n_(59308, "mid_num", lambda: mid_num)])
    _l_(59310)
    aux = _n_(59311, "node", lambda: node)
    _l_(59312)
    return aux

def preOrder(node):
    _l_(59332)

    if not _n_(59314, "node", lambda: node):
        _l_(59316)

        aux = ""
        _l_(59315)
        return aux
    _c_(59320, _n_(59317, "print", lambda: print), _a_(59319, _n_(59318, "node", lambda: node), "val"))
    _l_(59321)
    _c_(59325, _n_(59322, "preOrder", lambda: preOrder), _a_(59324, _n_(59323, "node", lambda: node), "left"))
    _l_(59326)
    _c_(59330, _n_(59327, "preOrder", lambda: preOrder), _a_(59329, _n_(59328, "node", lambda: node), "right"))
    _l_(59331)
array_nums = [1, 2, 3, 4, 5, 6, 7]
_l_(59333)
_c_(59335, _n_(59334, "print", lambda: print), 'Original array:')
_l_(59336)
_c_(59339, _n_(59337, "print", lambda: print), _n_(59338, "array_nums", lambda: array_nums))
_l_(59340)
result = _c_(59343, _n_(59341, "array_to_bst", lambda: array_to_bst), _n_(59342, "array_nums", lambda: array_nums))
_l_(59344)
_c_(59346, _n_(59345, "print", lambda: print), '\nArray to a height balanced BST:')
_l_(59347)
_c_(59352, _n_(59348, "print", lambda: print), _c_(59351, _n_(59349, "preOrder", lambda: preOrder), _n_(59350, "result", lambda: result)))
_l_(59353)