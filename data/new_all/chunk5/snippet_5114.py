# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60320610/nameerror-name-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Solution:
    _l_(672342)

    def rob(root: TreeNode) -> _n_(672296, "int", lambda: int):
        _l_(672310)

        sum = [0, 0]
        _l_(672297)
        _c_(672301, _n_(672298, "add", lambda: add), _n_(672299, "root", lambda: root), _n_(672300, "sum", lambda: sum), 0)
        _l_(672302)
        if _n_(672303, "sum", lambda: sum)[0] < _n_(672304, "sum", lambda: sum)[1]:
            _l_(672309)

            aux = _n_(672305, "sum", lambda: sum)[1]
            _l_(672306)
            return aux
        else:
            aux = _n_(672307, "sum", lambda: sum)[0]
            _l_(672308)
            return aux

    def add(node: TreeNode, sum: List[_n_(672311, "int", lambda: int)], index: _n_(672312, "int", lambda: int)):
        _l_(672341)

        if not _n_(672313, "node", lambda: node):
            _l_(672315)

            aux = ""
            _l_(672314)
            return aux
        _n_(672316, "sum", lambda: sum)[_n_(672317, "index", lambda: index)] += _n_(672318, "node", lambda: node).val
        _l_(672319)
        index += 1
        _l_(672320)
        if _n_(672321, "index", lambda: index) >= _c_(672324, _n_(672322, "len", lambda: len), _n_(672323, "sum", lambda: sum)):
            _l_(672326)

            index = 0;
            _l_(672325)
        _c_(672332, _n_(672327, "add", lambda: add), _a_(672329, _n_(672328, "node", lambda: node), "left"), _n_(672330, "sum", lambda: sum), _n_(672331, "index", lambda: index))
        _l_(672333)
        _c_(672339, _n_(672334, "add", lambda: add), _a_(672336, _n_(672335, "node", lambda: node), "right"), _n_(672337, "sum", lambda: sum), _n_(672338, "index", lambda: index))
        _l_(672340)