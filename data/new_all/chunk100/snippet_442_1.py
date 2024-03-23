# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(46038, "object", lambda: object)):
    _l_(46047)


    def __init__(self, x):
        _l_(46046)

        _n_(46039, "self", lambda: self).val = _n_(46040, "x", lambda: x)
        _l_(46041)
        _n_(46042, "self", lambda: self).left = None
        _l_(46043)
        _n_(46044, "self", lambda: self).right = None
        _l_(46045)

def kth_smallest(root, k):
    _l_(46076)

    stack = []
    _l_(46048)
    while _n_(46049, "root", lambda: root) or _n_(46050, "stack", lambda: stack):
        _l_(46072)

        while _n_(46051, "root", lambda: root):
            _l_(46060)

            _c_(46055, _a_(46053, _n_(46052, "stack", lambda: stack), "append"), _n_(46054, "root", lambda: root))
            _l_(46056)
            root = _a_(46058, _n_(46057, "root", lambda: root), "left")
            _l_(46059)
        root = _c_(46063, _a_(46062, _n_(46061, "stack", lambda: stack), "pop"))
        _l_(46064)
        k -= 1
        _l_(46065)
        if _n_(46066, "k", lambda: k) == 0:
            _l_(46068)

            break
            _l_(46067)
        root = _a_(46070, _n_(46069, "root", lambda: root), "right")
        _l_(46071)
    aux = _a_(46074, _n_(46073, "root", lambda: root), "val")
    _l_(46075)
    return aux
root = _c_(46078, _n_(46077, "TreeNode", lambda: TreeNode), 8)
_l_(46079)
_n_(46080, "root", lambda: root).left = _c_(46082, _n_(46081, "TreeNode", lambda: TreeNode), 5)
_l_(46083)
_n_(46084, "root", lambda: root).right = _c_(46086, _n_(46085, "TreeNode", lambda: TreeNode), 14)
_l_(46087)
_a_(46089, _n_(46088, "root", lambda: root), "left").left = _c_(46091, _n_(46090, "TreeNode", lambda: TreeNode), 4)
_l_(46092)
_a_(46094, _n_(46093, "root", lambda: root), "left").right = _c_(46096, _n_(46095, "TreeNode", lambda: TreeNode), 6)
_l_(46097)
_a_(46100, _a_(46099, _n_(46098, "root", lambda: root), "left"), "right").left = _c_(46102, _n_(46101, "TreeNode", lambda: TreeNode), 8)
_l_(46103)
_a_(46105, _n_(46104, "root", lambda: root), "right").right = _c_(46107, _n_(46106, "TreeNode", lambda: TreeNode), 24)
_l_(46108)
_a_(46111, _a_(46110, _n_(46109, "root", lambda: root), "right"), "right").left = _c_(46113, _n_(46112, "TreeNode", lambda: TreeNode), 22)
_l_(46114)
_c_(46119, _n_(46115, "print", lambda: print), _c_(46118, _n_(46116, "kth_smallest", lambda: kth_smallest), _n_(46117, "root", lambda: root), 2))
_l_(46120)
_c_(46125, _n_(46121, "print", lambda: print), _c_(46124, _n_(46122, "kth_smallest", lambda: kth_smallest), _n_(46123, "root", lambda: root), 3))
_l_(46126)