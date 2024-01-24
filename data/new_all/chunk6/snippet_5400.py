# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55641918/how-to-fix-a-nonetype-error-in-append-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
some_list = []
_l_(367495)
for i in _c_(367497, _n_(367496, "range", lambda: range), 10):
    _l_(367517)

    if _n_(367498, "i", lambda: i) % 2 == 0:
        _l_(367516)

        i = _c_(367501, _n_(367499, "abs", lambda: abs), _n_(367500, "i", lambda: i))
        _l_(367502)
        some_list = _c_(367506, _a_(367504, _n_(367503, "some_list", lambda: some_list), "append"), _n_(367505, "i", lambda: i))
        _l_(367507)
    elif _n_(367508, "i", lambda: i) % 2 == 1:
        _l_(367515)

        some_list = _c_(367512, _a_(367510, _n_(367509, "some_list", lambda: some_list), "append"), _n_(367511, "i", lambda: i))
        _l_(367513)
    else:
        pass
        _l_(367514)
_n_(367518, "some_list", lambda: some_list)
_l_(367519)