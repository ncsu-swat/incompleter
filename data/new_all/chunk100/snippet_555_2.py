# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(56348, "object", lambda: object)):
    _l_(56357)


    def __init__(self, x):
        _l_(56356)

        _n_(56349, "self", lambda: self).val = _n_(56350, "x", lambda: x)
        _l_(56351)
        _n_(56352, "self", lambda: self).left = None
        _l_(56353)
        _n_(56354, "self", lambda: self).right = None
        _l_(56355)

def delete_Node(root, key):
    _l_(56421)

    if not _n_(56358, "root", lambda: root):
        _l_(56361)

        aux = _n_(56359, "root", lambda: root)
        _l_(56360)
        return aux
    if _a_(56363, _n_(56362, "root", lambda: root), "val") > _n_(56364, "key", lambda: key):
        _l_(56418)

        _n_(56365, "root", lambda: root).left = _c_(56370, _n_(56366, "delete_Node", lambda: delete_Node), _a_(56368, _n_(56367, "root", lambda: root), "left"), _n_(56369, "key", lambda: key))
        _l_(56371)
    elif _a_(56373, _n_(56372, "root", lambda: root), "val") < _n_(56374, "key", lambda: key):
        _l_(56417)

        _n_(56375, "root", lambda: root).right = _c_(56380, _n_(56376, "delete_Node", lambda: delete_Node), _a_(56378, _n_(56377, "root", lambda: root), "right"), _n_(56379, "key", lambda: key))
        _l_(56381)
    else:
        if not _a_(56383, _n_(56382, "root", lambda: root), "right"):
            _l_(56387)

            aux = _a_(56385, _n_(56384, "root", lambda: root), "left")
            _l_(56386)
            return aux
        if not _a_(56389, _n_(56388, "root", lambda: root), "left"):
            _l_(56393)

            aux = _a_(56391, _n_(56390, "root", lambda: root), "right")
            _l_(56392)
            return aux
        temp_val = _a_(56395, _n_(56394, "root", lambda: root), "right")
        _l_(56396)
        mini_val = _a_(56398, _n_(56397, "temp_val", lambda: temp_val), "val")
        _l_(56399)
        while _a_(56401, _n_(56400, "temp_val", lambda: temp_val), "left"):
            _l_(56408)

            temp_val = _a_(56403, _n_(56402, "temp_val", lambda: temp_val), "left")
            _l_(56404)
            mini_val = _a_(56406, _n_(56405, "temp_val", lambda: temp_val), "val")
            _l_(56407)
        _n_(56409, "root", lambda: root).right = _c_(56415, _n_(56410, "deleteNode", lambda: deleteNode), _a_(56412, _n_(56411, "root", lambda: root), "right"), _a_(56414, _n_(56413, "root", lambda: root), "val"))
        _l_(56416)
    aux = _n_(56419, "root", lambda: root)
    _l_(56420)
    return aux

def preOrder(node):
    _l_(56440)

    if not _n_(56422, "node", lambda: node):
        _l_(56424)

        aux = ""
        _l_(56423)
        return aux
    _c_(56428, _n_(56425, "print", lambda: print), _a_(56427, _n_(56426, "node", lambda: node), "val"))
    _l_(56429)
    _c_(56433, _n_(56430, "preOrder", lambda: preOrder), _a_(56432, _n_(56431, "node", lambda: node), "left"))
    _l_(56434)
    _c_(56438, _n_(56435, "preOrder", lambda: preOrder), _a_(56437, _n_(56436, "node", lambda: node), "right"))
    _l_(56439)
root = _c_(56442, _n_(56441, "TreeNode", lambda: TreeNode), 5)
_l_(56443)
_n_(56444, "root", lambda: root).left = _c_(56446, _n_(56445, "TreeNode", lambda: TreeNode), 3)
_l_(56447)
_n_(56448, "root", lambda: root).right = _c_(56450, _n_(56449, "TreeNode", lambda: TreeNode), 6)
_l_(56451)
_a_(56453, _n_(56452, "root", lambda: root), "left").right = _c_(56455, _n_(56454, "TreeNode", lambda: TreeNode), 4)
_l_(56456)
_a_(56459, _a_(56458, _n_(56457, "root", lambda: root), "left"), "right").left = _c_(56461, _n_(56460, "TreeNode", lambda: TreeNode), 7)
_l_(56462)
_c_(56464, _n_(56463, "print", lambda: print), 'Original node:')
_l_(56465)
_c_(56470, _n_(56466, "print", lambda: print), _c_(56469, _n_(56467, "preOrder", lambda: preOrder), _n_(56468, "root", lambda: root)))
_l_(56471)
result = _c_(56474, _n_(56472, "delete_Node", lambda: delete_Node), _n_(56473, "root", lambda: root), 4)
_l_(56475)
_c_(56477, _n_(56476, "print", lambda: print), 'After deleting specified node:')
_l_(56478)
_c_(56483, _n_(56479, "print", lambda: print), _c_(56482, _n_(56480, "preOrder", lambda: preOrder), _n_(56481, "result", lambda: result)))
_l_(56484)