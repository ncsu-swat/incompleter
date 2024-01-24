# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55641918/how-to-fix-a-nonetype-error-in-append-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
some_list = []
_l_(343164)
for i in _c_(343166, _n_(343165, "range", lambda: range), 10):
    _l_(343186)

    if _n_(343167, "i", lambda: i) % 2 == 0:
        _l_(343185)

        i = _c_(343170, _n_(343168, "abs", lambda: abs), _n_(343169, "i", lambda: i))
        _l_(343171)
        some_list = _c_(343175, _a_(343173, _n_(343172, "some_list", lambda: some_list), "append"), _n_(343174, "i", lambda: i))
        _l_(343176)
    elif _n_(343177, "i", lambda: i) % 2 == 1:
        _l_(343184)

        some_list = _c_(343181, _a_(343179, _n_(343178, "some_list", lambda: some_list), "append"), _n_(343180, "i", lambda: i))
        _l_(343182)
    else:
        pass
        _l_(343183)
_n_(343187, "some_list", lambda: some_list)
_l_(343188)