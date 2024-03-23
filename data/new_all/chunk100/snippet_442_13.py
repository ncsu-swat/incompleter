# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(46400, "object", lambda: object)):
    _l_(46409)


    def __init__(self, x):
        _l_(46408)

        _n_(46401, "self", lambda: self).val = _n_(46402, "x", lambda: x)
        _l_(46403)
        _n_(46404, "self", lambda: self).left = None
        _l_(46405)
        _n_(46406, "self", lambda: self).right = None
        _l_(46407)

def kth_smallest(root, k):
    _l_(46438)

    stack = []
    _l_(46410)
    while _n_(46411, "root", lambda: root) or _n_(46412, "stack", lambda: stack):
        _l_(46434)

        while _n_(46413, "root", lambda: root):
            _l_(46422)

            _c_(46417, _a_(46415, _n_(46414, "stack", lambda: stack), "append"), _n_(46416, "root", lambda: root))
            _l_(46418)
            root = _a_(46420, _n_(46419, "root", lambda: root), "left")
            _l_(46421)
        root = _c_(46425, _a_(46424, _n_(46423, "stack", lambda: stack), "pop"))
        _l_(46426)
        k -= 1
        _l_(46427)
        if _n_(46428, "k", lambda: k) == 0:
            _l_(46430)

            break
            _l_(46429)
        root = _a_(46432, _n_(46431, "root", lambda: root), "right")
        _l_(46433)
    aux = _a_(46436, _n_(46435, "root", lambda: root), "val")
    _l_(46437)
    return aux
root = _c_(46440, _n_(46439, "TreeNode", lambda: TreeNode), 8)
_l_(46441)
_n_(46442, "root", lambda: root).left = _c_(46444, _n_(46443, "TreeNode", lambda: TreeNode), 5)
_l_(46445)
_n_(46446, "root", lambda: root).right = _c_(46448, _n_(46447, "TreeNode", lambda: TreeNode), 14)
_l_(46449)
_a_(46451, _n_(46450, "root", lambda: root), "left").left = _c_(46453, _n_(46452, "TreeNode", lambda: TreeNode), 4)
_l_(46454)
_a_(46456, _n_(46455, "root", lambda: root), "left").right = _c_(46458, _n_(46457, "TreeNode", lambda: TreeNode), 6)
_l_(46459)
_a_(46462, _a_(46461, _n_(46460, "root", lambda: root), "left"), "right").right = _c_(46464, _n_(46463, "TreeNode", lambda: TreeNode), 7)
_l_(46465)
_a_(46467, _n_(46466, "root", lambda: root), "right").right = _c_(46469, _n_(46468, "TreeNode", lambda: TreeNode), 24)
_l_(46470)
_a_(46473, _a_(46472, _n_(46471, "root", lambda: root), "right"), "right").left = _c_(46475, _n_(46474, "TreeNode", lambda: TreeNode), 22)
_l_(46476)
_c_(46481, _n_(46477, "print", lambda: print), _c_(46480, _n_(46478, "kth_smallest", lambda: kth_smallest), _n_(46479, "root", lambda: root), 2))
_l_(46482)
_c_(46487, _n_(46483, "print", lambda: print), _c_(46486, _n_(46484, "kth_smallest", lambda: kth_smallest), _n_(46485, "root", lambda: root), 3))
_l_(46488)