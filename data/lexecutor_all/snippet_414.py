# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/464864/how-to-get-all-possible-combinations-of-a-list-s-elements
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def combinations(arr, carry):
    _l_(1547197)

    for i in _c_(1547183, _n_(1547179, "range", lambda: range), _c_(1547182, _n_(1547180, "len", lambda: len), _n_(1547181, "arr", lambda: arr))):
        _l_(1547196)

        yield _n_(1547184, "carry", lambda: carry) + _n_(1547185, "arr", lambda: arr)[_n_(1547186, "i", lambda: i)]
        _l_(1547187)
        yield from _c_(1547194, _n_(1547188, "combinations", lambda: combinations), _n_(1547189, "arr", lambda: arr)[_n_(1547190, "i", lambda: i) + 1:], _n_(1547191, "carry", lambda: carry) + _n_(1547192, "arr", lambda: arr)[_n_(1547193, "i", lambda: i)])
        _l_(1547195)

