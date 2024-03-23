# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(56622, "object", lambda: object)):
    _l_(56629)


    def __init__(self, x):
        _l_(56628)

        _n_(56623, "self", lambda: self).val = _n_(56624, "x", lambda: x)
        _l_(56625)
        _n_(56626, "self", lambda: self).right = None
        _l_(56627)

def delete_Node(root, key):
    _l_(56693)

    if not _n_(56630, "root", lambda: root):
        _l_(56633)

        aux = _n_(56631, "root", lambda: root)
        _l_(56632)
        return aux
    if _a_(56635, _n_(56634, "root", lambda: root), "val") > _n_(56636, "key", lambda: key):
        _l_(56690)

        _n_(56637, "root", lambda: root).left = _c_(56642, _n_(56638, "delete_Node", lambda: delete_Node), _a_(56640, _n_(56639, "root", lambda: root), "left"), _n_(56641, "key", lambda: key))
        _l_(56643)
    elif _a_(56645, _n_(56644, "root", lambda: root), "val") < _n_(56646, "key", lambda: key):
        _l_(56689)

        _n_(56647, "root", lambda: root).right = _c_(56652, _n_(56648, "delete_Node", lambda: delete_Node), _a_(56650, _n_(56649, "root", lambda: root), "right"), _n_(56651, "key", lambda: key))
        _l_(56653)
    else:
        if not _a_(56655, _n_(56654, "root", lambda: root), "right"):
            _l_(56659)

            aux = _a_(56657, _n_(56656, "root", lambda: root), "left")
            _l_(56658)
            return aux
        if not _a_(56661, _n_(56660, "root", lambda: root), "left"):
            _l_(56665)

            aux = _a_(56663, _n_(56662, "root", lambda: root), "right")
            _l_(56664)
            return aux
        temp_val = _a_(56667, _n_(56666, "root", lambda: root), "right")
        _l_(56668)
        mini_val = _a_(56670, _n_(56669, "temp_val", lambda: temp_val), "val")
        _l_(56671)
        while _a_(56673, _n_(56672, "temp_val", lambda: temp_val), "left"):
            _l_(56680)

            temp_val = _a_(56675, _n_(56674, "temp_val", lambda: temp_val), "left")
            _l_(56676)
            mini_val = _a_(56678, _n_(56677, "temp_val", lambda: temp_val), "val")
            _l_(56679)
        _n_(56681, "root", lambda: root).right = _c_(56687, _n_(56682, "deleteNode", lambda: deleteNode), _a_(56684, _n_(56683, "root", lambda: root), "right"), _a_(56686, _n_(56685, "root", lambda: root), "val"))
        _l_(56688)
    aux = _n_(56691, "root", lambda: root)
    _l_(56692)
    return aux

def preOrder(node):
    _l_(56712)

    if not _n_(56694, "node", lambda: node):
        _l_(56696)

        aux = ""
        _l_(56695)
        return aux
    _c_(56700, _n_(56697, "print", lambda: print), _a_(56699, _n_(56698, "node", lambda: node), "val"))
    _l_(56701)
    _c_(56705, _n_(56702, "preOrder", lambda: preOrder), _a_(56704, _n_(56703, "node", lambda: node), "left"))
    _l_(56706)
    _c_(56710, _n_(56707, "preOrder", lambda: preOrder), _a_(56709, _n_(56708, "node", lambda: node), "right"))
    _l_(56711)
root = _c_(56714, _n_(56713, "TreeNode", lambda: TreeNode), 5)
_l_(56715)
_n_(56716, "root", lambda: root).left = _c_(56718, _n_(56717, "TreeNode", lambda: TreeNode), 3)
_l_(56719)
_n_(56720, "root", lambda: root).right = _c_(56722, _n_(56721, "TreeNode", lambda: TreeNode), 6)
_l_(56723)
_a_(56725, _n_(56724, "root", lambda: root), "left").left = _c_(56727, _n_(56726, "TreeNode", lambda: TreeNode), 2)
_l_(56728)
_a_(56730, _n_(56729, "root", lambda: root), "left").right = _c_(56732, _n_(56731, "TreeNode", lambda: TreeNode), 4)
_l_(56733)
_a_(56736, _a_(56735, _n_(56734, "root", lambda: root), "left"), "right").left = _c_(56738, _n_(56737, "TreeNode", lambda: TreeNode), 7)
_l_(56739)
_c_(56741, _n_(56740, "print", lambda: print), 'Original node:')
_l_(56742)
_c_(56747, _n_(56743, "print", lambda: print), _c_(56746, _n_(56744, "preOrder", lambda: preOrder), _n_(56745, "root", lambda: root)))
_l_(56748)
result = _c_(56751, _n_(56749, "delete_Node", lambda: delete_Node), _n_(56750, "root", lambda: root), 4)
_l_(56752)
_c_(56754, _n_(56753, "print", lambda: print), 'After deleting specified node:')
_l_(56755)
_c_(56760, _n_(56756, "print", lambda: print), _c_(56759, _n_(56757, "preOrder", lambda: preOrder), _n_(56758, "result", lambda: result)))
_l_(56761)