# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36961007/typeerror-unsupported-operand-types-for-nonetype-and-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def calculatePerimeter(length, depth):
    _l_(392811)

    if _n_(392798, "depth", lambda: depth) == 1:
        _l_(392810)

        aux = 3 * _n_(392799, "length", lambda: length)
        _l_(392800)
        return aux
    else:
        _c_(392807, _n_(392801, "print", lambda: print), _c_(392805, _n_(392802, "calculatePerimeter", lambda: calculatePerimeter), _n_(392803, "length", lambda: length), _n_(392804, "depth", lambda: depth)-1) * (4/3)**_n_(392806, "depth", lambda: (depth))) / ((4/3)**(_n_(392808, "depth", lambda: depth)-1))
        _l_(392809)

_c_(392813, _n_(392812, "calculatePerimeter", lambda: calculatePerimeter), 100, 3)
_l_(392814)