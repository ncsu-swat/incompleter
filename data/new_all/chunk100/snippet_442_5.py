# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(47136, "object", lambda: object)):
    _l_(47145)


    def __init__(self, x):
        _l_(47144)

        _n_(47137, "self", lambda: self).val = _n_(47138, "x", lambda: x)
        _l_(47139)
        _n_(47140, "self", lambda: self).left = None
        _l_(47141)
        _n_(47142, "self", lambda: self).right = None
        _l_(47143)

def kth_smallest(root, k):
    _l_(47174)

    stack = []
    _l_(47146)
    while _n_(47147, "root", lambda: root) or _n_(47148, "stack", lambda: stack):
        _l_(47170)

        while _n_(47149, "root", lambda: root):
            _l_(47158)

            _c_(47153, _a_(47151, _n_(47150, "stack", lambda: stack), "append"), _n_(47152, "root", lambda: root))
            _l_(47154)
            root = _a_(47156, _n_(47155, "root", lambda: root), "left")
            _l_(47157)
        root = _c_(47161, _a_(47160, _n_(47159, "stack", lambda: stack), "pop"))
        _l_(47162)
        k -= 1
        _l_(47163)
        if _n_(47164, "k", lambda: k) == 0:
            _l_(47166)

            break
            _l_(47165)
        root = _a_(47168, _n_(47167, "root", lambda: root), "right")
        _l_(47169)
    aux = _a_(47172, _n_(47171, "root", lambda: root), "val")
    _l_(47173)
    return aux
_n_(47175, "root", lambda: root).left = _c_(47177, _n_(47176, "TreeNode", lambda: TreeNode), 5)
_l_(47178)
_n_(47179, "root", lambda: root).right = _c_(47181, _n_(47180, "TreeNode", lambda: TreeNode), 14)
_l_(47182)
_a_(47184, _n_(47183, "root", lambda: root), "left").left = _c_(47186, _n_(47185, "TreeNode", lambda: TreeNode), 4)
_l_(47187)
_a_(47189, _n_(47188, "root", lambda: root), "left").right = _c_(47191, _n_(47190, "TreeNode", lambda: TreeNode), 6)
_l_(47192)
_a_(47195, _a_(47194, _n_(47193, "root", lambda: root), "left"), "right").left = _c_(47197, _n_(47196, "TreeNode", lambda: TreeNode), 8)
_l_(47198)
_a_(47201, _a_(47200, _n_(47199, "root", lambda: root), "left"), "right").right = _c_(47203, _n_(47202, "TreeNode", lambda: TreeNode), 7)
_l_(47204)
_a_(47206, _n_(47205, "root", lambda: root), "right").right = _c_(47208, _n_(47207, "TreeNode", lambda: TreeNode), 24)
_l_(47209)
_a_(47212, _a_(47211, _n_(47210, "root", lambda: root), "right"), "right").left = _c_(47214, _n_(47213, "TreeNode", lambda: TreeNode), 22)
_l_(47215)
_c_(47220, _n_(47216, "print", lambda: print), _c_(47219, _n_(47217, "kth_smallest", lambda: kth_smallest), _n_(47218, "root", lambda: root), 2))
_l_(47221)
_c_(47226, _n_(47222, "print", lambda: print), _c_(47225, _n_(47223, "kth_smallest", lambda: kth_smallest), _n_(47224, "root", lambda: root), 3))
_l_(47227)