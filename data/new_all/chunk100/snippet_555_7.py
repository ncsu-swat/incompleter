# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(57038, "object", lambda: object)):
    _l_(57045)


    def __init__(self, x):
        _l_(57044)

        _n_(57039, "self", lambda: self).val = _n_(57040, "x", lambda: x)
        _l_(57041)
        _n_(57042, "self", lambda: self).left = None
        _l_(57043)

def delete_Node(root, key):
    _l_(57109)

    if not _n_(57046, "root", lambda: root):
        _l_(57049)

        aux = _n_(57047, "root", lambda: root)
        _l_(57048)
        return aux
    if _a_(57051, _n_(57050, "root", lambda: root), "val") > _n_(57052, "key", lambda: key):
        _l_(57106)

        _n_(57053, "root", lambda: root).left = _c_(57058, _n_(57054, "delete_Node", lambda: delete_Node), _a_(57056, _n_(57055, "root", lambda: root), "left"), _n_(57057, "key", lambda: key))
        _l_(57059)
    elif _a_(57061, _n_(57060, "root", lambda: root), "val") < _n_(57062, "key", lambda: key):
        _l_(57105)

        _n_(57063, "root", lambda: root).right = _c_(57068, _n_(57064, "delete_Node", lambda: delete_Node), _a_(57066, _n_(57065, "root", lambda: root), "right"), _n_(57067, "key", lambda: key))
        _l_(57069)
    else:
        if not _a_(57071, _n_(57070, "root", lambda: root), "right"):
            _l_(57075)

            aux = _a_(57073, _n_(57072, "root", lambda: root), "left")
            _l_(57074)
            return aux
        if not _a_(57077, _n_(57076, "root", lambda: root), "left"):
            _l_(57081)

            aux = _a_(57079, _n_(57078, "root", lambda: root), "right")
            _l_(57080)
            return aux
        temp_val = _a_(57083, _n_(57082, "root", lambda: root), "right")
        _l_(57084)
        mini_val = _a_(57086, _n_(57085, "temp_val", lambda: temp_val), "val")
        _l_(57087)
        while _a_(57089, _n_(57088, "temp_val", lambda: temp_val), "left"):
            _l_(57096)

            temp_val = _a_(57091, _n_(57090, "temp_val", lambda: temp_val), "left")
            _l_(57092)
            mini_val = _a_(57094, _n_(57093, "temp_val", lambda: temp_val), "val")
            _l_(57095)
        _n_(57097, "root", lambda: root).right = _c_(57103, _n_(57098, "deleteNode", lambda: deleteNode), _a_(57100, _n_(57099, "root", lambda: root), "right"), _a_(57102, _n_(57101, "root", lambda: root), "val"))
        _l_(57104)
    aux = _n_(57107, "root", lambda: root)
    _l_(57108)
    return aux

def preOrder(node):
    _l_(57128)

    if not _n_(57110, "node", lambda: node):
        _l_(57112)

        aux = ""
        _l_(57111)
        return aux
    _c_(57116, _n_(57113, "print", lambda: print), _a_(57115, _n_(57114, "node", lambda: node), "val"))
    _l_(57117)
    _c_(57121, _n_(57118, "preOrder", lambda: preOrder), _a_(57120, _n_(57119, "node", lambda: node), "left"))
    _l_(57122)
    _c_(57126, _n_(57123, "preOrder", lambda: preOrder), _a_(57125, _n_(57124, "node", lambda: node), "right"))
    _l_(57127)
root = _c_(57130, _n_(57129, "TreeNode", lambda: TreeNode), 5)
_l_(57131)
_n_(57132, "root", lambda: root).left = _c_(57134, _n_(57133, "TreeNode", lambda: TreeNode), 3)
_l_(57135)
_n_(57136, "root", lambda: root).right = _c_(57138, _n_(57137, "TreeNode", lambda: TreeNode), 6)
_l_(57139)
_a_(57141, _n_(57140, "root", lambda: root), "left").left = _c_(57143, _n_(57142, "TreeNode", lambda: TreeNode), 2)
_l_(57144)
_a_(57146, _n_(57145, "root", lambda: root), "left").right = _c_(57148, _n_(57147, "TreeNode", lambda: TreeNode), 4)
_l_(57149)
_a_(57152, _a_(57151, _n_(57150, "root", lambda: root), "left"), "right").left = _c_(57154, _n_(57153, "TreeNode", lambda: TreeNode), 7)
_l_(57155)
_c_(57157, _n_(57156, "print", lambda: print), 'Original node:')
_l_(57158)
_c_(57163, _n_(57159, "print", lambda: print), _c_(57162, _n_(57160, "preOrder", lambda: preOrder), _n_(57161, "root", lambda: root)))
_l_(57164)
result = _c_(57167, _n_(57165, "delete_Node", lambda: delete_Node), _n_(57166, "root", lambda: root), 4)
_l_(57168)
_c_(57170, _n_(57169, "print", lambda: print), 'After deleting specified node:')
_l_(57171)
_c_(57176, _n_(57172, "print", lambda: print), _c_(57175, _n_(57173, "preOrder", lambda: preOrder), _n_(57174, "result", lambda: result)))
_l_(57177)