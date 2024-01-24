# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60919797/python3-nameerror-variable-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Solution:
    _l_(533647)

    def kthSmallest(self, root: TreeNode, k: _n_(533617, "int", lambda: int)) -> _n_(533618, "int", lambda: int):
        _l_(533646)

        i = 0
        _l_(533619)
        def inOrder(root):
            _l_(533639)

            global i
            _l_(533620)
            if _n_(533621, "root", lambda: root) == None:
                _l_(533623)

                aux = ""
                _l_(533622)
                return aux
            _c_(533627, _n_(533624, "inOrder", lambda: inOrder), _a_(533626, _n_(533625, "root", lambda: root), "left"))
            _l_(533628)
            i += 1
            _l_(533629)
            if _n_(533630, "i", lambda: i) == _n_(533631, "k", lambda: k):
                _l_(533633)

                aux = ""
                _l_(533632)
                return aux
            _c_(533637, _n_(533634, "inOrder", lambda: inOrder), _a_(533636, _n_(533635, "root", lambda: root), "right"))
            _l_(533638)

        _c_(533642, _n_(533640, "inOrder", lambda: inOrder), _n_(533641, "root", lambda: root))
        _l_(533643)
        aux = _n_(533644, "i", lambda: i)
        _l_(533645)
        return aux