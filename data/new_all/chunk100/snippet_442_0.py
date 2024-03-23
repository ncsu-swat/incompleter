# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(45947, "object", lambda: object)):
    _l_(45956)


    def __init__(self, x):
        _l_(45955)

        _n_(45948, "self", lambda: self).val = _n_(45949, "x", lambda: x)
        _l_(45950)
        _n_(45951, "self", lambda: self).left = None
        _l_(45952)
        _n_(45953, "self", lambda: self).right = None
        _l_(45954)

def kth_smallest(root, k):
    _l_(45985)

    stack = []
    _l_(45957)
    while _n_(45958, "root", lambda: root) or _n_(45959, "stack", lambda: stack):
        _l_(45981)

        while _n_(45960, "root", lambda: root):
            _l_(45969)

            _c_(45964, _a_(45962, _n_(45961, "stack", lambda: stack), "append"), _n_(45963, "root", lambda: root))
            _l_(45965)
            root = _a_(45967, _n_(45966, "root", lambda: root), "left")
            _l_(45968)
        root = _c_(45972, _a_(45971, _n_(45970, "stack", lambda: stack), "pop"))
        _l_(45973)
        k -= 1
        _l_(45974)
        if _n_(45975, "k", lambda: k) == 0:
            _l_(45977)

            break
            _l_(45976)
        root = _a_(45979, _n_(45978, "root", lambda: root), "right")
        _l_(45980)
    aux = _a_(45983, _n_(45982, "root", lambda: root), "val")
    _l_(45984)
    return aux
root = _c_(45987, _n_(45986, "TreeNode", lambda: TreeNode), 8)
_l_(45988)
_n_(45989, "root", lambda: root).left = _c_(45991, _n_(45990, "TreeNode", lambda: TreeNode), 5)
_l_(45992)
_a_(45994, _n_(45993, "root", lambda: root), "left").left = _c_(45996, _n_(45995, "TreeNode", lambda: TreeNode), 4)
_l_(45997)
_a_(45999, _n_(45998, "root", lambda: root), "left").right = _c_(46001, _n_(46000, "TreeNode", lambda: TreeNode), 6)
_l_(46002)
_a_(46005, _a_(46004, _n_(46003, "root", lambda: root), "left"), "right").left = _c_(46007, _n_(46006, "TreeNode", lambda: TreeNode), 8)
_l_(46008)
_a_(46011, _a_(46010, _n_(46009, "root", lambda: root), "left"), "right").right = _c_(46013, _n_(46012, "TreeNode", lambda: TreeNode), 7)
_l_(46014)
_a_(46016, _n_(46015, "root", lambda: root), "right").right = _c_(46018, _n_(46017, "TreeNode", lambda: TreeNode), 24)
_l_(46019)
_a_(46022, _a_(46021, _n_(46020, "root", lambda: root), "right"), "right").left = _c_(46024, _n_(46023, "TreeNode", lambda: TreeNode), 22)
_l_(46025)
_c_(46030, _n_(46026, "print", lambda: print), _c_(46029, _n_(46027, "kth_smallest", lambda: kth_smallest), _n_(46028, "root", lambda: root), 2))
_l_(46031)
_c_(46036, _n_(46032, "print", lambda: print), _c_(46035, _n_(46033, "kth_smallest", lambda: kth_smallest), _n_(46034, "root", lambda: root), 3))
_l_(46037)