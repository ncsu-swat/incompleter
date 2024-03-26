# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(116501, "object", lambda: object)):
    _l_(116510)


    def __init__(self, x):
        _l_(116509)

        _n_(116502, "self", lambda: self).val = _n_(116503, "x", lambda: x)
        _l_(116504)
        _n_(116505, "self", lambda: self).left = None
        _l_(116506)
        _n_(116507, "self", lambda: self).right = None
        _l_(116508)

def kth_smallest(root, k):
    _l_(116539)

    stack = []
    _l_(116511)
    while _n_(116512, "root", lambda: root) or _n_(116513, "stack", lambda: stack):
        _l_(116535)

        while _n_(116514, "root", lambda: root):
            _l_(116523)

            _c_(116518, _a_(116516, _n_(116515, "stack", lambda: stack), "append"), _n_(116517, "root", lambda: root))
            _l_(116519)
            root = _a_(116521, _n_(116520, "root", lambda: root), "left")
            _l_(116522)
        root = _c_(116526, _a_(116525, _n_(116524, "stack", lambda: stack), "pop"))
        _l_(116527)
        k -= 1
        _l_(116528)
        if _n_(116529, "k", lambda: k) == 0:
            _l_(116531)

            break
            _l_(116530)
        root = _a_(116533, _n_(116532, "root", lambda: root), "right")
        _l_(116534)
    aux = _a_(116537, _n_(116536, "root", lambda: root), "val")
    _l_(116538)
    return aux
_n_(116540, "root", lambda: root).left = _c_(116542, _n_(116541, "TreeNode", lambda: TreeNode), 5)
_l_(116543)
_n_(116544, "root", lambda: root).right = _c_(116546, _n_(116545, "TreeNode", lambda: TreeNode), 14)
_l_(116547)
_a_(116549, _n_(116548, "root", lambda: root), "left").left = _c_(116551, _n_(116550, "TreeNode", lambda: TreeNode), 4)
_l_(116552)
_a_(116554, _n_(116553, "root", lambda: root), "left").right = _c_(116556, _n_(116555, "TreeNode", lambda: TreeNode), 6)
_l_(116557)
_a_(116560, _a_(116559, _n_(116558, "root", lambda: root), "left"), "right").left = _c_(116562, _n_(116561, "TreeNode", lambda: TreeNode), 8)
_l_(116563)
_a_(116566, _a_(116565, _n_(116564, "root", lambda: root), "left"), "right").right = _c_(116568, _n_(116567, "TreeNode", lambda: TreeNode), 7)
_l_(116569)
_a_(116571, _n_(116570, "root", lambda: root), "right").right = _c_(116573, _n_(116572, "TreeNode", lambda: TreeNode), 24)
_l_(116574)
_a_(116577, _a_(116576, _n_(116575, "root", lambda: root), "right"), "right").left = _c_(116579, _n_(116578, "TreeNode", lambda: TreeNode), 22)
_l_(116580)
_c_(116585, _n_(116581, "print", lambda: print), _c_(116584, _n_(116582, "kth_smallest", lambda: kth_smallest), _n_(116583, "root", lambda: root), 2))
_l_(116586)
_c_(116591, _n_(116587, "print", lambda: print), _c_(116590, _n_(116588, "kth_smallest", lambda: kth_smallest), _n_(116589, "root", lambda: root), 3))
_l_(116592)