# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74298573/getting-an-error-in-binary-tree-question-attributeerror-int-object-has-no-at
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Solution:
    _l_(630996)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[_n_(630929, "int", lambda: int)]]:
        _l_(630995)

        if not _n_(630930, "root", lambda: root):
            _l_(630932)

            aux = None
            _l_(630931)
            return aux

        li = []
        _l_(630933)
        curr = _n_(630934, "root", lambda: root)
        _l_(630935)
        _c_(630940, _a_(630937, _n_(630936, "li", lambda: li), "append"), [_a_(630939, _n_(630938, "root", lambda: root), "val")])
        _l_(630941)
        if _a_(630943, _n_(630942, "curr", lambda: curr), "right") and _a_(630945, _n_(630944, "curr", lambda: curr), "left"):
            _l_(630994)

            _c_(630960, _a_(630947, _n_(630946, "li", lambda: li), "append"), [_c_(630953, _a_(630949, _n_(630948, "self", lambda: self), "levelOrder"), _a_(630952, _a_(630951, _n_(630950, "curr", lambda: curr), "left"), "val")), _c_(630959, _a_(630955, _n_(630954, "self", lambda: self), "levelOrder"), _a_(630958, _a_(630957, _n_(630956, "curr", lambda: curr), "right"), "val"))])
            _l_(630961)
        elif not _a_(630963, _n_(630962, "curr", lambda: curr), "right") and _a_(630965, _n_(630964, "curr", lambda: curr), "left"):
            _l_(630993)

            _c_(630974, _a_(630967, _n_(630966, "li", lambda: li), "append"), [_c_(630973, _a_(630969, _n_(630968, "self", lambda: self), "levelOrder"), _a_(630972, _a_(630971, _n_(630970, "curr", lambda: curr), "left"), "val"))])
            _l_(630975)
        elif _a_(630977, _n_(630976, "curr", lambda: curr), "right") and not _a_(630979, _n_(630978, "curr", lambda: curr), "left"):
            _l_(630992)

            _c_(630988, _a_(630981, _n_(630980, "li", lambda: li), "append"), [_c_(630987, _a_(630983, _n_(630982, "self", lambda: self), "levelOrder"), _a_(630986, _a_(630985, _n_(630984, "curr", lambda: curr), "right"), "val"))])
            _l_(630989)
#            elif not curr.right and not curr.left:
        else:
            aux = _n_(630990, "li", lambda: li)
            _l_(630991)
            return aux