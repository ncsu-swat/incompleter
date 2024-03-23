# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TreeNode(_n_(56485, "object", lambda: object)):
    _l_(56494)


    def __init__(self, x):
        _l_(56493)

        _n_(56486, "self", lambda: self).val = _n_(56487, "x", lambda: x)
        _l_(56488)
        _n_(56489, "self", lambda: self).left = None
        _l_(56490)
        _n_(56491, "self", lambda: self).right = None
        _l_(56492)

def delete_Node(root, key):
    _l_(56558)

    if not _n_(56495, "root", lambda: root):
        _l_(56498)

        aux = _n_(56496, "root", lambda: root)
        _l_(56497)
        return aux
    if _a_(56500, _n_(56499, "root", lambda: root), "val") > _n_(56501, "key", lambda: key):
        _l_(56555)

        _n_(56502, "root", lambda: root).left = _c_(56507, _n_(56503, "delete_Node", lambda: delete_Node), _a_(56505, _n_(56504, "root", lambda: root), "left"), _n_(56506, "key", lambda: key))
        _l_(56508)
    elif _a_(56510, _n_(56509, "root", lambda: root), "val") < _n_(56511, "key", lambda: key):
        _l_(56554)

        _n_(56512, "root", lambda: root).right = _c_(56517, _n_(56513, "delete_Node", lambda: delete_Node), _a_(56515, _n_(56514, "root", lambda: root), "right"), _n_(56516, "key", lambda: key))
        _l_(56518)
    else:
        if not _a_(56520, _n_(56519, "root", lambda: root), "right"):
            _l_(56524)

            aux = _a_(56522, _n_(56521, "root", lambda: root), "left")
            _l_(56523)
            return aux
        if not _a_(56526, _n_(56525, "root", lambda: root), "left"):
            _l_(56530)

            aux = _a_(56528, _n_(56527, "root", lambda: root), "right")
            _l_(56529)
            return aux
        temp_val = _a_(56532, _n_(56531, "root", lambda: root), "right")
        _l_(56533)
        mini_val = _a_(56535, _n_(56534, "temp_val", lambda: temp_val), "val")
        _l_(56536)
        while _a_(56538, _n_(56537, "temp_val", lambda: temp_val), "left"):
            _l_(56545)

            temp_val = _a_(56540, _n_(56539, "temp_val", lambda: temp_val), "left")
            _l_(56541)
            mini_val = _a_(56543, _n_(56542, "temp_val", lambda: temp_val), "val")
            _l_(56544)
        _n_(56546, "root", lambda: root).right = _c_(56552, _n_(56547, "deleteNode", lambda: deleteNode), _a_(56549, _n_(56548, "root", lambda: root), "right"), _a_(56551, _n_(56550, "root", lambda: root), "val"))
        _l_(56553)
    aux = _n_(56556, "root", lambda: root)
    _l_(56557)
    return aux

def preOrder(node):
    _l_(56577)

    if not _n_(56559, "node", lambda: node):
        _l_(56561)

        aux = ""
        _l_(56560)
        return aux
    _c_(56565, _n_(56562, "print", lambda: print), _a_(56564, _n_(56563, "node", lambda: node), "val"))
    _l_(56566)
    _c_(56570, _n_(56567, "preOrder", lambda: preOrder), _a_(56569, _n_(56568, "node", lambda: node), "left"))
    _l_(56571)
    _c_(56575, _n_(56572, "preOrder", lambda: preOrder), _a_(56574, _n_(56573, "node", lambda: node), "right"))
    _l_(56576)
root = _c_(56579, _n_(56578, "TreeNode", lambda: TreeNode), 5)
_l_(56580)
_n_(56581, "root", lambda: root).left = _c_(56583, _n_(56582, "TreeNode", lambda: TreeNode), 3)
_l_(56584)
_n_(56585, "root", lambda: root).right = _c_(56587, _n_(56586, "TreeNode", lambda: TreeNode), 6)
_l_(56588)
_a_(56590, _n_(56589, "root", lambda: root), "left").left = _c_(56592, _n_(56591, "TreeNode", lambda: TreeNode), 2)
_l_(56593)
_a_(56596, _a_(56595, _n_(56594, "root", lambda: root), "left"), "right").left = _c_(56598, _n_(56597, "TreeNode", lambda: TreeNode), 7)
_l_(56599)
_c_(56601, _n_(56600, "print", lambda: print), 'Original node:')
_l_(56602)
_c_(56607, _n_(56603, "print", lambda: print), _c_(56606, _n_(56604, "preOrder", lambda: preOrder), _n_(56605, "root", lambda: root)))
_l_(56608)
result = _c_(56611, _n_(56609, "delete_Node", lambda: delete_Node), _n_(56610, "root", lambda: root), 4)
_l_(56612)
_c_(56614, _n_(56613, "print", lambda: print), 'After deleting specified node:')
_l_(56615)
_c_(56620, _n_(56616, "print", lambda: print), _c_(56619, _n_(56617, "preOrder", lambda: preOrder), _n_(56618, "result", lambda: result)))
_l_(56621)