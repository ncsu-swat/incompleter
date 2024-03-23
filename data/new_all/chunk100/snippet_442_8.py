# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(47410, "object", lambda: object)):
    _l_(47419)


    def __init__(self, x):
        _l_(47418)

        _n_(47411, "self", lambda: self).val = _n_(47412, "x", lambda: x)
        _l_(47413)
        _n_(47414, "self", lambda: self).left = None
        _l_(47415)
        _n_(47416, "self", lambda: self).right = None
        _l_(47417)

def kth_smallest(root, k):
    _l_(47448)

    stack = []
    _l_(47420)
    while _n_(47421, "root", lambda: root) or _n_(47422, "stack", lambda: stack):
        _l_(47444)

        while _n_(47423, "root", lambda: root):
            _l_(47432)

            _c_(47427, _a_(47425, _n_(47424, "stack", lambda: stack), "append"), _n_(47426, "root", lambda: root))
            _l_(47428)
            root = _a_(47430, _n_(47429, "root", lambda: root), "left")
            _l_(47431)
        root = _c_(47435, _a_(47434, _n_(47433, "stack", lambda: stack), "pop"))
        _l_(47436)
        k -= 1
        _l_(47437)
        if _n_(47438, "k", lambda: k) == 0:
            _l_(47440)

            break
            _l_(47439)
        root = _a_(47442, _n_(47441, "root", lambda: root), "right")
        _l_(47443)
    aux = _a_(47446, _n_(47445, "root", lambda: root), "val")
    _l_(47447)
    return aux
root = _c_(47450, _n_(47449, "TreeNode", lambda: TreeNode), 8)
_l_(47451)
_n_(47452, "root", lambda: root).left = _c_(47454, _n_(47453, "TreeNode", lambda: TreeNode), 5)
_l_(47455)
_n_(47456, "root", lambda: root).right = _c_(47458, _n_(47457, "TreeNode", lambda: TreeNode), 14)
_l_(47459)
_a_(47461, _n_(47460, "root", lambda: root), "left").left = _c_(47463, _n_(47462, "TreeNode", lambda: TreeNode), 4)
_l_(47464)
_a_(47466, _n_(47465, "root", lambda: root), "left").right = _c_(47468, _n_(47467, "TreeNode", lambda: TreeNode), 6)
_l_(47469)
_a_(47472, _a_(47471, _n_(47470, "root", lambda: root), "left"), "right").left = _c_(47474, _n_(47473, "TreeNode", lambda: TreeNode), 8)
_l_(47475)
_a_(47478, _a_(47477, _n_(47476, "root", lambda: root), "left"), "right").right = _c_(47480, _n_(47479, "TreeNode", lambda: TreeNode), 7)
_l_(47481)
_a_(47484, _a_(47483, _n_(47482, "root", lambda: root), "right"), "right").left = _c_(47486, _n_(47485, "TreeNode", lambda: TreeNode), 22)
_l_(47487)
_c_(47492, _n_(47488, "print", lambda: print), _c_(47491, _n_(47489, "kth_smallest", lambda: kth_smallest), _n_(47490, "root", lambda: root), 2))
_l_(47493)
_c_(47498, _n_(47494, "print", lambda: print), _c_(47497, _n_(47495, "kth_smallest", lambda: kth_smallest), _n_(47496, "root", lambda: root), 3))
_l_(47499)