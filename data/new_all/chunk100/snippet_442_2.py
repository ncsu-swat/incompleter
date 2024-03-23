# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(46857, "object", lambda: object)):
    _l_(46866)


    def __init__(self, x):
        _l_(46865)

        _n_(46858, "self", lambda: self).val = _n_(46859, "x", lambda: x)
        _l_(46860)
        _n_(46861, "self", lambda: self).left = None
        _l_(46862)
        _n_(46863, "self", lambda: self).right = None
        _l_(46864)

def kth_smallest(root, k):
    _l_(46892)

    stack = []
    _l_(46867)
    while _n_(46868, "root", lambda: root) or _n_(46869, "stack", lambda: stack):
        _l_(46888)

        while _n_(46870, "root", lambda: root):
            _l_(46876)

            _c_(46874, _a_(46872, _n_(46871, "stack", lambda: stack), "append"), _n_(46873, "root", lambda: root))
            _l_(46875)
        root = _c_(46879, _a_(46878, _n_(46877, "stack", lambda: stack), "pop"))
        _l_(46880)
        k -= 1
        _l_(46881)
        if _n_(46882, "k", lambda: k) == 0:
            _l_(46884)

            break
            _l_(46883)
        root = _a_(46886, _n_(46885, "root", lambda: root), "right")
        _l_(46887)
    aux = _a_(46890, _n_(46889, "root", lambda: root), "val")
    _l_(46891)
    return aux
root = _c_(46894, _n_(46893, "TreeNode", lambda: TreeNode), 8)
_l_(46895)
_n_(46896, "root", lambda: root).left = _c_(46898, _n_(46897, "TreeNode", lambda: TreeNode), 5)
_l_(46899)
_n_(46900, "root", lambda: root).right = _c_(46902, _n_(46901, "TreeNode", lambda: TreeNode), 14)
_l_(46903)
_a_(46905, _n_(46904, "root", lambda: root), "left").left = _c_(46907, _n_(46906, "TreeNode", lambda: TreeNode), 4)
_l_(46908)
_a_(46910, _n_(46909, "root", lambda: root), "left").right = _c_(46912, _n_(46911, "TreeNode", lambda: TreeNode), 6)
_l_(46913)
_a_(46916, _a_(46915, _n_(46914, "root", lambda: root), "left"), "right").left = _c_(46918, _n_(46917, "TreeNode", lambda: TreeNode), 8)
_l_(46919)
_a_(46922, _a_(46921, _n_(46920, "root", lambda: root), "left"), "right").right = _c_(46924, _n_(46923, "TreeNode", lambda: TreeNode), 7)
_l_(46925)
_a_(46927, _n_(46926, "root", lambda: root), "right").right = _c_(46929, _n_(46928, "TreeNode", lambda: TreeNode), 24)
_l_(46930)
_a_(46933, _a_(46932, _n_(46931, "root", lambda: root), "right"), "right").left = _c_(46935, _n_(46934, "TreeNode", lambda: TreeNode), 22)
_l_(46936)
_c_(46941, _n_(46937, "print", lambda: print), _c_(46940, _n_(46938, "kth_smallest", lambda: kth_smallest), _n_(46939, "root", lambda: root), 2))
_l_(46942)
_c_(46947, _n_(46943, "print", lambda: print), _c_(46946, _n_(46944, "kth_smallest", lambda: kth_smallest), _n_(46945, "root", lambda: root), 3))
_l_(46948)