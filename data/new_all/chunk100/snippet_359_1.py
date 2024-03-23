# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
matrix = [[0] * _n_(35503, "size", lambda: size) for row in _c_(35506, _n_(35504, "range", lambda: range), 0, _n_(35505, "size", lambda: size))]
_l_(35507)
for x in _c_(35510, _n_(35508, "range", lambda: range), 0, _n_(35509, "size", lambda: size)):
    _l_(35531)

    line = _c_(35519, _n_(35511, "list", lambda: list), _c_(35518, _n_(35512, "map", lambda: map), _n_(35513, "int", lambda: int), _c_(35517, _a_(35516, _c_(35515, _n_(35514, "input", lambda: input)), "split"))))
    _l_(35520)
    for y in _c_(35523, _n_(35521, "range", lambda: range), 0, _n_(35522, "size", lambda: size)):
        _l_(35530)

        _n_(35524, "matrix", lambda: matrix)[_n_(35525, "x", lambda: x)][_n_(35526, "y", lambda: y)] = _n_(35527, "line", lambda: line)[_n_(35528, "y", lambda: y)]
        _l_(35529)
matrix_sum_diagonal = _c_(35541, _n_(35532, "sum", lambda: sum), (_n_(35533, "matrix", lambda: matrix)[_n_(35534, "size", lambda: size) - _n_(35535, "i", lambda: i) - 1][_n_(35536, "size", lambda: size) - _n_(35537, "i", lambda: i) - 1] for i in _c_(35540, _n_(35538, "range", lambda: range), _n_(35539, "size", lambda: size))))
_l_(35542)
_c_(35544, _n_(35543, "print", lambda: print), 'Sum of matrix primary diagonal:')
_l_(35545)
_c_(35548, _n_(35546, "print", lambda: print), _n_(35547, "matrix_sum_diagonal", lambda: matrix_sum_diagonal))
_l_(35549)