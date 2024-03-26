# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def combination(n, n_list):
    _l_(106529)

    if _n_(106506, "n", lambda: n) <= 0:
        _l_(106509)

        yield []
        _l_(106507)
        aux = ""
        _l_(106508)
        return aux
    for i in _c_(106514, _n_(106510, "range", lambda: range), _c_(106513, _n_(106511, "len", lambda: len), _n_(106512, "n_list", lambda: n_list))):
        _l_(106528)

        c_num = _n_(106515, "n_list", lambda: n_list)[_n_(106516, "i", lambda: i):_n_(106517, "i", lambda: i) + 1]
        _l_(106518)
        for a_num in _c_(106523, _n_(106519, "combination", lambda: combination), _n_(106520, "n", lambda: n) - 1, _n_(106521, "n_list", lambda: n_list)[_n_(106522, "i", lambda: i) + 1:]):
            _l_(106527)

            yield (_n_(106524, "c_num", lambda: c_num) + _n_(106525, "a_num", lambda: a_num))
            _l_(106526)
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
_l_(106530)
_c_(106532, _n_(106531, "print", lambda: print), 'Original list:')
_l_(106533)
_c_(106536, _n_(106534, "print", lambda: print), _n_(106535, "n_list", lambda: n_list))
_l_(106537)
result = _c_(106541, _n_(106538, "combination", lambda: combination), _n_(106539, "n", lambda: n), _n_(106540, "n_list", lambda: n_list))
_l_(106542)
_c_(106545, _n_(106543, "print", lambda: print), '\nCombinations of', _n_(106544, "n", lambda: n), 'distinct objects:')
_l_(106546)
for e in _n_(106547, "result", lambda: result):
    _l_(106552)

    _c_(106550, _n_(106548, "print", lambda: print), _n_(106549, "e", lambda: e))
    _l_(106551)