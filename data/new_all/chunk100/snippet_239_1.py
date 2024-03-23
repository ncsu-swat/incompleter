# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def combination(n, n_list):
    _l_(18932)

    if _n_(18909, "n", lambda: n) <= 0:
        _l_(18912)

        yield []
        _l_(18910)
        aux = ""
        _l_(18911)
        return aux
    for i in _c_(18917, _n_(18913, "range", lambda: range), _c_(18916, _n_(18914, "len", lambda: len), _n_(18915, "n_list", lambda: n_list))):
        _l_(18931)

        c_num = _n_(18918, "n_list", lambda: n_list)[_n_(18919, "i", lambda: i):_n_(18920, "i", lambda: i) + 1]
        _l_(18921)
        for a_num in _c_(18926, _n_(18922, "combination", lambda: combination), _n_(18923, "n", lambda: n) - 1, _n_(18924, "n_list", lambda: n_list)[_n_(18925, "i", lambda: i) + 1:]):
            _l_(18930)

            yield (_n_(18927, "c_num", lambda: c_num) + _n_(18928, "a_num", lambda: a_num))
            _l_(18929)
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
_l_(18933)
_c_(18935, _n_(18934, "print", lambda: print), 'Original list:')
_l_(18936)
_c_(18939, _n_(18937, "print", lambda: print), _n_(18938, "n_list", lambda: n_list))
_l_(18940)
n = 2
_l_(18941)
_c_(18944, _n_(18942, "print", lambda: print), '\nCombinations of', _n_(18943, "n", lambda: n), 'distinct objects:')
_l_(18945)
for e in _n_(18946, "result", lambda: result):
    _l_(18951)

    _c_(18949, _n_(18947, "print", lambda: print), _n_(18948, "e", lambda: e))
    _l_(18950)