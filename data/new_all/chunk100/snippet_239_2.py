# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def combination(n, n_list):
    _l_(18971)

    if _n_(18952, "n", lambda: n) <= 0:
        _l_(18955)

        yield []
        _l_(18953)
        aux = ""
        _l_(18954)
        return aux
    for i in _c_(18960, _n_(18956, "range", lambda: range), _c_(18959, _n_(18957, "len", lambda: len), _n_(18958, "n_list", lambda: n_list))):
        _l_(18970)

        for a_num in _c_(18965, _n_(18961, "combination", lambda: combination), _n_(18962, "n", lambda: n) - 1, _n_(18963, "n_list", lambda: n_list)[_n_(18964, "i", lambda: i) + 1:]):
            _l_(18969)

            yield (_n_(18966, "c_num", lambda: c_num) + _n_(18967, "a_num", lambda: a_num))
            _l_(18968)
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
_l_(18972)
_c_(18974, _n_(18973, "print", lambda: print), 'Original list:')
_l_(18975)
_c_(18978, _n_(18976, "print", lambda: print), _n_(18977, "n_list", lambda: n_list))
_l_(18979)
n = 2
_l_(18980)
result = _c_(18984, _n_(18981, "combination", lambda: combination), _n_(18982, "n", lambda: n), _n_(18983, "n_list", lambda: n_list))
_l_(18985)
_c_(18988, _n_(18986, "print", lambda: print), '\nCombinations of', _n_(18987, "n", lambda: n), 'distinct objects:')
_l_(18989)
for e in _n_(18990, "result", lambda: result):
    _l_(18995)

    _c_(18993, _n_(18991, "print", lambda: print), _n_(18992, "e", lambda: e))
    _l_(18994)