# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(57178, "object", lambda: object)):
    _l_(57187)


    def __init__(self, x):
        _l_(57186)

        _n_(57179, "self", lambda: self).val = _n_(57180, "x", lambda: x)
        _l_(57181)
        _n_(57182, "self", lambda: self).left = None
        _l_(57183)
        _n_(57184, "self", lambda: self).right = None
        _l_(57185)

def delete_Node(root, key):
    _l_(57251)

    if not _n_(57188, "root", lambda: root):
        _l_(57191)

        aux = _n_(57189, "root", lambda: root)
        _l_(57190)
        return aux
    if _a_(57193, _n_(57192, "root", lambda: root), "val") > _n_(57194, "key", lambda: key):
        _l_(57248)

        _n_(57195, "root", lambda: root).left = _c_(57200, _n_(57196, "delete_Node", lambda: delete_Node), _a_(57198, _n_(57197, "root", lambda: root), "left"), _n_(57199, "key", lambda: key))
        _l_(57201)
    elif _a_(57203, _n_(57202, "root", lambda: root), "val") < _n_(57204, "key", lambda: key):
        _l_(57247)

        _n_(57205, "root", lambda: root).right = _c_(57210, _n_(57206, "delete_Node", lambda: delete_Node), _a_(57208, _n_(57207, "root", lambda: root), "right"), _n_(57209, "key", lambda: key))
        _l_(57211)
    else:
        if not _a_(57213, _n_(57212, "root", lambda: root), "right"):
            _l_(57217)

            aux = _a_(57215, _n_(57214, "root", lambda: root), "left")
            _l_(57216)
            return aux
        if not _a_(57219, _n_(57218, "root", lambda: root), "left"):
            _l_(57223)

            aux = _a_(57221, _n_(57220, "root", lambda: root), "right")
            _l_(57222)
            return aux
        temp_val = _a_(57225, _n_(57224, "root", lambda: root), "right")
        _l_(57226)
        mini_val = _a_(57228, _n_(57227, "temp_val", lambda: temp_val), "val")
        _l_(57229)
        while _a_(57231, _n_(57230, "temp_val", lambda: temp_val), "left"):
            _l_(57238)

            temp_val = _a_(57233, _n_(57232, "temp_val", lambda: temp_val), "left")
            _l_(57234)
            mini_val = _a_(57236, _n_(57235, "temp_val", lambda: temp_val), "val")
            _l_(57237)
        _n_(57239, "root", lambda: root).right = _c_(57245, _n_(57240, "deleteNode", lambda: deleteNode), _a_(57242, _n_(57241, "root", lambda: root), "right"), _a_(57244, _n_(57243, "root", lambda: root), "val"))
        _l_(57246)
    aux = _n_(57249, "root", lambda: root)
    _l_(57250)
    return aux

def preOrder(node):
    _l_(57270)

    if not _n_(57252, "node", lambda: node):
        _l_(57254)

        aux = ""
        _l_(57253)
        return aux
    _c_(57258, _n_(57255, "print", lambda: print), _a_(57257, _n_(57256, "node", lambda: node), "val"))
    _l_(57259)
    _c_(57263, _n_(57260, "preOrder", lambda: preOrder), _a_(57262, _n_(57261, "node", lambda: node), "left"))
    _l_(57264)
    _c_(57268, _n_(57265, "preOrder", lambda: preOrder), _a_(57267, _n_(57266, "node", lambda: node), "right"))
    _l_(57269)
root = _c_(57272, _n_(57271, "TreeNode", lambda: TreeNode), 5)
_l_(57273)
_n_(57274, "root", lambda: root).left = _c_(57276, _n_(57275, "TreeNode", lambda: TreeNode), 3)
_l_(57277)
_n_(57278, "root", lambda: root).right = _c_(57280, _n_(57279, "TreeNode", lambda: TreeNode), 6)
_l_(57281)
_a_(57283, _n_(57282, "root", lambda: root), "left").left = _c_(57285, _n_(57284, "TreeNode", lambda: TreeNode), 2)
_l_(57286)
_a_(57288, _n_(57287, "root", lambda: root), "left").right = _c_(57290, _n_(57289, "TreeNode", lambda: TreeNode), 4)
_l_(57291)
_c_(57293, _n_(57292, "print", lambda: print), 'Original node:')
_l_(57294)
_c_(57299, _n_(57295, "print", lambda: print), _c_(57298, _n_(57296, "preOrder", lambda: preOrder), _n_(57297, "root", lambda: root)))
_l_(57300)
result = _c_(57303, _n_(57301, "delete_Node", lambda: delete_Node), _n_(57302, "root", lambda: root), 4)
_l_(57304)
_c_(57306, _n_(57305, "print", lambda: print), 'After deleting specified node:')
_l_(57307)
_c_(57312, _n_(57308, "print", lambda: print), _c_(57311, _n_(57309, "preOrder", lambda: preOrder), _n_(57310, "result", lambda: result)))
_l_(57313)