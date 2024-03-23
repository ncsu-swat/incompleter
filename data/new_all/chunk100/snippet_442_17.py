# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(46764, "object", lambda: object)):
    _l_(46771)


    def __init__(self, x):
        _l_(46770)

        _n_(46765, "self", lambda: self).val = _n_(46766, "x", lambda: x)
        _l_(46767)
        _n_(46768, "self", lambda: self).left = None
        _l_(46769)

def kth_smallest(root, k):
    _l_(46800)

    stack = []
    _l_(46772)
    while _n_(46773, "root", lambda: root) or _n_(46774, "stack", lambda: stack):
        _l_(46796)

        while _n_(46775, "root", lambda: root):
            _l_(46784)

            _c_(46779, _a_(46777, _n_(46776, "stack", lambda: stack), "append"), _n_(46778, "root", lambda: root))
            _l_(46780)
            root = _a_(46782, _n_(46781, "root", lambda: root), "left")
            _l_(46783)
        root = _c_(46787, _a_(46786, _n_(46785, "stack", lambda: stack), "pop"))
        _l_(46788)
        k -= 1
        _l_(46789)
        if _n_(46790, "k", lambda: k) == 0:
            _l_(46792)

            break
            _l_(46791)
        root = _a_(46794, _n_(46793, "root", lambda: root), "right")
        _l_(46795)
    aux = _a_(46798, _n_(46797, "root", lambda: root), "val")
    _l_(46799)
    return aux
root = _c_(46802, _n_(46801, "TreeNode", lambda: TreeNode), 8)
_l_(46803)
_n_(46804, "root", lambda: root).left = _c_(46806, _n_(46805, "TreeNode", lambda: TreeNode), 5)
_l_(46807)
_n_(46808, "root", lambda: root).right = _c_(46810, _n_(46809, "TreeNode", lambda: TreeNode), 14)
_l_(46811)
_a_(46813, _n_(46812, "root", lambda: root), "left").left = _c_(46815, _n_(46814, "TreeNode", lambda: TreeNode), 4)
_l_(46816)
_a_(46818, _n_(46817, "root", lambda: root), "left").right = _c_(46820, _n_(46819, "TreeNode", lambda: TreeNode), 6)
_l_(46821)
_a_(46824, _a_(46823, _n_(46822, "root", lambda: root), "left"), "right").left = _c_(46826, _n_(46825, "TreeNode", lambda: TreeNode), 8)
_l_(46827)
_a_(46830, _a_(46829, _n_(46828, "root", lambda: root), "left"), "right").right = _c_(46832, _n_(46831, "TreeNode", lambda: TreeNode), 7)
_l_(46833)
_a_(46835, _n_(46834, "root", lambda: root), "right").right = _c_(46837, _n_(46836, "TreeNode", lambda: TreeNode), 24)
_l_(46838)
_a_(46841, _a_(46840, _n_(46839, "root", lambda: root), "right"), "right").left = _c_(46843, _n_(46842, "TreeNode", lambda: TreeNode), 22)
_l_(46844)
_c_(46849, _n_(46845, "print", lambda: print), _c_(46848, _n_(46846, "kth_smallest", lambda: kth_smallest), _n_(46847, "root", lambda: root), 2))
_l_(46850)
_c_(46855, _n_(46851, "print", lambda: print), _c_(46854, _n_(46852, "kth_smallest", lambda: kth_smallest), _n_(46853, "root", lambda: root), 3))
_l_(46856)