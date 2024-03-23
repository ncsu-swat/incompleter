# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(46310, "object", lambda: object)):
    _l_(46319)


    def __init__(self, x):
        _l_(46318)

        _n_(46311, "self", lambda: self).val = _n_(46312, "x", lambda: x)
        _l_(46313)
        _n_(46314, "self", lambda: self).left = None
        _l_(46315)
        _n_(46316, "self", lambda: self).right = None
        _l_(46317)

def kth_smallest(root, k):
    _l_(46348)

    stack = []
    _l_(46320)
    while _n_(46321, "root", lambda: root) or _n_(46322, "stack", lambda: stack):
        _l_(46344)

        while _n_(46323, "root", lambda: root):
            _l_(46332)

            _c_(46327, _a_(46325, _n_(46324, "stack", lambda: stack), "append"), _n_(46326, "root", lambda: root))
            _l_(46328)
            root = _a_(46330, _n_(46329, "root", lambda: root), "left")
            _l_(46331)
        root = _c_(46335, _a_(46334, _n_(46333, "stack", lambda: stack), "pop"))
        _l_(46336)
        k -= 1
        _l_(46337)
        if _n_(46338, "k", lambda: k) == 0:
            _l_(46340)

            break
            _l_(46339)
        root = _a_(46342, _n_(46341, "root", lambda: root), "right")
        _l_(46343)
    aux = _a_(46346, _n_(46345, "root", lambda: root), "val")
    _l_(46347)
    return aux
root = _c_(46350, _n_(46349, "TreeNode", lambda: TreeNode), 8)
_l_(46351)
_n_(46352, "root", lambda: root).left = _c_(46354, _n_(46353, "TreeNode", lambda: TreeNode), 5)
_l_(46355)
_n_(46356, "root", lambda: root).right = _c_(46358, _n_(46357, "TreeNode", lambda: TreeNode), 14)
_l_(46359)
_a_(46361, _n_(46360, "root", lambda: root), "left").left = _c_(46363, _n_(46362, "TreeNode", lambda: TreeNode), 4)
_l_(46364)
_a_(46367, _a_(46366, _n_(46365, "root", lambda: root), "left"), "right").left = _c_(46369, _n_(46368, "TreeNode", lambda: TreeNode), 8)
_l_(46370)
_a_(46373, _a_(46372, _n_(46371, "root", lambda: root), "left"), "right").right = _c_(46375, _n_(46374, "TreeNode", lambda: TreeNode), 7)
_l_(46376)
_a_(46378, _n_(46377, "root", lambda: root), "right").right = _c_(46380, _n_(46379, "TreeNode", lambda: TreeNode), 24)
_l_(46381)
_a_(46384, _a_(46383, _n_(46382, "root", lambda: root), "right"), "right").left = _c_(46386, _n_(46385, "TreeNode", lambda: TreeNode), 22)
_l_(46387)
_c_(46392, _n_(46388, "print", lambda: print), _c_(46391, _n_(46389, "kth_smallest", lambda: kth_smallest), _n_(46390, "root", lambda: root), 2))
_l_(46393)
_c_(46398, _n_(46394, "print", lambda: print), _c_(46397, _n_(46395, "kth_smallest", lambda: kth_smallest), _n_(46396, "root", lambda: root), 3))
_l_(46399)