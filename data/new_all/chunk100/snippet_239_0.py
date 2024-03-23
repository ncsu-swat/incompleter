# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def combination(n, n_list):
    _l_(18885)

    if _n_(18862, "n", lambda: n) <= 0:
        _l_(18865)

        yield []
        _l_(18863)
        aux = ""
        _l_(18864)
        return aux
    for i in _c_(18870, _n_(18866, "range", lambda: range), _c_(18869, _n_(18867, "len", lambda: len), _n_(18868, "n_list", lambda: n_list))):
        _l_(18884)

        c_num = _n_(18871, "n_list", lambda: n_list)[_n_(18872, "i", lambda: i):_n_(18873, "i", lambda: i) + 1]
        _l_(18874)
        for a_num in _c_(18879, _n_(18875, "combination", lambda: combination), _n_(18876, "n", lambda: n) - 1, _n_(18877, "n_list", lambda: n_list)[_n_(18878, "i", lambda: i) + 1:]):
            _l_(18883)

            yield (_n_(18880, "c_num", lambda: c_num) + _n_(18881, "a_num", lambda: a_num))
            _l_(18882)
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
_l_(18886)
_c_(18888, _n_(18887, "print", lambda: print), 'Original list:')
_l_(18889)
_c_(18892, _n_(18890, "print", lambda: print), _n_(18891, "n_list", lambda: n_list))
_l_(18893)
result = _c_(18897, _n_(18894, "combination", lambda: combination), _n_(18895, "n", lambda: n), _n_(18896, "n_list", lambda: n_list))
_l_(18898)
_c_(18901, _n_(18899, "print", lambda: print), '\nCombinations of', _n_(18900, "n", lambda: n), 'distinct objects:')
_l_(18902)
for e in _n_(18903, "result", lambda: result):
    _l_(18908)

    _c_(18906, _n_(18904, "print", lambda: print), _n_(18905, "e", lambda: e))
    _l_(18907)