# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58791891/what-does-this-error-mean-typeerror-parameters-to-generic-types-must-be-types
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def in_matrix(matr: _n_(383831, "List", lambda: List)[_n_(383832, "List", lambda: List):_n_(383833, "int", lambda: int)], cell: _n_(383834, "List", lambda: List)[_n_(383835, "int", lambda: int)]) -> _n_(383836, "bool", lambda: bool):
    _l_(383872)

    b = _c_(383839, _a_(383838, _n_(383837, "cell", lambda: cell), "pop"))
    _l_(383840)
    a = _c_(383843, _a_(383842, _n_(383841, "cell", lambda: cell), "pop"))
    _l_(383844)
    _c_(383847, _n_(383845, "print", lambda: print), _n_(383846, "a", lambda: a))
    _l_(383848)
    _c_(383851, _n_(383849, "print", lambda: print), _n_(383850, "b", lambda: b))
    _l_(383852)
    for y in _c_(383857, _n_(383853, "range", lambda: range), _c_(383856, _n_(383854, "len", lambda: len), _n_(383855, "matr", lambda: matr))):
        _l_(383871)

        for x in _c_(383863, _n_(383858, "range", lambda: range), _c_(383862, _n_(383859, "len", lambda: len), _n_(383860, "matr", lambda: matr)[_n_(383861, "y", lambda: y)])):
            _l_(383870)

            if _n_(383864, "matr", lambda: matr)[_n_(383865, "a", lambda: a)][_n_(383866, "b", lambda: b)] == True:
                _l_(383869)

                aux = True
                _l_(383867)
                return aux
            else:
                aux = False
                _l_(383868)
                return aux