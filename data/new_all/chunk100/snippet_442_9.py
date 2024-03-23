# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(47500, "object", lambda: object)):
    _l_(47509)


    def __init__(self, x):
        _l_(47508)

        _n_(47501, "self", lambda: self).val = _n_(47502, "x", lambda: x)
        _l_(47503)
        _n_(47504, "self", lambda: self).left = None
        _l_(47505)
        _n_(47506, "self", lambda: self).right = None
        _l_(47507)

def kth_smallest(root, k):
    _l_(47538)

    stack = []
    _l_(47510)
    while _n_(47511, "root", lambda: root) or _n_(47512, "stack", lambda: stack):
        _l_(47534)

        while _n_(47513, "root", lambda: root):
            _l_(47522)

            _c_(47517, _a_(47515, _n_(47514, "stack", lambda: stack), "append"), _n_(47516, "root", lambda: root))
            _l_(47518)
            root = _a_(47520, _n_(47519, "root", lambda: root), "left")
            _l_(47521)
        root = _c_(47525, _a_(47524, _n_(47523, "stack", lambda: stack), "pop"))
        _l_(47526)
        k -= 1
        _l_(47527)
        if _n_(47528, "k", lambda: k) == 0:
            _l_(47530)

            break
            _l_(47529)
        root = _a_(47532, _n_(47531, "root", lambda: root), "right")
        _l_(47533)
    aux = _a_(47536, _n_(47535, "root", lambda: root), "val")
    _l_(47537)
    return aux
root = _c_(47540, _n_(47539, "TreeNode", lambda: TreeNode), 8)
_l_(47541)
_n_(47542, "root", lambda: root).left = _c_(47544, _n_(47543, "TreeNode", lambda: TreeNode), 5)
_l_(47545)
_n_(47546, "root", lambda: root).right = _c_(47548, _n_(47547, "TreeNode", lambda: TreeNode), 14)
_l_(47549)
_a_(47551, _n_(47550, "root", lambda: root), "left").left = _c_(47553, _n_(47552, "TreeNode", lambda: TreeNode), 4)
_l_(47554)
_a_(47556, _n_(47555, "root", lambda: root), "left").right = _c_(47558, _n_(47557, "TreeNode", lambda: TreeNode), 6)
_l_(47559)
_a_(47562, _a_(47561, _n_(47560, "root", lambda: root), "left"), "right").left = _c_(47564, _n_(47563, "TreeNode", lambda: TreeNode), 8)
_l_(47565)
_a_(47568, _a_(47567, _n_(47566, "root", lambda: root), "left"), "right").right = _c_(47570, _n_(47569, "TreeNode", lambda: TreeNode), 7)
_l_(47571)
_a_(47573, _n_(47572, "root", lambda: root), "right").right = _c_(47575, _n_(47574, "TreeNode", lambda: TreeNode), 24)
_l_(47576)
_c_(47581, _n_(47577, "print", lambda: print), _c_(47580, _n_(47578, "kth_smallest", lambda: kth_smallest), _n_(47579, "root", lambda: root), 2))
_l_(47582)
_c_(47587, _n_(47583, "print", lambda: print), _c_(47586, _n_(47584, "kth_smallest", lambda: kth_smallest), _n_(47585, "root", lambda: root), 3))
_l_(47588)