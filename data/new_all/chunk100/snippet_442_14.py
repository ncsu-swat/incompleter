# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(46489, "object", lambda: object)):
    _l_(46498)


    def __init__(self, x):
        _l_(46497)

        _n_(46490, "self", lambda: self).val = _n_(46491, "x", lambda: x)
        _l_(46492)
        _n_(46493, "self", lambda: self).left = None
        _l_(46494)
        _n_(46495, "self", lambda: self).right = None
        _l_(46496)

def kth_smallest(root, k):
    _l_(46527)

    stack = []
    _l_(46499)
    while _n_(46500, "root", lambda: root) or _n_(46501, "stack", lambda: stack):
        _l_(46523)

        while _n_(46502, "root", lambda: root):
            _l_(46511)

            _c_(46506, _a_(46504, _n_(46503, "stack", lambda: stack), "append"), _n_(46505, "root", lambda: root))
            _l_(46507)
            root = _a_(46509, _n_(46508, "root", lambda: root), "left")
            _l_(46510)
        root = _c_(46514, _a_(46513, _n_(46512, "stack", lambda: stack), "pop"))
        _l_(46515)
        k -= 1
        _l_(46516)
        if _n_(46517, "k", lambda: k) == 0:
            _l_(46519)

            break
            _l_(46518)
        root = _a_(46521, _n_(46520, "root", lambda: root), "right")
        _l_(46522)
    aux = _a_(46525, _n_(46524, "root", lambda: root), "val")
    _l_(46526)
    return aux
root = _c_(46529, _n_(46528, "TreeNode", lambda: TreeNode), 8)
_l_(46530)
_n_(46531, "root", lambda: root).right = _c_(46533, _n_(46532, "TreeNode", lambda: TreeNode), 14)
_l_(46534)
_a_(46536, _n_(46535, "root", lambda: root), "left").left = _c_(46538, _n_(46537, "TreeNode", lambda: TreeNode), 4)
_l_(46539)
_a_(46541, _n_(46540, "root", lambda: root), "left").right = _c_(46543, _n_(46542, "TreeNode", lambda: TreeNode), 6)
_l_(46544)
_a_(46547, _a_(46546, _n_(46545, "root", lambda: root), "left"), "right").left = _c_(46549, _n_(46548, "TreeNode", lambda: TreeNode), 8)
_l_(46550)
_a_(46553, _a_(46552, _n_(46551, "root", lambda: root), "left"), "right").right = _c_(46555, _n_(46554, "TreeNode", lambda: TreeNode), 7)
_l_(46556)
_a_(46558, _n_(46557, "root", lambda: root), "right").right = _c_(46560, _n_(46559, "TreeNode", lambda: TreeNode), 24)
_l_(46561)
_a_(46564, _a_(46563, _n_(46562, "root", lambda: root), "right"), "right").left = _c_(46566, _n_(46565, "TreeNode", lambda: TreeNode), 22)
_l_(46567)
_c_(46572, _n_(46568, "print", lambda: print), _c_(46571, _n_(46569, "kth_smallest", lambda: kth_smallest), _n_(46570, "root", lambda: root), 2))
_l_(46573)
_c_(46578, _n_(46574, "print", lambda: print), _c_(46577, _n_(46575, "kth_smallest", lambda: kth_smallest), _n_(46576, "root", lambda: root), 3))
_l_(46579)