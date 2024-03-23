# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(47318, "object", lambda: object)):
    _l_(47327)


    def __init__(self, x):
        _l_(47326)

        _n_(47319, "self", lambda: self).val = _n_(47320, "x", lambda: x)
        _l_(47321)
        _n_(47322, "self", lambda: self).left = None
        _l_(47323)
        _n_(47324, "self", lambda: self).right = None
        _l_(47325)

def kth_smallest(root, k):
    _l_(47353)

    stack = []
    _l_(47328)
    while _n_(47329, "root", lambda: root) or _n_(47330, "stack", lambda: stack):
        _l_(47349)

        while _n_(47331, "root", lambda: root):
            _l_(47337)

            _c_(47335, _a_(47333, _n_(47332, "stack", lambda: stack), "append"), _n_(47334, "root", lambda: root))
            _l_(47336)
        root = _c_(47340, _a_(47339, _n_(47338, "stack", lambda: stack), "pop"))
        _l_(47341)
        k -= 1
        _l_(47342)
        if _n_(47343, "k", lambda: k) == 0:
            _l_(47345)

            break
            _l_(47344)
        root = _a_(47347, _n_(47346, "root", lambda: root), "right")
        _l_(47348)
    aux = _a_(47351, _n_(47350, "root", lambda: root), "val")
    _l_(47352)
    return aux
root = _c_(47355, _n_(47354, "TreeNode", lambda: TreeNode), 8)
_l_(47356)
_n_(47357, "root", lambda: root).left = _c_(47359, _n_(47358, "TreeNode", lambda: TreeNode), 5)
_l_(47360)
_n_(47361, "root", lambda: root).right = _c_(47363, _n_(47362, "TreeNode", lambda: TreeNode), 14)
_l_(47364)
_a_(47366, _n_(47365, "root", lambda: root), "left").left = _c_(47368, _n_(47367, "TreeNode", lambda: TreeNode), 4)
_l_(47369)
_a_(47371, _n_(47370, "root", lambda: root), "left").right = _c_(47373, _n_(47372, "TreeNode", lambda: TreeNode), 6)
_l_(47374)
_a_(47377, _a_(47376, _n_(47375, "root", lambda: root), "left"), "right").left = _c_(47379, _n_(47378, "TreeNode", lambda: TreeNode), 8)
_l_(47380)
_a_(47383, _a_(47382, _n_(47381, "root", lambda: root), "left"), "right").right = _c_(47385, _n_(47384, "TreeNode", lambda: TreeNode), 7)
_l_(47386)
_a_(47388, _n_(47387, "root", lambda: root), "right").right = _c_(47390, _n_(47389, "TreeNode", lambda: TreeNode), 24)
_l_(47391)
_a_(47394, _a_(47393, _n_(47392, "root", lambda: root), "right"), "right").left = _c_(47396, _n_(47395, "TreeNode", lambda: TreeNode), 22)
_l_(47397)
_c_(47402, _n_(47398, "print", lambda: print), _c_(47401, _n_(47399, "kth_smallest", lambda: kth_smallest), _n_(47400, "root", lambda: root), 2))
_l_(47403)
_c_(47408, _n_(47404, "print", lambda: print), _c_(47407, _n_(47405, "kth_smallest", lambda: kth_smallest), _n_(47406, "root", lambda: root), 3))
_l_(47409)