# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56580094/attributeerror-float-object-has-no-attribute-write
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for x in _c_(365322, _n_(365321, "range", lambda: range), 0, 500):
    _l_(365346)


    t1 = _c_(365325, _a_(365324, _n_(365323, "timeit", lambda: timeit), "default_timer"))
    _l_(365326)
    x=_n_(365327, "x", lambda: x)+1
    _l_(365328)
    _c_(365334, _a_(365330, _n_(365329, "t", lambda: t), "write"), _c_(365333, _n_(365331, "str", lambda: str), _n_(365332, "t1", lambda: t1)) + '\n')
    _l_(365335)

    t = _c_(365338, _a_(365337, _n_(365336, "timeit", lambda: timeit), "default_timer")) - _n_(365339, "t1", lambda: t1)
    _l_(365340)
    _c_(365343, _n_(365341, "print", lambda: print), "Pretecen cas: ", _n_(365342, "t", lambda: t))
    _l_(365344)

    break
    _l_(365345)