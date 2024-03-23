# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(56762, "object", lambda: object)):
    _l_(56771)


    def __init__(self, x):
        _l_(56770)

        _n_(56763, "self", lambda: self).val = _n_(56764, "x", lambda: x)
        _l_(56765)
        _n_(56766, "self", lambda: self).left = None
        _l_(56767)
        _n_(56768, "self", lambda: self).right = None
        _l_(56769)

def delete_Node(root, key):
    _l_(56835)

    if not _n_(56772, "root", lambda: root):
        _l_(56775)

        aux = _n_(56773, "root", lambda: root)
        _l_(56774)
        return aux
    if _a_(56777, _n_(56776, "root", lambda: root), "val") > _n_(56778, "key", lambda: key):
        _l_(56832)

        _n_(56779, "root", lambda: root).left = _c_(56784, _n_(56780, "delete_Node", lambda: delete_Node), _a_(56782, _n_(56781, "root", lambda: root), "left"), _n_(56783, "key", lambda: key))
        _l_(56785)
    elif _a_(56787, _n_(56786, "root", lambda: root), "val") < _n_(56788, "key", lambda: key):
        _l_(56831)

        _n_(56789, "root", lambda: root).right = _c_(56794, _n_(56790, "delete_Node", lambda: delete_Node), _a_(56792, _n_(56791, "root", lambda: root), "right"), _n_(56793, "key", lambda: key))
        _l_(56795)
    else:
        if not _a_(56797, _n_(56796, "root", lambda: root), "right"):
            _l_(56801)

            aux = _a_(56799, _n_(56798, "root", lambda: root), "left")
            _l_(56800)
            return aux
        if not _a_(56803, _n_(56802, "root", lambda: root), "left"):
            _l_(56807)

            aux = _a_(56805, _n_(56804, "root", lambda: root), "right")
            _l_(56806)
            return aux
        temp_val = _a_(56809, _n_(56808, "root", lambda: root), "right")
        _l_(56810)
        mini_val = _a_(56812, _n_(56811, "temp_val", lambda: temp_val), "val")
        _l_(56813)
        while _a_(56815, _n_(56814, "temp_val", lambda: temp_val), "left"):
            _l_(56822)

            temp_val = _a_(56817, _n_(56816, "temp_val", lambda: temp_val), "left")
            _l_(56818)
            mini_val = _a_(56820, _n_(56819, "temp_val", lambda: temp_val), "val")
            _l_(56821)
        _n_(56823, "root", lambda: root).right = _c_(56829, _n_(56824, "deleteNode", lambda: deleteNode), _a_(56826, _n_(56825, "root", lambda: root), "right"), _a_(56828, _n_(56827, "root", lambda: root), "val"))
        _l_(56830)
    aux = _n_(56833, "root", lambda: root)
    _l_(56834)
    return aux

def preOrder(node):
    _l_(56854)

    if not _n_(56836, "node", lambda: node):
        _l_(56838)

        aux = ""
        _l_(56837)
        return aux
    _c_(56842, _n_(56839, "print", lambda: print), _a_(56841, _n_(56840, "node", lambda: node), "val"))
    _l_(56843)
    _c_(56847, _n_(56844, "preOrder", lambda: preOrder), _a_(56846, _n_(56845, "node", lambda: node), "left"))
    _l_(56848)
    _c_(56852, _n_(56849, "preOrder", lambda: preOrder), _a_(56851, _n_(56850, "node", lambda: node), "right"))
    _l_(56853)
root = _c_(56856, _n_(56855, "TreeNode", lambda: TreeNode), 5)
_l_(56857)
_n_(56858, "root", lambda: root).right = _c_(56860, _n_(56859, "TreeNode", lambda: TreeNode), 6)
_l_(56861)
_a_(56863, _n_(56862, "root", lambda: root), "left").left = _c_(56865, _n_(56864, "TreeNode", lambda: TreeNode), 2)
_l_(56866)
_a_(56868, _n_(56867, "root", lambda: root), "left").right = _c_(56870, _n_(56869, "TreeNode", lambda: TreeNode), 4)
_l_(56871)
_a_(56874, _a_(56873, _n_(56872, "root", lambda: root), "left"), "right").left = _c_(56876, _n_(56875, "TreeNode", lambda: TreeNode), 7)
_l_(56877)
_c_(56879, _n_(56878, "print", lambda: print), 'Original node:')
_l_(56880)
_c_(56885, _n_(56881, "print", lambda: print), _c_(56884, _n_(56882, "preOrder", lambda: preOrder), _n_(56883, "root", lambda: root)))
_l_(56886)
result = _c_(56889, _n_(56887, "delete_Node", lambda: delete_Node), _n_(56888, "root", lambda: root), 4)
_l_(56890)
_c_(56892, _n_(56891, "print", lambda: print), 'After deleting specified node:')
_l_(56893)
_c_(56898, _n_(56894, "print", lambda: print), _c_(56897, _n_(56895, "preOrder", lambda: preOrder), _n_(56896, "result", lambda: result)))
_l_(56899)