# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(56071, "object", lambda: object)):
    _l_(56080)


    def __init__(self, x):
        _l_(56079)

        _n_(56072, "self", lambda: self).val = _n_(56073, "x", lambda: x)
        _l_(56074)
        _n_(56075, "self", lambda: self).left = None
        _l_(56076)
        _n_(56077, "self", lambda: self).right = None
        _l_(56078)

def delete_Node(root, key):
    _l_(56144)

    if not _n_(56081, "root", lambda: root):
        _l_(56084)

        aux = _n_(56082, "root", lambda: root)
        _l_(56083)
        return aux
    if _a_(56086, _n_(56085, "root", lambda: root), "val") > _n_(56087, "key", lambda: key):
        _l_(56141)

        _n_(56088, "root", lambda: root).left = _c_(56093, _n_(56089, "delete_Node", lambda: delete_Node), _a_(56091, _n_(56090, "root", lambda: root), "left"), _n_(56092, "key", lambda: key))
        _l_(56094)
    elif _a_(56096, _n_(56095, "root", lambda: root), "val") < _n_(56097, "key", lambda: key):
        _l_(56140)

        _n_(56098, "root", lambda: root).right = _c_(56103, _n_(56099, "delete_Node", lambda: delete_Node), _a_(56101, _n_(56100, "root", lambda: root), "right"), _n_(56102, "key", lambda: key))
        _l_(56104)
    else:
        if not _a_(56106, _n_(56105, "root", lambda: root), "right"):
            _l_(56110)

            aux = _a_(56108, _n_(56107, "root", lambda: root), "left")
            _l_(56109)
            return aux
        if not _a_(56112, _n_(56111, "root", lambda: root), "left"):
            _l_(56116)

            aux = _a_(56114, _n_(56113, "root", lambda: root), "right")
            _l_(56115)
            return aux
        temp_val = _a_(56118, _n_(56117, "root", lambda: root), "right")
        _l_(56119)
        mini_val = _a_(56121, _n_(56120, "temp_val", lambda: temp_val), "val")
        _l_(56122)
        while _a_(56124, _n_(56123, "temp_val", lambda: temp_val), "left"):
            _l_(56131)

            temp_val = _a_(56126, _n_(56125, "temp_val", lambda: temp_val), "left")
            _l_(56127)
            mini_val = _a_(56129, _n_(56128, "temp_val", lambda: temp_val), "val")
            _l_(56130)
        _n_(56132, "root", lambda: root).right = _c_(56138, _n_(56133, "deleteNode", lambda: deleteNode), _a_(56135, _n_(56134, "root", lambda: root), "right"), _a_(56137, _n_(56136, "root", lambda: root), "val"))
        _l_(56139)
    aux = _n_(56142, "root", lambda: root)
    _l_(56143)
    return aux

def preOrder(node):
    _l_(56163)

    if not _n_(56145, "node", lambda: node):
        _l_(56147)

        aux = ""
        _l_(56146)
        return aux
    _c_(56151, _n_(56148, "print", lambda: print), _a_(56150, _n_(56149, "node", lambda: node), "val"))
    _l_(56152)
    _c_(56156, _n_(56153, "preOrder", lambda: preOrder), _a_(56155, _n_(56154, "node", lambda: node), "left"))
    _l_(56157)
    _c_(56161, _n_(56158, "preOrder", lambda: preOrder), _a_(56160, _n_(56159, "node", lambda: node), "right"))
    _l_(56162)
_n_(56164, "root", lambda: root).left = _c_(56166, _n_(56165, "TreeNode", lambda: TreeNode), 3)
_l_(56167)
_n_(56168, "root", lambda: root).right = _c_(56170, _n_(56169, "TreeNode", lambda: TreeNode), 6)
_l_(56171)
_a_(56173, _n_(56172, "root", lambda: root), "left").left = _c_(56175, _n_(56174, "TreeNode", lambda: TreeNode), 2)
_l_(56176)
_a_(56178, _n_(56177, "root", lambda: root), "left").right = _c_(56180, _n_(56179, "TreeNode", lambda: TreeNode), 4)
_l_(56181)
_a_(56184, _a_(56183, _n_(56182, "root", lambda: root), "left"), "right").left = _c_(56186, _n_(56185, "TreeNode", lambda: TreeNode), 7)
_l_(56187)
_c_(56189, _n_(56188, "print", lambda: print), 'Original node:')
_l_(56190)
_c_(56195, _n_(56191, "print", lambda: print), _c_(56194, _n_(56192, "preOrder", lambda: preOrder), _n_(56193, "root", lambda: root)))
_l_(56196)
result = _c_(56199, _n_(56197, "delete_Node", lambda: delete_Node), _n_(56198, "root", lambda: root), 4)
_l_(56200)
_c_(56202, _n_(56201, "print", lambda: print), 'After deleting specified node:')
_l_(56203)
_c_(56208, _n_(56204, "print", lambda: print), _c_(56207, _n_(56205, "preOrder", lambda: preOrder), _n_(56206, "result", lambda: result)))
_l_(56209)