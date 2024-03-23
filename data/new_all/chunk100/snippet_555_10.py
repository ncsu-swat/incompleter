# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(56210, "object", lambda: object)):
    _l_(56219)


    def __init__(self, x):
        _l_(56218)

        _n_(56211, "self", lambda: self).val = _n_(56212, "x", lambda: x)
        _l_(56213)
        _n_(56214, "self", lambda: self).left = None
        _l_(56215)
        _n_(56216, "self", lambda: self).right = None
        _l_(56217)

def delete_Node(root, key):
    _l_(56283)

    if not _n_(56220, "root", lambda: root):
        _l_(56223)

        aux = _n_(56221, "root", lambda: root)
        _l_(56222)
        return aux
    if _a_(56225, _n_(56224, "root", lambda: root), "val") > _n_(56226, "key", lambda: key):
        _l_(56280)

        _n_(56227, "root", lambda: root).left = _c_(56232, _n_(56228, "delete_Node", lambda: delete_Node), _a_(56230, _n_(56229, "root", lambda: root), "left"), _n_(56231, "key", lambda: key))
        _l_(56233)
    elif _a_(56235, _n_(56234, "root", lambda: root), "val") < _n_(56236, "key", lambda: key):
        _l_(56279)

        _n_(56237, "root", lambda: root).right = _c_(56242, _n_(56238, "delete_Node", lambda: delete_Node), _a_(56240, _n_(56239, "root", lambda: root), "right"), _n_(56241, "key", lambda: key))
        _l_(56243)
    else:
        if not _a_(56245, _n_(56244, "root", lambda: root), "right"):
            _l_(56249)

            aux = _a_(56247, _n_(56246, "root", lambda: root), "left")
            _l_(56248)
            return aux
        if not _a_(56251, _n_(56250, "root", lambda: root), "left"):
            _l_(56255)

            aux = _a_(56253, _n_(56252, "root", lambda: root), "right")
            _l_(56254)
            return aux
        temp_val = _a_(56257, _n_(56256, "root", lambda: root), "right")
        _l_(56258)
        mini_val = _a_(56260, _n_(56259, "temp_val", lambda: temp_val), "val")
        _l_(56261)
        while _a_(56263, _n_(56262, "temp_val", lambda: temp_val), "left"):
            _l_(56270)

            temp_val = _a_(56265, _n_(56264, "temp_val", lambda: temp_val), "left")
            _l_(56266)
            mini_val = _a_(56268, _n_(56267, "temp_val", lambda: temp_val), "val")
            _l_(56269)
        _n_(56271, "root", lambda: root).right = _c_(56277, _n_(56272, "deleteNode", lambda: deleteNode), _a_(56274, _n_(56273, "root", lambda: root), "right"), _a_(56276, _n_(56275, "root", lambda: root), "val"))
        _l_(56278)
    aux = _n_(56281, "root", lambda: root)
    _l_(56282)
    return aux

def preOrder(node):
    _l_(56302)

    if not _n_(56284, "node", lambda: node):
        _l_(56286)

        aux = ""
        _l_(56285)
        return aux
    _c_(56290, _n_(56287, "print", lambda: print), _a_(56289, _n_(56288, "node", lambda: node), "val"))
    _l_(56291)
    _c_(56295, _n_(56292, "preOrder", lambda: preOrder), _a_(56294, _n_(56293, "node", lambda: node), "left"))
    _l_(56296)
    _c_(56300, _n_(56297, "preOrder", lambda: preOrder), _a_(56299, _n_(56298, "node", lambda: node), "right"))
    _l_(56301)
root = _c_(56304, _n_(56303, "TreeNode", lambda: TreeNode), 5)
_l_(56305)
_n_(56306, "root", lambda: root).left = _c_(56308, _n_(56307, "TreeNode", lambda: TreeNode), 3)
_l_(56309)
_a_(56311, _n_(56310, "root", lambda: root), "left").left = _c_(56313, _n_(56312, "TreeNode", lambda: TreeNode), 2)
_l_(56314)
_a_(56316, _n_(56315, "root", lambda: root), "left").right = _c_(56318, _n_(56317, "TreeNode", lambda: TreeNode), 4)
_l_(56319)
_a_(56322, _a_(56321, _n_(56320, "root", lambda: root), "left"), "right").left = _c_(56324, _n_(56323, "TreeNode", lambda: TreeNode), 7)
_l_(56325)
_c_(56327, _n_(56326, "print", lambda: print), 'Original node:')
_l_(56328)
_c_(56333, _n_(56329, "print", lambda: print), _c_(56332, _n_(56330, "preOrder", lambda: preOrder), _n_(56331, "root", lambda: root)))
_l_(56334)
result = _c_(56337, _n_(56335, "delete_Node", lambda: delete_Node), _n_(56336, "root", lambda: root), 4)
_l_(56338)
_c_(56340, _n_(56339, "print", lambda: print), 'After deleting specified node:')
_l_(56341)
_c_(56346, _n_(56342, "print", lambda: print), _c_(56345, _n_(56343, "preOrder", lambda: preOrder), _n_(56344, "result", lambda: result)))
_l_(56347)