# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
size = _c_(35459, _n_(35456, "int", lambda: int), _c_(35458, _n_(35457, "input", lambda: input), 'Input the size of the matrix: '))
_l_(35460)
for x in _c_(35463, _n_(35461, "range", lambda: range), 0, _n_(35462, "size", lambda: size)):
    _l_(35484)

    line = _c_(35472, _n_(35464, "list", lambda: list), _c_(35471, _n_(35465, "map", lambda: map), _n_(35466, "int", lambda: int), _c_(35470, _a_(35469, _c_(35468, _n_(35467, "input", lambda: input)), "split"))))
    _l_(35473)
    for y in _c_(35476, _n_(35474, "range", lambda: range), 0, _n_(35475, "size", lambda: size)):
        _l_(35483)

        _n_(35477, "matrix", lambda: matrix)[_n_(35478, "x", lambda: x)][_n_(35479, "y", lambda: y)] = _n_(35480, "line", lambda: line)[_n_(35481, "y", lambda: y)]
        _l_(35482)
matrix_sum_diagonal = _c_(35494, _n_(35485, "sum", lambda: sum), (_n_(35486, "matrix", lambda: matrix)[_n_(35487, "size", lambda: size) - _n_(35488, "i", lambda: i) - 1][_n_(35489, "size", lambda: size) - _n_(35490, "i", lambda: i) - 1] for i in _c_(35493, _n_(35491, "range", lambda: range), _n_(35492, "size", lambda: size))))
_l_(35495)
_c_(35497, _n_(35496, "print", lambda: print), 'Sum of matrix primary diagonal:')
_l_(35498)
_c_(35501, _n_(35499, "print", lambda: print), _n_(35500, "matrix_sum_diagonal", lambda: matrix_sum_diagonal))
_l_(35502)