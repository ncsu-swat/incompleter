# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(58988, "object", lambda: object)):
    _l_(58997)


    def __init__(self, x):
        _l_(58996)

        _n_(58989, "self", lambda: self).val = _n_(58990, "x", lambda: x)
        _l_(58991)
        _n_(58992, "self", lambda: self).left = None
        _l_(58993)
        _n_(58994, "self", lambda: self).right = None
        _l_(58995)

def array_to_bst(array_nums):
    _l_(59024)

    if not _n_(58998, "array_nums", lambda: array_nums):
        _l_(59000)

        aux = None
        _l_(58999)
        return aux
    mid_num = _c_(59003, _n_(59001, "len", lambda: len), _n_(59002, "array_nums", lambda: array_nums)) // 2
    _l_(59004)
    node = _c_(59008, _n_(59005, "TreeNode", lambda: TreeNode), _n_(59006, "array_nums", lambda: array_nums)[_n_(59007, "mid_num", lambda: mid_num)])
    _l_(59009)
    _n_(59010, "node", lambda: node).left = _c_(59014, _n_(59011, "array_to_bst", lambda: array_to_bst), _n_(59012, "array_nums", lambda: array_nums)[:_n_(59013, "mid_num", lambda: mid_num)])
    _l_(59015)
    _n_(59016, "node", lambda: node).right = _c_(59020, _n_(59017, "array_to_bst", lambda: array_to_bst), _n_(59018, "array_nums", lambda: array_nums)[_n_(59019, "mid_num", lambda: mid_num) + 1:])
    _l_(59021)
    aux = _n_(59022, "node", lambda: node)
    _l_(59023)
    return aux

def preOrder(node):
    _l_(59043)

    if not _n_(59025, "node", lambda: node):
        _l_(59027)

        aux = ""
        _l_(59026)
        return aux
    _c_(59031, _n_(59028, "print", lambda: print), _a_(59030, _n_(59029, "node", lambda: node), "val"))
    _l_(59032)
    _c_(59036, _n_(59033, "preOrder", lambda: preOrder), _a_(59035, _n_(59034, "node", lambda: node), "left"))
    _l_(59037)
    _c_(59041, _n_(59038, "preOrder", lambda: preOrder), _a_(59040, _n_(59039, "node", lambda: node), "right"))
    _l_(59042)
array_nums = [1, 2, 3, 4, 5, 6, 7]
_l_(59044)
_c_(59046, _n_(59045, "print", lambda: print), 'Original array:')
_l_(59047)
_c_(59050, _n_(59048, "print", lambda: print), _n_(59049, "array_nums", lambda: array_nums))
_l_(59051)
_c_(59053, _n_(59052, "print", lambda: print), '\nArray to a height balanced BST:')
_l_(59054)
_c_(59059, _n_(59055, "print", lambda: print), _c_(59058, _n_(59056, "preOrder", lambda: preOrder), _n_(59057, "result", lambda: result)))
_l_(59060)