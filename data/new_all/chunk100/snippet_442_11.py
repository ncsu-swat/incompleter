# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(46218, "object", lambda: object)):
    _l_(46227)


    def __init__(self, x):
        _l_(46226)

        _n_(46219, "self", lambda: self).val = _n_(46220, "x", lambda: x)
        _l_(46221)
        _n_(46222, "self", lambda: self).left = None
        _l_(46223)
        _n_(46224, "self", lambda: self).right = None
        _l_(46225)

def kth_smallest(root, k):
    _l_(46253)

    stack = []
    _l_(46228)
    while _n_(46229, "root", lambda: root) or _n_(46230, "stack", lambda: stack):
        _l_(46249)

        while _n_(46231, "root", lambda: root):
            _l_(46240)

            _c_(46235, _a_(46233, _n_(46232, "stack", lambda: stack), "append"), _n_(46234, "root", lambda: root))
            _l_(46236)
            root = _a_(46238, _n_(46237, "root", lambda: root), "left")
            _l_(46239)
        root = _c_(46243, _a_(46242, _n_(46241, "stack", lambda: stack), "pop"))
        _l_(46244)
        k -= 1
        _l_(46245)
        if _n_(46246, "k", lambda: k) == 0:
            _l_(46248)

            break
            _l_(46247)
    aux = _a_(46251, _n_(46250, "root", lambda: root), "val")
    _l_(46252)
    return aux
root = _c_(46255, _n_(46254, "TreeNode", lambda: TreeNode), 8)
_l_(46256)
_n_(46257, "root", lambda: root).left = _c_(46259, _n_(46258, "TreeNode", lambda: TreeNode), 5)
_l_(46260)
_n_(46261, "root", lambda: root).right = _c_(46263, _n_(46262, "TreeNode", lambda: TreeNode), 14)
_l_(46264)
_a_(46266, _n_(46265, "root", lambda: root), "left").left = _c_(46268, _n_(46267, "TreeNode", lambda: TreeNode), 4)
_l_(46269)
_a_(46271, _n_(46270, "root", lambda: root), "left").right = _c_(46273, _n_(46272, "TreeNode", lambda: TreeNode), 6)
_l_(46274)
_a_(46277, _a_(46276, _n_(46275, "root", lambda: root), "left"), "right").left = _c_(46279, _n_(46278, "TreeNode", lambda: TreeNode), 8)
_l_(46280)
_a_(46283, _a_(46282, _n_(46281, "root", lambda: root), "left"), "right").right = _c_(46285, _n_(46284, "TreeNode", lambda: TreeNode), 7)
_l_(46286)
_a_(46288, _n_(46287, "root", lambda: root), "right").right = _c_(46290, _n_(46289, "TreeNode", lambda: TreeNode), 24)
_l_(46291)
_a_(46294, _a_(46293, _n_(46292, "root", lambda: root), "right"), "right").left = _c_(46296, _n_(46295, "TreeNode", lambda: TreeNode), 22)
_l_(46297)
_c_(46302, _n_(46298, "print", lambda: print), _c_(46301, _n_(46299, "kth_smallest", lambda: kth_smallest), _n_(46300, "root", lambda: root), 2))
_l_(46303)
_c_(46308, _n_(46304, "print", lambda: print), _c_(46307, _n_(46305, "kth_smallest", lambda: kth_smallest), _n_(46306, "root", lambda: root), 3))
_l_(46309)