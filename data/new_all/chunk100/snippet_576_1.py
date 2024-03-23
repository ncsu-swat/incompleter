# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(59061, "object", lambda: object)):
    _l_(59070)


    def __init__(self, x):
        _l_(59069)

        _n_(59062, "self", lambda: self).val = _n_(59063, "x", lambda: x)
        _l_(59064)
        _n_(59065, "self", lambda: self).left = None
        _l_(59066)
        _n_(59067, "self", lambda: self).right = None
        _l_(59068)

def array_to_bst(array_nums):
    _l_(59097)

    if not _n_(59071, "array_nums", lambda: array_nums):
        _l_(59073)

        aux = None
        _l_(59072)
        return aux
    mid_num = _c_(59076, _n_(59074, "len", lambda: len), _n_(59075, "array_nums", lambda: array_nums)) // 2
    _l_(59077)
    node = _c_(59081, _n_(59078, "TreeNode", lambda: TreeNode), _n_(59079, "array_nums", lambda: array_nums)[_n_(59080, "mid_num", lambda: mid_num)])
    _l_(59082)
    _n_(59083, "node", lambda: node).left = _c_(59087, _n_(59084, "array_to_bst", lambda: array_to_bst), _n_(59085, "array_nums", lambda: array_nums)[:_n_(59086, "mid_num", lambda: mid_num)])
    _l_(59088)
    _n_(59089, "node", lambda: node).right = _c_(59093, _n_(59090, "array_to_bst", lambda: array_to_bst), _n_(59091, "array_nums", lambda: array_nums)[_n_(59092, "mid_num", lambda: mid_num) + 1:])
    _l_(59094)
    aux = _n_(59095, "node", lambda: node)
    _l_(59096)
    return aux

def preOrder(node):
    _l_(59116)

    if not _n_(59098, "node", lambda: node):
        _l_(59100)

        aux = ""
        _l_(59099)
        return aux
    _c_(59104, _n_(59101, "print", lambda: print), _a_(59103, _n_(59102, "node", lambda: node), "val"))
    _l_(59105)
    _c_(59109, _n_(59106, "preOrder", lambda: preOrder), _a_(59108, _n_(59107, "node", lambda: node), "left"))
    _l_(59110)
    _c_(59114, _n_(59111, "preOrder", lambda: preOrder), _a_(59113, _n_(59112, "node", lambda: node), "right"))
    _l_(59115)
_c_(59118, _n_(59117, "print", lambda: print), 'Original array:')
_l_(59119)
_c_(59122, _n_(59120, "print", lambda: print), _n_(59121, "array_nums", lambda: array_nums))
_l_(59123)
result = _c_(59126, _n_(59124, "array_to_bst", lambda: array_to_bst), _n_(59125, "array_nums", lambda: array_nums))
_l_(59127)
_c_(59129, _n_(59128, "print", lambda: print), '\nArray to a height balanced BST:')
_l_(59130)
_c_(59135, _n_(59131, "print", lambda: print), _c_(59134, _n_(59132, "preOrder", lambda: preOrder), _n_(59133, "result", lambda: result)))
_l_(59136)