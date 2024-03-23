# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(47228, "object", lambda: object)):
    _l_(47237)


    def __init__(self, x):
        _l_(47236)

        _n_(47229, "self", lambda: self).val = _n_(47230, "x", lambda: x)
        _l_(47231)
        _n_(47232, "self", lambda: self).left = None
        _l_(47233)
        _n_(47234, "self", lambda: self).right = None
        _l_(47235)

def kth_smallest(root, k):
    _l_(47266)

    stack = []
    _l_(47238)
    while _n_(47239, "root", lambda: root) or _n_(47240, "stack", lambda: stack):
        _l_(47262)

        while _n_(47241, "root", lambda: root):
            _l_(47250)

            _c_(47245, _a_(47243, _n_(47242, "stack", lambda: stack), "append"), _n_(47244, "root", lambda: root))
            _l_(47246)
            root = _a_(47248, _n_(47247, "root", lambda: root), "left")
            _l_(47249)
        root = _c_(47253, _a_(47252, _n_(47251, "stack", lambda: stack), "pop"))
        _l_(47254)
        k -= 1
        _l_(47255)
        if _n_(47256, "k", lambda: k) == 0:
            _l_(47258)

            break
            _l_(47257)
        root = _a_(47260, _n_(47259, "root", lambda: root), "right")
        _l_(47261)
    aux = _a_(47264, _n_(47263, "root", lambda: root), "val")
    _l_(47265)
    return aux
root = _c_(47268, _n_(47267, "TreeNode", lambda: TreeNode), 8)
_l_(47269)
_n_(47270, "root", lambda: root).left = _c_(47272, _n_(47271, "TreeNode", lambda: TreeNode), 5)
_l_(47273)
_n_(47274, "root", lambda: root).right = _c_(47276, _n_(47275, "TreeNode", lambda: TreeNode), 14)
_l_(47277)
_a_(47279, _n_(47278, "root", lambda: root), "left").right = _c_(47281, _n_(47280, "TreeNode", lambda: TreeNode), 6)
_l_(47282)
_a_(47285, _a_(47284, _n_(47283, "root", lambda: root), "left"), "right").left = _c_(47287, _n_(47286, "TreeNode", lambda: TreeNode), 8)
_l_(47288)
_a_(47291, _a_(47290, _n_(47289, "root", lambda: root), "left"), "right").right = _c_(47293, _n_(47292, "TreeNode", lambda: TreeNode), 7)
_l_(47294)
_a_(47296, _n_(47295, "root", lambda: root), "right").right = _c_(47298, _n_(47297, "TreeNode", lambda: TreeNode), 24)
_l_(47299)
_a_(47302, _a_(47301, _n_(47300, "root", lambda: root), "right"), "right").left = _c_(47304, _n_(47303, "TreeNode", lambda: TreeNode), 22)
_l_(47305)
_c_(47310, _n_(47306, "print", lambda: print), _c_(47309, _n_(47307, "kth_smallest", lambda: kth_smallest), _n_(47308, "root", lambda: root), 2))
_l_(47311)
_c_(47316, _n_(47312, "print", lambda: print), _c_(47315, _n_(47313, "kth_smallest", lambda: kth_smallest), _n_(47314, "root", lambda: root), 3))
_l_(47317)