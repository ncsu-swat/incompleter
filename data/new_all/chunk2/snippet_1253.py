# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/36896672/pascals-triangle-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def combination(n, k):
    _l_(447353)

    if _n_(447339, "k", lambda: k) == 0 or _n_(447340, "k", lambda: k) == _n_(447341, "n", lambda: n):
        _l_(447343)

        aux = 1
        _l_(447342)
        return aux
    aux = _c_(447347, _n_(447344, "combination", lambda: combination), _n_(447345, "n", lambda: n) - 1, _n_(447346, "k", lambda: k) - 1) + _c_(447351, _n_(447348, "combination", lambda: combination), _n_(447349, "n", lambda: n) - 1, _n_(447350, "k", lambda: k))
    _l_(447352)
    return aux

def pascals_triangle(rows):
    _l_(447373)

    for row in _c_(447356, _n_(447354, "range", lambda: range), _n_(447355, "rows", lambda: rows)):
        _l_(447372)

        answer = ""
        _l_(447357)
        for column in _c_(447360, _n_(447358, "range", lambda: range), _n_(447359, "row", lambda: row) + 1):
            _l_(447367)

            answer = _n_(447361, "answer", lambda: answer) + _c_(447365, _n_(447362, "combination", lambda: combination), _n_(447363, "row", lambda: row), _n_(447364, "column", lambda: column)) + "\t"
            _l_(447366)
        _c_(447370, _n_(447368, "print", lambda: print), _n_(447369, "answer", lambda: answer))
        _l_(447371)

_c_(447375, _n_(447374, "pascals_triangle", lambda: pascals_triangle), 10)
_l_(447376)