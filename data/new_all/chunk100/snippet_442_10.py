# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(46127, "object", lambda: object)):
    _l_(46136)


    def __init__(self, x):
        _l_(46135)

        _n_(46128, "self", lambda: self).val = _n_(46129, "x", lambda: x)
        _l_(46130)
        _n_(46131, "self", lambda: self).left = None
        _l_(46132)
        _n_(46133, "self", lambda: self).right = None
        _l_(46134)

def kth_smallest(root, k):
    _l_(46161)

    stack = []
    _l_(46137)
    while _n_(46138, "root", lambda: root) or _n_(46139, "stack", lambda: stack):
        _l_(46157)

        while _n_(46140, "root", lambda: root):
            _l_(46149)

            _c_(46144, _a_(46142, _n_(46141, "stack", lambda: stack), "append"), _n_(46143, "root", lambda: root))
            _l_(46145)
            root = _a_(46147, _n_(46146, "root", lambda: root), "left")
            _l_(46148)
        k -= 1
        _l_(46150)
        if _n_(46151, "k", lambda: k) == 0:
            _l_(46153)

            break
            _l_(46152)
        root = _a_(46155, _n_(46154, "root", lambda: root), "right")
        _l_(46156)
    aux = _a_(46159, _n_(46158, "root", lambda: root), "val")
    _l_(46160)
    return aux
root = _c_(46163, _n_(46162, "TreeNode", lambda: TreeNode), 8)
_l_(46164)
_n_(46165, "root", lambda: root).left = _c_(46167, _n_(46166, "TreeNode", lambda: TreeNode), 5)
_l_(46168)
_n_(46169, "root", lambda: root).right = _c_(46171, _n_(46170, "TreeNode", lambda: TreeNode), 14)
_l_(46172)
_a_(46174, _n_(46173, "root", lambda: root), "left").left = _c_(46176, _n_(46175, "TreeNode", lambda: TreeNode), 4)
_l_(46177)
_a_(46179, _n_(46178, "root", lambda: root), "left").right = _c_(46181, _n_(46180, "TreeNode", lambda: TreeNode), 6)
_l_(46182)
_a_(46185, _a_(46184, _n_(46183, "root", lambda: root), "left"), "right").left = _c_(46187, _n_(46186, "TreeNode", lambda: TreeNode), 8)
_l_(46188)
_a_(46191, _a_(46190, _n_(46189, "root", lambda: root), "left"), "right").right = _c_(46193, _n_(46192, "TreeNode", lambda: TreeNode), 7)
_l_(46194)
_a_(46196, _n_(46195, "root", lambda: root), "right").right = _c_(46198, _n_(46197, "TreeNode", lambda: TreeNode), 24)
_l_(46199)
_a_(46202, _a_(46201, _n_(46200, "root", lambda: root), "right"), "right").left = _c_(46204, _n_(46203, "TreeNode", lambda: TreeNode), 22)
_l_(46205)
_c_(46210, _n_(46206, "print", lambda: print), _c_(46209, _n_(46207, "kth_smallest", lambda: kth_smallest), _n_(46208, "root", lambda: root), 2))
_l_(46211)
_c_(46216, _n_(46212, "print", lambda: print), _c_(46215, _n_(46213, "kth_smallest", lambda: kth_smallest), _n_(46214, "root", lambda: root), 3))
_l_(46217)