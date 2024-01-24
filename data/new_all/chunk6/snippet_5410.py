# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55195483/typeerror-int-object-is-not-subscriptable-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Solution:
    _l_(366925)

    def generate(self, numRows: _n_(366888, "int", lambda: int)) -> List[List[_n_(366889, "int", lambda: int)]]:
        _l_(366924)

        pascal = []
        _l_(366890)

        for i in _c_(366893, _n_(366891, "range", lambda: range), _n_(366892, "numRows", lambda: numRows)):
            _l_(366921)

            _c_(366896, _a_(366895, _n_(366894, "pascal", lambda: pascal), "append"), [])
            _l_(366897)
            for j in _c_(366900, _n_(366898, "range", lambda: range), _n_(366899, "i", lambda: i)+1):
                _l_(366920)

                if _n_(366901, "j", lambda: j) == 0 or _n_(366902, "j", lambda: j) == _n_(366903, "i", lambda: i):
                    _l_(366919)

                    _c_(366906, _a_(366905, _n_(366904, "pascal", lambda: pascal), "append"), 1)
                    _l_(366907)
                else:
                    _c_(366917, _a_(366910, _n_(366908, "pascal", lambda: pascal)[_n_(366909, "i", lambda: i)], "append"), _n_(366911, "pascal", lambda: pascal)[_n_(366912, "i", lambda: i) - 1][_n_(366913, "j", lambda: j) - 1] + _n_(366914, "pascal", lambda: pascal)[_n_(366915, "i", lambda: i) - 1][_n_(366916, "j", lambda: j)])
                    _l_(366918)
        aux = _n_(366922, "pascal", lambda: pascal)
        _l_(366923)
        return aux