# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(55932, "object", lambda: object)):
    _l_(55938)


    def __init__(self, x):
        _l_(55937)

        _n_(55933, "self", lambda: self).left = None
        _l_(55934)
        _n_(55935, "self", lambda: self).right = None
        _l_(55936)

def delete_Node(root, key):
    _l_(56002)

    if not _n_(55939, "root", lambda: root):
        _l_(55942)

        aux = _n_(55940, "root", lambda: root)
        _l_(55941)
        return aux
    if _a_(55944, _n_(55943, "root", lambda: root), "val") > _n_(55945, "key", lambda: key):
        _l_(55999)

        _n_(55946, "root", lambda: root).left = _c_(55951, _n_(55947, "delete_Node", lambda: delete_Node), _a_(55949, _n_(55948, "root", lambda: root), "left"), _n_(55950, "key", lambda: key))
        _l_(55952)
    elif _a_(55954, _n_(55953, "root", lambda: root), "val") < _n_(55955, "key", lambda: key):
        _l_(55998)

        _n_(55956, "root", lambda: root).right = _c_(55961, _n_(55957, "delete_Node", lambda: delete_Node), _a_(55959, _n_(55958, "root", lambda: root), "right"), _n_(55960, "key", lambda: key))
        _l_(55962)
    else:
        if not _a_(55964, _n_(55963, "root", lambda: root), "right"):
            _l_(55968)

            aux = _a_(55966, _n_(55965, "root", lambda: root), "left")
            _l_(55967)
            return aux
        if not _a_(55970, _n_(55969, "root", lambda: root), "left"):
            _l_(55974)

            aux = _a_(55972, _n_(55971, "root", lambda: root), "right")
            _l_(55973)
            return aux
        temp_val = _a_(55976, _n_(55975, "root", lambda: root), "right")
        _l_(55977)
        mini_val = _a_(55979, _n_(55978, "temp_val", lambda: temp_val), "val")
        _l_(55980)
        while _a_(55982, _n_(55981, "temp_val", lambda: temp_val), "left"):
            _l_(55989)

            temp_val = _a_(55984, _n_(55983, "temp_val", lambda: temp_val), "left")
            _l_(55985)
            mini_val = _a_(55987, _n_(55986, "temp_val", lambda: temp_val), "val")
            _l_(55988)
        _n_(55990, "root", lambda: root).right = _c_(55996, _n_(55991, "deleteNode", lambda: deleteNode), _a_(55993, _n_(55992, "root", lambda: root), "right"), _a_(55995, _n_(55994, "root", lambda: root), "val"))
        _l_(55997)
    aux = _n_(56000, "root", lambda: root)
    _l_(56001)
    return aux

def preOrder(node):
    _l_(56021)

    if not _n_(56003, "node", lambda: node):
        _l_(56005)

        aux = ""
        _l_(56004)
        return aux
    _c_(56009, _n_(56006, "print", lambda: print), _a_(56008, _n_(56007, "node", lambda: node), "val"))
    _l_(56010)
    _c_(56014, _n_(56011, "preOrder", lambda: preOrder), _a_(56013, _n_(56012, "node", lambda: node), "left"))
    _l_(56015)
    _c_(56019, _n_(56016, "preOrder", lambda: preOrder), _a_(56018, _n_(56017, "node", lambda: node), "right"))
    _l_(56020)
root = _c_(56023, _n_(56022, "TreeNode", lambda: TreeNode), 5)
_l_(56024)
_n_(56025, "root", lambda: root).left = _c_(56027, _n_(56026, "TreeNode", lambda: TreeNode), 3)
_l_(56028)
_n_(56029, "root", lambda: root).right = _c_(56031, _n_(56030, "TreeNode", lambda: TreeNode), 6)
_l_(56032)
_a_(56034, _n_(56033, "root", lambda: root), "left").left = _c_(56036, _n_(56035, "TreeNode", lambda: TreeNode), 2)
_l_(56037)
_a_(56039, _n_(56038, "root", lambda: root), "left").right = _c_(56041, _n_(56040, "TreeNode", lambda: TreeNode), 4)
_l_(56042)
_a_(56045, _a_(56044, _n_(56043, "root", lambda: root), "left"), "right").left = _c_(56047, _n_(56046, "TreeNode", lambda: TreeNode), 7)
_l_(56048)
_c_(56050, _n_(56049, "print", lambda: print), 'Original node:')
_l_(56051)
_c_(56056, _n_(56052, "print", lambda: print), _c_(56055, _n_(56053, "preOrder", lambda: preOrder), _n_(56054, "root", lambda: root)))
_l_(56057)
result = _c_(56060, _n_(56058, "delete_Node", lambda: delete_Node), _n_(56059, "root", lambda: root), 4)
_l_(56061)
_c_(56063, _n_(56062, "print", lambda: print), 'After deleting specified node:')
_l_(56064)
_c_(56069, _n_(56065, "print", lambda: print), _c_(56068, _n_(56066, "preOrder", lambda: preOrder), _n_(56067, "result", lambda: result)))
_l_(56070)