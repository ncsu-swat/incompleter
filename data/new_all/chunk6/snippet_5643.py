# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56580094/attributeerror-float-object-has-no-attribute-write
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for x in _c_(370428, _n_(370427, "range", lambda: range), 0, 500):
    _l_(370452)


    t1 = _c_(370431, _a_(370430, _n_(370429, "timeit", lambda: timeit), "default_timer"))
    _l_(370432)
    x=_n_(370433, "x", lambda: x)+1
    _l_(370434)
    _c_(370440, _a_(370436, _n_(370435, "t", lambda: t), "write"), _c_(370439, _n_(370437, "str", lambda: str), _n_(370438, "t1", lambda: t1)) + '\n')
    _l_(370441)

    t = _c_(370444, _a_(370443, _n_(370442, "timeit", lambda: timeit), "default_timer")) - _n_(370445, "t1", lambda: t1)
    _l_(370446)
    _c_(370449, _n_(370447, "print", lambda: print), "Pretecen cas: ", _n_(370448, "t", lambda: t))
    _l_(370450)

    break
    _l_(370451)