# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(46949, "object", lambda: object)):
    _l_(46958)


    def __init__(self, x):
        _l_(46957)

        _n_(46950, "self", lambda: self).val = _n_(46951, "x", lambda: x)
        _l_(46952)
        _n_(46953, "self", lambda: self).left = None
        _l_(46954)
        _n_(46955, "self", lambda: self).right = None
        _l_(46956)

def kth_smallest(root, k):
    _l_(46986)

    while _n_(46959, "root", lambda: root) or _n_(46960, "stack", lambda: stack):
        _l_(46982)

        while _n_(46961, "root", lambda: root):
            _l_(46970)

            _c_(46965, _a_(46963, _n_(46962, "stack", lambda: stack), "append"), _n_(46964, "root", lambda: root))
            _l_(46966)
            root = _a_(46968, _n_(46967, "root", lambda: root), "left")
            _l_(46969)
        root = _c_(46973, _a_(46972, _n_(46971, "stack", lambda: stack), "pop"))
        _l_(46974)
        k -= 1
        _l_(46975)
        if _n_(46976, "k", lambda: k) == 0:
            _l_(46978)

            break
            _l_(46977)
        root = _a_(46980, _n_(46979, "root", lambda: root), "right")
        _l_(46981)
    aux = _a_(46984, _n_(46983, "root", lambda: root), "val")
    _l_(46985)
    return aux
root = _c_(46988, _n_(46987, "TreeNode", lambda: TreeNode), 8)
_l_(46989)
_n_(46990, "root", lambda: root).left = _c_(46992, _n_(46991, "TreeNode", lambda: TreeNode), 5)
_l_(46993)
_n_(46994, "root", lambda: root).right = _c_(46996, _n_(46995, "TreeNode", lambda: TreeNode), 14)
_l_(46997)
_a_(46999, _n_(46998, "root", lambda: root), "left").left = _c_(47001, _n_(47000, "TreeNode", lambda: TreeNode), 4)
_l_(47002)
_a_(47004, _n_(47003, "root", lambda: root), "left").right = _c_(47006, _n_(47005, "TreeNode", lambda: TreeNode), 6)
_l_(47007)
_a_(47010, _a_(47009, _n_(47008, "root", lambda: root), "left"), "right").left = _c_(47012, _n_(47011, "TreeNode", lambda: TreeNode), 8)
_l_(47013)
_a_(47016, _a_(47015, _n_(47014, "root", lambda: root), "left"), "right").right = _c_(47018, _n_(47017, "TreeNode", lambda: TreeNode), 7)
_l_(47019)
_a_(47021, _n_(47020, "root", lambda: root), "right").right = _c_(47023, _n_(47022, "TreeNode", lambda: TreeNode), 24)
_l_(47024)
_a_(47027, _a_(47026, _n_(47025, "root", lambda: root), "right"), "right").left = _c_(47029, _n_(47028, "TreeNode", lambda: TreeNode), 22)
_l_(47030)
_c_(47035, _n_(47031, "print", lambda: print), _c_(47034, _n_(47032, "kth_smallest", lambda: kth_smallest), _n_(47033, "root", lambda: root), 2))
_l_(47036)
_c_(47041, _n_(47037, "print", lambda: print), _c_(47040, _n_(47038, "kth_smallest", lambda: kth_smallest), _n_(47039, "root", lambda: root), 3))
_l_(47042)