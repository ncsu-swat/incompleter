# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(56900, "object", lambda: object)):
    _l_(56909)


    def __init__(self, x):
        _l_(56908)

        _n_(56901, "self", lambda: self).val = _n_(56902, "x", lambda: x)
        _l_(56903)
        _n_(56904, "self", lambda: self).left = None
        _l_(56905)
        _n_(56906, "self", lambda: self).right = None
        _l_(56907)

def delete_Node(root, key):
    _l_(56973)

    if not _n_(56910, "root", lambda: root):
        _l_(56913)

        aux = _n_(56911, "root", lambda: root)
        _l_(56912)
        return aux
    if _a_(56915, _n_(56914, "root", lambda: root), "val") > _n_(56916, "key", lambda: key):
        _l_(56970)

        _n_(56917, "root", lambda: root).left = _c_(56922, _n_(56918, "delete_Node", lambda: delete_Node), _a_(56920, _n_(56919, "root", lambda: root), "left"), _n_(56921, "key", lambda: key))
        _l_(56923)
    elif _a_(56925, _n_(56924, "root", lambda: root), "val") < _n_(56926, "key", lambda: key):
        _l_(56969)

        _n_(56927, "root", lambda: root).right = _c_(56932, _n_(56928, "delete_Node", lambda: delete_Node), _a_(56930, _n_(56929, "root", lambda: root), "right"), _n_(56931, "key", lambda: key))
        _l_(56933)
    else:
        if not _a_(56935, _n_(56934, "root", lambda: root), "right"):
            _l_(56939)

            aux = _a_(56937, _n_(56936, "root", lambda: root), "left")
            _l_(56938)
            return aux
        if not _a_(56941, _n_(56940, "root", lambda: root), "left"):
            _l_(56945)

            aux = _a_(56943, _n_(56942, "root", lambda: root), "right")
            _l_(56944)
            return aux
        temp_val = _a_(56947, _n_(56946, "root", lambda: root), "right")
        _l_(56948)
        mini_val = _a_(56950, _n_(56949, "temp_val", lambda: temp_val), "val")
        _l_(56951)
        while _a_(56953, _n_(56952, "temp_val", lambda: temp_val), "left"):
            _l_(56960)

            temp_val = _a_(56955, _n_(56954, "temp_val", lambda: temp_val), "left")
            _l_(56956)
            mini_val = _a_(56958, _n_(56957, "temp_val", lambda: temp_val), "val")
            _l_(56959)
        _n_(56961, "root", lambda: root).right = _c_(56967, _n_(56962, "deleteNode", lambda: deleteNode), _a_(56964, _n_(56963, "root", lambda: root), "right"), _a_(56966, _n_(56965, "root", lambda: root), "val"))
        _l_(56968)
    aux = _n_(56971, "root", lambda: root)
    _l_(56972)
    return aux

def preOrder(node):
    _l_(56992)

    if not _n_(56974, "node", lambda: node):
        _l_(56976)

        aux = ""
        _l_(56975)
        return aux
    _c_(56980, _n_(56977, "print", lambda: print), _a_(56979, _n_(56978, "node", lambda: node), "val"))
    _l_(56981)
    _c_(56985, _n_(56982, "preOrder", lambda: preOrder), _a_(56984, _n_(56983, "node", lambda: node), "left"))
    _l_(56986)
    _c_(56990, _n_(56987, "preOrder", lambda: preOrder), _a_(56989, _n_(56988, "node", lambda: node), "right"))
    _l_(56991)
root = _c_(56994, _n_(56993, "TreeNode", lambda: TreeNode), 5)
_l_(56995)
_n_(56996, "root", lambda: root).left = _c_(56998, _n_(56997, "TreeNode", lambda: TreeNode), 3)
_l_(56999)
_n_(57000, "root", lambda: root).right = _c_(57002, _n_(57001, "TreeNode", lambda: TreeNode), 6)
_l_(57003)
_a_(57005, _n_(57004, "root", lambda: root), "left").left = _c_(57007, _n_(57006, "TreeNode", lambda: TreeNode), 2)
_l_(57008)
_a_(57010, _n_(57009, "root", lambda: root), "left").right = _c_(57012, _n_(57011, "TreeNode", lambda: TreeNode), 4)
_l_(57013)
_a_(57016, _a_(57015, _n_(57014, "root", lambda: root), "left"), "right").left = _c_(57018, _n_(57017, "TreeNode", lambda: TreeNode), 7)
_l_(57019)
_c_(57021, _n_(57020, "print", lambda: print), 'Original node:')
_l_(57022)
_c_(57027, _n_(57023, "print", lambda: print), _c_(57026, _n_(57024, "preOrder", lambda: preOrder), _n_(57025, "root", lambda: root)))
_l_(57028)
_c_(57030, _n_(57029, "print", lambda: print), 'After deleting specified node:')
_l_(57031)
_c_(57036, _n_(57032, "print", lambda: print), _c_(57035, _n_(57033, "preOrder", lambda: preOrder), _n_(57034, "result", lambda: result)))
_l_(57037)