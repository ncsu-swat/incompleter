# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(59716, "object", lambda: object)):
    _l_(59722)


    def __init__(self, x):
        _l_(59721)

        _n_(59717, "self", lambda: self).left = None
        _l_(59718)
        _n_(59719, "self", lambda: self).right = None
        _l_(59720)

def array_to_bst(array_nums):
    _l_(59749)

    if not _n_(59723, "array_nums", lambda: array_nums):
        _l_(59725)

        aux = None
        _l_(59724)
        return aux
    mid_num = _c_(59728, _n_(59726, "len", lambda: len), _n_(59727, "array_nums", lambda: array_nums)) // 2
    _l_(59729)
    node = _c_(59733, _n_(59730, "TreeNode", lambda: TreeNode), _n_(59731, "array_nums", lambda: array_nums)[_n_(59732, "mid_num", lambda: mid_num)])
    _l_(59734)
    _n_(59735, "node", lambda: node).left = _c_(59739, _n_(59736, "array_to_bst", lambda: array_to_bst), _n_(59737, "array_nums", lambda: array_nums)[:_n_(59738, "mid_num", lambda: mid_num)])
    _l_(59740)
    _n_(59741, "node", lambda: node).right = _c_(59745, _n_(59742, "array_to_bst", lambda: array_to_bst), _n_(59743, "array_nums", lambda: array_nums)[_n_(59744, "mid_num", lambda: mid_num) + 1:])
    _l_(59746)
    aux = _n_(59747, "node", lambda: node)
    _l_(59748)
    return aux

def preOrder(node):
    _l_(59768)

    if not _n_(59750, "node", lambda: node):
        _l_(59752)

        aux = ""
        _l_(59751)
        return aux
    _c_(59756, _n_(59753, "print", lambda: print), _a_(59755, _n_(59754, "node", lambda: node), "val"))
    _l_(59757)
    _c_(59761, _n_(59758, "preOrder", lambda: preOrder), _a_(59760, _n_(59759, "node", lambda: node), "left"))
    _l_(59762)
    _c_(59766, _n_(59763, "preOrder", lambda: preOrder), _a_(59765, _n_(59764, "node", lambda: node), "right"))
    _l_(59767)
array_nums = [1, 2, 3, 4, 5, 6, 7]
_l_(59769)
_c_(59771, _n_(59770, "print", lambda: print), 'Original array:')
_l_(59772)
_c_(59775, _n_(59773, "print", lambda: print), _n_(59774, "array_nums", lambda: array_nums))
_l_(59776)
result = _c_(59779, _n_(59777, "array_to_bst", lambda: array_to_bst), _n_(59778, "array_nums", lambda: array_nums))
_l_(59780)
_c_(59782, _n_(59781, "print", lambda: print), '\nArray to a height balanced BST:')
_l_(59783)
_c_(59788, _n_(59784, "print", lambda: print), _c_(59787, _n_(59785, "preOrder", lambda: preOrder), _n_(59786, "result", lambda: result)))
_l_(59789)