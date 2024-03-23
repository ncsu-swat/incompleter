# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(47043, "object", lambda: object)):
    _l_(47050)


    def __init__(self, x):
        _l_(47049)

        _n_(47044, "self", lambda: self).val = _n_(47045, "x", lambda: x)
        _l_(47046)
        _n_(47047, "self", lambda: self).right = None
        _l_(47048)

def kth_smallest(root, k):
    _l_(47079)

    stack = []
    _l_(47051)
    while _n_(47052, "root", lambda: root) or _n_(47053, "stack", lambda: stack):
        _l_(47075)

        while _n_(47054, "root", lambda: root):
            _l_(47063)

            _c_(47058, _a_(47056, _n_(47055, "stack", lambda: stack), "append"), _n_(47057, "root", lambda: root))
            _l_(47059)
            root = _a_(47061, _n_(47060, "root", lambda: root), "left")
            _l_(47062)
        root = _c_(47066, _a_(47065, _n_(47064, "stack", lambda: stack), "pop"))
        _l_(47067)
        k -= 1
        _l_(47068)
        if _n_(47069, "k", lambda: k) == 0:
            _l_(47071)

            break
            _l_(47070)
        root = _a_(47073, _n_(47072, "root", lambda: root), "right")
        _l_(47074)
    aux = _a_(47077, _n_(47076, "root", lambda: root), "val")
    _l_(47078)
    return aux
root = _c_(47081, _n_(47080, "TreeNode", lambda: TreeNode), 8)
_l_(47082)
_n_(47083, "root", lambda: root).left = _c_(47085, _n_(47084, "TreeNode", lambda: TreeNode), 5)
_l_(47086)
_n_(47087, "root", lambda: root).right = _c_(47089, _n_(47088, "TreeNode", lambda: TreeNode), 14)
_l_(47090)
_a_(47092, _n_(47091, "root", lambda: root), "left").left = _c_(47094, _n_(47093, "TreeNode", lambda: TreeNode), 4)
_l_(47095)
_a_(47097, _n_(47096, "root", lambda: root), "left").right = _c_(47099, _n_(47098, "TreeNode", lambda: TreeNode), 6)
_l_(47100)
_a_(47103, _a_(47102, _n_(47101, "root", lambda: root), "left"), "right").left = _c_(47105, _n_(47104, "TreeNode", lambda: TreeNode), 8)
_l_(47106)
_a_(47109, _a_(47108, _n_(47107, "root", lambda: root), "left"), "right").right = _c_(47111, _n_(47110, "TreeNode", lambda: TreeNode), 7)
_l_(47112)
_a_(47114, _n_(47113, "root", lambda: root), "right").right = _c_(47116, _n_(47115, "TreeNode", lambda: TreeNode), 24)
_l_(47117)
_a_(47120, _a_(47119, _n_(47118, "root", lambda: root), "right"), "right").left = _c_(47122, _n_(47121, "TreeNode", lambda: TreeNode), 22)
_l_(47123)
_c_(47128, _n_(47124, "print", lambda: print), _c_(47127, _n_(47125, "kth_smallest", lambda: kth_smallest), _n_(47126, "root", lambda: root), 2))
_l_(47129)
_c_(47134, _n_(47130, "print", lambda: print), _c_(47133, _n_(47131, "kth_smallest", lambda: kth_smallest), _n_(47132, "root", lambda: root), 3))
_l_(47135)