# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(46580, "object", lambda: object)):
    _l_(46589)


    def __init__(self, x):
        _l_(46588)

        _n_(46581, "self", lambda: self).val = _n_(46582, "x", lambda: x)
        _l_(46583)
        _n_(46584, "self", lambda: self).left = None
        _l_(46585)
        _n_(46586, "self", lambda: self).right = None
        _l_(46587)

def kth_smallest(root, k):
    _l_(46615)

    stack = []
    _l_(46590)
    while _n_(46591, "root", lambda: root) or _n_(46592, "stack", lambda: stack):
        _l_(46611)

        while _n_(46593, "root", lambda: root):
            _l_(46602)

            _c_(46597, _a_(46595, _n_(46594, "stack", lambda: stack), "append"), _n_(46596, "root", lambda: root))
            _l_(46598)
            root = _a_(46600, _n_(46599, "root", lambda: root), "left")
            _l_(46601)
        root = _c_(46605, _a_(46604, _n_(46603, "stack", lambda: stack), "pop"))
        _l_(46606)
        k -= 1
        _l_(46607)
        if _n_(46608, "k", lambda: k) == 0:
            _l_(46610)

            break
            _l_(46609)
    aux = _a_(46613, _n_(46612, "root", lambda: root), "val")
    _l_(46614)
    return aux
root = _c_(46617, _n_(46616, "TreeNode", lambda: TreeNode), 8)
_l_(46618)
_n_(46619, "root", lambda: root).left = _c_(46621, _n_(46620, "TreeNode", lambda: TreeNode), 5)
_l_(46622)
_n_(46623, "root", lambda: root).right = _c_(46625, _n_(46624, "TreeNode", lambda: TreeNode), 14)
_l_(46626)
_a_(46628, _n_(46627, "root", lambda: root), "left").left = _c_(46630, _n_(46629, "TreeNode", lambda: TreeNode), 4)
_l_(46631)
_a_(46633, _n_(46632, "root", lambda: root), "left").right = _c_(46635, _n_(46634, "TreeNode", lambda: TreeNode), 6)
_l_(46636)
_a_(46639, _a_(46638, _n_(46637, "root", lambda: root), "left"), "right").left = _c_(46641, _n_(46640, "TreeNode", lambda: TreeNode), 8)
_l_(46642)
_a_(46645, _a_(46644, _n_(46643, "root", lambda: root), "left"), "right").right = _c_(46647, _n_(46646, "TreeNode", lambda: TreeNode), 7)
_l_(46648)
_a_(46650, _n_(46649, "root", lambda: root), "right").right = _c_(46652, _n_(46651, "TreeNode", lambda: TreeNode), 24)
_l_(46653)
_a_(46656, _a_(46655, _n_(46654, "root", lambda: root), "right"), "right").left = _c_(46658, _n_(46657, "TreeNode", lambda: TreeNode), 22)
_l_(46659)
_c_(46664, _n_(46660, "print", lambda: print), _c_(46663, _n_(46661, "kth_smallest", lambda: kth_smallest), _n_(46662, "root", lambda: root), 2))
_l_(46665)
_c_(46670, _n_(46666, "print", lambda: print), _c_(46669, _n_(46667, "kth_smallest", lambda: kth_smallest), _n_(46668, "root", lambda: root), 3))
_l_(46671)