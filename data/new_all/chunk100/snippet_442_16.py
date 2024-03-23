# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(46672, "object", lambda: object)):
    _l_(46678)


    def __init__(self, x):
        _l_(46677)

        _n_(46673, "self", lambda: self).left = None
        _l_(46674)
        _n_(46675, "self", lambda: self).right = None
        _l_(46676)

def kth_smallest(root, k):
    _l_(46707)

    stack = []
    _l_(46679)
    while _n_(46680, "root", lambda: root) or _n_(46681, "stack", lambda: stack):
        _l_(46703)

        while _n_(46682, "root", lambda: root):
            _l_(46691)

            _c_(46686, _a_(46684, _n_(46683, "stack", lambda: stack), "append"), _n_(46685, "root", lambda: root))
            _l_(46687)
            root = _a_(46689, _n_(46688, "root", lambda: root), "left")
            _l_(46690)
        root = _c_(46694, _a_(46693, _n_(46692, "stack", lambda: stack), "pop"))
        _l_(46695)
        k -= 1
        _l_(46696)
        if _n_(46697, "k", lambda: k) == 0:
            _l_(46699)

            break
            _l_(46698)
        root = _a_(46701, _n_(46700, "root", lambda: root), "right")
        _l_(46702)
    aux = _a_(46705, _n_(46704, "root", lambda: root), "val")
    _l_(46706)
    return aux
root = _c_(46709, _n_(46708, "TreeNode", lambda: TreeNode), 8)
_l_(46710)
_n_(46711, "root", lambda: root).left = _c_(46713, _n_(46712, "TreeNode", lambda: TreeNode), 5)
_l_(46714)
_n_(46715, "root", lambda: root).right = _c_(46717, _n_(46716, "TreeNode", lambda: TreeNode), 14)
_l_(46718)
_a_(46720, _n_(46719, "root", lambda: root), "left").left = _c_(46722, _n_(46721, "TreeNode", lambda: TreeNode), 4)
_l_(46723)
_a_(46725, _n_(46724, "root", lambda: root), "left").right = _c_(46727, _n_(46726, "TreeNode", lambda: TreeNode), 6)
_l_(46728)
_a_(46731, _a_(46730, _n_(46729, "root", lambda: root), "left"), "right").left = _c_(46733, _n_(46732, "TreeNode", lambda: TreeNode), 8)
_l_(46734)
_a_(46737, _a_(46736, _n_(46735, "root", lambda: root), "left"), "right").right = _c_(46739, _n_(46738, "TreeNode", lambda: TreeNode), 7)
_l_(46740)
_a_(46742, _n_(46741, "root", lambda: root), "right").right = _c_(46744, _n_(46743, "TreeNode", lambda: TreeNode), 24)
_l_(46745)
_a_(46748, _a_(46747, _n_(46746, "root", lambda: root), "right"), "right").left = _c_(46750, _n_(46749, "TreeNode", lambda: TreeNode), 22)
_l_(46751)
_c_(46756, _n_(46752, "print", lambda: print), _c_(46755, _n_(46753, "kth_smallest", lambda: kth_smallest), _n_(46754, "root", lambda: root), 2))
_l_(46757)
_c_(46762, _n_(46758, "print", lambda: print), _c_(46761, _n_(46759, "kth_smallest", lambda: kth_smallest), _n_(46760, "root", lambda: root), 3))
_l_(46763)